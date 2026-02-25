#!/usr/bin/env python3
"""
DICOM to PNG Converter for Chest X-Ray Analysis

Converts DICOM medical imaging files to PNG format for analysis.
Handles windowing and normalization for optimal chest X-ray viewing.

Usage:
    python scripts/dicom_to_png.py input.dcm output.png
    python scripts/dicom_to_png.py input.dcm output.png --window chest
    python scripts/dicom_to_png.py /path/to/dicoms/ /path/to/output/ --batch

Requirements:
    pip install pydicom pillow numpy
"""

import argparse
import sys
from pathlib import Path

try:
    import pydicom
    import numpy as np
    from PIL import Image
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install pydicom pillow numpy")
    sys.exit(1)


# Standard window presets for chest X-ray
WINDOW_PRESETS = {
    "chest": {"center": -600, "width": 1500},  # Standard lung window
    "mediastinum": {"center": 40, "width": 400},  # Soft tissue
    "bone": {"center": 400, "width": 1800},  # Bone detail
    "auto": None,  # Use DICOM metadata or auto-calculate
}


def apply_windowing(pixel_array: np.ndarray, center: float, width: float) -> np.ndarray:
    """Apply window/level transformation to pixel data."""
    min_val = center - width / 2
    max_val = center + width / 2

    windowed = np.clip(pixel_array, min_val, max_val)
    normalized = ((windowed - min_val) / (max_val - min_val) * 255).astype(np.uint8)

    return normalized


def convert_dicom_to_png(
    dicom_path: str,
    output_path: str,
    window_preset: str = "auto"
) -> str:
    """
    Convert a DICOM file to PNG.

    Args:
        dicom_path: Path to input DICOM file
        output_path: Path for output PNG file
        window_preset: Window preset name or "auto"

    Returns:
        Path to output file
    """
    # Read DICOM
    ds = pydicom.dcmread(dicom_path)
    pixel_array = ds.pixel_array.astype(float)

    # Apply rescale if present (convert to Hounsfield units for CT, or just rescale)
    if hasattr(ds, 'RescaleSlope') and hasattr(ds, 'RescaleIntercept'):
        pixel_array = pixel_array * ds.RescaleSlope + ds.RescaleIntercept

    # Determine windowing
    if window_preset == "auto":
        # Try to get from DICOM metadata
        if hasattr(ds, 'WindowCenter') and hasattr(ds, 'WindowWidth'):
            center = ds.WindowCenter
            width = ds.WindowWidth
            # Handle multi-valued windows (take first)
            if isinstance(center, pydicom.multival.MultiValue):
                center = center[0]
            if isinstance(width, pydicom.multival.MultiValue):
                width = width[0]
        else:
            # Auto-calculate from pixel data
            center = np.median(pixel_array)
            width = np.percentile(pixel_array, 99) - np.percentile(pixel_array, 1)
    else:
        preset = WINDOW_PRESETS.get(window_preset)
        if preset is None:
            raise ValueError(f"Unknown window preset: {window_preset}")
        center = preset["center"]
        width = preset["width"]

    # Apply windowing
    normalized = apply_windowing(pixel_array, center, width)

    # Handle photometric interpretation (invert if needed)
    if hasattr(ds, 'PhotometricInterpretation'):
        if ds.PhotometricInterpretation == "MONOCHROME1":
            normalized = 255 - normalized

    # Create and save image
    image = Image.fromarray(normalized)

    # Convert to RGB if grayscale (some viewers expect this)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    image.save(output_path)

    return output_path


def batch_convert(input_dir: str, output_dir: str, window_preset: str = "auto") -> list:
    """
    Convert all DICOM files in a directory.

    Args:
        input_dir: Directory containing DICOM files
        output_dir: Directory for output PNGs
        window_preset: Window preset to use

    Returns:
        List of output file paths
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    outputs = []

    # Common DICOM extensions
    dicom_patterns = ["*.dcm", "*.DCM", "*.dicom", "*.DICOM"]

    dicom_files = []
    for pattern in dicom_patterns:
        dicom_files.extend(input_path.glob(pattern))

    # Also check files without extension (common for DICOM)
    for f in input_path.iterdir():
        if f.is_file() and f.suffix == "":
            try:
                pydicom.dcmread(f, stop_before_pixels=True)
                dicom_files.append(f)
            except:
                pass

    for dicom_file in dicom_files:
        output_file = output_path / f"{dicom_file.stem}.png"
        try:
            convert_dicom_to_png(str(dicom_file), str(output_file), window_preset)
            outputs.append(str(output_file))
            print(f"Converted: {dicom_file.name} -> {output_file.name}")
        except Exception as e:
            print(f"Error converting {dicom_file.name}: {e}")

    return outputs


def main():
    parser = argparse.ArgumentParser(
        description="Convert DICOM files to PNG for chest X-ray analysis"
    )
    parser.add_argument("input", help="Input DICOM file or directory")
    parser.add_argument("output", help="Output PNG file or directory")
    parser.add_argument(
        "--window",
        choices=list(WINDOW_PRESETS.keys()),
        default="auto",
        help="Window preset (default: auto)"
    )
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Batch convert directory of DICOMs"
    )

    args = parser.parse_args()

    if args.batch:
        outputs = batch_convert(args.input, args.output, args.window)
        print(f"\nConverted {len(outputs)} files")
    else:
        output = convert_dicom_to_png(args.input, args.output, args.window)
        print(f"Saved: {output}")


if __name__ == "__main__":
    main()
