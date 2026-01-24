# Evaluation Design

## Purpose

Prove your bit flip works. Evaluation is the evidence that your alternative approach is better than the assumption you challenged.

## The 3-Step Evaluation Design Process

### Step 1: Articulate Your Thesis Precisely
Derived from your bit flip. What exactly are you claiming?
- Vague thesis = impossible to evaluate
- Precise thesis = clear evaluation design

### Step 2: Map to Claim Type

| Claim Type | Structure | Example |
|------------|-----------|---------|
| x > y | Your approach outperforms baseline | "Our method achieves higher accuracy than prior work" |
| ∃ x | It's possible to construct X | "We can generate realistic images from text" |
| Bounding x | Approach works under certain conditions | "Our method works when data is sparse but fails with noise" |

### Step 3: Select Evaluation Design

Match your claim type to appropriate evaluation:

**For x > y claims:**
- Comparative experiments
- Same task, different methods
- Statistical significance testing

**For ∃ x claims:**
- Demonstrations
- Case studies
- User studies showing the output is acceptable

**For bounding claims:**
- Ablation studies
- Varying conditions systematically
- Identifying failure modes

## The 4 Core Constructs

### 1. Dependent Variable (DV)
What outcome you're measuring:
- Accuracy, efficiency, user satisfaction, learning gain, trust, etc.
- Choose ONE primary DV; others are auxiliary
- Must directly relate to your thesis

### 2. Independent Variable (IV)
What you manipulate to cause DV change:
- Your method vs. baseline
- Different configurations
- Presence/absence of your contribution

### 3. Task
The specific routine participants/systems execute:
- Must be concrete and replicable
- Should isolate the effect you're measuring
- Avoid confounding with other factors

### 4. Threats to Validity
Potential biases or confounds. Address via:
1. **Argue irrelevant**: Explain why the threat doesn't apply
2. **Stratify**: Test across multiple settings
3. **Randomize**: Control variables you can't eliminate

## Analysis Framework

### Before Statistics
1. **Visualize first**: Graphs, distributions, error bars
2. **Descriptive statistics**: Mean, median, std dev
3. **Identify outliers**: Understand before removing

### Statistical Tests

| Data Type | Conditions | Test |
|-----------|------------|------|
| Categorical | 2+ groups | Chi-square |
| Continuous | 2 groups | t-test |
| Continuous | 3+ groups | ANOVA |

### P-Value Interpretation
- p < 0.05: Results likely repeatable (~95% confidence)
- p-value is NOT the probability your hypothesis is true
- Statistical significance ≠ practical significance

## Best Practices

### Model on Prior Work
- Find your nearest-neighbor paper
- Adopt their evaluation approach
- Adapt established norms rather than inventing new ones

### Don't Rush to Statistics
- Visualization prevents artifacts
- Understand your data before testing
- Statistics can't fix bad experimental design

### Precision Enables Evaluation
- If you can't articulate your bit flip precisely, you can't evaluate it
- Vague ideas lead to vague evaluations
- Iterate on thesis before designing evaluation

## Common Mistakes

- Evaluating something other than your thesis
- No baseline comparison (for x > y claims)
- Too many variables changing at once
- Ignoring threats to validity
- Cherry-picking results
