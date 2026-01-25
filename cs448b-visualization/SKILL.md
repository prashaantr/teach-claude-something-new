---
name: cs448b-visualization
description: "Data visualization design based on Stanford CS448B. Use for: (1) choosing chart types for data, (2) selecting visual encodings (position, color, size, shape), (3) critiquing/improving visualizations, (4) building D3.js visualizations, (5) designing interactions and animations, (6) choosing color palettes, (7) visualizing networks/graphs, (8) visualizing text data. Covers Bertin, Mackinlay, Cleveland & McGill perceptual principles."
---

# CS448B Visualization

## Workflows

### 1. Choose a Chart
Quick decision tree:

**What's your data?**
- Distribution -> Histogram
- Categories -> Bar chart
- X=Time, Y=Quantitative -> Line chart
- X=Quant, Y=Quant -> Scatterplot
- Hierarchy -> Treemap or node-link tree
- Network -> Force-directed or matrix

For details: See [chart-design.md](references/chart-design.md)

### 2. Choose Encodings
Priority order for quantitative data:
1. Position (most accurate)
2. Length
3. Angle/Slope
4. Area
5. Color saturation (least accurate)

**Rules:**
- Position for most important data
- Hue for categories (~7 max)
- Size for magnitude
- Never use area/volume without considering underestimation

For details: See [encoding-perception.md](references/encoding-perception.md)

### 3. Critique a Visualization
Checklist:
- [ ] Expressiveness: Shows all facts? Only facts? No lies?
- [ ] Effectiveness: Most important data on best encoding (position)?
- [ ] Zero baseline: Required for bar charts
- [ ] Color accessibility: Works for colorblind (~8% males)?
- [ ] Data-ink ratio: Remove unnecessary elements?
- [ ] Aspect ratio: Line charts banked to ~45deg?

### 4. Build with D3
Core pattern:
```javascript
svg.selectAll("circle")
  .data(data)
  .join("circle")
  .attr("cx", d => xScale(d.x))
  .attr("cy", d => yScale(d.y))
  .attr("r", 5);
```

For scales, axes, transitions: See [d3-patterns.md](references/d3-patterns.md)

### 5. Add Interaction
Techniques:
- **Brushing & Linking**: Select in one view, highlight in others
- **Dynamic Queries**: Filter via sliders
- **Details on Demand**: Tooltips

For animation timing and principles: See [interaction-animation.md](references/interaction-animation.md)

### 6. Choose Colors
| Data Type | Palette |
|-----------|---------|
| Categorical | Distinct hues (~6 max) |
| Sequential | Single hue, varying lightness |
| Diverging | Two hues + neutral midpoint |

Always test for colorblind accessibility.

For details: See [color.md](references/color.md)

### 7. Visualize Networks
Layout selection:
- **Force-directed**: Discover clusters
- **Sugiyama**: Show hierarchy
- **Matrix**: Dense networks, no occlusion

Centrality measures:
- Degree = hubs
- Betweenness = bridges
- Closeness = central access

For details: See [networks-text.md](references/networks-text.md)

### 8. Visualize Text
Use TF-IDF weighting: `log(1+tf) * log(N/df)`

Techniques:
- Word Tree: Context and continuations
- TileBars: Query distribution in documents
- Phrase Nets: Word relationships

Avoid word clouds for serious analysis.

For details: See [networks-text.md](references/networks-text.md)
