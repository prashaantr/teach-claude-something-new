# Component Catalog

All available SVG components with pin maps and dimensions.

## Microcontrollers

### arduino_uno
- Dimensions: 69×53mm board
- Pins: D0-D13, A0-A5, 5V, 3.3V, GND, VIN, RESET
- USB: Type-B connector at top
- Power: barrel jack at bottom-left

### arduino_nano
- Dimensions: 45×18mm board
- Pins: D0-D13, A0-A7, 5V, 3.3V, GND, VIN, RESET
- USB: Mini-USB at top
- Breadboard compatible (dual-row DIP)

### esp32
- Dimensions: 51×26mm module
- Pins: GPIO0-GPIO39 (selected), 3.3V, GND, VIN, EN
- USB: Micro-USB at bottom
- Breadboard compatible

### raspberry_pi_pico
- Dimensions: 51×21mm board
- Pins: GP0-GP28, 3.3V, GND, VSYS, VBUS
- USB: Micro-USB at top
- Breadboard compatible

## Sensors

### pir_sensor
- Dimensions: 32×24mm module (with dome lens)
- Pins: VCC, OUT, GND
- Operating voltage: 5V
- Detection angle shown as arc in diagrams

### ultrasonic_sensor (HC-SR04)
- Dimensions: 45×20mm module
- Pins: VCC, TRIG, ECHO, GND
- Two cylindrical transducers visible

### dht11_temp
- Dimensions: 16×12mm module (on breakout: 32×14mm)
- Pins: VCC(+), DATA, GND(-)
- Blue housing distinctive

### photoresistor (LDR module)
- Dimensions: 32×14mm breakout
- Pins: VCC, OUT/AO, GND
- Or raw component: 2 legs, no polarity

### button (tactile switch module)
- Dimensions: 12×12mm switch (on breakout: 32×14mm)
- Pins: VCC, OUT, GND (module) or 2-pin/4-pin (raw)

### potentiometer
- Dimensions: 16mm diameter knob
- Pins: VCC, WIPER/OUT, GND
- Rotary knob visible in diagrams

## Output Devices

### led_single
- Dimensions: 5mm dome
- Pins: + (anode/long), - (cathode/short)
- Polarity indicator (flat edge on cathode side)
- Optional: on breakout module with resistor

### led_rgb
- Dimensions: 5mm dome (4 pins)
- Pins: R, GND (common cathode), G, B
- Or common anode: R, VCC, G, B

### servo_motor (SG90)
- Dimensions: 23×12×22mm body
- Wires: Orange(signal), Red(VCC), Brown(GND)
- Horn attachment shown

### relay_module
- Dimensions: 50×26mm board
- Pins: VCC, GND, IN (signal)
- Screw terminals: COM, NO, NC
- LED indicator visible

### buzzer (piezo)
- Dimensions: 12mm diameter
- Pins: + (long), - (short)
- Or module: VCC, I/O, GND

### lcd_16x2 (with I2C backpack)
- Dimensions: 80×36mm display
- Pins: VCC, GND, SDA, SCL (I2C)
- Or 16-pin parallel (without backpack)

## Power

### battery_holder_4aa
- Dimensions: 62×58mm holder
- Wires: Red(+), Black(-)
- Output: ~6V

### usb_cable
- Types: Mini-USB, Micro-USB, USB-C
- Drawn as cable with connector shape visible

### dc_barrel_jack
- Dimensions: 14×9mm connector
- Center-positive indicator
- Wires: Red(+), Black(-)

## Connectivity

### breadboard_half
- Dimensions: 83×55mm (400 tie points)
- Power rails: 2 per side (red +, blue -)
- 30 rows × 5 columns per side
- Center divider visible

### breadboard_mini
- Dimensions: 47×35mm (170 tie points)
- 17 rows × 5 columns per side
- No power rails

### jumper_wire
- Types: male-male, male-female, female-female
- Colors: red, black, yellow, green, blue, white, orange, purple
- Drawn as colored paths between connection points

## Structural

### rect (parametric)
- Configurable width, height, depth
- Rendered as isometric rectangle with optional mounting holes

### l_bracket
- Configurable arm lengths
- Standard mounting holes at ends

### standoff (hex)
- Configurable height
- M3 thread shown at both ends

### enclosure_box (parametric)
- Configurable width, height, depth
- Open-top view for showing internal components

## Hardware / Fasteners

### screw_phillips
- Drawn at actual scale in inventory
- Cross-head detail visible in callouts

### screw_hex
- Hex socket head detail
- Wrench icon in callout

### nut
- Hex outline
- Shown on screw in callouts

### wall_anchor
- Expansion anchor shape
- Shown being inserted into wall in steps

### cable_tie
- Zip-tie shape
- Drawn securing cable bundles

### adhesive_strip
- Double-sided tape
- Peel-and-stick action in steps
