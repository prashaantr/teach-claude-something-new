# Bauhaus Layout & Grid System

## Table of Contents
1. [Core Layout Principles](#core-layout-principles)
2. [Grid Specifications](#grid-specifications)
3. [Spacing System](#spacing-system)
4. [Rules and Geometric Elements](#rules-and-geometric-elements)
5. [CSS Implementation](#css-implementation)
6. [Design Tokens](#design-tokens)

---

## Core Layout Principles

### Asymmetry Always

- Centered/symmetric arrangements rejected as "boring and lacking hierarchy"
- Flush-left alignment default
- White space as active design element, not void
- "The blank space of the page should be positive"

### Structural Elements

- Heavy typographic rules (horizontal/vertical lines) as dividers, not ornamental borders
- Thin bars at 45-degree angles across layout elements (signature Bauhaus device)
- Circles mark section breaks (bold) and footnotes (small)
- Lines, bars, geometric shapes function as structural and rhythmic elements

### Photography Integration

- Photography at equal status with type (typophoto)
- Image as structural element, not decoration
- Photography over illustration for objective communication

---

## Grid Specifications

### Tschichold's Page Canon

Divides page into 9 x 9 grid (81 rectangles). Text block preserves 2:3 ratio.

**Margin Ratios**:
```
Inner : Top : Outer : Bottom = 1 : 1.5 : 2 : 3
```

### DIN Paper Proportions

Uses √2 ratio (1:1.414). Each size folds to next smaller size.

| Size | Dimensions (mm) |
|------|-----------------|
| A4 | 210 x 297 |
| A3 | 297 x 420 |
| A2 | 420 x 594 |

### Golden Ratio Divisions (1:1.618)

For major layout divisions:
- Content area: 61.8%
- Sidebar: 38.2%

### Bauhaus Magazine Grid (1926)

- Asymmetric column structures
- Generous margins
- Rag-right text blocks
- Modular alignment systems

---

## Spacing System

### Base Unit: 8px

Fibonacci-aligned spacing scale:

| Token | Value | Use |
|-------|-------|-----|
| `--space-xs` | 4px | Tight spacing, inline elements |
| `--space-sm` | 8px | Base unit, compact spacing |
| `--space-md` | 16px | Standard spacing |
| `--space-lg` | 24px | Section spacing |
| `--space-xl` | 32px | Large gaps |
| `--space-2xl` | 48px | Major sections |
| `--space-3xl` | 80px | Page sections |
| `--space-4xl` | 128px | Hero spacing |

### Asymmetric Margin Pattern

```
top: 5%
right: 8%
bottom: 10%
left: 5%
```

Heavier bottom margin creates visual stability. Wider right margin for notes/overflow.

---

## Rules and Geometric Elements

### Typographic Rules (Lines)

Heavy lines serve as structural dividers replacing ornamental borders:

| Type | Weight | Use |
|------|--------|-----|
| Heavy rule | 4-8px | Major section dividers |
| Medium rule | 2-3px | Subsection dividers |
| Hairline | 1px | Table rules, subtle divisions |

### Diagonal Bars

45-degree thin bars across layout elements - signature Bauhaus device.

```css
.bauhaus-diagonal {
  position: relative;
}
.bauhaus-diagonal::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 2px;
  background: var(--bauhaus-red);
  transform: rotate(-45deg);
  transform-origin: left center;
}
```

### Geometric Markers

| Element | Use |
|---------|-----|
| Bold circle | Section breaks |
| Small circle | Footnotes |
| Triangle | Directional indicators |
| Square | Structural anchors |

### Three Fundamental Shapes

All graphic elements derive from circle, triangle, square - the visual vocabulary.

---

## CSS Implementation

### Basic Grid

```css
.bauhaus-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 16px;
  padding: 5% 8% 10% 5%; /* Asymmetric: top right bottom left */
}

.content-main {
  grid-column: 1 / 5; /* 4 of 6 columns */
}

.content-side {
  grid-column: 5 / 7; /* 2 of 6 columns */
}
```

### Golden Ratio Layout

```css
.bauhaus-golden {
  display: grid;
  grid-template-columns: 61.8fr 38.2fr;
  gap: var(--space-lg);
}

/* Reversed */
.bauhaus-golden-reverse {
  grid-template-columns: 38.2fr 61.8fr;
}
```

### 9x9 Canon Grid

```css
.bauhaus-canon {
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-template-rows: repeat(9, 1fr);
}

.canon-text-block {
  grid-column: 2 / 8;
  grid-row: 2 / 8;
}
```

### Spacing Variables

```css
:root {
  /* Spacing scale - 8px base, Fibonacci-aligned */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 80px;
  --space-4xl: 128px;

  /* Grid */
  --grid-columns: 6;
  --grid-gap: var(--space-md);

  /* Margins - asymmetric */
  --margin-top: 5%;
  --margin-right: 8%;
  --margin-bottom: 10%;
  --margin-left: 5%;
}
```

### Complete Layout Component

```css
.bauhaus-layout {
  display: grid;
  grid-template-columns: repeat(var(--grid-columns), 1fr);
  gap: var(--grid-gap);
  padding: var(--margin-top) var(--margin-right) var(--margin-bottom) var(--margin-left);
  min-height: 100vh;
}

/* Structural rule */
.bauhaus-rule {
  height: 4px;
  background: var(--bauhaus-black);
  margin: var(--space-xl) 0;
}

.bauhaus-rule--accent {
  background: var(--bauhaus-red);
}

/* Section marker */
.bauhaus-marker {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--bauhaus-black);
  display: inline-block;
}

/* Flush-left text block */
.bauhaus-text {
  text-align: left;
  max-width: 75ch;
}
```

---

## Design Tokens

### JSON Format

```json
{
  "spacing": {
    "xs": { "value": "4px" },
    "sm": { "value": "8px" },
    "md": { "value": "16px" },
    "lg": { "value": "24px" },
    "xl": { "value": "32px" },
    "2xl": { "value": "48px" },
    "3xl": { "value": "80px" },
    "4xl": { "value": "128px" }
  },
  "grid": {
    "columns": { "value": 6 },
    "gap": { "value": "{spacing.md}" }
  },
  "margin": {
    "top": { "value": "5%" },
    "right": { "value": "8%" },
    "bottom": { "value": "10%" },
    "left": { "value": "5%" }
  },
  "ratio": {
    "golden": { "value": 1.618 },
    "din": { "value": 1.414 },
    "text-block": { "value": "2:3" }
  }
}
```

### Tailwind Config Extension

```js
module.exports = {
  theme: {
    extend: {
      spacing: {
        'bauhaus-xs': '4px',
        'bauhaus-sm': '8px',
        'bauhaus-md': '16px',
        'bauhaus-lg': '24px',
        'bauhaus-xl': '32px',
        'bauhaus-2xl': '48px',
        'bauhaus-3xl': '80px',
        'bauhaus-4xl': '128px',
      },
      gridTemplateColumns: {
        'bauhaus': 'repeat(6, 1fr)',
        'golden': '61.8fr 38.2fr',
        'golden-reverse': '38.2fr 61.8fr',
      }
    }
  }
}
```
