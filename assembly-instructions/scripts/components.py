#!/usr/bin/env python3
"""
SVG Component Library for Assembly Instructions.

Renders electronic components, hardware, and structural parts as SVG groups
using drawsvg. Each component is drawn in a consistent isometric style with
labeled pins for wiring diagrams.

Usage:
    python3 components.py --list                    # List all components
    python3 components.py --render arduino_nano     # Render single component
    python3 components.py --render-all --output-dir ./previews  # Render all
"""

import drawsvg as dw
import sys
import os
import math

# ─── Isometric Helpers ─────────────────────────────────────────────

ISO_ANGLE = math.radians(30)
COS30 = math.cos(ISO_ANGLE)
SIN30 = math.sin(ISO_ANGLE)

def iso_x(x, y):
    """Convert grid (x,y) to screen X in isometric projection."""
    return (x - y) * COS30

def iso_y(x, y, z=0):
    """Convert grid (x,y,z) to screen Y in isometric projection."""
    return (x + y) * SIN30 - z

def iso_point(x, y, z=0):
    """Convert 3D grid coords to 2D screen coords."""
    return (iso_x(x, y), iso_y(x, y, z))

def iso_rect_top(g, x, y, z, w, h, fill="#e0e0e0", stroke="#333", sw=1.5):
    """Draw the top face of an isometric box."""
    p1 = iso_point(x, y, z)
    p2 = iso_point(x + w, y, z)
    p3 = iso_point(x + w, y + h, z)
    p4 = iso_point(x, y + h, z)
    g.append(dw.Lines(
        p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p4[0], p4[1],
        close=True, fill=fill, stroke=stroke, stroke_width=sw
    ))

def iso_rect_right(g, x, y, z, h, d, fill="#c0c0c0", stroke="#333", sw=1.5):
    """Draw the right face of an isometric box."""
    p1 = iso_point(x, y + h, z)
    p2 = iso_point(x, y + h, z - d)
    p3 = iso_point(x, y, z - d) if False else iso_point(x, y + h, z - d)
    # Right face: front-bottom edge
    pb1 = iso_point(x, y + h, z)
    pb2 = iso_point(x, y + h, z - d)
    pb3 = iso_point(x + 0, y + h + 0, z - d)  # need to go along y=h edge
    # Simpler approach: draw as polygon
    tl = iso_point(x, y, z)
    tr = iso_point(x, y + h, z)
    br = iso_point(x, y + h, z - d)
    bl = iso_point(x, y, z - d)
    g.append(dw.Lines(
        tr[0], tr[1], br[0], br[1], bl[0], bl[1], tl[0], tl[1],
        close=True, fill=fill, stroke=stroke, stroke_width=sw
    ))

def iso_box(g, x, y, z, w, h, d, top_fill="#e0e0e0", right_fill="#c0c0c0",
            front_fill="#d0d0d0", stroke="#333", sw=1.5):
    """Draw a complete isometric box with three visible faces."""
    # Front face (left-facing)
    fl_tl = iso_point(x + w, y, z)
    fl_tr = iso_point(x + w, y + h, z)
    fl_br = iso_point(x + w, y + h, z - d)
    fl_bl = iso_point(x + w, y, z - d)
    g.append(dw.Lines(
        fl_tl[0], fl_tl[1], fl_tr[0], fl_tr[1],
        fl_br[0], fl_br[1], fl_bl[0], fl_bl[1],
        close=True, fill=right_fill, stroke=stroke, stroke_width=sw
    ))
    # Right face (right-facing)
    rt_tl = iso_point(x, y + h, z)
    rt_tr = iso_point(x + w, y + h, z)
    rt_br = iso_point(x + w, y + h, z - d)
    rt_bl = iso_point(x, y + h, z - d)
    g.append(dw.Lines(
        rt_tl[0], rt_tl[1], rt_tr[0], rt_tr[1],
        rt_br[0], rt_br[1], rt_bl[0], rt_bl[1],
        close=True, fill=front_fill, stroke=stroke, stroke_width=sw
    ))
    # Top face
    iso_rect_top(g, x, y, z, w, h, fill=top_fill, stroke=stroke, sw=sw)


# ─── Pin Label Helper ──────────────────────────────────────────────

def add_pin_label(g, sx, sy, label, side="right", font_size=7):
    """Add a pin label with a small dot at the connection point."""
    g.append(dw.Circle(sx, sy, 2, fill="#333"))
    tx = sx + (8 if side == "right" else -8)
    anchor = "start" if side == "right" else "end"
    g.append(dw.Text(label, font_size, tx, sy + 2.5,
                      font_family="monospace", fill="#333", text_anchor=anchor))


# ─── Electronic Components ─────────────────────────────────────────

