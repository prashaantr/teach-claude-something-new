---
name: pdf
description: |
  Process PDF files. Use when:
  (1) Reading or extracting text and tables from PDFs
  (2) Merging, splitting, or rotating PDF pages
  (3) Adding watermarks or creating new PDFs
  (4) Filling forms or extracting images
  (5) Running OCR on scanned documents
  (6) Encrypting or decrypting PDF files
---

# PDF Processing

## Reading PDFs

```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

# Extract text
for page in reader.pages:
    print(page.extract_text())
```

## Extract Tables

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(row)
```

## Merge PDFs

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

## Split PDF

```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

## Create PDF

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("output.pdf", pagesize=letter)
width, height = letter
c.drawString(100, height - 100, "Hello World!")
c.save()
```

## Command Line Tools

```bash
# Extract text (requires poppler-utils)
pdftotext input.pdf output.txt
pdftotext -layout input.pdf output.txt  # preserve layout

# Merge with qpdf
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf
```

## Quick Reference

| Task | Tool | Method |
|------|------|--------|
| Read text | pypdf/pdfplumber | `page.extract_text()` |
| Tables | pdfplumber | `page.extract_tables()` |
| Merge | pypdf | `writer.add_page()` |
| Create | reportlab | Canvas or Platypus |
| OCR | pytesseract + pdf2image | Convert to image first |
