#!/usr/bin/env python3
"""
CXR Pneumonia Detection Benchmark Runner

Evaluates the skill against the Kaggle Chest X-Ray Pneumonia dataset.
Uses Claude API to analyze images with the structured workflow.

Usage:
    python benchmark/run_benchmark.py --data-dir /path/to/chest_xray --sample 50
    python benchmark/run_benchmark.py --data-dir /path/to/chest_xray --full

Requirements:
    pip install anthropic pillow

Environment:
    ANTHROPIC_API_KEY must be set
"""

import argparse
import base64
import json
import os
import random
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import anthropic
    from PIL import Image
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install anthropic pillow")
    sys.exit(1)


# Load the skill prompt
SKILL_DIR = Path(__file__).parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"


def load_skill_prompt():
    """Load the SKILL.md content as the system prompt."""
    with open(SKILL_MD) as f:
        content = f.read()

    # Extract content after the YAML frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].strip()

    return content


def encode_image(image_path: str) -> tuple[str, str]:
    """Encode image to base64 and determine media type."""
    with open(image_path, "rb") as f:
        data = base64.standard_b64encode(f.read()).decode("utf-8")

    suffix = Path(image_path).suffix.lower()
    media_type = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }.get(suffix, "image/jpeg")

    return data, media_type


def analyze_image(client: anthropic.Anthropic, image_path: str, skill_prompt: str) -> dict:
    """Analyze a single CXR image using the skill workflow."""
    image_data, media_type = encode_image(image_path)

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        system=skill_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Analyze this chest X-ray for pneumonia following the 6-stage workflow. Provide your structured assessment.",
                    },
                ],
            }
        ],
    )

    response_text = message.content[0].text

    # Parse the assessment from the response
    assessment = parse_assessment(response_text)
    assessment["raw_response"] = response_text
    assessment["image_path"] = str(image_path)

    return assessment


def parse_assessment(response: str) -> dict:
    """Extract structured assessment from model response."""
    assessment = {
        "pneumonia": None,  # YES, NO, or INDETERMINATE
        "confidence": None,  # 1-5 scale
        "confidence_pct": None,  # percentage
    }

    # Look for pneumonia verdict
    pneumonia_match = re.search(r"\*\*Pneumonia:\*\*\s*(YES|NO|INDETERMINATE)", response, re.IGNORECASE)
    if pneumonia_match:
        assessment["pneumonia"] = pneumonia_match.group(1).upper()

    # Look for confidence score
    confidence_match = re.search(r"\*\*Confidence:\*\*\s*(\d)\s*(?:\((\d+)%\))?", response)
    if confidence_match:
        assessment["confidence"] = int(confidence_match.group(1))
        if confidence_match.group(2):
            assessment["confidence_pct"] = int(confidence_match.group(2))

    return assessment


def get_ground_truth(image_path: str) -> str:
    """Get ground truth label from directory structure."""
    # Kaggle dataset structure: chest_xray/{train,test,val}/{NORMAL,PNEUMONIA}/image.jpeg
    parent_dir = Path(image_path).parent.name
    if parent_dir.upper() == "PNEUMONIA":
        return "YES"
    elif parent_dir.upper() == "NORMAL":
        return "NO"
    return "UNKNOWN"


def collect_images(data_dir: str, split: str = "test") -> list[tuple[str, str]]:
    """Collect image paths and labels from dataset."""
    data_path = Path(data_dir)

    # Handle nested structure (chest_xray/chest_xray/)
    if (data_path / "chest_xray").exists():
        data_path = data_path / "chest_xray"

    images = []

    for category in ["NORMAL", "PNEUMONIA"]:
        category_dir = data_path / split / category
        if not category_dir.exists():
            print(f"Warning: {category_dir} not found")
            continue

        label = "NO" if category == "NORMAL" else "YES"

        for img_path in category_dir.glob("*.jpeg"):
            images.append((str(img_path), label))
        for img_path in category_dir.glob("*.jpg"):
            images.append((str(img_path), label))
        for img_path in category_dir.glob("*.png"):
            images.append((str(img_path), label))

    return images


