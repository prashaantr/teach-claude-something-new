# Lecture 04: Exploratory Data Analysis (EDA)

## What is EDA?
**"Exposure, the effective laying open of data to display the unanticipated"** - Tukey 1962

Nothing substitutes for the **flexibility of the informed human mind** - tools must facilitate human involvement.

## EDA Process
1. Construct graphics to address questions
2. Inspect "answer" and assess new questions
3. Repeat!

**Key principle**: "Show data variation, not design variation" - Tufte

## Data Wrangling Reality
- ~80% of time spent preparing data, 20% complaining about it
- Tasks: reformat, clean, quality assess, integrate

### Tidy Data (Wickham 2014)
1. Each **field** forms a column
2. Each **observation** forms a row
3. Each **observational unit type** forms a table

### Data Quality Hurdles
| Issue | Examples |
|-------|----------|
| Missing Data | No measurements, redacted |
| Erroneous Values | Misspellings, outliers |
| Type Conversion | Zip code → lat/lon |
| Entity Resolution | "Stanford" vs "Stanford University" |
| Data Integration | Errors combining sources |

## EDA Workflow

### 1. Profile Data First
- Check univariate distributions (histograms)
- Look for missing/null values
- Identify outliers and anomalies

### 2. Then Explore Relationships
- Scatterplots for Q×Q
- Compare distributions across categories
- Look for unexpected patterns

### 3. Exercise Skepticism
- **"First sign a visualization is good: it shows a problem in your data"** - Wattenberg
- Check assumptions continuously
- Avoid premature fixation on one view

## Tools for EDA

### Wrangling
- **Code**: Arquero (JS), dplyr (R), pandas (Python)
- **GUI**: Tableau, Open Refine

### Visualization
- **Tableau/Polaris**: Simultaneously specify database queries + visualization
- Choose data first, then visualization (not vice versa)
- Uses smart defaults for encodings (like APT)

## Historical Context
| Era | Period | Key Development |
|-----|--------|-----------------|
| Golden Age | 1786-1900 | Playfair charts, Nightingale, Minard |
| Rise of Statistics | 1900-1950 | Formal methods, little graphical innovation |
| Modern EDA | 1962+ | Tukey's call for exploratory approaches |
