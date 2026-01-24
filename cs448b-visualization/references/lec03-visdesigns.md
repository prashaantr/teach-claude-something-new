# Lecture 03: Visualization Design and Redesign

## Design Considerations Checklist

### Essential Guides
- Title, labels, legend, captions, source attribution

### Expressiveness & Effectiveness
- Express **all** facts and **only** the facts
- Avoid unexpressive marks (unnecessary lines, gradients)
- Match encodings to data type (perceptually effective)
- Don't distract: faint gridlines, pastel highlights/fills
- **"Elimination diet"**: start minimal, add only what's needed

### Support Comparison & Pattern Perception
- Enable comparisons: between elements, to reference lines, to counts
- Use reader-friendly units and labels

### Data Organization
- Group/sort by meaningful dimensions
- Transform data when needed (filter, log, normalize)
- Verify model choices (e.g., regression lines) are appropriate

### Reduce Cognitive Overhead
- Minimize visual search and ambiguity
- Appropriate size, aspect ratio, legible text
- **Direct labeling** over legend lookups when possible
- Avoid indiscernible color mappings
- **Be consistent**: visual inferences should match data inferences

## Chart Type Guide

### Bar Charts
- Best for: Comparing discrete categories
- Can show multiple measures (e.g., athletes vs medal winners)
- Horizontal bars better for long category labels

### Stacked Bar Charts
- Best for: Part-to-whole relationships over categories
- Shows composition within each bar
- Color encodes sub-categories (e.g., Gold/Silver/Bronze)
- Limitation: Hard to compare middle segments across bars

### Line Charts
- Best for: Continuous data, trends over time
- Implies connection/continuity between points
- Multiple lines for comparison (use direct labels or legend)
- Can overlay with bars for dual encoding

### Area Charts
- Best for: Cumulative values over time
- Filled area emphasizes magnitude
- Good for showing coverage/span (e.g., coach tenure periods)

### Stacked Area Charts
- Best for: Part-to-whole over continuous dimension (time)
- Shows both total and composition
- Order matters: most stable categories at bottom
- Limitation: Hard to read individual layer values

### Other Chart Types
| Type | Use Case | Caution |
|------|----------|---------|
| Pie Charts | Part-to-whole (few categories) | Angle comparison is imprecise |
| Word Clouds | Frequency/prominence | Not precise; decorative |
| Sankey Diagrams | Flow between categories | Can get cluttered |
| Geographic Maps | Location-based data | Size distortion issues |
| Bubble Charts | 3 variables (x, y, size) | Area perception imprecise |

## Design Patterns

### Dual-Axis Charts
- Combine different scales (e.g., count + percentage)
- Label axes clearly, use visual distinction
- Example: Total medals (area) + Female % (line)

### Tooltips
- Provide details on demand
- Include: category, value, percentage, context

### Comparison Annotations
- Add reference lines for benchmarks
- Include percentage/text callouts for key insights
- Example: "52% of Aquatics athletes won medals"

## Common Pitfalls
1. Too many colors/categories in legends
2. Missing titles/labels
3. Inconsistent scales across related charts
4. Using lines for discrete/unconnected data
5. Pie charts with many small slices
