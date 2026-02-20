#!/usr/bin/env python3
"""
Page Layout Engine for Assembly Instructions.

Handles page composition, isometric grid, callout positioning, action arrows,
step numbering, and wire routing. Used by render_manual.py.
"""

import drawsvg as dw
import math

# ─── Page Constants ────────────────────────────────────────────────

PAGE_W = 595   # A4 width in points (≈210mm)
PAGE_H = 842   # A4 height in points (≈297mm)
MARGIN = 40
CONTENT_W = PAGE_W - 2 * MARGIN
CONTENT_H = PAGE_H - 2 * MARGIN

# ─── Colors ────────────────────────────────────────────────────────

WIRE_COLORS = {
    "red": "#e63946",
    "black": "#333333",
    "yellow": "#f4a261",
    "green": "#2a9d8f",
    "blue": "#457b9d",
    "white": "#cccccc",
    "orange": "#e76f51",
    "purple": "#7b2cbf",
}

STEP_NUMBER_COLOR = "#333333"
CALLOUT_STROKE = "#666666"
ARROW_COLOR = "#444444"
GRID_COLOR = "#f0f0f0"


# ─── Page Creators ─────────────────────────────────────────────────

def new_page():
    """Create a new blank A4 page."""
    d = dw.Drawing(PAGE_W, PAGE_H)
    d.append(dw.Rectangle(0, 0, PAGE_W, PAGE_H, fill="white"))
    return d

def add_page_border(d):
    """Add subtle border to page."""
    d.append(dw.Rectangle(MARGIN/2, MARGIN/2,
                           PAGE_W - MARGIN, PAGE_H - MARGIN,
                           fill="none", stroke="#e0e0e0", stroke_width=0.5))


# ─── Cover Page ────────────────────────────────────────────────────

def create_cover_page(project_name, version="1.0", description=""):
    """Create the cover page with product name and assembled preview area."""
    d = new_page()
    add_page_border(d)

    # Product name
    d.append(dw.Text(project_name, 28, PAGE_W/2, 80,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="#222", text_anchor="middle", font_weight="bold"))

    if description:
        d.append(dw.Text(description, 14, PAGE_W/2, 110,
                          font_family="Helvetica, Arial, sans-serif",
                          fill="#666", text_anchor="middle"))

    # Large assembly preview area (placeholder frame)
    preview_x = MARGIN + 40
    preview_y = 150
    preview_w = CONTENT_W - 80
    preview_h = 500
    d.append(dw.Rectangle(preview_x, preview_y, preview_w, preview_h,
                           fill="#fafafa", stroke="#ddd", stroke_width=1, rx=8))
    d.append(dw.Text("[ Assembled Product ]", 16, PAGE_W/2, preview_y + preview_h/2,
                      font_family="sans-serif", fill="#ccc", text_anchor="middle"))

    # Version and footer
    d.append(dw.Text(f"v{version}", 10, PAGE_W - MARGIN, PAGE_H - MARGIN/2,
                      font_family="sans-serif", fill="#999", text_anchor="end"))

    return d


# ─── Safety Page ───────────────────────────────────────────────────

def create_safety_page(has_electronics=True, has_soldering=False, two_person=False):
    """Create safety warnings and tips page."""
    d = new_page()
    add_page_border(d)

    y = 60
    d.append(dw.Text("⚠", 36, MARGIN + 20, y + 10,
                      font_family="sans-serif", fill="#e63946"))
    d.append(dw.Text("Before you begin", 20, MARGIN + 60, y,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="#333", font_weight="bold"))
    y += 50

    warnings = []

    if has_electronics:
        warnings.append(("⚡", "Disconnect power before making any wiring changes"))
        warnings.append(("🖐", "Handle circuit boards by edges only — avoid touching chips"))

    if has_soldering:
        warnings.append(("🔥", "Soldering iron gets very hot — use stand, avoid burns"))
        warnings.append(("💨", "Solder in well-ventilated area"))

    if two_person:
        warnings.append(("👥", "Two people recommended for this assembly"))

    warnings.append(("📋", "Verify all parts before starting (see next pages)"))
    warnings.append(("🔧", "Do not overtighten screws — snug is enough"))

    for icon, text in warnings:
        # Warning row
        d.append(dw.Rectangle(MARGIN, y - 5, CONTENT_W, 40,
                               fill="#fff8f0", stroke="#f0e0d0", stroke_width=0.5, rx=4))
        d.append(dw.Text(icon, 20, MARGIN + 25, y + 18,
                          font_family="sans-serif", text_anchor="middle"))
        d.append(dw.Text(text, 12, MARGIN + 55, y + 20,
                          font_family="Helvetica, Arial, sans-serif", fill="#444"))
        y += 50

    # Tools needed section
    y += 20
    d.append(dw.Text("Tools needed:", 14, MARGIN + 10, y,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="#333", font_weight="bold"))

    return d, y + 30  # Return page and Y position for tool icons


