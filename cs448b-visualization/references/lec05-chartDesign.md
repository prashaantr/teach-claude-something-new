# Lecture 05: Chart Design

## Design Space of Visual Encodings

Map **data fields** (N, O, Q types) → **visual channels** (x, y, color, shape, size) for **mark types** (point, bar, line)

Additional choices: encoding parameters (log scale, sorting) + data transforms (bin, group, aggregate)

## Mackinlay's Criteria (Review)

### Expressiveness
Visualization must express **all** facts and **only** facts in data

### Effectiveness
More effective = information more readily **perceived**

## Scales and Axes

### Include Zero?
| Task | Recommendation |
|------|----------------|
| Compare **proportions** (Q-Ratio) | Yes, include zero |
| Compare **relative position** (Q-Interval) | No, zoom to data range |

**Rule**: Bar charts always need zero baseline (length encodes value)

### Axis Tick Mark Selection
- **Simplicity**: multiples of 10, 5, 2
- **Coverage**: ticks near data range ends
- **Density**: not too many/few
- **Legibility**: whitespace, horizontal text

### Scale Breaks vs Log Scale
| Approach | Use When | Limitation |
|----------|----------|------------|
| Clip outliers | Few extreme values | Hides data |
| Scale break | Need both ranges | Hard to compare across break |
| **Log scale** | Multiple orders of magnitude | Only for positive values |

### When to Use Log Scale
- Address data skew (long tails, outliers)
- Focus on **multiplicative factors** / percent change
- Exponential growth patterns
- **Constraint**: positive, non-zero values only

**Key insight**: `log(xy) = log(x) + log(y)` — equal steps = equal % change

## Aspect Ratio

### Banking to 45° (Cleveland 1985)
- Line segments maximally discriminable at 45° angles
- **Method**: Optimize aspect ratio so average segment angle ≈ 45°
- Helps perceive trends in time series

**Note**: Trends occur at different scales — bank to fitted trend lines, not raw data

## Fitting Data

### Regression Lines
- Human "by eye" fits often biased by outliers
- Linear regression sensitive to outliers
- **Residual plots**: show vertical distance from fit, reveal fit quality

### Data Transformations
- Log transforms for exponential relationships
- Residual plots to assess model fit

## Sorting

### Trellis/Small Multiples (Becker 1996)
- **Panel variables**: what's shown in each panel
- **Condition variables**: what varies across panels

### Ordering Strategies
| Order | Effect |
|-------|--------|
| Alphabetical | Easy lookup, no data insight |
| **Main-effects** | Sort by data value, reveals patterns |

## Summary

Well-designed visualizations:
1. Use **expressive** and **effective** encodings
2. Avoid **over-encoding**
3. Emphasize features **relevant to task**

**Key insight**: Rarely does one visualization answer all questions — ability to generate appropriate visualizations quickly is critical!
