#!/usr/bin/env python3
"""
Assembly Instructions Rendering Pipeline.

Reads a project YAML file and generates a multi-page PDF manual with
IKEA-style assembly instructions.

Usage:
    python3 render_manual.py project.yaml --output manual.pdf
    python3 render_manual.py project.yaml --output-dir ./build  # SVG pages only
"""

import sys
import os
import yaml
import math

# Add scripts dir to path for imports
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import drawsvg as dw
from components import COMPONENTS, render_component, iso_point, iso_box, iso_rect_top
from layout import (
    PAGE_W, PAGE_H, MARGIN, CONTENT_W, CONTENT_H, WIRE_COLORS,
    new_page, add_page_border,
    create_cover_page, create_safety_page,
    create_hardware_inventory_page, create_parts_inventory_page,
    create_step_page, create_wiring_diagram_page,
    draw_action_arrow, draw_callout_circle, draw_quantity_marker,
    draw_wire, draw_wire_legend,
    iso_to_page
)


def load_project(yaml_path):
    """Load and validate project YAML."""
    with open(yaml_path, 'r') as f:
        project = yaml.safe_load(f)

    # Basic validation
    assert 'project' in project, "Missing 'project' section"
    assert 'name' in project['project'], "Missing project name"
    assert 'steps' in project, "Missing 'steps' section"

    # Defaults
    project.setdefault('parts', {})
    project['parts'].setdefault('structural', [])
    project['parts'].setdefault('hardware', [])
    project['parts'].setdefault('electronic', [])
    project.setdefault('tools', [])
    project.setdefault('wiring', [])
    project.setdefault('safety', [])

    return project


def render_cover(project):
    """Render cover page with assembled preview."""
    name = project['project']['name']
    version = project['project'].get('version', '1.0')
    desc = project['project'].get('description', '')

    d = create_cover_page(name, version, desc)

    # Render electronic components in the preview area as a collage
    preview_cx = PAGE_W / 2
    preview_cy = 400
    g = dw.Group()

    electronic = project['parts'].get('electronic', [])
    n = len(electronic)
    if n > 0:
        spacing = min(120, CONTENT_W / (n + 1))
        start_x = preview_cx - (n - 1) * spacing / 2
        for i, part in enumerate(electronic):
            comp_name = part.get('component', '')
            if comp_name in COMPONENTS:
                pg = dw.Group(transform=f"translate({start_x + i * spacing},{preview_cy})")
                import inspect
                func = COMPONENTS[comp_name]
                sig = inspect.signature(func)
                kwargs = {"g": pg, "cx": 0, "cy": 0}
                if "show_pins" in sig.parameters:
                    kwargs["show_pins"] = False
                func(**kwargs)
                g.append(pg)

    d.append(g)
    return d


def render_safety(project):
    """Render safety and tips page."""
    has_electronics = len(project['parts']['electronic']) > 0
    has_soldering = 'soldering_iron' in project.get('tools', [])
    two_person = project['project'].get('two_person', False)

    d, tool_y = create_safety_page(has_electronics, has_soldering, two_person)

    # Add tool icons
    tools = project.get('tools', [])
    tool_names = {
        'phillips_screwdriver': '🔧 Phillips screwdriver',
        'hex_wrench': '🔧 Hex wrench',
        'wire_strippers': '✂️ Wire strippers',
        'soldering_iron': '🔥 Soldering iron',
        'drill': '🔩 Drill',
        'pliers': '🔧 Pliers',
        'multimeter': '📊 Multimeter',
    }

    for i, tool in enumerate(tools):
        name = tool_names.get(tool, f"🔧 {tool}")
        d.append(dw.Text(name, 12, MARGIN + 30, tool_y + i * 25,
                          font_family="sans-serif", fill="#444"))

    return d