# ─── Inventory Pages ───────────────────────────────────────────────

def create_hardware_inventory_page(hardware_items):
    """Create hardware/fastener inventory grid page."""
    d = new_page()
    add_page_border(d)

    d.append(dw.Text("Hardware", 20, PAGE_W/2, 50,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="#333", text_anchor="middle", font_weight="bold"))

    # Grid layout
    cols = 4
    cell_w = CONTENT_W / cols
    cell_h = 100

    for i, item in enumerate(hardware_items):
        col = i % cols
        row = i // cols
        x = MARGIN + col * cell_w
        y = 80 + row * cell_h

        # Cell border
        d.append(dw.Rectangle(x + 5, y + 5, cell_w - 10, cell_h - 10,
                               fill="#fafafa", stroke="#e0e0e0", stroke_width=0.5, rx=4))

        # Component drawing area (center of cell)
        comp_cx = x + cell_w / 2
        comp_cy = y + cell_h / 2 - 10

        # ID label
        d.append(dw.Text(item.get("id", ""), 10, x + 15, y + 20,
                          font_family="monospace", fill="#666", font_weight="bold"))

        # Quantity
        qty = item.get("quantity", 1)
        d.append(dw.Text(f"×{qty}", 14, x + cell_w - 15, y + 22,
                          font_family="sans-serif", fill="#333",
                          text_anchor="end", font_weight="bold"))

        # Name
        d.append(dw.Text(item.get("name", ""), 8, comp_cx, y + cell_h - 15,
                          font_family="sans-serif", fill="#666", text_anchor="middle"))

        # Checkbox
        d.append(dw.Rectangle(x + cell_w - 25, y + cell_h - 25, 12, 12,
                               fill="none", stroke="#ccc", stroke_width=1, rx=2))

    return d

def create_parts_inventory_page(structural_items, electronic_items):
    """Create parts inventory page for structural and electronic components."""
    d = new_page()
    add_page_border(d)

    d.append(dw.Text("Parts", 20, PAGE_W/2, 50,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="#333", text_anchor="middle", font_weight="bold"))

    all_items = []
    for item in structural_items:
        all_items.append({"id": item["id"], "name": item["name"], "type": "structural"})
    for item in electronic_items:
        all_items.append({"id": item["id"], "name": item["name"],
                          "component": item.get("component", ""), "type": "electronic"})

    cols = 3
    cell_w = CONTENT_W / cols
    cell_h = 140

    for i, item in enumerate(all_items):
        col = i % cols
        row = i // cols
        x = MARGIN + col * cell_w
        y = 80 + row * cell_h

        d.append(dw.Rectangle(x + 5, y + 5, cell_w - 10, cell_h - 10,
                               fill="#fafafa", stroke="#e0e0e0", stroke_width=0.5, rx=4))

        # ID badge
        badge_x = x + 15
        badge_y = y + 15
        d.append(dw.Circle(badge_x, badge_y, 12,
                            fill="#333", stroke="none"))
        d.append(dw.Text(item["id"], 10, badge_x, badge_y + 4,
                          font_family="monospace", fill="white",
                          text_anchor="middle", font_weight="bold"))

        # Component drawing area
        comp_cx = x + cell_w / 2
        comp_cy = y + cell_h / 2

        # Placeholder for component rendering
        d.append(dw.Rectangle(comp_cx - 30, comp_cy - 20, 60, 40,
                               fill="#f0f0f0", stroke="#ddd", stroke_width=0.5,
                               stroke_dasharray="4,2", rx=4))

        # Name
        d.append(dw.Text(item["name"], 9, comp_cx, y + cell_h - 15,
                          font_family="sans-serif", fill="#555", text_anchor="middle"))

    return d