def draw_arduino_nano(g, cx=0, cy=0, show_pins=True):
    """Arduino Nano - 45×18mm DIP package."""
    w, h, d = 45, 18, 4
    ox, oy = cx - w/2, cy - h/2
    # PCB body
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#1a7a6d", right_fill="#146b5f", front_fill="#117a6d")
    # USB connector (mini) at top
    usb_w, usb_h, usb_d = 8, 7, 3
    ux = ox + w/2 - usb_w/2
    uy = oy - 2
    iso_box(g, ux, uy, 1, usb_w, usb_h, usb_d + 1,
            top_fill="#aaa", right_fill="#888", front_fill="#999")
    # Chip (black rectangle on top)
    chip_w, chip_h = 12, 10
    chip_x = ox + w/2 - chip_w/2
    chip_y = oy + h/2 - chip_h/2 + 2
    iso_rect_top(g, chip_x, chip_y, 0.5, chip_w, chip_h, fill="#222")
    # Label
    lp = iso_point(ox + w/2, oy + h/2, 1)
    g.append(dw.Text("NANO", 6, lp[0], lp[1],
                      font_family="sans-serif", fill="#afd", text_anchor="middle",
                      font_weight="bold"))
    # Pin labels
    if show_pins:
        pins_left = ["D13","D12","D11","D10","D9","D8","D7","D6","D5","D4","D3","D2","GND","RESET","RX","TX"]
        pins_right = ["3.3V","AREF","A0","A1","A2","A3","A4","A5","A6","A7","5V","RESET","GND","VIN","D0","D1"]
        pin_count = min(len(pins_left), 8)
        for i in range(pin_count):
            py = oy + 2 + i * (h - 4) / (pin_count - 1) if pin_count > 1 else oy + h/2
            lp = iso_point(ox - 1, py, 0)
            add_pin_label(g, lp[0], lp[1], pins_left[i], side="left", font_size=5)
            rp = iso_point(ox + w + 1, py, 0)
            ri = min(i, len(pins_right)-1)
            add_pin_label(g, rp[0], rp[1], pins_right[ri], side="right", font_size=5)
    return {"w": w, "h": h, "d": d}

def draw_arduino_uno(g, cx=0, cy=0, show_pins=True):
    """Arduino Uno - 69×53mm board."""
    w, h, d = 69, 53, 5
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#1a7a6d", right_fill="#146b5f", front_fill="#117a6d")
    # USB-B connector
    iso_box(g, ox + 2, oy - 3, 1, 12, 12, 7,
            top_fill="#aaa", right_fill="#888", front_fill="#999")
    # Barrel jack
    iso_box(g, ox + 18, oy - 2, 1, 9, 9, 6,
            top_fill="#222", right_fill="#111", front_fill="#181818")
    # Chip
    iso_rect_top(g, ox + 25, oy + 15, 0.5, 18, 22, fill="#222")
    # Label
    lp = iso_point(ox + w/2, oy + h/2, 1)
    g.append(dw.Text("UNO", 8, lp[0], lp[1],
                      font_family="sans-serif", fill="#afd", text_anchor="middle",
                      font_weight="bold"))
    if show_pins:
        for i, pin in enumerate(["D0","D1","D2","D3","D4","D5","D6","D7"]):
            py = oy + 2 + i * 5
            p = iso_point(ox + w + 1, py, 0)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=5)
        for i, pin in enumerate(["A0","A1","A2","A3","A4","A5"]):
            py = oy + h - 30 + i * 5
            p = iso_point(ox - 1, py, 0)
            add_pin_label(g, p[0], p[1], pin, side="left", font_size=5)
        for i, pin in enumerate(["5V","3.3V","GND"]):
            py = oy + 2 + i * 5
            p = iso_point(ox - 1, py, 0)
            add_pin_label(g, p[0], p[1], pin, side="left", font_size=5)
    return {"w": w, "h": h, "d": d}

def draw_esp32(g, cx=0, cy=0, show_pins=True):
    """ESP32 DevKit - 51×26mm."""
    w, h, d = 51, 26, 4
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#1a1a2e", right_fill="#111128", front_fill="#16162b")
    # Antenna area (top)
    iso_rect_top(g, ox, oy, 0.3, 18, h, fill="#2a2a4a")
    # USB
    iso_box(g, ox + w - 10, oy + h/2 - 4, 1, 8, 8, 3,
            top_fill="#aaa", right_fill="#888", front_fill="#999")
    lp = iso_point(ox + w/2, oy + h/2, 1)
    g.append(dw.Text("ESP32", 6, lp[0], lp[1],
                      font_family="sans-serif", fill="#88f", text_anchor="middle",
                      font_weight="bold"))
    if show_pins:
        for i, pin in enumerate(["3.3V", "GND", "GPIO2", "GPIO4"]):
            py = oy + 2 + i * 6
            p = iso_point(ox - 1, py, 0)
            add_pin_label(g, p[0], p[1], pin, side="left", font_size=5)
    return {"w": w, "h": h, "d": d}

