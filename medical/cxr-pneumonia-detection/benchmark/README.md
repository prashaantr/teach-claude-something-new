# CXR Pneumonia Detection Benchmark

Evaluates the skill against the [Kaggle Chest X-Ray Pneumonia dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) (Kermany et al.).

## Dataset

- **Source**: Guangzhou Women and Children's Medical Center
- **Size**: 5,863 chest X-ray images (JPEG)
- **Classes**: NORMAL, PNEUMONIA
- **Split**: train (5,216), test (624), val (16)

## Setup

1. Download the dataset:
```bash
kaggle datasets download -d paultimothymooney/chest-xray-pneumonia
unzip chest-xray-pneumonia.zip
```

2. Install dependencies:
```bash
pip install anthropic pillow
```

3. Set API key:
```bash
export ANTHROPIC_API_KEY=your_key_here
```

## Running the Benchmark

Quick test (20 images):
```bash
python benchmark/run_benchmark.py --data-dir /path/to/chest_xray
```

Sample run (50 images):
```bash
python benchmark/run_benchmark.py --data-dir /path/to/chest_xray --sample 50
```

Full test set (624 images):
```bash
python benchmark/run_benchmark.py --data-dir /path/to/chest_xray --full
```

## Expected Results

| Method | Accuracy | Notes |
|--------|----------|-------|
| Naive zero-shot | ~58% | No structured prompting |
| This skill (target) | >74% | Structured radiologist workflow |
| Finetuned models | ~97% | Not comparable, requires training |

## Output

Results are saved to JSON with:
- Per-image predictions and confidence scores
- Overall accuracy, precision, recall, F1
- Confusion matrix
- Comparison to baselines

## Baselines

- **GPT-4V naive**: 7.3% F1 (Tiu et al.)
- **GPT-4o best prompt**: 74% accuracy (Sonoda et al.)
- **Claude 3 Opus**: 70.29% accuracy (Sonoda et al.)
- **Finetuned ResNet**: 97%+ accuracy (Kaggle leaderboard)

## Research References

- Sonoda et al. (2025): Two-step structured reasoning
- Wada et al. (2024): Confidence calibration
- Kermany et al. (2018): Original dataset paper
