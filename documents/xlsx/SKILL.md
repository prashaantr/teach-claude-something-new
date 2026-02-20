---
name: xlsx
description: |
  Use this skill for Excel/spreadsheet files. This includes: creating,
  editing, reading .xlsx/.xlsm/.csv/.tsv files, data analysis, formulas,
  formatting, charts. Trigger when user mentions spreadsheets, Excel,
  or data tables.
---

# Excel/Spreadsheet Processing

## Reading Excel Files

```python
import pandas as pd

# Read entire file
df = pd.read_excel("data.xlsx")
print(df.head())

# Read specific sheet
df = pd.read_excel("data.xlsx", sheet_name="Sheet2")

# Read CSV
df = pd.read_csv("data.csv")
```

## Creating Excel Files

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Value': [100, 200, 300]
}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)
```

## With Formatting (openpyxl)

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
ws = wb.active

# Add data
ws['A1'] = 'Name'
ws['B1'] = 'Value'
ws['A2'] = 'Alice'
ws['B2'] = 100

# Format headers
header_font = Font(bold=True)
ws['A1'].font = header_font
ws['B1'].font = header_font

wb.save("formatted.xlsx")
```

## Formulas

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 10
ws['A2'] = 20
ws['A3'] = '=SUM(A1:A2)'  # Formula, not hardcoded value

wb.save("with_formulas.xlsx")
```

## Professional Standards

**Color Coding (Financial Models):**
- Blue text: hardcoded inputs
- Black text: formulas
- Green text: internal links
- Yellow background: key assumptions

**Number Formatting:**
- Currency with units in headers: "Revenue ($mm)"
- Zeros displayed as "-"
- Negative numbers in parentheses

**Best Practices:**
- Use formulas, not hardcoded calculated values
- Place assumptions in separate cells
- Document sources for hardcoded values