def draw_raspberry_pi_pico(g, cx=0, cy=0, show_pins=True):
    """Raspberry Pi Pico - 51×21mm."""
    w, h, d = 51, 21, 3
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#4a9e4a", right_fill="#3a8a3a", front_fill="#45964a")
    iso_box(g, ox + w - 8, oy + h/2 - 3, 1, 7, 6, 2,
            top_fill="#aaa", right_fill="#888", front_fill="#999")
    lp = iso_point(ox + w/2, oy + h/2, 1)
    g.append(dw.Text("PICO", 6, lp[0], lp[1],
                      font_family="sans-serif", fill="#fff", text_anchor="middle",
                      font_weight="bold"))
    return {"w": w, "h": h, "d": d}


# ─── Sensors ───────────────────────────────────────────────────────

def draw_pir_sensor(g, cx=0, cy=0, show_pins=True):
    """HC-SR501 PIR motion sensor with dome lens."""
    w, h, d = 32, 24, 8
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#2a8a2a", right_fill="#1a7a1a", front_fill="#228a22")
    # Fresnel lens dome (circle on top)
    dome_center = iso_point(ox + w/2, oy + h/2, d)
    g.append(dw.Circle(dome_center[0], dome_center[1], 10,
                        fill="#e8e8dd", stroke="#999", stroke_width=1.5, fill_opacity=0.8))
    g.append(dw.Circle(dome_center[0], dome_center[1], 7,
                        fill="none", stroke="#ccc", stroke_width=0.5))
    if show_pins:
        pins = ["VCC", "OUT", "GND"]
        for i, pin in enumerate(pins):
            py = oy + h + 3 + i * 0
            px = ox + 5 + i * (w - 10) / 2
            p = iso_point(px, oy + h + 2, -d)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=6)
    return {"w": w, "h": h, "d": d}

def draw_ultrasonic_sensor(g, cx=0, cy=0, show_pins=True):
    """HC-SR04 ultrasonic distance sensor."""
    w, h, d = 45, 20, 6
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#2266bb", right_fill="#1a55aa", front_fill="#2060b0")
    # Two transducer cylinders
    for dx in [12, 33]:
        tc = iso_point(ox + dx, oy + h/2, d)
        g.append(dw.Circle(tc[0], tc[1], 7,
                            fill="#ddd", stroke="#999", stroke_width=1.5))
        g.append(dw.Circle(tc[0], tc[1], 5,
                            fill="#bbb", stroke="#999", stroke_width=0.5))
    if show_pins:
        for i, pin in enumerate(["VCC", "TRIG", "ECHO", "GND"]):
            px = ox + 8 + i * 9
            p = iso_point(px, oy + h + 2, -d)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=5)
    return {"w": w, "h": h, "d": d}

def draw_dht11_temp(g, cx=0, cy=0, show_pins=True):
    """DHT11 temperature/humidity sensor on breakout board."""
    w, h, d = 32, 14, 8
    ox, oy = cx - w/2, cy - h/2
    # Breakout PCB
    iso_box(g, ox, oy, 0, w, h, 3,
            top_fill="#2a8a2a", right_fill="#1a7a1a", front_fill="#228a22")
    # Blue sensor housing
    iso_box(g, ox + 6, oy + 1, 3, 20, 12, d - 3,
            top_fill="#4488cc", right_fill="#3377bb", front_fill="#4080c0")
    if show_pins:
        for i, pin in enumerate(["+", "DATA", "-"]):
            px = ox + 5 + i * 11
            p = iso_point(px, oy + h + 2, -3)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=6)
    return {"w": w, "h": h, "d": d}

def draw_photoresistor(g, cx=0, cy=0, show_pins=True):
    """LDR / photoresistor on breakout module."""
    w, h, d = 32, 14, 4
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#2a8a2a", right_fill="#1a7a1a", front_fill="#228a22")
    # LDR element
    ldr_c = iso_point(ox + w/2, oy + h/2, d)
    g.append(dw.Circle(ldr_c[0], ldr_c[1], 5,
                        fill="#cc8844", stroke="#996633", stroke_width=1))
    if show_pins:
        for i, pin in enumerate(["VCC", "OUT", "GND"]):
            px = ox + 5 + i * 11
            p = iso_point(px, oy + h + 2, -d)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=6)
    return {"w": w, "h": h, "d": d}

