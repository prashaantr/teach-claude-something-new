# Bauhaus Typography

## Table of Contents
1. [Core Typography Principles](#core-typography-principles)
2. [Tschichold's New Typography Rules](#tschicholds-new-typography-rules)
3. [Type Scale Specification](#type-scale-specification)
4. [Bayer's Universal Alphabet](#bayers-universal-alphabet)
5. [Recommended Typefaces](#recommended-typefaces)
6. [Moholy-Nagy's Typophoto](#moholy-nagys-typophoto)
7. [CSS Implementation](#css-implementation)

---

## Core Typography Principles

The Bauhaus typographic revolution was not about inventing radical typefaces but using existing typefaces in a radical way:

1. **Flush-left alignment** (never centered)
2. **Asymmetric layouts**
3. **Dramatic scale contrast**
4. **Integration of photography as structural element**
5. **Lowercase preference** (Bayer's advocacy)
6. **Sans-serif only** (Tschichold's rule)

### What They Actually Used

The Bauhaus print shop relied on commercially available typefaces:
- **Display**: Breite Grotesk, Venus, Aurora-Grotesk, Industria
- **Body**: Genzsch-Antiqua (serif) for extended reading
- **Later**: Futura (after 1927 release)

---

## Tschichold's New Typography Rules

Jan Tschichold's *Die Neue Typographie* (1928) codified Bauhaus typographic practice:

### Absolute Rules

1. **Sans-serif typefaces only** - all other typefaces condemned
2. **Asymmetric layouts always** - centered/symmetric arrangements "boring and lacking hierarchy"
3. **Flush-left, ragged-right** - the default alignment
4. **Standardized DIN paper sizes** - for all printed matter
5. **Photography over illustration** - objective, modern communication
6. **Hierarchy through size, weight, position** - never through ornament
7. **White space as active element** - "the blank space should be positive"
8. **Sizes must be clearly different** - subtle differences look like mistakes
9. **Exhaust one typeface family** before introducing another

### Penguin Composition Rules (Later Tschichold)

Precise specifications from his Penguin work (1947-49):
- Word spacing: approximately half the width of lowercase 'i'
- Footnotes: 2 points smaller than body text
- No extra space between sentences
- Cover dimensions: golden ratio (110mm x 180mm)

---

## Type Scale Specification

### Hierarchy Table

| Level | Scale | Weight | Case | Alignment |
|-------|-------|--------|------|-----------|
| Display | 3.5-4x base | Bold/Black | Lowercase | Flush-left |
| H1 | 2.5-3x base | Bold | Lowercase | Flush-left |
| H2 | 2-2.5x base | Bold | Lowercase | Flush-left |
| H3 | 1.5-1.75x base | Medium/Semibold | Lowercase | Flush-left |
| Body | 16px base | Regular | Sentence case | Flush-left, ragged-right |
| Caption | 0.75-0.85x base | Regular/Light | Lowercase | Flush-left |

### Key Metrics

| Metric | Value |
|--------|-------|
| Base size | 16px |
| Line length | 45-75 characters |
| Line height (leading) | 1.4-1.6x point size |
| Word spacing | ~0.5x width of lowercase 'i' |
| Letter-spacing | Optical (visual, not mechanical) |

### Golden Ratio Scale (1.618)

| Level | Size | Rounded |
|-------|------|---------|
| Caption | 10px | 10px |
| Body | 16px | 16px |
| H3 | 25.9px | 26px |
| H2 | 41.9px | 42px |
| H1 | 67.8px | 68px |
| Display | 109.7px | 110px |

### Augmented Fourth Scale (1.5)

| Level | Size | Rounded |
|-------|------|---------|
| Caption | 11px | 11px |
| Body | 16px | 16px |
| H3 | 24px | 24px |
| H2 | 36px | 36px |
| H1 | 54px | 54px |
| Display | 81px | 81px |

---

## Bayer's Universal Alphabet

Herbert Bayer designed Universal in 1925 for all official Bauhaus communications.

### Construction Principles

- Built from three geometric primitives: circles, straight lines, simple arcs
- All constructible with ruler and compass
- Every stroke maintains uniform weight
- No serifs, no calligraphic suggestion
- **No uppercase** - "since speech reveals no difference between upper and lower case, why should written text?"

### Limitations

- Horizontals and verticals at identical weight caused fill-in at small sizes
- Never cast as commercial metal type during Bayer's lifetime
- Served as lettering model for posters, mastheads, signage

### Digital Revivals

| Typeface | Year | Designer | Notes |
|----------|------|----------|-------|
| ITC Bauhaus | 1975 | Ed Benguiat, Victor Caruso | Includes both cases |
| Architype Bayer | 1997 | The Foundry | Lowercase only, faithful |

### Related Experiments

- **Albers Kombinations-Schrift** (1926-28): Modular stencil alphabet using only rectangles, circles, semicircles, quarter circles on grid
- **Joost Schmidt**: Modular geometric alphabets

---

## Recommended Typefaces

### Google Fonts

| Typeface | Use | Notes |
|----------|-----|-------|
| **Jost** | Display | Closest free Futura revival (originally named "Renner*") |
| **Josefin Sans** | Display | Echoes Bayer's Universal proportions |
| **Poppins** | Display/Body | Pure geometric monolinear forms |
| **DM Sans** | Body | Geometric, optimized for screens |
| **Inter** | Body | Tall x-height, designed for digital interfaces |
| **Work Sans** | Body | Grotesk-style for body text |

### Pairing Strategy

Pair geometric sans for display (Jost, Josefin Sans) with humanist sans for body (Inter, DM Sans). This mirrors Bauhaus hierarchy: bold, architecturally-scaled headlines over functional body text.

### Historical Geometric Sans-Serifs

| Typeface | Designer | Year | Notes |
|----------|----------|------|-------|
| Erbar-Grotesk | Jakob Erbar | c. 1926 | First geometric sans-serif |
| Futura | Paul Renner | 1927 | De facto Bauhaus typeface, low x-height |
| Kabel | Rudolf Koch | 1927-29 | Subtle calligraphic qualities |
| DIN | — | — | Industrial standardization emphasis |

---

## Moholy-Nagy's Typophoto

László Moholy-Nagy coined "typophoto" in *Painting, Photography, Film* (1925):

> "Typography is communication composed in type. Photography is the visual presentation of what can be optically apprehended. Typophoto is the visually most exact rendering of communication."

### Key Concept: Tempo

Variable pacing and filmic quality in reading experience. "Dynamic of the Metropolis" demonstrated this: chapter-as-storyboard with dynamic montage.

### Layout Innovations

- Bold type used liberally for emphasis
- Heavy rules on left margin to indent important passages
- Bold circles for section breaks
- Smaller circles for footnotes
- Printed page as visual field: type, image, white space as equal elements

---

## CSS Implementation

```css
:root {
  /* Type scale - Golden Ratio */
  --type-scale-ratio: 1.618;
  --type-base: 16px;

  --type-caption: 10px;
  --type-body: 16px;
  --type-h3: 26px;
  --type-h2: 42px;
  --type-h1: 68px;
  --type-display: 110px;

  /* Font families */
  --font-display: 'Jost', 'Josefin Sans', sans-serif;
  --font-body: 'Inter', 'DM Sans', sans-serif;

  /* Metrics */
  --line-height-body: 1.5;
  --line-height-heading: 1.2;
  --line-length-min: 45ch;
  --line-length-max: 75ch;
}

/* Base typography */
body {
  font-family: var(--font-body);
  font-size: var(--type-body);
  line-height: var(--line-height-body);
  text-align: left;
}

/* Headings - lowercase, flush-left */
h1, h2, h3 {
  font-family: var(--font-display);
  line-height: var(--line-height-heading);
  text-transform: lowercase;
  text-align: left;
  margin-bottom: 0.5em;
}

h1 {
  font-size: var(--type-h1);
  font-weight: 700;
}

h2 {
  font-size: var(--type-h2);
  font-weight: 700;
}

h3 {
  font-size: var(--type-h3);
  font-weight: 500;
}

/* Display text */
.display {
  font-family: var(--font-display);
  font-size: var(--type-display);
  font-weight: 900;
  text-transform: lowercase;
  line-height: 1.1;
}

/* Caption */
.caption {
  font-size: var(--type-caption);
  font-weight: 400;
  text-transform: lowercase;
}

/* Optimal line length */
p, .prose {
  max-width: var(--line-length-max);
}
```

### Font Import

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Jost:wght@400;500;700;900&display=swap" rel="stylesheet">
```
