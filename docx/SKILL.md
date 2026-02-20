---
name: docx
description: |
  Use this skill for Word documents (.docx). This includes: creating,
  editing, reading documents, adding tables, headings, formatting,
  page numbers, headers/footers. Trigger when user mentions Word docs,
  .docx files, or document creation.
---

# Word Document Processing

## Reading Documents

```python
from docx import Document

doc = Document("document.docx")

# Extract all text
for para in doc.paragraphs:
    print(para.text)

# Extract tables
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            print(cell.text, end='\t')
        print()
```

## Creating Documents

```python
from docx import Document
from docx.shared import Inches, Pt

doc = Document()

# Add heading
doc.add_heading('Document Title', 0)

# Add paragraph
doc.add_paragraph('This is a paragraph of text.')

# Add bullet list
doc.add_paragraph('First item', style='List Bullet')
doc.add_paragraph('Second item', style='List Bullet')

# Add table
table = doc.add_table(rows=2, cols=2)
table.cell(0, 0).text = 'Header 1'
table.cell(0, 1).text = 'Header 2'
table.cell(1, 0).text = 'Data 1'
table.cell(1, 1).text = 'Data 2'

doc.save('output.docx')
```

## Formatting

```python
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Formatted paragraph
para = doc.add_paragraph()
run = para.add_run('Bold and ')
run.bold = True
run = para.add_run('italic text')
run.italic = True

# Font size
para = doc.add_paragraph()
run = para.add_run('Large text')
run.font.size = Pt(24)

# Alignment
para = doc.add_paragraph('Centered text')
para.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.save('formatted.docx')
```

## Critical Rules

- Always set page size explicitly (default is A4, not US Letter)
- Use proper list styles, don't insert bullet characters manually
- Tables need width specified in DXA units
- Use smart quotes for professional typography
