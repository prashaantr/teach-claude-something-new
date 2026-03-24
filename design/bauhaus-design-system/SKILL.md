---
name: bauhaus-design-system
description: |
  Bauhaus design system reference for typography, color, layout, and visual hierarchy based on Mid/Late Bauhaus (1925-1933) principles. Use when: (1) designing interfaces with Bauhaus aesthetics, (2) applying geometric sans-serif typography, (3) implementing primary color palettes with Kandinsky's color-form theory, (4) creating asymmetric grid layouts, (5) building design systems with Bauhaus foundations, (6) seeking historical context on Bayer, Moholy-Nagy, Albers, or Tschichold. Triggers: "Bauhaus style", "geometric design", "Universal typeface", "New Typography", "Kandinsky colors", "Albers color theory", "Swiss style foundations", "modernist design system".
---

# Bauhaus Design System

A codified design reference based on Mid/Late Bauhaus (1925-1933) principles from the Dessau and Berlin eras. These principles became the foundation for Swiss International Typographic Style and every major digital design system today.

## Core Principles

1. **Geometric construction** - All forms derive from circle, triangle, square
2. **Sans-serif typography** - Flush-left, lowercase preference, dramatic scale contrast
3. **Primary palette** - Red, yellow, blue + black, white, gray; flat color only
4. **Asymmetric layouts** - Grid-based, generous white space as active element
5. **Photography over illustration** - Typophoto integration
6. **Function determines form** - Every element serves communication

## Quick Reference

### Color-Form Associations (Kandinsky)

| Shape | Color | Character |
|-------|-------|-----------|
| Triangle | Yellow | Aggressive, angular, lightweight |
| Square | Red | Static, heavy, grounded |
| Circle | Blue | Relaxed, concentric, spiritual |

### Typography Hierarchy

- **Display**: 3.5-4x base, Bold/Black, lowercase, flush-left
- **H1**: 2.5-3x base, Bold, lowercase
- **H2**: 2-2.5x base, Bold, lowercase
- **Body**: 16px base, Regular, sentence case, ragged-right
- **Caption**: 0.75-0.85x base, Regular/Light, lowercase

Key metrics: 45-75 character line length, 1.4-1.6x leading.

### Primary Color Tokens

```
--bauhaus-red:    #BE1E2D
--bauhaus-yellow: #FFDE17
--bauhaus-blue:   #21409A
--bauhaus-black:  #000000
--bauhaus-white:  #FFFFFF
```

### Recommended Fonts (Google Fonts)

- **Display**: Jost (closest free Futura), Josefin Sans
- **Body**: Inter, DM Sans, Work Sans

## Detailed References

- **Color System**: See [references/color-system.md](references/color-system.md) for complete tokens, usage rules, Albers principles
- **Typography**: See [references/typography.md](references/typography.md) for type scales, Tschichold rules, font pairing
- **Layout & Grid**: See [references/layout-grid.md](references/layout-grid.md) for grid specs, spacing scales, CSS examples
- **Key Designers**: See [references/designers.md](references/designers.md) for Moholy-Nagy, Bayer, Albers, Schmidt, Bill

## Design Rules

### Do
- Maximum 3 chromatic colors per composition
- Use black as primary structure color
- Treat white space as active design element
- Make size differences clearly distinct (not subtle)
- Use one typeface family, exhaust its variations before adding another
- Apply heavy rules/lines as structural dividers

### Don't
- Use gradients, shadows, or complex transitions
- Center-align layouts (asymmetric always)
- Use decorative ornament for hierarchy
- Mix uppercase and lowercase inconsistently
- Add illustration where photography serves better

## Modern Application

Bauhaus principles directly inform:
- **Material Design**: 8px baseline grid, systematic type scale, constrained color
- **IBM Carbon**: Enterprise-scale systematic consistency
- **Apple Design**: Through Dieter Rams/Braun lineage
- **WCAG Accessibility**: 4.5:1 contrast (AA), functional color use

### Albers Principle for Dark Mode

Color is relational - the same brand color requires separate tokens for light/dark themes because context transforms perception.
