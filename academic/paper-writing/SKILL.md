---
name: paper-writing
description: Writes and develops ML conference manuscripts. This skill should be used when users want to brainstorm contributions, write paper sections, position work vs prior work, or craft abstracts and arguments.
---

# Manuscript Writing

## Paper Section Guidance

### Abstract (150-250 words)
- Problem statement and motivation
- Key insight or approach
- Main results (quantitative)
- Broader significance

### Introduction
- Hook: Why does this problem matter?
- Gap: What's wrong with current approaches?
- Contribution: What do you propose? (be specific)
- Results preview: What did you achieve?

### Related Work
- Position clearly relative to each category of prior work
- Explain what you do differently, not just what others did
- Ensure proper citation coverage

### Method
- Problem formulation first
- Architecture overview (figure helps)
- Each component in detail with justifications
- Design choices explained

### Experiments
- Datasets with statistics
- Baselines and evaluation metrics
- Implementation details (reproducibility)
- Main results (tables), analysis by difficulty (figures)
- Ablation studies
- Error analysis

### Discussion/Conclusion
- Summary of contributions
- Limitations (be honest)
- Future work

## Workflow

### Step 1: Gather Context
Ask user for:
1. **Current stage**: Early idea, partial draft, or near-complete manuscript?
2. **Target venue**: ICML, NeurIPS, ICLR, EMNLP, ACL, or other?
3. **Core contribution**: What is the main novel idea or finding?
4. **Related work**: Key papers to position against?
5. **Codebase**: Is there implementation code to verify against?

### Step 2: Draft or Improve
- **Specific**: Point to exact locations and issues
- **Constructive**: Suggest solutions, not just problems
- **Balanced**: Acknowledge strengths while addressing weaknesses
- **Actionable**: Provide clear guidance for revision

### Step 3: Anticipate Reviewers
- Identify the strongest and weakest aspects
- Flag potential reviewer concerns proactively
- Suggest how to frame contributions for maximum impact
- Ensure claims are properly supported by evidence

## Quality Checks

Before finalizing any output:
1. **Claims supported**: Every claim has evidence or citation
2. **Consistent terminology**: Notation and terms used consistently
3. **Logical flow**: Clear transitions between sections and paragraphs
4. **Honest limitations**: Weaknesses acknowledged, not hidden
5. **Proper positioning**: Clear differentiation from prior work
