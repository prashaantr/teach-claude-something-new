# Lecture 07: Introduction to D3

## What is D3?
**D3 = "Data-Driven Documents"**

Data visualization API built on HTML, CSS, JavaScript, & SVG

| Pros | Cons |
|------|------|
| Highly customizable | Very "low-level" |
| Dev/debugging tools | |
| Good docs, large community | |
| Integrates with web | |

## Web Technology Stack

### HTML Structure
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>/* CSS */</style>
</head>
<body>
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <script>/* D3 code */</script>
</body>
</html>
```

### SVG (Scalable Vector Graphics)
```html
<svg width="960" height="500">
  <circle cx="120" cy="150" r="60" style="fill: gold;"/>
</svg>
```

## Document Object Model (DOM)
HTML → Tree structure of elements
- D3 manipulates this tree to create visualizations
- SVG elements become children of DOM nodes

## D3 Selection

### Basic Selection
```javascript
// Select first matching element
d3.select("circle")

// Select ALL matching elements
d3.selectAll("circle")
```

### Manipulation (Chaining)
```javascript
d3.select("circle")
  .attr("cx", 40)      // set attribute
  .attr("cy", 50)
  .attr("r", 24)
  .style("fill", "red"); // set CSS style
```

## Data Binding & Joining

### The Join Pattern
```javascript
selection
  .selectAll('li')
  .data(listData)
  .join(
    enter => enter.append('li'),  // new data: create element
    update => update,              // existing: update element
    exit => exit.remove()          // removed data: delete element
  )
  .text(d => `${d.country}: ${d.pop}`)
```

### Three Sub-Selections

| Selection | Contains | Action |
|-----------|----------|--------|
| **Enter** | Placeholders for data without DOM elements | Create new elements |
| **Update** | Existing DOM elements matching data | Modify attributes |
| **Exit** | Existing DOM elements without matching data | Remove elements |

### Visual Model
```
     Data          Elements
       ○               ○
      ╱ ╲             ╱ ╲
   Enter  ───────  Update  ───────  Exit
   (new)          (matched)        (removed)
```

## Key Concepts

1. **Selection**: Query DOM elements using CSS selectors
2. **Data binding**: Associate data array with DOM elements
3. **Join**: Sync data changes to visual elements
4. **Chaining**: Fluent API for setting multiple properties

## Common Pattern for Visualization
```javascript
// 1. Create SVG container
const svg = d3.select("body")
  .append("svg")
  .attr("width", 960)
  .attr("height", 500);

// 2. Binddata and create marks
svg.selectAll("circle")
  .data(dataset)
  .join("circle")
  .attr("cx", d => xScale(d.x))
  .attr("cy", d => yScale(d.y))
  .attr("r", 5);
```

## Resources
- D3 docs: https://d3js.org
- Observable notebooks for interactive D3 development
