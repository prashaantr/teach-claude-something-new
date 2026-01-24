# Lecture 02: Data & Image Models

## The Big Picture
Task (questions/goals) + Data (types, domain) → Processing → Mapping (visual encoding) → Image (marks, visual channels)

## Data Concepts

### Data Table Structure
- **Dataset**: Collection of data items
- **Data Item/Observation**: Single row/record
- **Data Field**: Column/attribute
- **Cell Value**: Individual data point

### Data Models vs Conceptual Models
- **Data Model**: Formal description (how data is stored - strings, bools, floats)
- **Conceptual Model**: Mental construction with semantics (what data means - supports reasoning)

### Data Types (Stevens 1946)
| Type | Description | Operations | Example |
|------|-------------|------------|---------|
| **N - Nominal** | Labels/categories | =, ≠ | Fruits: apple, orange |
| **O - Ordinal** | Ordered categories | =, ≠, <, > | Egg grades: AA, A, B |
| **Q - Interval** | Zero arbitrary | =, ≠, <, >, - | Dates, Lat/Lon |
| **Q - Ratio** | Zero fixed/meaningful | =, ≠, <, >, -, ÷ | Length, mass, counts |

Note: Q ⊂ O ⊂ N (hierarchy)

### Dimensions vs Measures
- **Dimensions**: Independent variables, qualitative descriptors (names, dates, categories)
- **Measures**: Dependent variables, quantitative values that can be aggregated (sum, count, avg)
- Distinction is task-dependent

## Data Transformations (SQL/Relational Algebra)
- **Projection (SELECT)**: Choose columns
- **Selection (WHERE)**: Filter rows
- **Sorting (ORDER BY)**: Order rows
- **Aggregation (GROUP BY)**: Partition and summarize
- **Combination (JOIN, UNION)**: Integrate tables

## Image Model (Bertin 1967)

### Marks
Geometric primitives: points, lines, areas

### Visual Attributes/Channels
| Attribute | N | O | Q |
|-----------|---|---|---|
| Position | ✓ | ✓ | ✓ |
| Size | ✓ | ✓ | ✓ |
| Value (lightness) | ✓ | ✓ | ~ |
| Texture | ✓ | ~ | |
| Color (hue) | ✓ | | |
| Orientation | ✓ | | |
| Shape | ✓ | | |

- **Value** (lightness): Perceived as ordered → good for O, okay for Q
- **Hue**: Perceived as unordered → good for N only

## Visual Encoding
Mapping data fields to mark attributes: `data → visual channel`

Example: `mark: points; data1 → x-pos; data2 → y-pos; data3 → color; data4 → size`

## Design Principles (Mackinlay 1986)

### Expressiveness Criterion
Visualization must express **all** facts in data and **only** facts in data
- Bad: 1-to-many relations on single position (loses data)
- Bad: Bar length for nominal data (implies false ordering)

### Effectiveness Criterion
More effective = information more readily perceived

### Mackinlay's Ranking (by data type)
**Quantitative**: Position > Length > Angle > Slope > Area > Volume > Density > Saturation > Hue > ...
**Ordinal**: Position > Density > Saturation > Hue > Texture > ...
**Nominal**: Position > Hue > Texture > Connection > Containment > ...

### Principles
1. **Consistency**: Visual variable properties should match data properties
2. **Importance Ordering**: Encode most important data with most effective channel

## APT - Automatic Presentation Tool (Mackinlay 1986)
Algorithm: Given prioritized data fields →
1. Test expressiveness of encodings
2. Rank by effectiveness
3. Output most effective visualization

### Limitations
- Doesn't cover networks, maps, 3D, animation
- Ignores interaction, semantics, conventions
- Single visualization output only
