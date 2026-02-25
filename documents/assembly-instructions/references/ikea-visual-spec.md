# IKEA Visual Specification

Exact visual specifications derived from analyzing official IKEA assembly manuals (KURA bed AA-843436-8 and others). Use this reference when generating AI images to achieve authentic IKEA style.

## Core Visual Rules

### 1. WORDLESS Communication
IKEA manuals contain almost NO text. The only permitted text elements are:
- Step numbers: Large bold numerals (1, 2, 3...) in top-left
- Quantities: "4x", "28x", "18x" near hardware
- Part codes: 6-digit numbers (128745, 100092, 121030)
- Rare words: "Click!" for snap-fit connections
- Cover only: Product name, "IKEA" logo, "Design and Quality IKEA of Sweden"

**NEVER include:** Labels, explanations, titles on step pages, instructions, captions, descriptions.

### 2. Line Art Style
- **Stroke weight:** Consistent 1.5-2pt black lines throughout
- **Background:** Pure white (#FFFFFF)
- **No fills except:** Light grey (10-15% black) for depth on interior surfaces, human figures
- **No gradients, textures, shadows, or decorative elements**
- **Every mark serves an instructional purpose**

### 3. Perspective
- **Fixed 30° isometric** for all assembly steps
- **Never rotate the camera** between steps
- Same angle throughout entire manual
- Product thumbnail in corner shows "where we are" in assembly

### 4. Human Figures
When humans appear (for scale, grip, or "2 people needed"):
- **Head:** Egg/oval shape, NO hair, NO facial features except dot eyes
- **Body:** Simple rounded outline, light grey fill
- **Hands:** Simplified forms showing grip position
- **Pose:** Minimal detail, functional only

### 5. Hardware Drawing
Screws, dowels, cam locks drawn with technical precision:
- Screw threads visible as parallel diagonal lines
- Phillips/hex heads clearly distinguished
- Dowels show grooved texture
- Cam locks show rotation mechanism
- Part numbers printed vertically alongside (e.g., "128745")

### 6. Callout Bubbles
For detail views:
- **Circle shape** (not square, not rounded rectangle)
- **Curved leader line** connecting to main illustration
- Shows magnified view of connection point
- Quantity marker ("3x") appears near callout

### 7. Arrows
- **Motion arrows:** Thick black, curved for arcing movements
- **Direction arrows:** Straight with solid head
- **Insertion arrows:** Point toward hole/slot
- **Rotation arrows:** Curved around pivot point

### 8. Do/Don't Panels
Side-by-side comparison showing:
- **Left (correct):** Normal illustration, subtle checkmark optional
- **Right (wrong):** Same view with bold X drawn through it
- Both panels show same scenario, different execution
- NO text explanation—visual difference is self-evident

### 9. Parts Inventory Layout
- Parts **float** on white background
- NO boxes, frames, or containers around parts
- Isometric technical drawing of each part
- Part code below each item (6-digit)
- Quantity marker to the right ("1x", "4x")
- Arranged in logical grid

### 10. Page Layout
- **Cover:** Product name huge at top, isometric finished product centered, IKEA logo bottom-right
- **Page 2:** Safety/setup icons (tools needed, 2-person lift, work surface)
- **Page 3:** Hardware inventory (screws, dowels, cam locks)
- **Page 4+:** Assembly steps, one action per page
- **Page numbers:** Small, bottom corner with document code (AA-843436-8)

## Page Templates

### Cover Page
```
┌─────────────────────────────────────┐
│                                     │
│    PRODUKTNAMN                      │  ← Massive bold sans-serif
│                                     │
│                                     │
│         ┌─────────────┐             │
│         │             │             │
│         │  [Isometric │             │
│         │   finished  │             │
│         │   product]  │             │
│         │             │             │
│         └─────────────┘             │
│                                     │
│                                     │
│                          ┌────┐     │
│                          │IKEA│     │
│                          └────┘     │
│                    Design and Quality│
│                    IKEA of Sweden   │
└─────────────────────────────────────┘
```

### Safety/Info Page
```
┌─────────────────────────────────────┐
│ ┌─────────────────┐                 │
│ │ [Person]  [Tool]│  ← Tools needed │
│ └─────────────────┘                 │
│ ┌─────────────────────────────┬───┐ │
│ │ [2 people]  [2 people]  │ X │   │ ← 2 people required
│ └─────────────────────────────┴───┘ │
│ ┌─────────────────────────────────┐ │
│ │ [Work on carpet/soft surface]  │ │
│ └─────────────────────────────────┘ │
│ ┌─────────────────────────────────┐ │
│ │ [?] → [Call IKEA if missing]   │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

### Parts Inventory Page
```
┌─────────────────────────────────────┐
│                                     │
│  [Rail part]        [Hex key]       │
│   121030             100092         │
│     1x                 1x           │
│                                     │
│  [Screw]  [Screw]  [Dowel] [Cap]    │
│  128745   100215   100343  104850   │
│   27x      18x      28x     28x     │
│                                     │
│  [Slat]                             │
│  147717                             │
│    2x                               │
│                                     │
│ ┌───────────────────────────────┐   │
│ │ (i) [Assembly detail diagram] │   │
│ └───────────────────────────────┘   │
└─────────────────────────────────────┘
```

### Assembly Step Page
```
┌─────────────────────────────────────┐
│                                     │
│ 7                    ┌──────────┐   │ ← Large bold step number
│                      │(i)       │   │
│                      │[Detail   │   │ ← Info box if needed
│                      │ diagram] │   │
│                      │    4     │   │ ← Reference to part position
│                      └──────────┘   │
│                                     │
│     ┌──────────────────────┐        │
│     │                      │   3x   │ ← Quantity
│     │   [Main assembly     │ ⌒⌒⌒   │ ← Hardware callout
│     │    illustration]     │128745  │
│     │                      │        │
│     └──────────────────────┘        │
│              ↑                      │
│         [Curved arrow               │
│          showing motion]            │
│                                     │
│                            7        │
│                       AA-843436-8   │
└─────────────────────────────────────┘
```

## Common Mistakes to Avoid

1. **Adding text labels** - Never label parts with words, only numeric codes
2. **Using boxes/frames** - Parts float freely on white
3. **Cartoon style** - Must be technical illustration, not cute
4. **Busy compositions** - One action per step, lots of white space
5. **Decorative elements** - No ornaments, badges, icons beyond functional ones
6. **Inconsistent perspective** - Always same 30° isometric
7. **Photo-realistic style** - Pure line art only
8. **Colored elements** - Black lines, white background, light grey fills only
