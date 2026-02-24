# PDF Generation Reference

PDF processing capabilities for assembly manual output and manipulation.

## Creating PDFs with ReportLab

```python
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm

c = canvas.Canvas("output.pdf", pagesize=letter)
width, height = letter
c.drawString(100, height - 100, "Assembly Manual")
c.showPage()
c.save()
```

## Adding Images to PDF

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("manual.pdf", pagesize=A4)
width, height = A4
c.drawImage("step-01.png", x=50, y=height-400, width=400, height=300)
c.showPage()
c.save()
```

## Multi-Page Assembly Manual Pattern

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import glob

def compile_assembly_pdf(image_folder, output_path, title="Assembly Manual"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    margin = 20 * mm

    # Cover page
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height/2, title)
    c.showPage()

    # Step pages
    images = sorted(glob.glob(f"{image_folder}/step-*.png"))
    for i, img_path in enumerate(images, 1):
        c.setFont("Helvetica-Bold", 14)
        c.drawString(margin, height - margin, f"Step {i}")
        c.drawImage(img_path, margin, margin,
                   width - 2*margin, height - 2*margin - 30,
                   preserveAspectRatio=True)
        c.showPage()
    c.save()
```

## Merging PDFs

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["cover.pdf", "parts.pdf", "steps.pdf", "wiring.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("complete_manual.pdf", "wb") as output:
    writer.write(output)
```

## Splitting PDFs

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("manual.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

## SVG to PDF Conversion

```python
import cairosvg

cairosvg.svg2pdf(url="step-01.svg", write_to="step-01.pdf")
cairosvg.svg2pdf(url="diagram.svg", write_to="diagram.pdf",
                 output_width=595, output_height=842)  # A4 size
```

## Command Line Tools

```bash
# Merge with qpdf
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf

# Convert images to PDF (ImageMagick)
convert step-*.png assembly_steps.pdf

# Compress PDF
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=compressed.pdf input.pdf
```

## Quick Reference

| Task | Tool | Method |
|------|------|--------|
| Create PDF | reportlab | `canvas.Canvas()` |
| Add images | reportlab | `c.drawImage()` |
| Merge PDFs | pypdf | `writer.add_page()` |
| Split PDF | pypdf | Iterate `reader.pages` |
| SVG→PDF | cairosvg | `svg2pdf()` |
