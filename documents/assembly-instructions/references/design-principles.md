# Cognitive Design Principles for Assembly Instructions

Based on validated research from the Stanford Graphics Lab (Heiser, Phan, Agrawala,
Tversky & Hanrahan, 2004) and reverse-engineering of IKEA's instruction design system.

## The 12 Principles

### 1. Fixed Viewpoint
Render every illustration from the same 3/4 isometric angle (30° standard).
Never rotate the camera between steps. The assembler orients between page and
physical parts by matching the consistent perspective.

### 2. Action Diagrams
Show new parts floating toward their destination with directional arrows.
Do NOT show parts already in final position. The spatial gap between a new part
and its target is the primary visual cue for "what to do next."
Stanford finding: action diagrams reduce assembly time 35% vs structural diagrams.

### 3. One Step = One Action
Each numbered step introduces exactly one operation (or one group of identical
operations like "insert 4 screws"). Never combine "attach shelf AND screw back panel."
This respects working memory limits.

### 4. Progressive Disclosure
Sequence assembly so recognizable shapes appear early. Build the frame before
internals. Front-load visible progress for early gratification. IKEA's research:
"seeing bigger parts completed early makes you want to continue."

### 5. Wordless Communication
No text in assembly steps. Use arrows, callout circles, quantity markers (×4),
hand icons, checkmarks, and X-marks. Zero translation cost, zero misinterpretation
risk. Text only appears for safety warnings.

### 6. Spatial Separation
New parts are drawn offset from their attachment point with a dashed guideline
or arrow showing the connection path. Already-assembled parts render as a solid
unit. This separation distinguishes "what you're about to do" from "what's done."

### 7. Callout Circles
When a connection detail is too small for the main illustration (screw insertion,
pin connection, cam lock), show a magnified callout circle connected to the main
view with a thin leader line. This is a visual zoom lens.

### 8. Consistent Part Numbering
Every part gets a persistent label established on inventory pages and used
identically in all steps. Structural parts: A, B, C. Hardware: H1, H2, H3.
Electronic: E1, E2, E3. The assembler never guesses which part is which.

### 9. Quantity Markers
"×4" next to a screw means "do this four times." "×2" next to a sub-assembly
means "build two of these." This avoids cluttering illustrations with identical
repeated arrows.

### 10. Do's and Don'ts
Show wrong actions with a circle-slash (⊘) alongside the correct action with
a checkmark (✓). People need to see what failure looks like to avoid it.
IKEA finding: showing only the right way is insufficient.

### 11. Human Scale References
Hand icons show grip position, push direction, and hold points. Stick figure
appears when two people are needed or body positioning matters. These ground
abstract diagrams in physical reality.

### 12. Minimal Shading
Black lines on white background. Light grey fill for depth/interior surfaces.
No gradients, textures, or decorative elements. Every mark serves an
informational purpose.

## Electronics-Specific Additions

Beyond IKEA's furniture principles, electronics assembly needs:

### 13. Color-Coded Wiring
Wire paths use actual wire colors (red=power, black=ground, yellow/green/blue=signal).
Include a wire color legend on every wiring step.

### 14. Pin Labels
Electronic component pins are labeled at all times. Pin names (D2, 5V, GND)
must be readable at the illustration scale.

### 15. ESD Warnings
Electrostatic discharge warnings appear on the safety page. Hand icons show
proper handling (edges only, don't touch chips).

### 16. Power Sequencing
Wiring steps always happen with power disconnected. A "power off" icon
appears before any wiring step. Final step is "power on and test."
