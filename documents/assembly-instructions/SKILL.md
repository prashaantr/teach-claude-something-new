---
name: assembly-instructions
description: |
  Generate IKEA-style visual assembly manuals with AI-generated illustrations. Use when:
  (1) Creating assembly instructions for any physical product
  (2) Making build guides or setup manuals
  (3) Documenting how to assemble furniture, devices, or kits
  (4) Creating step-by-step visual instructions for non-technical users
  Uses Nano Banana Pro (Gemini 3 Pro Image) to generate isometric illustrations.
---

# Assembly Instructions Generator

Generate IKEA-style visual assembly manuals with AI-generated isometric illustrations.

## Workflow

1. **Define** — Structure the project as YAML (or help user create one interactively)
2. **Generate Images** — Use Nano Banana Pro to create step illustrations
3. **Compile** — Assemble into multi-page PDF

## Image Generation with Nano Banana Pro

Generate IKEA-style illustrations using the Gemini 3 Pro Image API:

```bash
uv run scripts/generate_image.py \
  --prompt "<ikea-style prompt>" --filename "step-01.png" --resolution 2K
```

### IKEA-Style Illustration Prompt Template

**CRITICAL:** Use this exact template for consistent IKEA-style output:

```
Create an IKEA-style assembly instruction illustration. Style: clean black line art on white background, 30-degree isometric view, minimal shading (light grey fills only), no gradients or textures, thick outlines, simplified shapes.

Subject: [describe the step - e.g., "shelf panel being attached to side panel"]

Show: [new part] floating 2cm above [target location] with a curved arrow indicating insertion direction. Already-assembled parts rendered as solid unit in lighter grey.

Include: [specific details - callout circle for small connections, quantity marker "×4" for repeated parts, hand icon if grip position matters]

Do NOT include: text labels, realistic textures, shadows, decorative elements, photorealistic rendering.
```

### Step-by-Step Image Generation

**Step 1 (Base):**
```bash
uv run scripts/generate_image.py \
  --prompt "Create an IKEA-style assembly instruction illustration. Style: clean black line art on white background, 30-degree isometric view, minimal shading. Subject: [BASE COMPONENT] sitting on a work surface. Clean, simple, no arrows needed for first step." \
  --filename "step-01-base.png" --resolution 2K
```

**Step 2+ (Action diagrams):**
```bash
uv run scripts/generate_image.py \
  --prompt "Create an IKEA-style assembly instruction illustration. Style: clean black line art on white background, 30-degree isometric view, minimal shading. Subject: [NEW PART] floating above [EXISTING ASSEMBLY] with curved arrow showing insertion direction. The [EXISTING ASSEMBLY] is shown as solid grey unit. Include callout circle showing [CONNECTION DETAIL] if needed." \
  --filename "step-02-attach-part.png" --resolution 2K
```

### Image Types to Generate

| Page Type | Prompt Focus |
|-----------|--------------|
| Cover | Finished assembled product, clean isometric view, product name |
| Parts Inventory | Grid layout of all parts with ID labels (A, B, H1), quantities |
| Tools Required | Simple icons of required tools |
| Assembly Step | Action diagram with floating part + arrow + callout if needed |
| Final Result | Complete assembly, clean isometric, optional checkmark |

## Design Principles

Stanford research: action diagrams reduce assembly time 35% and errors 50%.

- **Fixed Viewpoint** — Same 30° isometric angle every illustration. Never rotate.
- **Action Diagrams** — New parts float toward destination with arrows (not already placed).
- **One Step = One Action** — Never combine multiple operations.
- **Wordless** — No text in steps. Arrows, callouts, quantity markers (×4), hand icons only.
- **Minimal Shading** — Black lines, white background, light grey fill for depth.

See [references/design-principles.md](references/design-principles.md) for all principles.

## Project YAML Schema

```yaml
project:
  name: "Product Name"

parts:
  structural:
    - id: "A"
      name: "Main panel"
    - id: "B"
      name: "Side panel"
  hardware:
    - id: "H1"
      name: "Screw"
      quantity: 4

tools:
  - screwdriver

steps:
  - step: 1
    action: place
    parts: ["A"]
    image_prompt: "Main panel sitting on work surface"
  - step: 2
    action: attach
    parts: ["B", "A"]
    hardware: ["H1"]
    image_prompt: "Side panel floating above main panel with screws, arrows showing attachment"
```

See [references/yaml-schema.md](references/yaml-schema.md) for full schema.

## Complete Workflow Example

```bash
# 1. Generate cover image
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly manual cover. Clean black line art, white background. Show completed product in 30-degree isometric view. Title area at top. Minimal, professional." \
  --filename "cover.png" --resolution 2K

# 2. Generate parts inventory
uv run scripts/generate_image.py \
  --prompt "IKEA-style parts inventory page. Grid layout, black line art on white. Show all parts with ID labels. Quantities shown as ×4 for multiple items." \
  --filename "parts-inventory.png" --resolution 2K

# 3. Generate each assembly step
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly step. Black line art, 30-degree isometric. Show new part floating above existing assembly with curved arrows indicating attachment. Callout circle magnifying connection detail. Base shown in light grey." \
  --filename "step-02.png" --resolution 2K

# 4. Compile PDF (after all images generated)
python3 scripts/render_manual.py project.yaml --output manual.pdf
```

## API Key

Set `GEMINI_API_KEY` environment variable or pass `--api-key` argument.
