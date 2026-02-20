# Project YAML Schema Reference

Complete specification for the assembly instructions input format.

## Top-Level Structure

```yaml
project:        # Required - project metadata
parts:          # Required - all components
  structural:   # Optional - physical mounting/enclosure parts
  hardware:     # Optional - fasteners, connectors
  electronic:   # Optional - boards, sensors, actuators
tools:          # Optional - tools needed for assembly
wiring:         # Optional - electrical connections
safety:         # Optional - custom safety warnings
steps:          # Required - assembly sequence
```

## project (required)

```yaml
project:
  name: "string"           # Required. Display name on cover page
  version: "string"        # Optional. Version number (default "1.0")
  two_person: false         # Optional. If true, shows 2-person icon
  description: "string"    # Optional. Subtitle on cover page
```

## parts.structural

Physical parts that aren't electronic — brackets, plates, enclosures, standoffs.

```yaml
parts:
  structural:
    - id: "A"              # Required. Single letter preferred (A-Z)
      name: "string"       # Required. Human-readable name
      shape: rect           # Required. One of: rect, l_bracket, standoff, enclosure_box
      dimensions:            # Required for rect and enclosure_box
        w: 100              # Width in mm
        h: 60               # Height in mm
        d: 3                # Depth/thickness in mm (optional, default 3)
      material: "string"   # Optional. Display in parts list ("3D printed PLA")
      color: "#hex"        # Optional. Fill color in illustrations
```

## parts.hardware

Fasteners, connectors, and small mechanical parts.

```yaml
parts:
  hardware:
    - id: "H1"            # Required. "H" + number
      name: "string"      # Required. "M3×8mm Phillips screw"
      quantity: 4          # Required. How many included
      type: screw_phillips # Required. Component library type. One of:
                           #   screw_phillips, screw_hex, nut, washer,
                           #   wall_anchor, cable_tie, adhesive_strip,
                           #   standoff_hex, wire_nut
```

## parts.electronic

Circuit boards, sensors, actuators, and electronic modules.

```yaml
parts:
  electronic:
    - id: "E1"            # Required. "E" + number
      name: "string"      # Required. "Arduino Nano"
      component: string    # Required. Component library ID. One of:
                           #   arduino_uno, arduino_nano, esp32, raspberry_pi_pico
                           #   pir_sensor, ultrasonic_sensor, dht11_temp,
                           #   photoresistor, button, potentiometer
                           #   led_single, led_rgb, servo_motor, relay_module,
                           #   buzzer, lcd_16x2
                           #   battery_holder_4aa, usb_cable, dc_barrel_jack
                           #   breadboard_half, breadboard_mini
      quantity: 1          # Optional (default 1)
```

## tools

```yaml
tools:                      # List of tool IDs
  - phillips_screwdriver
  - hex_wrench
  - wire_strippers
  - soldering_iron          # Shows additional safety warning
  - drill
  - pliers
  - multimeter
```

## wiring

Electrical connections between electronic parts.

```yaml
wiring:
  - from:
      part: "E1"           # Required. Part ID
      pin: "D2"            # Required. Pin name on that component
    to:
      part: "E2"           # Required. Part ID
      pin: "OUT"           # Required. Pin name on that component
    color: yellow           # Required. Wire color. One of:
                            #   red, black, yellow, green, blue, white, orange, purple
    label: "Signal"        # Optional. Label in wiring diagram legend
```

## safety

Custom safety warnings beyond defaults.

```yaml
safety:
  - icon: warning_triangle  # Icon type
    text: "Disconnect power before wiring"
  - icon: esd
    text: "Handle boards by edges only"
```

Default safety items are auto-generated based on parts:
- Electronic parts → ESD warning + power-off-before-wiring
- Soldering iron in tools → burn warning
- Wall anchors → proper mounting warning
- Heavy parts → two-person lift warning

## steps (required)

Assembly sequence. Each step is one action.

```yaml
steps:
  - step: 1                # Required. Sequential number
    action: place           # Required. One of:
                            #   place    - position a part
                            #   attach   - fasten parts together
                            #   insert   - push/snap a part in
                            #   wire     - make electrical connections
                            #   flip     - turn assembly over
                            #   test     - power on and verify
    parts: ["A"]           # Parts involved (IDs from parts section)
    hardware: ["H1"]       # Hardware used (IDs from parts section)
    wiring: all             # For wire action: "all" or list of wiring indices
    description: "string"  # Human description (used for YAML readability, not rendered)
    callout: true           # Optional. Generate magnified detail callout
    callout_focus: "H1"   # Optional. Which part to zoom into
    repeat: 4              # Optional. Show "×4" quantity marker
    position:               # Optional. Override auto-positioning
      x: 200
      y: 150
```

## Complete Example

```yaml
project:
  name: "Smart Doorbell Sensor"
  version: "1.0"
  description: "PIR-activated notification system"

parts:
  structural:
    - id: "A"
      name: "Wall mount plate"
      shape: rect
      dimensions: {w: 80, h: 60}
      material: "3D printed PLA"
  hardware:
    - id: "H1"
      name: "M3×10mm Phillips screw"
      quantity: 2
      type: screw_phillips
    - id: "H2"
      name: "Wall anchor"
      quantity: 2
      type: wall_anchor
  electronic:
    - id: "E1"
      name: "Arduino Nano"
      component: arduino_nano
    - id: "E2"
      name: "PIR Motion Sensor"
      component: pir_sensor
    - id: "E3"
      name: "Piezo Buzzer"
      component: buzzer
    - id: "E4"
      name: "Mini Breadboard"
      component: breadboard_mini

tools:
  - phillips_screwdriver
  - wire_strippers
  - drill

wiring:
  - from: {part: "E1", pin: "D2"}
    to: {part: "E2", pin: "OUT"}
    color: yellow
    label: "Motion signal"
  - from: {part: "E1", pin: "5V"}
    to: {part: "E2", pin: "VCC"}
    color: red
  - from: {part: "E1", pin: "GND"}
    to: {part: "E2", pin: "GND"}
    color: black
  - from: {part: "E1", pin: "D8"}
    to: {part: "E3", pin: "+"}
    color: green
    label: "Buzzer signal"
  - from: {part: "E1", pin: "GND"}
    to: {part: "E3", pin: "-"}
    color: black

steps:
  - step: 1
    action: place
    parts: ["A"]
    hardware: ["H2"]
    description: "Mark and drill wall anchor positions, insert anchors"
    callout: true
  - step: 2
    action: attach
    parts: ["A"]
    hardware: ["H1"]
    description: "Screw mount plate to wall"
    repeat: 2
  - step: 3
    action: attach
    parts: ["E4", "A"]
    description: "Press breadboard adhesive onto mount plate"
  - step: 4
    action: insert
    parts: ["E1", "E4"]
    description: "Insert Arduino Nano into breadboard"
  - step: 5
    action: wire
    wiring: all
    description: "Connect all wiring per diagram"
  - step: 6
    action: attach
    parts: ["E2"]
    description: "Position PIR sensor facing doorway"
  - step: 7
    action: test
    description: "Connect USB power and test motion detection"
```
