# Lecture 11: Color

## Purpose of Color
- To **label** (categorical distinction)
- To **measure** (encode quantities)
- To **represent** and imitate
- To **enliven** and decorate

*"Above all, do no harm."* — Edward Tufte

## Color Perception Pipeline

```
Light → Cone Response → Opponent Signals → Color Perception → Color Appearance → Color Cognition ("Yellow")
```

### LMS Cones
- **L** (Long) / **M** (Medium) / **S** (Short) wavelength sensitivity
- **Metamers**: Different spectra producing same LMS response appear identical
- Basis for RGB displays, cameras, scanners

### Opponent Processing
LMS responses combine into 3 channels:
| Channel | Description |
|---------|-------------|
| **A** (Achromatic) | Lightness |
| **R-G** | Red-green contrast |
| **Y-B** | Yellow-blue contrast |

No "reddish-green" or "bluish-yellow" exists (opponent pairs).

## Color Vision Deficiency
| Type | Missing/Weak | Prevalence |
|------|--------------|------------|
| **Protanopia** | L cones (red) | ~1% males |
| **Deuteranopia** | M cones (green) | ~1% males |
| **Tritanopia** | S cones (blue) | Rare |

**Design tip**: Use color vision simulators; avoid red-green only encoding.

## Perceptual Color Spaces

### Munsell System (1905)
- **Hue**: Position on color wheel
- **Value**: Lightness (dark → light)
- **Chroma**: Saturation/colorfulness

### HSL vs LAB
| Space | Perceptual Uniformity |
|-------|----------------------|
| HSL Lightness | Poor (yellow appears brighter than blue at same L) |
| CIE LAB L* | Good (matches perceived brightness) |

## Color Appearance Effects

| Effect | Description |
|--------|-------------|
| **Simultaneous Contrast** | Same color looks different on different backgrounds |
| **Bezold Effect** | Adjacent colors alter appearance |
| **Crispening** | Perceived difference enhanced when background matches |
| **Spreading** | Adjacent colors visually blend at high spatial frequency |

*"Color deceives continually."* — Josef Albers

## Color Naming

### Basic Color Terms (Berlin & Kay)
11 universal terms across languages:
White, Grey, Black, Red, Yellow, Green, Blue, Pink, Orange, Brown, Purple

### Design Implication
- Maximize **color name distance** between palette entries
- Avoid blue/green boundary, orange/red boundary
- Use colors with high **naming salience** (agreement on name)

## Colormap Design Considerations
1. Perceptually distinguishable colors
2. Value distance matches perceptual distance
3. Colors align with concepts
4. Aesthetically pleasing
5. Respect color vision deficiency
6. Survive B&W printing
7. Don't overwhelm (~6 hues max for categorical)

## Scale Types

### Categorical/Discrete
- Use distinct hues with similar luminance
- Limit to ~6-8 colors
- Maximize color name distance

### Sequential (Quantitative)
- Ramp in luminance (+ optional hue)
- Higher values → darker colors typically

### Diverging
- Meaningful midpoint (use neutral grey)
- Saturated colors at endpoints
- Limit to 3-9 steps

### Rainbow Colormaps
| Pros | Cons |
|------|------|
| High nameability aids inference | Hues not naturally ordered |
| Good for distribution tasks | Perceptual banding artifacts |
| | Unfriendly to colorblind |
| | Low-luminance blues hide detail |

**Task matters**: Rainbows help inference but hurt value comparison.

## Classing Methods
1. **Equal interval** — arithmetic progression
2. **Quantiles** — recommended default
3. **Standard deviations** — statistical meaning
4. **Jenks natural breaks** — minimize within-class variance

## Tools
- **ColorBrewer** (colorbrewer2.org) — curated palettes
- **Color naming tool** (vis.stanford.edu/color-names)