def draw_button(g, cx=0, cy=0, show_pins=True):
    """Tactile button on breakout module."""
    w, h, d = 32, 14, 4
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#2a2a8a", right_fill="#1a1a7a", front_fill="#22228a")
    # Button cap
    bc = iso_point(ox + w/2, oy + h/2, d + 2)
    g.append(dw.Circle(bc[0], bc[1], 5,
                        fill="#dd3333", stroke="#aa2222", stroke_width=1.5))
    if show_pins:
        for i, pin in enumerate(["VCC", "OUT", "GND"]):
            px = ox + 5 + i * 11
            p = iso_point(px, oy + h + 2, -d)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=6)
    return {"w": w, "h": h, "d": d}

def draw_potentiometer(g, cx=0, cy=0, show_pins=True):
    """Rotary potentiometer."""
    w, h, d = 16, 16, 10
    ox, oy = cx - w/2, cy - h/2
    # Body (cylindrical approximation)
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#4444aa", right_fill="#333399", front_fill="#3838a0")
    # Knob shaft
    kc = iso_point(ox + w/2, oy + h/2, d + 3)
    g.append(dw.Circle(kc[0], kc[1], 3, fill="#ccc", stroke="#999", stroke_width=1))
    if show_pins:
        for i, pin in enumerate(["VCC", "OUT", "GND"]):
            px = ox + 2 + i * 6
            p = iso_point(px, oy + h + 2, -d)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=5)
    return {"w": w, "h": h, "d": d}


# ─── Output Devices ────────────────────────────────────────────────

def draw_led_single(g, cx=0, cy=0, show_pins=True, color="#ff3333"):
    """5mm LED."""
    lp = iso_point(cx, cy, 5)
    # LED dome
    g.append(dw.Circle(lp[0], lp[1], 5,
                        fill=color, stroke="#666", stroke_width=1, fill_opacity=0.8))
    # Lens highlight
    g.append(dw.Circle(lp[0] - 1.5, lp[1] - 1.5, 1.5, fill="white", fill_opacity=0.4))
    # Legs
    for dx, pin in [(-2, "+"), (2, "-")]:
        leg_top = iso_point(cx + dx, cy, 0)
        leg_bot = iso_point(cx + dx, cy, -6)
        g.append(dw.Line(leg_top[0], leg_top[1], leg_bot[0], leg_bot[1],
                          stroke="#999", stroke_width=1))
        if show_pins:
            add_pin_label(g, leg_bot[0], leg_bot[1], pin, side="right", font_size=6)
    return {"w": 5, "h": 5, "d": 11}

def draw_led_rgb(g, cx=0, cy=0, show_pins=True):
    """RGB LED (common cathode, 4 pins)."""
    lp = iso_point(cx, cy, 5)
    g.append(dw.Circle(lp[0], lp[1], 5,
                        fill="white", stroke="#666", stroke_width=1, fill_opacity=0.9))
    # RGB indicator dots
    for dx, c in [(-2, "red"), (0, "green"), (2, "blue")]:
        dp = iso_point(cx + dx, cy, 6)
        g.append(dw.Circle(dp[0], dp[1], 1.2, fill=c))
    if show_pins:
        for i, pin in enumerate(["R", "GND", "G", "B"]):
            leg_bot = iso_point(cx - 3 + i * 2, cy, -6)
            g.append(dw.Line(iso_point(cx - 3 + i*2, cy, 0)[0],
                              iso_point(cx - 3 + i*2, cy, 0)[1],
                              leg_bot[0], leg_bot[1],
                              stroke="#999", stroke_width=1))
            add_pin_label(g, leg_bot[0], leg_bot[1], pin, side="right", font_size=5)
    return {"w": 8, "h": 5, "d": 11}

def draw_servo_motor(g, cx=0, cy=0, show_pins=True):
    """SG90 micro servo motor."""
    w, h, d = 23, 12, 22
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#3366bb", right_fill="#2255aa", front_fill="#2860b0")
    # Mounting tabs
    iso_rect_top(g, ox - 3, oy + 2, 0, w + 6, 2, fill="#3366bb")
    # Output shaft
    shaft = iso_point(ox + 6, oy + h/2, d + 2)
    g.append(dw.Circle(shaft[0], shaft[1], 3, fill="#fff", stroke="#999", stroke_width=1))
    # Wire bundle
    if show_pins:
        wires = [("ORG", "orange", "Signal"), ("RED", "red", "VCC"), ("BRN", "#8B4513", "GND")]
        for i, (label, color, name) in enumerate(wires):
            wp = iso_point(ox + w + 3, oy + 3 + i * 4, 0)
            g.append(dw.Circle(wp[0], wp[1], 2, fill=color, stroke="#333", stroke_width=0.5))
            add_pin_label(g, wp[0], wp[1], name, side="right", font_size=5)
    return {"w": w, "h": h, "d": d}