def calculate_metrics(results: list[dict]) -> dict:
    """Calculate accuracy, precision, recall, F1."""
    tp = fp = tn = fn = 0

    for r in results:
        pred = r.get("prediction")
        truth = r.get("ground_truth")

        if pred is None or truth == "UNKNOWN":
            continue

        if pred == "YES" and truth == "YES":
            tp += 1
        elif pred == "YES" and truth == "NO":
            fp += 1
        elif pred == "NO" and truth == "NO":
            tn += 1
        elif pred == "NO" and truth == "YES":
            fn += 1

    total = tp + fp + tn + fn
    accuracy = (tp + tn) / total if total > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "total": total,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "indeterminate": sum(1 for r in results if r.get("prediction") == "INDETERMINATE"),
    }


def run_benchmark(
    data_dir: str,
    sample_size: int = None,
    split: str = "test",
    output_file: str = None,
) -> dict:
    """Run the full benchmark."""
    # Initialize client
    client = anthropic.Anthropic()

    # Load skill
    skill_prompt = load_skill_prompt()
    print(f"Loaded skill prompt ({len(skill_prompt)} chars)")

    # Collect images
    images = collect_images(data_dir, split)
    print(f"Found {len(images)} images in {split} set")

    if not images:
        print("ERROR: No images found. Check data directory structure.")
        sys.exit(1)

    # Sample if requested
    if sample_size and sample_size < len(images):
        images = random.sample(images, sample_size)
        print(f"Sampled {sample_size} images")

    # Run analysis
    results = []
    for i, (img_path, label) in enumerate(images):
        print(f"\n[{i+1}/{len(images)}] Analyzing: {Path(img_path).name}")
        print(f"  Ground truth: {label}")

        try:
            assessment = analyze_image(client, img_path, skill_prompt)
            assessment["ground_truth"] = label
            assessment["prediction"] = assessment.get("pneumonia")

            print(f"  Prediction: {assessment.get('pneumonia')} (confidence: {assessment.get('confidence')})")

            correct = assessment.get("pneumonia") == label
            print(f"  {'CORRECT' if correct else 'INCORRECT'}")

            results.append(assessment)

        except Exception as e:
            print(f"  ERROR: {e}")
            results.append({
                "image_path": img_path,
                "ground_truth": label,
                "prediction": None,
                "error": str(e),
            })

    # Calculate metrics
    metrics = calculate_metrics(results)

    # Create report
    report = {
        "timestamp": datetime.now().isoformat(),
        "data_dir": data_dir,
        "split": split,
        "sample_size": len(images),
        "metrics": metrics,
        "results": results,
    }

    # Print summary
    print("\n" + "=" * 60)
    print("BENCHMARK RESULTS")
    print("=" * 60)
    print(f"Total images: {metrics['total']}")
    print(f"Accuracy: {metrics['accuracy']:.1%}")
    print(f"Precision: {metrics['precision']:.1%}")
    print(f"Recall: {metrics['recall']:.1%}")
    print(f"F1 Score: {metrics['f1']:.1%}")
    print(f"\nConfusion Matrix:")
    print(f"  TP: {metrics['tp']} | FP: {metrics['fp']}")
    print(f"  FN: {metrics['fn']} | TN: {metrics['tn']}")
    print(f"\nIndeterminate: {metrics['indeterminate']}")
    print("=" * 60)
    print(f"\nBaseline comparison:")
    print(f"  Naive zero-shot: ~58%")
    print(f"  Our result: {metrics['accuracy']:.1%}")
    print(f"  Target (GPT-4o best): >74%")

    # Save results
    if output_file:
        with open(output_file, "w") as f:
            json.dump(report, f, indent=2, default=str)
        print(f"\nResults saved to: {output_file}")

    return report


def main():
    parser = argparse.ArgumentParser(description="Run CXR Pneumonia Detection Benchmark")
    parser.add_argument("--data-dir", required=True, help="Path to chest_xray dataset")
    parser.add_argument("--sample", type=int, help="Number of images to sample (for quick testing)")
    parser.add_argument("--full", action="store_true", help="Run on full test set")
    parser.add_argument("--split", default="test", choices=["train", "test", "val"], help="Dataset split")
    parser.add_argument("--output", help="Output JSON file for results")

    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    sample_size = None if args.full else (args.sample or 20)

    output_file = args.output or f"benchmark_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    run_benchmark(
        data_dir=args.data_dir,
        sample_size=sample_size,
        split=args.split,
        output_file=output_file,
    )


if __name__ == "__main__":
    main()
