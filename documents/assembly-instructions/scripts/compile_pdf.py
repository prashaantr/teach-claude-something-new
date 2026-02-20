#!/usr/bin/env python3
"""
Compile SVG pages into a multi-page PDF.

Standalone compiler for when you have pre-rendered SVG pages
and just need to assemble them into a PDF.

Usage:
    python3 compile_pdf.py ./build --output manual.pdf
    python3 compile_pdf.py page_01.svg page_02.svg --output manual.pdf
"""

import sys
import os
import glob
import tempfile
import cairosvg
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


def compile_svgs_to_pdf(svg_paths, output_path, dpi_scale=2):
    """Compile a list of SVG files into a multi-page PDF.

    Args:
        svg_paths: List of SVG file paths (in page order)
        output_path: Output PDF path
        dpi_scale: Resolution multiplier for rasterization (2 = good quality)
    """
    page_w, page_h = A4  # 595.27 × 841.89 points

    temp_dir = tempfile.mkdtemp()
    png_paths = []

    for i, svg_path in enumerate(svg_paths):
        png_path = os.path.join(temp_dir, f"page_{i:03d}.png")
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=int(page_w * dpi_scale),
            output_height=int(page_h * dpi_scale),
        )
        png_paths.append(png_path)
        print(f"  Rasterized: {os.path.basename(svg_path)}")

    # Assemble PDF
    c = canvas.Canvas(output_path, pagesize=A4)
    for png_path in png_paths:
        img = ImageReader(png_path)
        c.drawImage(img, 0, 0, width=page_w, height=page_h,
                     preserveAspectRatio=True, anchor='c')
        c.showPage()
    c.save()

    # Cleanup temp files
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)

    print(f"\n✅ PDF compiled: {output_path} ({len(svg_paths)} pages)")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 compile_pdf.py ./build_dir --output manual.pdf")
        print("  python3 compile_pdf.py page1.svg page2.svg --output manual.pdf")
        sys.exit(1)

    output_path = "manual.pdf"
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        output_path = sys.argv[idx + 1]
        args = [a for a in sys.argv[1:] if a not in ("--output", output_path)]
    else:
        args = sys.argv[1:]

    # Determine SVG paths
    svg_paths = []
    for arg in args:
        if os.path.isdir(arg):
            # Directory mode: find all SVGs sorted by name
            svgs = sorted(glob.glob(os.path.join(arg, "*.svg")))
            svg_paths.extend(svgs)
        elif arg.endswith('.svg') and os.path.exists(arg):
            svg_paths.append(arg)
        else:
            print(f"⚠️  Skipping: {arg}")

    if not svg_paths:
        print("❌ No SVG files found")
        sys.exit(1)

    print(f"📄 Compiling {len(svg_paths)} SVG pages into PDF...")
    compile_svgs_to_pdf(svg_paths, output_path)


if __name__ == "__main__":
    main()
