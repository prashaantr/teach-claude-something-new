# Component Definition Guide

How to define any component for assembly instructions — not a fixed catalog, but patterns for consistency.

## Defining a Component

Every component needs these attributes for consistent rendering:

```yaml
- id: "A"              # Unique identifier (A-Z for structural, H1-Hn for hardware, E1-En for electronic)
  name: "string"       # Human-readable name
  category: string     # structural | hardware | electronic | power | connectivity
  dimensions: string   # Approximate size for scale reference
  connection_points: [] # Where it connects to other parts (pins, holes, terminals)
```

## Component Categories

### Structural
Physical parts that provide mounting, enclosure, or support.

**Pattern:** Describe shape, material, and mounting features.

```yaml
- id: "A"
  name: "Mounting plate"
  shape: rect | l_bracket | enclosure | custom
  dimensions: {w: 100, h: 60, d: 3}
  features: ["4x M3 holes at corners", "centered cutout"]
```

### Hardware
Fasteners and mechanical connectors.

**Pattern:** Describe type, size, and quantity.

```yaml
- id: "H1"
  name: "M3×8mm screw"
  type: screw | nut | bolt | anchor | clip | tie
  quantity: 4
  head: phillips | hex | flat
```

### Electronic
Circuit boards, sensors, actuators, modules.

**Pattern:** Describe form factor and connection interface.

```yaml
- id: "E1"
  name: "Microcontroller board"
  form_factor: "breadboard-compatible" | "module" | "breakout"
  interface: ["USB", "GPIO pins", "power terminals"]
  pins: ["5V", "GND", "D0-D13", "A0-A5"]  # List key pins for wiring
```

### Power
Power sources and distribution.

**Pattern:** Describe voltage, polarity, and connector type.

```yaml
- id: "P1"
  name: "Battery pack"
  output: "6V"
  connector: "bare wires" | "barrel jack" | "USB"
  polarity: ["Red (+)", "Black (-)"]
```

### Connectivity
Wires, cables, breadboards, connectors.

**Pattern:** Describe connection method and capacity.

```yaml
- id: "C1"
  name: "Breadboard"
  capacity: "400 tie points"
  features: ["power rails", "center divider"]
```

## Illustration Conventions

When rendering components, apply these conventions:

| Attribute | Convention |
|-----------|------------|
| Scale | Show relative sizes accurately |
| Labels | ID in corner (A, B, H1, E1) |
| Pins/terminals | Label key connection points |
| Polarity | Red=positive, Black=negative |
| Quantities | "×4" marker for multiples |

## Wiring Color Standards

```
Red    = Power positive (VCC, 5V, 3.3V)
Black  = Ground (GND)
Yellow = Signal / Data
Green  = Signal / Data (alternate)
Blue   = Signal / Data (alternate)
Orange = PWM / Control
White  = I2C SDA or misc
Purple = I2C SCL or misc
```

## Example: Defining a Custom Project

```yaml
parts:
  structural:
    - id: "A"
      name: "Base plate"
      shape: rect
      dimensions: {w: 150, h: 100}
      material: "3D printed PLA"

  hardware:
    - id: "H1"
      name: "M3×10mm Phillips screw"
      quantity: 4
      type: screw

  electronic:
    - id: "E1"
      name: "Controller board"
      form_factor: "module"
      pins: ["VIN", "GND", "D1", "D2", "D3"]

    - id: "E2"
      name: "Motion sensor"
      pins: ["VCC", "OUT", "GND"]
```

## Adding New Components

Don't limit to predefined parts. Define any component using the patterns above:

1. Assign a category and ID
2. Describe physical attributes (size, shape, form factor)
3. List connection points (pins, holes, terminals)
4. Note any special rendering needs (polarity, color coding)

Claude can render any component described this way — the patterns ensure consistency, not the specific catalog entries.