def draw_relay_module(g, cx=0, cy=0, show_pins=True):
    """Single-channel relay module."""
    w, h, d = 50, 26, 10
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#2266bb", right_fill="#1a55aa", front_fill="#2060b0")
    # Relay component
    iso_box(g, ox + 5, oy + 3, d, 20, 15, 8,
            top_fill="#3333bb", right_fill="#2222aa", front_fill="#2828b0")
    # Screw terminal block
    iso_box(g, ox + 30, oy + 3, d, 15, 8, 6,
            top_fill="#3388ff", right_fill="#2277ee", front_fill="#3080f0")
    if show_pins:
        # Signal side
        for i, pin in enumerate(["VCC", "GND", "IN"]):
            p = iso_point(ox - 1, oy + 3 + i * 8, 0)
            add_pin_label(g, p[0], p[1], pin, side="left", font_size=5)
        # Load side
        for i, pin in enumerate(["COM", "NO", "NC"]):
            p = iso_point(ox + w + 1, oy + 3 + i * 8, 0)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=5)
    return {"w": w, "h": h, "d": d}

def draw_buzzer(g, cx=0, cy=0, show_pins=True):
    """Piezo buzzer module."""
    w, h, d = 18, 18, 6
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#222", right_fill="#111", front_fill="#1a1a1a")
    # Sound hole
    sc = iso_point(ox + w/2, oy + h/2, d)
    g.append(dw.Circle(sc[0], sc[1], 3, fill="none", stroke="#555", stroke_width=1))
    if show_pins:
        for i, pin in enumerate(["+", "-"]):
            p = iso_point(ox + 5 + i * 8, oy + h + 2, -d)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=6)
    return {"w": w, "h": h, "d": d}

def draw_lcd_16x2(g, cx=0, cy=0, show_pins=True):
    """16×2 LCD with I2C backpack."""
    w, h, d = 80, 36, 8
    ox, oy = cx - w/2, cy - h/2
    # PCB
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#2266bb", right_fill="#1a55aa", front_fill="#2060b0")
    # Display area
    iso_rect_top(g, ox + 5, oy + 4, d + 0.5, 70, 20, fill="#88bb44")
    # Text rows (decorative)
    for row in range(2):
        rp = iso_point(ox + 10, oy + 8 + row * 8, d + 1)
        g.append(dw.Text("████████████████" if row == 0 else "                ",
                          4, rp[0], rp[1], font_family="monospace", fill="#446622"))
    if show_pins:
        for i, pin in enumerate(["VCC", "GND", "SDA", "SCL"]):
            p = iso_point(ox + w + 1, oy + 3 + i * 8, 0)
            add_pin_label(g, p[0], p[1], pin, side="right", font_size=5)
    return {"w": w, "h": h, "d": d}


# ─── Power Components ──────────────────────────────────────────────

def draw_battery_holder_4aa(g, cx=0, cy=0, show_pins=True):
    """4×AA battery holder."""
    w, h, d = 62, 58, 15
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#222", right_fill="#111", front_fill="#1a1a1a")
    # Battery slots
    for i in range(4):
        bx = ox + 4 + i * 14
        iso_rect_top(g, bx, oy + 5, d + 0.5, 12, h - 10, fill="#333")
    if show_pins:
        for i, (pin, c) in enumerate([("+", "red"), ("-", "black")]):
            wp = iso_point(ox + w + 3, oy + h/2 - 5 + i * 10, 0)
            g.append(dw.Circle(wp[0], wp[1], 2.5, fill=c, stroke="#333", stroke_width=0.5))
            add_pin_label(g, wp[0], wp[1], pin, side="right", font_size=6)
    return {"w": w, "h": h, "d": d}

def draw_usb_cable(g, cx=0, cy=0, show_pins=False):
    """USB cable with connector."""
    # Connector body
    iso_box(g, cx - 6, cy - 4, 0, 12, 8, 5,
            top_fill="#aaa", right_fill="#888", front_fill="#999")
    # Cable
    cable_start = iso_point(cx + 6, cy, 2)
    g.append(dw.Line(cable_start[0], cable_start[1],
                      cable_start[0] + 30, cable_start[1] + 5,
                      stroke="#333", stroke_width=3, stroke_linecap="round"))
    return {"w": 45, "h": 8, "d": 5}

def draw_dc_barrel_jack(g, cx=0, cy=0, show_pins=True):
    """DC barrel jack connector."""
    iso_box(g, cx - 7, cy - 5, 0, 14, 9, 6,
            top_fill="#222", right_fill="#111", front_fill="#181818")
    bc = iso_point(cx, cy, 6)
    g.append(dw.Circle(bc[0], bc[1], 3, fill="#444", stroke="#222", stroke_width=1))
    if show_pins:
        for i, (pin, c) in enumerate([("+", "red"), ("-", "black")]):
            wp = iso_point(cx + 10, cy - 3 + i * 6, 0)
            g.append(dw.Circle(wp[0], wp[1], 2, fill=c, stroke="#333", stroke_width=0.5))
            add_pin_label(g, wp[0], wp[1], pin, side="right", font_size=6)
    return {"w": 14, "h": 9, "d": 6}


