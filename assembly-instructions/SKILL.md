---
name: assembly-instructions
description: >
  Generate IKEA-style visual assembly instruction manuals as multi-page PDFs for hardware projects —
  especially Arduino/electronics builds, IoT devices, 3D-printed enclosures, and maker projects.
  Use this skill whenever the user wants to create assembly instructions, build guides, wiring diagrams,
  hardware setup manuals, or step-by-step visual instructions for physical builds. Also trigger when
  the user mentions "instruction manual", "assembly guide", "build instructions", "wiring guide",
  "hardware documentation", "maker instructions", or wants to document how to put together any
  physical project for a non-technical person (like a TaskRabbit worker or field technician).
  The output is a professional multi-page PDF with wordless IKEA-style illustrations including
  parts inventories, step-by-step diagrams with callouts, color-coded wiring, and action arrows.
---

# Assembly Instructions Generator

Generate IKEA-style visual assembly manuals for hardware/electronics projects as multi-page PDFs.

## When to Use This Skill

- User wants to document how to build/assemble a physical project
- User needs wiring instructions for Arduino or electronics
- User wants a "manual" or "guide" for a hardware build
- User mentions TaskRabbit, field technician, or non-technical assembler
- User has a YAML/JSON project description to turn into visual instructions
- User wants to create setup documentation for an IoT device

## Quick Start

The generation pipeline has 3 phases:

1. **Define** — Structure the project as YAML (or help the user create one interactively)
2. **Render** — Run the rendering pipeline to generate SVG pages
3. **Compile** — Assemble pages into a multi-page PDF

```bash
# Install dependencies
pip install drawsvg cairosvg reportlab pyyaml --break-system-packages

# Phase 1: If user provides YAML, validate it
python3 scripts/validate_project.py project.yaml

# Phase 2+3: Render and compile into PDF
python3 scripts/render_manual.py project.yaml --output manual.pdf
```

If the user describes their project conversationally, help them build the YAML
interactively by asking about parts, connections, and assembly order.

## Design Principles (Why This Works)

These manuals follow validated cognitive design principles from Stanford research that
cut assembly time 35% and errors 50%. The principles are baked into the rendering scripts:

- **Fixed Viewpoint** — Same isometric angle in every illustration. Never rotate.
- **Action Diagrams** — New parts float toward destination with arrows (not already placed).
- **One Step = One Action** — Never combine multiple operations in a single step.
- **Progressive Disclosure** — Start with recognizable sub-assemblies. Show progress early.
- **Wordless** — No text in steps. Arrows, callouts, quantity markers (×4), hand icons only.

For the full 12 principles, read `references/design-principles.md`.

## Project YAML Schema

The input is a YAML file. See `references/yaml-schema.md` for the full spec.

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
    - id: "E2"
      name: "PIR Sensor"
      component: pir_sensor

tools:
  - phillips_screwdriver
  - wire_strippers

wiring:
  - from: {part: "E1", pin: "D2"}
    to: {part: "E2", pin: "OUT"}
    color: yellow

steps:
  - step: 1
    action: place
    parts: ["A"]
    description: "Position bracket"
  - step: 2
    action: attach
    parts: ["E1", "A"]
    hardware: ["H1"]
    description: "Mount Arduino with screws"
    callout: true
  - step: 3
    action: wire
    wiring: all
    description: "Connect wiring"
```

## Component Library

The skill includes pre-drawn SVG components. See `references/component-catalog.md` for
the full list with pin maps and dimensions.

**Microcontrollers:** arduino_uno, arduino_nano, esp32, raspberry_pi_pico
**Sensors:** pir_sensor, ultrasonic_sensor, dht11_temp, photoresistor, button, potentiometer
**Output:** led_single, led_rgb, servo_motor, relay_module, buzzer, lcd_16x2
**Power:** battery_holder_4aa, usb_cable, dc_barrel_jack
**Connectivity:** breadboard_half, breadboard_mini, jumper_wire
**Structural:** rect, l_bracket, standoff, enclosure_box
**Hardware:** screw_phillips, screw_hex, nut, wall_anchor, cable_tie

## Page Sequence Generated

1. **Cover** — Product name + assembled product illustration
2. **Safety/Tips** — ESD warning, power-off-before-wiring, two-person if needed
3. **Hardware Inventory** — Grid of all fasteners with IDs and quantities
4. **Parts Inventory** — All structural and electronic components with IDs
5. **Assembly Steps** (1 per page) — Isometric drawing, action arrows, callouts
6. **Wiring Diagram** — Complete color-coded wiring overview with pin labels

## Rendering Scripts

Run in order of the pipeline:

1. `scripts/components.py` — SVG component library (run with `--list` or `--render <name>`)
2. `scripts/validate_project.py` — Validates YAML input
3. `scripts/render_manual.py` — Full pipeline: YAML → SVG pages → PDF
4. `scripts/compile_pdf.py` — Standalone SVG→PDF compiler (used internally)

## Working With the User

1. **YAML provided** → validate, render, present PDF
2. **Conversational description** → interview for parts/connections/order → generate YAML → render
3. **Photos or schematics uploaded** → analyze, extract component list → generate YAML → render

Always output final PDF to `/mnt/user-data/outputs/` and present it.
