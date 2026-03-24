# Bauhaus Color System

## Table of Contents
1. [Complete Color Tokens](#complete-color-tokens)
2. [Kandinsky's Color-Form Theory](#kandinskys-color-form-theory)
3. [Albers's Color Principles](#alberss-color-principles)
4. [Itten's Seven Contrasts](#ittens-seven-contrasts)
5. [Usage Rules](#usage-rules)
6. [CSS Implementation](#css-implementation)

---

## Complete Color Tokens

### Primary Palette

| Token | Hex | RGB | Role |
|-------|-----|-----|------|
| `--bauhaus-red` | #BE1E2D | (190, 30, 45) | Primary accent - square |
| `--bauhaus-yellow` | #FFDE17 | (255, 222, 23) | Secondary accent - triangle |
| `--bauhaus-blue` | #21409A | (33, 64, 154) | Tertiary accent - circle |

### High-Saturation Variants

| Token | Hex | RGB | Note |
|-------|-----|-----|------|
| `--bauhaus-red-vivid` | #E30022 | (227, 0, 34) | Cadmium red |
| `--bauhaus-yellow-vivid` | #FFF600 | (255, 246, 0) | Cadmium yellow |
| `--bauhaus-blue-vivid` | #4166F5 | (65, 102, 245) | Ultramarine |

### Neutrals

| Token | Hex | Role |
|-------|-----|------|
| `--bauhaus-black` | #000000 | Primary text and structure |
| `--bauhaus-white` | #FFFFFF | Background and negative space |
| `--bauhaus-gray-900` | #1A1A1A | Near-black surface |
| `--bauhaus-gray-700` | #444444 | Dark secondary |
| `--bauhaus-gray-500` | #686868 | Mid-tone |
| `--bauhaus-gray-300` | #A4B1C1 | Light steel |
| `--bauhaus-gray-100` | #E8E8E8 | Pale background |

### Secondary Colors (Itten Extension)

| Token | Hex | Role |
|-------|-----|------|
| `--bauhaus-orange` | #F49836 | Secondary (trapezium) |
| `--bauhaus-green` | #24A482 | Secondary (spherical triangle) |
| `--bauhaus-violet` | #4F186B | Secondary (ellipse) |

---

## Kandinsky's Color-Form Theory

From Kandinsky's 1923 questionnaire at the Bauhaus:

### Shape-Color Associations

| Shape | Color | 3D Form | Character |
|-------|-------|---------|-----------|
| Triangle | Yellow | Pyramid | Aggressive, angular, lightweight, eccentric - "like a middle C on a brassy trumpet" |
| Square | Red | Cube | Static, heavy, physical substance - "an intensive inner seething" |
| Circle | Blue | Sphere | Relaxed, concentric, spiritual - "points toward the fourth dimension" |

### Secondary Form Associations

| Shape | Color |
|-------|-------|
| Trapezium | Orange |
| Spherical triangle | Green |
| Ellipse | Violet |

**Application**: Peter Keler's 1922 cradle directly applied this system - yellow triangle base, red square side, blue circle rocker.

**Note**: Later research (1990, PubMed) found no universal perceptual support for these associations. Value lies in providing a consistent symbolic vocabulary for design, not perceptual universality.

---

## Albers's Color Principles

Josef Albers, longest-serving Bauhaus faculty member, developed the most rigorous systematic approach to color.

### Core Thesis

> "In order to use color effectively it is necessary to recognize that color deceives continually."

### Key Principles

1. **Color Relativity**: The same color appears entirely different depending on surrounding colors. One color can look like two; two different colors can look alike.

2. **Simultaneous Contrast**: Adjacent colors alter each other's perceived hue, value, and saturation. Dissimilar qualities intensify; similar qualities mute.

3. **Reject Traditional Harmonies**: "We may forget for a while those rules of thumb of complementaries... They are worn out."

### Teaching Methodology

- Practice-first: Students worked with colored paper scraps, not paint
- Placed identical hues on different colored grounds to observe context effects
- Color systems (Munsell, Ostwald) introduced last, after developing sensitive eye

### Homage to the Square Series (1949-1976)

- Over 1,000 paintings of nested squares
- Demonstrated identical colors in different arrangements produce radically different effects
- Unmixed paint directly from tube, palette knife application
- Always started from central square outward

### Modern Application: Dark Mode

Color is relational - the same brand color requires separate tokens for light and dark themes because context transforms perception. Simultaneous contrast explains why button hover states must account for background interaction.

---

## Itten's Seven Contrasts

Johannes Itten codified seven types of color contrast foundational to Bauhaus color pedagogy:

1. **Contrast of Hue**: Pure colors at maximum saturation
2. **Light-Dark Contrast**: Value differences (up to 44 tonal gradations in exercises)
3. **Cold-Warm Contrast**: Temperature differences
4. **Complementary Contrast**: Opposite colors on wheel
5. **Simultaneous Contrast**: Adjacent color interaction
6. **Contrast of Saturation**: Intensity differences
7. **Contrast of Extension**: Quantity/area differences

### Material/Form Contrasts (Systematic Vocabulary)

| Contrast Pair |
|---------------|
| Large / Small |
| Light / Dark |
| Smooth / Rough |
| Light / Heavy |
| Wide / Narrow |
| Soft / Hard |
| Static / Dynamic |

---

## Usage Rules

### Composition Rules

- Maximum 3 chromatic colors per composition
- Black defines structure and edges
- White creates breathing room
- Gray serves as balancing neutral
- Typical scheme: black and white with single primary accent (most often red)
- Secondary colors appear occasionally but always within primary palette context

### Flat Color Only

- No gradients
- No shading
- No textures
- No shadows or complex transitions

### High Contrast Priority

- Black on white preferred
- Single primary on white
- High-contrast combinations always

---

## CSS Implementation

```css
:root {
  /* Primary */
  --bauhaus-red: #BE1E2D;
  --bauhaus-yellow: #FFDE17;
  --bauhaus-blue: #21409A;

  /* Vivid variants */
  --bauhaus-red-vivid: #E30022;
  --bauhaus-yellow-vivid: #FFF600;
  --bauhaus-blue-vivid: #4166F5;

  /* Neutrals */
  --bauhaus-black: #000000;
  --bauhaus-white: #FFFFFF;
  --bauhaus-gray-900: #1A1A1A;
  --bauhaus-gray-700: #444444;
  --bauhaus-gray-500: #686868;
  --bauhaus-gray-300: #A4B1C1;
  --bauhaus-gray-100: #E8E8E8;

  /* Secondary */
  --bauhaus-orange: #F49836;
  --bauhaus-green: #24A482;
  --bauhaus-violet: #4F186B;
}

/* WCAG AA Compliant Combinations */
.text-on-white {
  color: var(--bauhaus-black);
  background: var(--bauhaus-white);
  /* Contrast: 21:1 */
}

.accent-on-white {
  color: var(--bauhaus-red);
  background: var(--bauhaus-white);
  /* Contrast: 7.8:1 - passes AA */
}

.text-on-dark {
  color: var(--bauhaus-white);
  background: var(--bauhaus-gray-900);
  /* Contrast: 16.1:1 */
}
```

### Design Tokens (JSON)

```json
{
  "color": {
    "primary": {
      "red": { "value": "#BE1E2D" },
      "yellow": { "value": "#FFDE17" },
      "blue": { "value": "#21409A" }
    },
    "neutral": {
      "black": { "value": "#000000" },
      "white": { "value": "#FFFFFF" },
      "gray": {
        "900": { "value": "#1A1A1A" },
        "700": { "value": "#444444" },
        "500": { "value": "#686868" },
        "300": { "value": "#A4B1C1" },
        "100": { "value": "#E8E8E8" }
      }
    }
  }
}
```