# ─── Connectivity ──────────────────────────────────────────────────

def draw_breadboard_half(g, cx=0, cy=0, show_pins=False):
    """Half-size breadboard (400 tie points)."""
    w, h, d = 83, 55, 3
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#f5f5f0", right_fill="#e0e0d8", front_fill="#eaeae2")
    # Power rails (colored lines)
    iso_rect_top(g, ox + 3, oy + 2, d + 0.2, w - 6, 2, fill="#ff4444")
    iso_rect_top(g, ox + 3, oy + 5, d + 0.2, w - 6, 2, fill="#4444ff")
    iso_rect_top(g, ox + 3, oy + h - 7, d + 0.2, w - 6, 2, fill="#ff4444")
    iso_rect_top(g, ox + 3, oy + h - 4, d + 0.2, w - 6, 2, fill="#4444ff")
    # Hole grid (simplified - just a few representative dots)
    for row in range(5):
        for col in range(10):
            hp = iso_point(ox + 8 + col * 7, oy + 12 + row * 3, d + 0.3)
            g.append(dw.Circle(hp[0], hp[1], 0.8, fill="#888"))
    # Center divider
    iso_rect_top(g, ox + 3, oy + h/2 - 1.5, d + 0.2, w - 6, 3, fill="#ddd")
    for row in range(5):
        for col in range(10):
            hp = iso_point(ox + 8 + col * 7, oy + h/2 + 5 + row * 3, d + 0.3)
            g.append(dw.Circle(hp[0], hp[1], 0.8, fill="#888"))
    return {"w": w, "h": h, "d": d}

def draw_breadboard_mini(g, cx=0, cy=0, show_pins=False):
    """Mini breadboard (170 tie points)."""
    w, h, d = 47, 35, 3
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="#f5f5f0", right_fill="#e0e0d8", front_fill="#eaeae2")
    # Simplified hole grid
    for row in range(5):
        for col in range(8):
            hp = iso_point(ox + 5 + col * 5, oy + 5 + row * 3, d + 0.3)
            g.append(dw.Circle(hp[0], hp[1], 0.7, fill="#888"))
    iso_rect_top(g, ox + 2, oy + h/2 - 1, d + 0.2, w - 4, 2, fill="#ddd")
    for row in range(5):
        for col in range(8):
            hp = iso_point(ox + 5 + col * 5, oy + h/2 + 4 + row * 3, d + 0.3)
            g.append(dw.Circle(hp[0], hp[1], 0.7, fill="#888"))
    return {"w": w, "h": h, "d": d}


# ─── Hardware / Fasteners ──────────────────────────────────────────

def draw_screw_phillips(g, cx=0, cy=0, scale=1.0):
    """Phillips head screw."""
    s = scale
    # Screw head (top circle)
    hp = iso_point(cx, cy, 3 * s)
    g.append(dw.Circle(hp[0], hp[1], 4 * s, fill="#ccc", stroke="#999", stroke_width=1))
    # Phillips cross
    g.append(dw.Line(hp[0] - 2.5*s, hp[1], hp[0] + 2.5*s, hp[1],
                      stroke="#888", stroke_width=1))
    g.append(dw.Line(hp[0], hp[1] - 2.5*s, hp[0], hp[1] + 2.5*s,
                      stroke="#888", stroke_width=1))
    # Shaft
    shaft_top = iso_point(cx, cy, 0)
    shaft_bot = iso_point(cx, cy, -8 * s)
    g.append(dw.Line(shaft_top[0], shaft_top[1], shaft_bot[0], shaft_bot[1],
                      stroke="#999", stroke_width=2 * s))
    return {"w": 8, "h": 8, "d": 11}

def draw_screw_hex(g, cx=0, cy=0, scale=1.0):
    """Hex socket head screw."""
    s = scale
    hp = iso_point(cx, cy, 3 * s)
    g.append(dw.Circle(hp[0], hp[1], 4 * s, fill="#bbb", stroke="#888", stroke_width=1))
    # Hex socket
    g.append(dw.RegularPolygon(6, hp[0], hp[1], 2 * s,
                                fill="none", stroke="#666", stroke_width=1))
    shaft_top = iso_point(cx, cy, 0)
    shaft_bot = iso_point(cx, cy, -8 * s)
    g.append(dw.Line(shaft_top[0], shaft_top[1], shaft_bot[0], shaft_bot[1],
                      stroke="#999", stroke_width=2 * s))
    return {"w": 8, "h": 8, "d": 11}