def render_hardware_inventory(project):
    """Render hardware inventory page with component drawings."""
    hardware = project['parts']['hardware']
    if not hardware:
        return None

    d = create_hardware_inventory_page(hardware)

    # Draw actual hardware components in cells
    cols = 4
    cell_w = CONTENT_W / cols
    cell_h = 100

    for i, item in enumerate(hardware):
        col = i % cols
        row = i // cols
        x = MARGIN + col * cell_w + cell_w / 2
        y = 80 + row * cell_h + cell_h / 2 - 5

        comp_type = item.get('type', 'screw_phillips')
        if comp_type in COMPONENTS:
            pg = dw.Group(transform=f"translate({x},{y}) scale(1.5)")
            import inspect
            func = COMPONENTS[comp_type]
            sig = inspect.signature(func)
            kwargs = {"g": pg, "cx": 0, "cy": 0}
            if "scale" in sig.parameters:
                kwargs["scale"] = 1.0
            if "show_pins" in sig.parameters:
                kwargs["show_pins"] = False
            func(**kwargs)
            d.append(pg)

    return d


def render_parts_inventory(project):
    """Render parts inventory page with component drawings."""
    structural = project['parts']['structural']
    electronic = project['parts']['electronic']

    if not structural and not electronic:
        return None

    d = create_parts_inventory_page(structural, electronic)

    # Draw actual components in cells
    all_items = structural + electronic
    cols = 3
    cell_w = CONTENT_W / cols
    cell_h = 140

    for i, item in enumerate(all_items):
        col = i % cols
        row = i // cols
        x = MARGIN + col * cell_w + cell_w / 2
        y = 80 + row * cell_h + cell_h / 2

        comp_name = item.get('component', item.get('shape', ''))
        if comp_name in COMPONENTS:
            pg = dw.Group(transform=f"translate({x},{y}) scale(0.9)")
            import inspect
            func = COMPONENTS[comp_name]
            sig = inspect.signature(func)
            kwargs = {"g": pg, "cx": 0, "cy": 0}
            if "show_pins" in sig.parameters:
                kwargs["show_pins"] = True
            # Handle parametric components
            if comp_name == "rect" and "dimensions" in item:
                kwargs["w"] = item["dimensions"].get("w", 80)
                kwargs["h"] = item["dimensions"].get("h", 50)
            func(**kwargs)
            d.append(pg)

    return d