# ─── Step Pages ────────────────────────────────────────────────────

def create_step_page(step_number, description=""):
    """Create a step page with number badge and content area."""
    d = new_page()
    add_page_border(d)

    # Step number circle
    badge_x = MARGIN + 30
    badge_y = 50
    d.append(dw.Circle(badge_x, badge_y, 22,
                        fill=STEP_NUMBER_COLOR, stroke="none"))
    d.append(dw.Text(str(step_number), 20, badge_x, badge_y + 7,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="white", text_anchor="middle", font_weight="bold"))

    # Content area frame
    content_y = 90
    content_h = PAGE_H - content_y - MARGIN - 40
    d.append(dw.Rectangle(MARGIN, content_y, CONTENT_W, content_h,
                           fill="#fafafa", stroke="#eee", stroke_width=0.5, rx=4))

    return d, content_y, content_h


# ─── Visual Elements ───────────────────────────────────────────────

def draw_action_arrow(d, x1, y1, x2, y2, color=ARROW_COLOR, width=2, dashed=False):
    """Draw an action arrow from source to destination."""
    # Arrow line
    kwargs = {"stroke": color, "stroke_width": width}
    if dashed:
        kwargs["stroke_dasharray"] = "6,3"
    d.append(dw.Line(x1, y1, x2, y2, **kwargs))

    # Arrowhead
    angle = math.atan2(y2 - y1, x2 - x1)
    head_len = 10
    head_angle = math.radians(25)

    ax1 = x2 - head_len * math.cos(angle - head_angle)
    ay1 = y2 - head_len * math.sin(angle - head_angle)
    ax2 = x2 - head_len * math.cos(angle + head_angle)
    ay2 = y2 - head_len * math.sin(angle + head_angle)

    d.append(dw.Lines(x2, y2, ax1, ay1, ax2, ay2,
                       close=True, fill=color, stroke="none"))

def draw_callout_circle(d, focus_x, focus_y, callout_x, callout_y, radius=60):
    """Draw a magnified callout circle with leader line."""
    # Leader line
    d.append(dw.Line(focus_x, focus_y, callout_x, callout_y,
                      stroke=CALLOUT_STROKE, stroke_width=1, stroke_dasharray="4,2"))

    # Small indicator circle at focus point
    d.append(dw.Circle(focus_x, focus_y, 5,
                        fill="none", stroke=CALLOUT_STROKE, stroke_width=1))

    # Callout circle
    d.append(dw.Circle(callout_x, callout_y, radius,
                        fill="white", stroke=CALLOUT_STROKE, stroke_width=1.5))

    # Return center coords for drawing magnified content inside
    return callout_x, callout_y

def draw_quantity_marker(d, x, y, quantity):
    """Draw a ×N quantity marker."""
    d.append(dw.Text(f"×{quantity}", 14, x, y,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="#333", font_weight="bold", text_anchor="start"))

def draw_checkmark(d, x, y, size=16):
    """Draw a green checkmark."""
    d.append(dw.Circle(x, y, size/2, fill="#2a9d8f", stroke="none"))
    # Check path
    d.append(dw.Lines(
        x - size*0.25, y,
        x - size*0.05, y + size*0.2,
        x + size*0.3, y - size*0.25,
        fill="none", stroke="white", stroke_width=2, stroke_linecap="round"
    ))