def draw_nut(g, cx=0, cy=0, scale=1.0):
    """Hex nut."""
    s = scale
    hp = iso_point(cx, cy, 1.5 * s)
    g.append(dw.RegularPolygon(6, hp[0], hp[1], 4 * s,
                                fill="#ccc", stroke="#999", stroke_width=1))
    g.append(dw.Circle(hp[0], hp[1], 1.5 * s, fill="#aaa", stroke="#888", stroke_width=0.5))
    return {"w": 8, "h": 8, "d": 3}

def draw_wall_anchor(g, cx=0, cy=0, scale=1.0):
    """Plastic wall expansion anchor."""
    s = scale
    top = iso_point(cx, cy, 0)
    bot = iso_point(cx, cy, -15 * s)
    g.append(dw.Line(top[0], top[1], bot[0], bot[1],
                      stroke="#ddd", stroke_width=4 * s, stroke_linecap="round"))
    # Flange at top
    g.append(dw.Circle(top[0], top[1], 3 * s, fill="#eee", stroke="#ccc", stroke_width=1))
    return {"w": 6, "h": 6, "d": 15}

def draw_cable_tie(g, cx=0, cy=0, scale=1.0):
    """Cable/zip tie."""
    s = scale
    # Simplified: loop shape
    p = iso_point(cx, cy, 0)
    g.append(dw.Circle(p[0], p[1], 6 * s,
                        fill="none", stroke="#eee", stroke_width=2 * s))
    # Tail
    g.append(dw.Line(p[0] + 6*s, p[1], p[0] + 18*s, p[1],
                      stroke="#eee", stroke_width=2 * s, stroke_linecap="round"))
    return {"w": 24, "h": 12, "d": 2}

def draw_adhesive_strip(g, cx=0, cy=0, scale=1.0):
    """Double-sided adhesive strip."""
    s = scale
    ox, oy = cx - 15 * s, cy - 3 * s
    iso_rect_top(g, ox, oy, 0, 30 * s, 6 * s, 1 * s,
                  fill="#ff6666", stroke="#cc4444")
    return {"w": 30, "h": 6, "d": 1}


# ─── Structural Parts ─────────────────────────────────────────────

def draw_rect(g, cx=0, cy=0, w=80, h=50, d=3, color="#d0d0d0"):
    """Parametric rectangular plate."""
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill=color,
            right_fill="#b0b0b0",
            front_fill="#c0c0c0")
    return {"w": w, "h": h, "d": d}

def draw_l_bracket(g, cx=0, cy=0, arm1=30, arm2=30, d=3):
    """L-shaped mounting bracket."""
    ox, oy = cx - arm1/2, cy - arm2/2
    # Horizontal arm
    iso_box(g, ox, oy, 0, arm1, d, d,
            top_fill="#ccc", right_fill="#aaa", front_fill="#bbb")
    # Vertical arm
    iso_box(g, ox, oy, 0, d, arm2, d,
            top_fill="#ccc", right_fill="#aaa", front_fill="#bbb")
    # Mounting holes
    for pos in [(ox + arm1/2, oy + d/2), (ox + d/2, oy + arm2/2)]:
        hp = iso_point(pos[0], pos[1], d + 0.5)
        g.append(dw.Circle(hp[0], hp[1], 2, fill="none", stroke="#888", stroke_width=0.8))
    return {"w": arm1, "h": arm2, "d": d}

def draw_standoff(g, cx=0, cy=0, height=10):
    """Hex standoff spacer."""
    hp = iso_point(cx, cy, height)
    bp = iso_point(cx, cy, 0)
    g.append(dw.Line(bp[0], bp[1], hp[0], hp[1],
                      stroke="#bbb", stroke_width=4, stroke_linecap="round"))
    g.append(dw.RegularPolygon(6, hp[0], hp[1], 3, fill="#ccc", stroke="#999", stroke_width=1))
    g.append(dw.RegularPolygon(6, bp[0], bp[1], 3, fill="#ccc", stroke="#999", stroke_width=1))
    return {"w": 6, "h": 6, "d": height}

def draw_enclosure_box(g, cx=0, cy=0, w=60, h=40, d=20):
    """Open-top enclosure box."""
    ox, oy = cx - w/2, cy - h/2
    iso_box(g, ox, oy, 0, w, h, d,
            top_fill="none", right_fill="#d8d8d8", front_fill="#e0e0e0")
    # Bottom
    iso_rect_top(g, ox + 2, oy + 2, -d + 2, w - 4, h - 4, fill="#eee")
    # Rim edges
    iso_rect_top(g, ox, oy, 0, w, h, fill="none", stroke="#999", sw=2)
    return {"w": w, "h": h, "d": d}


