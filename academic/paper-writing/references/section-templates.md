# Section Templates

Detailed templates and examples for each paper section.

## Abstract Template

```
[PROBLEM]: [One sentence describing the problem and why it matters]
[GAP]: [What current approaches miss or get wrong]
[APPROACH]: [Your key insight or method in one sentence]
[RESULTS]: [Quantitative results - be specific with numbers]
[SIGNIFICANCE]: [Why this matters for the field]
```

**Example:**
> Large language models struggle with multi-step reasoning, often producing plausible but incorrect chains of thought. Current prompting techniques lack mechanisms to verify intermediate steps. We introduce VerifyChain, which augments chain-of-thought with step-level verification using a learned critic model. On GSM8K, VerifyChain improves accuracy from 78.2% to 89.1% while reducing reasoning errors by 43%. Our approach enables more reliable deployment of LLMs in reasoning-critical applications.

## Introduction Structure

**Paragraph 1: Hook + Problem**
- Start with a compelling fact or observation
- Define the problem clearly
- Explain why it matters (real-world impact)

**Paragraph 2: Current Approaches + Gap**
- Summarize how the problem is currently addressed
- Identify the key limitation or gap
- Be specific about what's missing

**Paragraph 3: Your Approach**
- "In this paper, we propose/introduce/present..."
- Key insight in one sentence
- High-level description of method

**Paragraph 4: Results Preview**
- Main empirical findings
- Include specific numbers
- Highlight most impressive result

**Paragraph 5: Contributions (bulleted)**
- Contribution 1: The core technical innovation
- Contribution 2: The empirical validation
- Contribution 3: Additional findings or artifacts (code, datasets)

## Related Work Organization

**Pattern 1: By Approach Type**
```
## Related Work

### Approach Category A
Prior work in [category A] includes... However, these methods...

### Approach Category B
Another line of work focuses on... Unlike our approach, these...

### Approach Category C
Recent work has explored... Our method differs by...
```

**Pattern 2: By Problem Aspect**
```
## Related Work

### [Problem Aspect 1]
...

### [Problem Aspect 2]
...

### Connection to Our Work
We build on [X] while addressing limitations in [Y]...
```

**Key Phrases for Positioning:**
- "Unlike [X], our method..."
- "While [X] focuses on..., we address..."
- "Building on [X], we extend this to..."
- "In contrast to [X], which..., our approach..."

## Method Section Structure

1. **Problem Formulation** (1-2 paragraphs)
   - Formal notation
   - Input/output definitions
   - Key assumptions

2. **Overview** (1 paragraph + figure)
   - High-level description
   - Reference to architecture figure
   - Intuition for why it works

3. **Component Details** (one subsection each)
   - Technical description
   - Design choices with justification
   - Connection to other components

4. **Training/Optimization** (if applicable)
   - Loss function
   - Training procedure
   - Key hyperparameters

## Experiments Checklist

### Setup Section
- [ ] Datasets with statistics (size, splits, characteristics)
- [ ] Baselines with citations
- [ ] Evaluation metrics defined
- [ ] Implementation details (framework, hardware, training time)
- [ ] Hyperparameter selection method

### Results Section
- [ ] Main comparison table
- [ ] Statistical significance (if applicable)
- [ ] Analysis by difficulty/category
- [ ] Ablation studies
- [ ] Error analysis with examples

### Results Table Format
```
| Method | Metric 1 | Metric 2 | Metric 3 |
|--------|----------|----------|----------|
| Baseline 1 | X.X | X.X | X.X |
| Baseline 2 | X.X | X.X | X.X |
| **Ours** | **X.X** | **X.X** | **X.X** |
```

## Conclusion Template

**Paragraph 1: Summary**
- Restate the problem briefly
- Summarize your approach
- Key results in one sentence

**Paragraph 2: Limitations**
- Be honest about constraints
- Discuss failure cases
- Note computational requirements

**Paragraph 3: Future Work**
- Natural extensions
- Open questions
- Potential applications
