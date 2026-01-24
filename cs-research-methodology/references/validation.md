# Validation

How to prove your bit flip works.

## Match Evaluation to Claim Type

### Claim Type: X > Y (Comparison)
"Our approach outperforms the baseline"

**Evaluation design:**
- Same task, different methods
- Control all variables except your contribution
- Statistical significance testing

**Key requirements:**
- Fair baseline (not a strawman)
- Metrics that matter for the problem
- Sufficient sample size

### Claim Type: ∃ X (Existence)
"It's possible to do X" (when X was thought impossible)

**Evaluation design:**
- Demonstrations and case studies
- User studies showing acceptability
- Qualitative evidence of capability

**Key requirements:**
- Examples that are genuinely challenging
- Evidence the output meets the bar
- Comparison to what was possible before

### Claim Type: Bounding
"Our approach works under conditions C"

**Evaluation design:**
- Ablation studies varying conditions
- Systematic exploration of parameter space
- Identification of failure modes

**Key requirements:**
- Clear articulation of conditions
- Evidence at boundaries
- Honest reporting of failures

## The Four Constructs

### 1. Dependent Variable (DV)
What you measure (accuracy, speed, satisfaction, etc.)
- Pick ONE primary metric
- Others are secondary
- Must directly relate to your claim

### 2. Independent Variable (IV)
What you manipulate (your method vs. baseline)
- Isolate your contribution
- Control confounding factors

### 3. Task
What participants/systems do
- Concrete and replicable
- Representative of real use

### 4. Threats to Validity
What could invalidate results. Address via:
- **Argue irrelevant**: Explain why threat doesn't apply
- **Stratify**: Test across multiple conditions
- **Randomize**: Control what you can't eliminate

## Analysis Approach

1. **Visualize first**: Plot distributions, look for patterns
2. **Descriptive stats**: Mean, median, variance
3. **Identify outliers**: Understand before removing
4. **Statistical test**: Only after understanding data

| Data | Groups | Test |
|------|--------|------|
| Categorical | 2+ | Chi-square |
| Continuous | 2 | t-test |
| Continuous | 3+ | ANOVA |

## Best Practices

- **Copy nearest neighbor**: Adopt evaluation approach from most similar prior work
- **Precision enables evaluation**: Vague claims can't be tested
- **Visualize before statistics**: Understand your data
- **Report failures honestly**: Where doesn't your approach work?
