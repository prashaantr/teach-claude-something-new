---
name: assembly-instructions
description: |
  Generate IKEA-style visual assembly manuals as PDFs. Use when:
  (1) Creating assembly instructions for hardware projects
  (2) Making build guides for Arduino, IoT, or electronics
  (3) Documenting 3D-printed enclosure assembly
  (4) Writing wiring diagrams or hardware setup manuals
  (5) Creating step-by-step visual instructions for non-technical users
  (6) Compiling assembly images into multi-page PDFs
  (7) Merging, splitting, or manipulating assembly manual PDFs
  Supports two workflows: SVG component rendering (for electronics) or AI-generated images (Nano Banana Pro).
  Trigger words: "instruction manual", "assembly guide", "build instructions", "wiring guide".
  Output: Multi-page PDF with parts inventory, diagrams, callouts, and action arrows.
---

# Assembly Instructions Generator

Generate IKEA-style visual assembly manuals as multi-page PDFs.

## Two Workflows

1. **SVG Component Workflow** — Best for electronics/Arduino projects with wiring diagrams
2. **AI Image Workflow** — Best for furniture, general products, custom illustrations

## Quick Start: SVG Workflow (Electronics)

```bash
# Install dependencies
pip install -r requirements.txt

# Validate project YAML
python3 scripts/validate_project.py project.yaml

# Render and compile to PDF
python3 scripts/render_manual.py project.yaml --output manual.pdf
```

## Quick Start: AI Image Workflow (General Products)

```bash
# Generate images with AI
uv run scripts/generate_image.py \
  --prompt "IKEA-style technical illustration. Subject: [YOUR PRODUCT]" \
  --filename "step-01.png" --resolution 2K

# Compile to PDF
python3 scripts/compile_pdf.py *.png --output manual.pdf
```

Requires: `GEMINI_API_KEY` environment variable.

## References

Read these files when you need detailed information:

| Reference | When to Read |
|-----------|--------------|
| `references/ikea-visual-spec.md` | **CRITICAL for AI workflow.** Exact IKEA visual specifications: line weights, perspective, layout templates, common mistakes. Read BEFORE generating any images. |
| `references/design-principles.md` | When making design decisions about step ordering, layout, or diagram style. Contains 16 cognitive principles. |
| `references/yaml-schema.md` | When creating or editing project YAML files for SVG workflow. Contains full schema spec. |
| `references/component-catalog.md` | When defining parts for any project. Provides patterns for describing components consistently (not a fixed list). |
| `references/pdf-generation.md` | When doing advanced PDF manipulation: merging, splitting, adding covers. |

## Scripts

### scripts/validate_project.py

**When to use:** Before SVG rendering, to catch YAML errors early.

```bash
python3 scripts/validate_project.py project.yaml
```

Checks: required fields, valid part IDs, component references, wiring consistency.

### scripts/render_manual.py

**When to use:** Main SVG rendering pipeline — YAML to PDF.

```bash
python3 scripts/render_manual.py project.yaml --output manual.pdf
python3 scripts/render_manual.py project.yaml --output-dir ./build  # SVG only
```

### scripts/compile_pdf.py

**When to use:** Compile SVG or PNG files into PDF.

```bash
python3 scripts/compile_pdf.py ./build --output manual.pdf
python3 scripts/compile_pdf.py cover.svg parts.svg step1.svg --output manual.pdf
```

### scripts/components.py

**When to use:** Preview available SVG components or debug rendering.

```bash
python3 scripts/components.py --list
python3 scripts/components.py --render arduino_nano
```

### scripts/generate_image.py

**When to use:** Generate AI illustrations using Nano Banana Pro (Gemini 3 Pro Image).

```bash
uv run scripts/generate_image.py --prompt "description" --filename "output.png"
uv run scripts/generate_image.py --prompt "description" --filename "output.png" --resolution 2K
```

## AI Image Prompt Template

**CRITICAL:** Read `references/ikea-visual-spec.md` before generating images. Key rules:

