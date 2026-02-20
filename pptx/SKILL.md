---
name: pptx
description: |
  Use this skill for PowerPoint (.pptx) files. This includes:
  creating slide decks, reading/extracting text, editing presentations,
  working with templates, layouts, speaker notes. Trigger when user
  mentions "deck," "slides," "presentation," or any .pptx file.
---

# PowerPoint Presentations

## Reading/Extracting Content

```bash
# Extract text from presentation
python -m markitdown presentation.pptx

# Convert slides to images for visual review
python -c "
from pptx import Presentation
prs = Presentation('presentation.pptx')
for i, slide in enumerate(prs.slides):
    print(f'Slide {i+1}:')
    for shape in slide.shapes:
        if hasattr(shape, 'text'):
            print(f'  {shape.text}')
"
```

## Creating Presentations

Use `pptxgenjs` (JavaScript) or `python-pptx`:

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title + Content

title = slide.shapes.title
title.text = "My Title"

body = slide.placeholders[1]
body.text = "First bullet point"

prs.save('output.pptx')
```

## Design Principles

- **Color**: One dominant color (60-70%), supporting tones, one accent
- **Layout variety**: Mix columns, icon+text rows, grids, half-bleed images
- **Typography**: 36-44pt titles, 14-16pt body text
- **Avoid**: Text-only slides, repeated layouts, centered body text, default blue

## Quality Check

Always verify:
1. Extract text to confirm content
2. Review visually if possible
3. Never declare done without at least one revision
