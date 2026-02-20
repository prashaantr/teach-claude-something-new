---
name: mockup
description: |
  Generate realistic FINISHED PRODUCT photos only. Uses nano-banana-pro ($GEMINI_API_KEY).
  Use for: product photos, mockups, "what will it look like when done", TaskRabbit listing images.
  DO NOT use for: assembly instructions, build guides - use assembly-instructions instead.
---

# Product Mockups (Finished Photos Only)

Generate realistic photos of the FINISHED product. No instructions, no steps, just the final result.

**For build instructions → use assembly-instructions skill instead.**

## When to Use

- "Show me the finished product"
- "Create a photo for my TaskRabbit listing"
- "What will this look like when assembled?"
- "Generate a mockup"

## How It Works

This skill wraps nano-banana-pro with prompts optimized for realistic product photography:

1. Take the user's description of what they're building
2. Enhance the prompt for photorealistic output
3. Generate via nano-banana-pro

## Usage

Use the nano-banana-pro skill directly with enhanced prompts:

```bash
uv run /home/node/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Professional product photo of [ITEM], clean white background, studio lighting, high detail, realistic" \
  --filename "mockup-[name].png" \
  --resolution 2K
```

## Prompt Templates

### Product on White Background
```
Professional product photo of [ITEM], clean white background, soft studio lighting, high detail, commercial photography style
```

### In-Context / Lifestyle
```
Realistic photo of [ITEM] in use, natural lighting, real-world setting, professional photography
```

### Technical/Engineering
```
Technical product shot of [ITEM], showing details and construction, clean background, sharp focus
```

### Before/After
```
Side-by-side comparison showing [BEFORE STATE] and [AFTER STATE], clean presentation
```

## Examples

**TaskRabbit furniture assembly mockup:**
```bash
uv run /home/node/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Professional photo of assembled IKEA KALLAX shelf unit, white finish, styled with books and plants, modern living room setting, natural lighting" \
  --filename "2026-02-19-kallax-mockup.png" \
  --resolution 2K
```

**Arduino project visualization:**
```bash
uv run /home/node/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Realistic photo of Arduino Nano weather station in 3D printed enclosure, small OLED display showing temperature, clean white background, product photography" \
  --filename "2026-02-19-weather-station.png" \
  --resolution 2K
```

**Before/After repair:**
```bash
uv run /home/node/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Side-by-side comparison: damaged wooden chair with broken leg on left, fully repaired and refinished chair on right, clean white background" \
  --filename "2026-02-19-chair-repair.png" \
  --resolution 2K
```