def render_step(project, step_data, step_index):
    """Render a single assembly step page."""
    step_num = step_data.get('step', step_index + 1)
    d, content_y, content_h = create_step_page(step_num)

    # Main illustration area
    main_cx = PAGE_W / 2
    main_cy = content_y + content_h / 2 - 40
    g = dw.Group()

    action = step_data.get('action', 'place')
    parts = step_data.get('parts', [])
    hardware = step_data.get('hardware', [])

    # Build a lookup for all parts
    all_parts = {}
    for p in project['parts']['structural']:
        all_parts[p['id']] = p
    for p in project['parts']['electronic']:
        all_parts[p['id']] = p
    for p in project['parts']['hardware']:
        all_parts[p['id']] = p

    # Position parts in the illustration
    # For simplicity: place components horizontally centered, with new parts offset above
    n_parts = len(parts)
    if n_parts > 0:
        spacing = min(140, (CONTENT_W - 80) / max(n_parts, 1))
        start_x = main_cx - (n_parts - 1) * spacing / 2

        for i, part_id in enumerate(parts):
            part = all_parts.get(part_id, {})
            comp_name = part.get('component', part.get('shape', part.get('type', '')))

            px = start_x + i * spacing
            py = main_cy

            # For action=attach/insert: offset the attaching part above with arrow
            if action in ('attach', 'insert', 'wire') and i > 0:
                py = main_cy - 80  # Float above
                # Draw action arrow from floating part to destination
                draw_action_arrow(d, px, py + 30, px, main_cy - 30,
                                   color="#555", width=2, dashed=True)

            if comp_name and comp_name in COMPONENTS:
                import inspect
                pg = dw.Group(transform=f"translate({px},{py})")
                func = COMPONENTS[comp_name]
                sig = inspect.signature(func)
                kwargs = {"g": pg, "cx": 0, "cy": 0}
                if "show_pins" in sig.parameters:
                    kwargs["show_pins"] = (action == 'wire')
                if comp_name == "rect" and "dimensions" in part:
                    kwargs["w"] = part["dimensions"].get("w", 80)
                    kwargs["h"] = part["dimensions"].get("h", 50)
                func(**kwargs)
                g.append(pg)

            # Part ID label
            d.append(dw.Text(part_id, 10, px, py + 50,
                              font_family="monospace", fill="#666",
                              text_anchor="middle", font_weight="bold"))

    # Draw hardware callout if requested
    if step_data.get('callout', False) and hardware:
        hw_item = all_parts.get(hardware[0], {})
        hw_type = hw_item.get('type', 'screw_phillips')
        callout_x = PAGE_W - MARGIN - 80
        callout_y = content_y + 80

        cx_out, cy_out = draw_callout_circle(d, main_cx + 40, main_cy,
                                              callout_x, callout_y, radius=50)

        # Draw hardware inside callout
        if hw_type in COMPONENTS:
            import inspect
            cg = dw.Group(transform=f"translate({cx_out},{cy_out}) scale(2)")
            func = COMPONENTS[hw_type]
            sig = inspect.signature(func)
            kwargs = {"g": cg, "cx": 0, "cy": 0}
            if "scale" in sig.parameters:
                kwargs["scale"] = 1.0
            func(**kwargs)
            d.append(cg)

    # Quantity marker
    repeat = step_data.get('repeat', 0)
    if repeat > 0:
        draw_quantity_marker(d, main_cx + 80, main_cy - 50, repeat)

    # Wiring overlay
    if action == 'wire' and project.get('wiring'):
        wiring = project['wiring']
        legend_y = content_y + content_h - 20
        draw_wire_legend(d, MARGIN + 20, legend_y, wiring)

        # Draw simplified wire paths
        for wi, wire in enumerate(wiring):
            color = wire.get('color', 'black')
            wire_color = WIRE_COLORS.get(color, "#333")
            # Simple L-shaped wire routes
            wy = main_cy + 30 + wi * 12
            points = [
                (main_cx - 60, wy),
                (main_cx, wy + 5),
                (main_cx + 60, wy),
            ]
            draw_wire(d, points, color=color, label=wire.get('label', ''))

    d.append(g)
    return d


def render_wiring_diagram(project):
    """Render the complete wiring diagram page."""
    wiring = project.get('wiring', [])
    if not wiring:
        return None

    d = create_wiring_diagram_page(project['project']['name'])

    # Collect all electronic parts involved in wiring
    electronic = project['parts']['electronic']
    n = len(electronic)
    if n == 0:
        return d

    # Position components in a circle/row
    main_cx = PAGE_W / 2
    main_cy = PAGE_H / 2 - 40
    spacing = min(160, (CONTENT_W - 80) / max(n, 1))
    start_x = main_cx - (n - 1) * spacing / 2

    part_positions = {}
    for i, part in enumerate(electronic):
        px = start_x + i * spacing
        py = main_cy
        part_positions[part['id']] = (px, py)

        comp_name = part.get('component', '')
        if comp_name in COMPONENTS:
            import inspect
            pg = dw.Group(transform=f"translate({px},{py})")
            func = COMPONENTS[comp_name]
            sig = inspect.signature(func)
            kwargs = {"g": pg, "cx": 0, "cy": 0}
            if "show_pins" in sig.parameters:
                kwargs["show_pins"] = True
            func(**kwargs)
            d.append(pg)

        # Part label
        d.append(dw.Text(f"{part['id']}: {part['name']}", 9, px, py + 55,
                          font_family="sans-serif", fill="#555", text_anchor="middle"))

    # Draw wires
    for wire in wiring:
        from_id = wire.get('from', {}).get('part', '')
        to_id = wire.get('to', {}).get('part', '')
        color = wire.get('color', 'black')

        if from_id in part_positions and to_id in part_positions:
            fx, fy = part_positions[from_id]
            tx, ty = part_positions[to_id]
            # Route wire with offset to avoid overlap
            mid_y = max(fy, ty) + 40 + wiring.index(wire) * 10
            points = [(fx + 10, fy + 30), (fx + 10, mid_y), (tx - 10, mid_y), (tx - 10, ty + 30)]
            draw_wire(d, points, color=color, label=wire.get('label', ''))

    # Wire legend
    draw_wire_legend(d, MARGIN + 20, PAGE_H - MARGIN - 100, wiring)

    return d