# ─── Component Registry ───────────────────────────────────────────

COMPONENTS = {
    # Microcontrollers
    "arduino_uno": draw_arduino_uno,
    "arduino_nano": draw_arduino_nano,
    "esp32": draw_esp32,
    "raspberry_pi_pico": draw_raspberry_pi_pico,
    # Sensors
    "pir_sensor": draw_pir_sensor,
    "ultrasonic_sensor": draw_ultrasonic_sensor,
    "dht11_temp": draw_dht11_temp,
    "photoresistor": draw_photoresistor,
    "button": draw_button,
    "potentiometer": draw_potentiometer,
    # Output
    "led_single": draw_led_single,
    "led_rgb": draw_led_rgb,
    "servo_motor": draw_servo_motor,
    "relay_module": draw_relay_module,
    "buzzer": draw_buzzer,
    "lcd_16x2": draw_lcd_16x2,
    # Power
    "battery_holder_4aa": draw_battery_holder_4aa,
    "usb_cable": draw_usb_cable,
    "dc_barrel_jack": draw_dc_barrel_jack,
    # Connectivity
    "breadboard_half": draw_breadboard_half,
    "breadboard_mini": draw_breadboard_mini,
    # Hardware
    "screw_phillips": draw_screw_phillips,
    "screw_hex": draw_screw_hex,
    "nut": draw_nut,
    "wall_anchor": draw_wall_anchor,
    "cable_tie": draw_cable_tie,
    "adhesive_strip": draw_adhesive_strip,
    # Structural
    "rect": draw_rect,
    "l_bracket": draw_l_bracket,
    "standoff": draw_standoff,
    "enclosure_box": draw_enclosure_box,
}

def render_component(name, width=300, height=250, show_pins=True):
    """Render a single component to an SVG drawing."""
    d = dw.Drawing(width, height, origin="center")
    d.append(dw.Rectangle(-width/2, -height/2, width, height, fill="white"))
    g = dw.Group()
    func = COMPONENTS.get(name)
    if not func:
        raise ValueError(f"Unknown component: {name}. Available: {list(COMPONENTS.keys())}")
    # Call with appropriate kwargs
    import inspect
    sig = inspect.signature(func)
    kwargs = {"g": g, "cx": 0, "cy": 0}
    if "show_pins" in sig.parameters:
        kwargs["show_pins"] = show_pins
    func(**kwargs)
    d.append(g)
    # Label
    d.append(dw.Text(name, 12, 0, height/2 - 15,
                      font_family="sans-serif", fill="#333", text_anchor="middle"))
    return d


# ─── CLI ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    if "--list" in sys.argv:
        print("Available components:")
        print()
        categories = {
            "Microcontrollers": ["arduino_uno", "arduino_nano", "esp32", "raspberry_pi_pico"],
            "Sensors": ["pir_sensor", "ultrasonic_sensor", "dht11_temp", "photoresistor", "button", "potentiometer"],
            "Output": ["led_single", "led_rgb", "servo_motor", "relay_module", "buzzer", "lcd_16x2"],
            "Power": ["battery_holder_4aa", "usb_cable", "dc_barrel_jack"],
            "Connectivity": ["breadboard_half", "breadboard_mini"],
            "Hardware": ["screw_phillips", "screw_hex", "nut", "wall_anchor", "cable_tie", "adhesive_strip"],
            "Structural": ["rect", "l_bracket", "standoff", "enclosure_box"],
        }
        for cat, items in categories.items():
            print(f"  {cat}:")
            for item in items:
                print(f"    - {item}")
        print()
        print(f"Total: {len(COMPONENTS)} components")
    elif "--render" in sys.argv:
        idx = sys.argv.index("--render")
        name = sys.argv[idx + 1]
        output = sys.argv[sys.argv.index("--output") + 1] if "--output" in sys.argv else f"{name}.svg"
        d = render_component(name)
        d.save_svg(output)
        print(f"Rendered {name} → {output}")
    elif "--render-all" in sys.argv:
        output_dir = sys.argv[sys.argv.index("--output-dir") + 1] if "--output-dir" in sys.argv else "./previews"
        os.makedirs(output_dir, exist_ok=True)
        for name in COMPONENTS:
            d = render_component(name)
            path = os.path.join(output_dir, f"{name}.svg")
            d.save_svg(path)
            print(f"  {name} → {path}")
        print(f"\nRendered {len(COMPONENTS)} components to {output_dir}/")
    else:
        print("Usage:")
        print("  python3 components.py --list")
        print("  python3 components.py --render <component_name> [--output file.svg]")
        print("  python3 components.py --render-all [--output-dir ./previews]")