- **WORDLESS** — No text except step numbers, quantities ("4x"), part codes (6-digit)
- **Line art** — 2pt black lines on pure white, light grey fills only
- **30° isometric** — Same angle for every page, never changes
- **Parts float** — No boxes, frames, or containers

### Base Prompt (prepend to all image prompts):
```
Authentic IKEA assembly manual. Pure black line art, white background, 30° isometric.
2pt uniform lines. NO text except step numbers or quantities. NO gradients, textures, shadows.
Simple human figures if needed: oval head, dot eyes, light grey fill.
```

### Page Types:
- **Cover:** Product name huge at top, isometric finished product centered, IKEA logo bottom-right
- **Parts inventory:** Parts floating on white, part codes below, quantities to right
- **Assembly step:** Large step number top-left, one action shown, callout circles for details
- **Do/Don't:** Side-by-side panels, X overlay on wrong action

See `references/ikea-visual-spec.md` for complete templates and common mistakes.

## Project YAML Schema (SVG Workflow)

Minimal example (see `references/yaml-schema.md` for full spec):

```yaml
project:
  name: "Motion-Activated LED Strip"

parts:
  structural:
    - id: "A"
      name: "Mounting bracket"
      shape: rect
      dimensions: {w: 100, h: 60}
  hardware:
    - id: "H1"
      name: "M3×8mm screw"
      quantity: 4
      type: screw_phillips
  electronic:
    - id: "E1"
      name: "Arduino Nano"
      component: arduino_nano

wiring:
  - from: {part: "E1", pin: "D2"}
    to: {part: "E2", pin: "OUT"}
    color: yellow

steps:
  - step: 1
    action: place
    parts: ["A"]
  - step: 2
    action: attach
    parts: ["E1", "A"]
    hardware: ["H1"]
```

## Defining Components

Any component can be used — see `references/component-catalog.md` for patterns:

- **Structural:** plates, brackets, enclosures, standoffs (shape + dimensions)
- **Hardware:** screws, nuts, anchors, clips (type + quantity)
- **Electronic:** boards, sensors, modules (form factor + pins)
- **Power:** batteries, cables, jacks (voltage + polarity)
- **Connectivity:** breadboards, wires, connectors (capacity + features)

Define components by describing their attributes, not by choosing from a fixed list.

## Design Principles

Stanford research: action diagrams reduce assembly time 35% and errors 50%.

- **Fixed Viewpoint** — Same 30° isometric angle in every image
- **Action Diagrams** — New parts float toward destination with arrows
- **One Step = One Action** — Never combine operations
- **Wordless** — No text except part labels and quantity markers

See `references/design-principles.md` for all 16 principles.

## Action Diagram Rules

| Action Type | Visual Treatment |
|-------------|------------------|
| Place | Part sitting on surface, no arrows |
| Attach | New part floating above target with curved arrow |
| Insert | Hardware floating near hole with straight arrow |
| Rotate | Curved arrow around part showing rotation |
| Flip | Part shown in two positions with flip arrow |

## Page Sequence Generated

1. **Cover** — Product name + assembled preview
2. **Safety/Tips** — ESD warning, power-off-before-wiring
3. **Hardware Inventory** — Grid of fasteners with IDs
4. **Parts Inventory** — Components with IDs
5. **Assembly Steps** — One page per step
6. **Wiring Diagram** — Color-coded wiring (SVG workflow only)

## Working With the User

| Input | Workflow |
|-------|----------|
| YAML provided | Validate → Render → Present PDF |
| Conversational description | Interview → Generate YAML → Validate → Render |
| Photos/schematics | Analyze → Generate YAML or AI images → Compile |

## PDF Manipulation

For advanced operations, see `references/pdf-generation.md`:

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for section in ["cover.pdf", "parts.pdf", "steps.pdf"]:
    for page in PdfReader(section).pages:
        writer.add_page(page)
with open("complete.pdf", "wb") as f:
    writer.write(f)
```

## Dependencies

```bash
pip install -r requirements.txt
# drawsvg, cairosvg, reportlab, pyyaml, pypdf, pdfplumber
```

For AI workflow: `GEMINI_API_KEY` environment variable.