def draw_x_mark(d, x, y, size=16):
    """Draw a red X mark."""
    d.append(dw.Circle(x, y, size/2, fill="#e63946", stroke="none"))
    r = size * 0.22
    d.append(dw.Line(x - r, y - r, x + r, y + r,
                      stroke="white", stroke_width=2, stroke_linecap="round"))
    d.append(dw.Line(x - r, y + r, x + r, y - r,
                      stroke="white", stroke_width=2, stroke_linecap="round"))

def draw_do_dont(d, x, y, do_text="", dont_text=""):
    """Draw a do/don't comparison side by side."""
    mid = x + 100
    draw_checkmark(d, x + 10, y + 10)
    draw_x_mark(d, mid + 10, y + 10)


# ─── Wire Drawing ──────────────────────────────────────────────────

def draw_wire(d, points, color="red", width=2.5, label=""):
    """Draw a color-coded wire path through a series of points."""
    wire_color = WIRE_COLORS.get(color, color)
    if len(points) < 2:
        return

    # Build path
    path_d = f"M {points[0][0]} {points[0][1]}"
    for px, py in points[1:]:
        path_d += f" L {px} {py}"

    d.append(dw.Path(path_d, fill="none", stroke=wire_color,
                      stroke_width=width, stroke_linecap="round",
                      stroke_linejoin="round"))

    # Wire dots at endpoints
    for px, py in [points[0], points[-1]]:
        d.append(dw.Circle(px, py, 3, fill=wire_color, stroke="white", stroke_width=1))

    # Label
    if label:
        mid_idx = len(points) // 2
        mx, my = points[mid_idx]
        d.append(dw.Text(label, 7, mx + 5, my - 5,
                          font_family="sans-serif", fill=wire_color))

def draw_wire_legend(d, x, y, wires):
    """Draw a wire color legend."""
    d.append(dw.Text("Wire Legend", 10, x, y,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="#333", font_weight="bold"))
    y += 18
    for wire in wires:
        color = WIRE_COLORS.get(wire.get("color", "black"), "#333")
        d.append(dw.Line(x, y, x + 20, y, stroke=color, stroke_width=3, stroke_linecap="round"))
        label = wire.get("label", wire.get("color", ""))
        from_part = wire.get("from", {}).get("part", "")
        from_pin = wire.get("from", {}).get("pin", "")
        to_part = wire.get("to", {}).get("part", "")
        to_pin = wire.get("to", {}).get("pin", "")
        desc = f"{from_part}:{from_pin} → {to_part}:{to_pin}"
        if label:
            desc = f"{label} ({desc})"
        d.append(dw.Text(desc, 8, x + 28, y + 3,
                          font_family="monospace", fill="#555"))
        y += 18
    return y


# ─── Wiring Diagram Page ──────────────────────────────────────────

def create_wiring_diagram_page(project_name):
    """Create the wiring diagram overview page."""
    d = new_page()
    add_page_border(d)

    d.append(dw.Text("Wiring Diagram", 20, PAGE_W/2, 50,
                      font_family="Helvetica, Arial, sans-serif",
                      fill="#333", text_anchor="middle", font_weight="bold"))

    d.append(dw.Text(project_name, 12, PAGE_W/2, 70,
                      font_family="sans-serif", fill="#888", text_anchor="middle"))

    # Content area
    d.append(dw.Rectangle(MARGIN, 90, CONTENT_W, PAGE_H - 90 - MARGIN - 60,
                           fill="#fafafa", stroke="#eee", stroke_width=0.5, rx=4))

    return d


# ─── Utility ───────────────────────────────────────────────────────

def iso_to_page(ix, iy, iz=0, page_cx=None, page_cy=None):
    """Convert isometric grid coordinates to page coordinates.

    Centers the isometric view in the page content area.
    """
    if page_cx is None:
        page_cx = PAGE_W / 2
    if page_cy is None:
        page_cy = PAGE_H / 2

    cos30 = math.cos(math.radians(30))
    sin30 = math.sin(math.radians(30))

    sx = (ix - iy) * cos30
    sy = (ix + iy) * sin30 - iz

    return page_cx + sx, page_cy + sy