def render_manual(yaml_path, output_path=None, output_dir=None):
    """Full rendering pipeline: YAML → SVG pages → PDF."""
    project = load_project(yaml_path)

    print(f"📋 Generating assembly instructions for: {project['project']['name']}")
    pages = []

    # 1. Cover page
    print("  📄 Cover page...")
    pages.append(render_cover(project))

    # 2. Safety page
    print("  📄 Safety page...")
    pages.append(render_safety(project))

    # 3. Hardware inventory
    print("  📄 Hardware inventory...")
    hw_page = render_hardware_inventory(project)
    if hw_page:
        pages.append(hw_page)

    # 4. Parts inventory
    print("  📄 Parts inventory...")
    parts_page = render_parts_inventory(project)
    if parts_page:
        pages.append(parts_page)

    # 5. Assembly steps
    for i, step in enumerate(project['steps']):
        step_num = step.get('step', i + 1)
        print(f"  📄 Step {step_num}...")
        pages.append(render_step(project, step, i))

    # 6. Wiring diagram
    if project.get('wiring'):
        print("  📄 Wiring diagram...")
        wd = render_wiring_diagram(project)
        if wd:
            pages.append(wd)

    # Save SVGs
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        svg_paths = []
        for i, page in enumerate(pages):
            svg_path = os.path.join(output_dir, f"page_{i:02d}.svg")
            page.save_svg(svg_path)
            svg_paths.append(svg_path)
            print(f"    → {svg_path}")
        return svg_paths

    # Compile to PDF
    if output_path is None:
        name = project['project']['name'].lower().replace(' ', '_')
        output_path = f"{name}_assembly.pdf"

    print(f"  📄 Compiling PDF...")
    compile_to_pdf(pages, output_path)
    print(f"\n✅ Manual generated: {output_path}")
    print(f"   {len(pages)} pages total")
    return output_path


def compile_to_pdf(pages, output_path):
    """Compile SVG pages into a multi-page PDF."""
    import tempfile
    import cairosvg
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader

    temp_dir = tempfile.mkdtemp()

    # Convert each SVG to PNG first (more reliable than direct SVG→PDF)
    png_paths = []
    for i, page in enumerate(pages):
        svg_path = os.path.join(temp_dir, f"page_{i:02d}.svg")
        png_path = os.path.join(temp_dir, f"page_{i:02d}.png")
        page.save_svg(svg_path)

        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=int(PAGE_W * 2),   # 2x for quality
            output_height=int(PAGE_H * 2),
        )
        png_paths.append(png_path)

    # Assemble PDF with reportlab
    c = canvas.Canvas(output_path, pagesize=A4)
    for png_path in png_paths:
        img = ImageReader(png_path)
        c.drawImage(img, 0, 0, width=A4[0], height=A4[1],
                     preserveAspectRatio=True, anchor='c')
        c.showPage()
    c.save()

    # Cleanup
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)


# ─── CLI ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 render_manual.py project.yaml --output manual.pdf")
        print("  python3 render_manual.py project.yaml --output-dir ./build")
        sys.exit(1)

    yaml_path = sys.argv[1]

    output_path = None
    output_dir = None

    if "--output" in sys.argv:
        output_path = sys.argv[sys.argv.index("--output") + 1]
    if "--output-dir" in sys.argv:
        output_dir = sys.argv[sys.argv.index("--output-dir") + 1]

    render_manual(yaml_path, output_path=output_path, output_dir=output_dir)
