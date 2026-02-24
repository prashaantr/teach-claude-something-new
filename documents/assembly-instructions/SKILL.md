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

## Core Principle: One Step = One Image

Each assembly step gets its own dedicated image. Generate them sequentially, maintaining visual consistency across all steps.

## Workflow

1. **Define Parts** — List all parts with IDs and descriptions
2. **Generate Part Illustrations** — Create individual reference images for each part
3. **Generate Step Illustrations** — One image per assembly action, referencing the part images
4. **Compile** — Assemble into multi-page PDF

## Maintaining Visual Consistency

**CRITICAL:** All images must look like they belong to the same manual.

### Step 1: Establish the Visual Style

First, generate a "style reference" image of the completed product:

```bash
uv run scripts/generate_image.py \
  --prompt "IKEA-style technical illustration. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Simplified geometric shapes. Subject: [DESCRIBE YOUR COMPLETED PRODUCT]" \
  --filename "00-style-reference.png" --resolution 2K
```

### Step 2: Generate Individual Part Images

Generate each part as a separate image. Use identical style language:

```bash
# Part A
uv run scripts/generate_image.py \
  --prompt "IKEA-style technical illustration. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Simplified geometric shapes. Subject: [PART A DESCRIPTION]. Show part isolated, centered, with label 'A' in corner." \
  --filename "part-A.png" --resolution 2K

# Part B
uv run scripts/generate_image.py \
  --prompt "IKEA-style technical illustration. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Simplified geometric shapes. Subject: [PART B DESCRIPTION]. Show part isolated, centered, with label 'B' in corner." \
  --filename "part-B.png" --resolution 2K

# Hardware H1 (with quantity)
uv run scripts/generate_image.py \
  --prompt "IKEA-style technical illustration. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Simplified geometric shapes. Subject: [HARDWARE DESCRIPTION]. Show single item with '×4' quantity marker." \
  --filename "part-H1.png" --resolution 2K
```

### Step 3: Generate Step-by-Step Action Images

Each step shows ONE action. Reference the established part appearances:

```bash
# Step 1: Place base part
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly instruction. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: [PART A] sitting on work surface. No arrows needed. Part labeled 'A'." \
  --filename "step-01.png" --resolution 2K

# Step 2: Attach second part
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly instruction. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: [PART B] floating 3cm above [PART A] with curved arrow showing attachment direction. [PART A] shown as solid grey base. Parts labeled." \
  --filename "step-02.png" --resolution 2K

# Step 3: Insert hardware
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly instruction. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: Screw floating above hole in assembly with arrow showing insertion. Callout circle magnifying the screw and hole detail. '×4' marker indicating four screws needed." \
  --filename "step-03.png" --resolution 2K
```

## Standard Prompt Components

Always include these in every prompt for consistency:

```
IKEA-style technical illustration. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Simplified geometric shapes.
```

Then add the step-specific subject.

## Action Diagram Rules

| Action Type | Visual Treatment |
|-------------|------------------|
| Place | Part sitting on surface, no arrows |
| Attach | New part floating above target with curved arrow |
| Insert | Hardware floating near hole with straight arrow, callout circle for detail |
| Rotate | Curved arrow around part showing rotation direction |
| Flip | Part shown in two positions with flip arrow |
| Connect | Two parts with line/arrow between connection points |

## Visual Symbols

- **Arrows** — Curved for attachment direction, straight for insertion
- **Callout circles** — Magnified detail connected by thin line
- **Quantity markers** — "×4" next to repeated items
- **Hand icons** — Show grip position when relevant
- **Checkmark** — Completion indicator

## Design Principles

Stanford research: action diagrams reduce assembly time 35% and errors 50%.

- **Fixed Viewpoint** — Same 30° isometric angle in every image
- **Action Diagrams** — New parts float toward destination (not already placed)
- **One Step = One Action** — Never combine operations
- **Wordless** — No text except part labels and quantity markers
- **Consistent Parts** — Same part must look identical across all steps

## Example: 4-Step Assembly

```bash
# Style reference
uv run scripts/generate_image.py \
  --prompt "IKEA-style technical illustration. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: Simple wooden stool with four legs and round seat, fully assembled." \
  --filename "00-reference.png" --resolution 2K

# Parts inventory - each part separate
uv run scripts/generate_image.py \
  --prompt "IKEA-style technical illustration. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: Round wooden seat, isolated, label 'A'." \
  --filename "part-A-seat.png" --resolution 2K

uv run scripts/generate_image.py \
  --prompt "IKEA-style technical illustration. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: Single wooden stool leg, tapered, isolated, label 'B', with '×4' marker." \
  --filename "part-B-leg.png" --resolution 2K

# Step 1
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly instruction. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: Round wooden seat (A) placed upside-down on work surface, showing four leg holes visible on underside." \
  --filename "step-01.png" --resolution 2K

# Step 2
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly instruction. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: One wooden leg (B) floating above corner hole of upside-down seat with curved arrow showing insertion. Seat shown in light grey. '×4' marker." \
  --filename "step-02.png" --resolution 2K

# Step 3
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly instruction. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: All four legs now inserted into upside-down seat. Checkmark indicator." \
  --filename "step-03.png" --resolution 2K

# Step 4
uv run scripts/generate_image.py \
  --prompt "IKEA-style assembly instruction. Clean black line art on pure white background. 30-degree isometric view. Minimal shading using only light grey fills. No gradients, no textures, no shadows. Thick uniform outlines. Subject: Completed stool being flipped right-side-up, shown with curved flip arrow indicating rotation." \
  --filename "step-04.png" --resolution 2K
```

## API Key

Set `GEMINI_API_KEY` environment variable or pass `--api-key` argument.

## Compiling to PDF

After generating all images:

```bash
python3 scripts/render_manual.py project.yaml --output manual.pdf
```
