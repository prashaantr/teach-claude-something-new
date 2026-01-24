# Lecture 06: Interaction

## Core Concept
Interaction requires **mutual intelligibility** / shared understanding between people and machines.

## Gulfs of Execution and Evaluation (Norman 1986)

### Gulf of Execution
The difference between user's **intentions** and **allowable actions**
- Example: "Draw a scatterplot" vs. low-level commands (Move 90 30, Rotate 35...)
- Reduced by: high-level visualization tools (Tableau, Excel)

### Gulf of Evaluation
Effort to **interpret system state** and determine if expectations met
- Example: Raw data table vs. scatterplot vs. correlation coefficient
- Visualization reduces this gulf by making patterns visible

## Selection Methods

### Point Selection
- Mouse hover / click
- Touch / tap
- Select nearby element (Bubble Cursor - Voronoi regions)

### Region Selection
- Rubber-band / lasso
- Area cursors ("Brushes")

## Brushing and Linking

**Brush**: Direct attention to a subset of data
**Link**: See selected data highlighted in other views

### Linking Types
| Type | Description |
|------|-------------|
| **By tuple** | Match same data point across views |
| **By query** | Match range or field values |

### Example: Baseball Statistics (Wills 1995)
- Multiple coordinated views (salary, years, hits, assists, position)
- Select in one view → see distribution in others
- Reveals relationships across dimensions

## Dynamic Queries

### Problems with SQL-style queries
1. For programmers only
2. Rigid syntax
3. Only exact matches
4. Too few/many hits
5. No hint on reformulation
6. Slow question-answer loop
7. Results as table

### Direct Manipulation Principles (Shneiderman)
1. **Visual representation** of objects and actions
2. **Rapid, incremental, reversible** actions
3. **Selection by pointing** (not typing)
4. **Immediate, continuous** display of results

### Key Examples
| System | Year | Innovation |
|--------|------|------------|
| HomeFinder | 1992 | Sliders for price/bedrooms, map display |
| ZipDecode | 2004 | Progressive filtering by typing digits |
| NameVoyager | 2005 | Animated stacked area, type to filter |
| TimeSearcher | 2002 | Sketch-based time-series queries |
| Parallel Coordinates | - | Brush ranges on multiple axes |

## Early Systems: Bertin's Matrices (1981)

### Reorderable Matrix Algorithm
1. Choose row with particular visual aspect → move to extremity
2. Move similar rows close, opposite rows to bottom
3. Creates two opposing groups + middle group
4. Repeat for columns
5. Iterate

**Modern implementation**: Bertifier (Perin 2014)

## Cross-Filtering
Brushing where selection in one histogram filters data shown in other histograms.

## Dynamic Queries: Pros & Cons

| Pros | Cons |
|------|------|
| Useful for novices and experts | Simple queries only |
| Quick exploration | Lots of controls |
| | Screen space limits data shown |

## Summary
- Good visualizations are **task dependent**
- Pick interaction technique to support the task
- Fundamental techniques: **Selection**, **Brushing & Linking**, **Dynamic Queries**
