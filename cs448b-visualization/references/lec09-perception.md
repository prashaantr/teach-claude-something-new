# Lecture 09: Perception

## Core Concept
**Graphical Perception**: The ability to interpret visual encodings and decode information in graphs.

## Design Principles (Mackinlay 1986)

### Expressiveness
Tell the truth and nothing but the truth (don't lie, don't lie by omission)

### Effectiveness
Use encodings that people decode better (faster and/or more accurate)

## Signal Detection

### Weber's Law (Just Noticeable Difference)
```
ΔS = k × (ΔI / I)
```
- **Ratios** more important than magnitude
- Continuous variations perceived in **discrete steps**

### Color Encoding Implications
| Attribute | Perceived As | Best For |
|-----------|--------------|----------|
| **Value** (lightness) | Ordered | Ordinal (O), Quantitative (Q) |
| **Hue** | Unordered | Nominal (N) |

## Magnitude Estimation

### Stevens' Power Law
```
S = I^p
```
- p < 1: underestimate (area, volume, brightness)
- p = 1: accurate (length)
- p > 1: overestimate (electric shock)

| Sensation | Exponent |
|-----------|----------|
| Length | ~1.0 |
| Area | ~0.7 |
| Volume | ~0.6 |
| Brightness | 0.33 |

### Flannery Scaling (for circles)
```
r = r₀(v/v₀)^0.5716
```
Compensates for area underestimation in proportional symbol maps.

## Cleveland & McGill's Ranking (1984)

**Most accurate → Least accurate:**
1. Position (common scale)
2. Position (non-aligned)
3. Length
4. Slope / Angle
5. Area
6. Volume
7. Color hue-saturation-density

## Multiple Attributes

### Dimension Types
| Type | Behavior |
|------|----------|
| **Integral** | Filtering interference AND redundancy gain |
| **Separable** | No interference or gain |
| **Configural** | Only interference, no redundancy gain |
| **Asymmetrical** | One separable from other, not vice versa (Stroop effect) |

### Design Implications
- **Redundant encoding** (same data → multiple channels): facilitates reading
- **Orthogonal encoding** (different data → multiple channels): may cause interference

## Pre-Attentive Processing

### Pre-Attentive Features (pop-out)
- Color (hue)
- Orientation
- Size
- Shape
- Motion
- Curvature
- Length, width
- Closure, intersection

### NOT Pre-Attentive
- **Feature conjunctions** (e.g., red AND circle among red squares and blue circles)
- Requires serial search

### Feature Integration Theory (Treisman)
- Separate feature maps for color, orientation, etc.
- Attention required to bind features at a location

## Gestalt Principles

| Principle | Description |
|-----------|-------------|
| **Figure/Ground** | Separating foreground from background |
| **Proximity** | Close elements grouped together |
| **Similarity** | Similar elements grouped |
| **Symmetry** | Bilateral symmetry → strong figure |
| **Connectedness** | Connected elements grouped (overrules others) |
| **Continuity** | Prefer smooth, continuous contours |
| **Closure** | Complete incomplete shapes |
| **Common Fate** | Elements moving together grouped |
| **Transparency** | Requires continuity + proper color correspondence |

## Change Blindness
- Large changes can go unnoticed if attention is diverted
- Flicker paradigm: A → blank → A' → blank → ...
- Implications: Don't assume users see everything; use animation/highlighting for important changes

## Summary
1. Effective encodings require perceptual knowledge
2. Individual visual attributes often **pre-attentive**
3. Multiple attributes may be **separable** or **integral**
4. **Gestalt principles** guide higher-level design
5. We don't always see everything (change blindness)
