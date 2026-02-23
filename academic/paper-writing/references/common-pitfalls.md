# Common Pitfalls

Mistakes that frequently lead to paper rejection and how to avoid them.

## Claim-Evidence Mismatches

**Problem:** Claims exceed what the evidence supports.

**Examples:**
- Claiming "state-of-the-art" without comprehensive baselines
- Claiming "generalizes well" from one dataset
- Claiming "efficient" without runtime comparisons

**Fix:** Audit every claim. Ask: "What evidence directly supports this?"

## Weak Baselines

**Problem:** Comparisons against outdated or weak methods.

**Red flags:**
- Baselines more than 3 years old
- Missing recent strong methods
- Unfair hyperparameter tuning (yours vs. defaults)

**Fix:** Include at least one baseline from the last 12 months. Use official implementations. Report baseline performance on your exact splits.

## Missing Ablations

**Problem:** Readers can't identify what makes the method work.

**Essential ablations:**
- Each major component removed
- Key design choices (e.g., loss function variants)
- Hyperparameter sensitivity

**Fix:** For each novel component, show performance without it.

## Overclaiming Novelty

**Problem:** Claiming contribution is "the first" or "novel" when prior work exists.

**Fix:**
1. Search thoroughly (Google Scholar, Semantic Scholar, arXiv)
2. Use hedged language: "To our knowledge..." or "Among the first to..."
3. Acknowledge related work even if slightly different

## Poor Related Work Coverage

**Problem:** Missing relevant citations or mischaracterizing prior work.

**Consequences:**
- Reviewers who authored missing papers get assigned
- Appears unfamiliar with the field

**Fix:**
1. Search for each key term in your title
2. Check citations of your closest baselines
3. Include papers from target venue's recent years

## Inconsistent Notation

**Problem:** Same concept with different symbols, or different concepts with same symbol.

**Fix:**
1. Create notation table before writing
2. Define each symbol on first use
3. Search-and-replace when changing notation

## Vague Contributions

**Problem:** Contributions stated too abstractly.

**Bad:** "We propose a novel method for text classification."
**Good:** "We introduce attention-weighted class prototypes that improve few-shot text classification accuracy by 12% on average."

**Fix:** Include the mechanism AND the improvement in contribution statements.

## Results Without Context

**Problem:** Numbers without interpretation.

**Bad:** "Our method achieves 87.3% accuracy."
**Good:** "Our method achieves 87.3% accuracy, a 4.2% absolute improvement over the previous best (83.1%, Chen et al. 2023)."

**Fix:** Always compare to baselines. Explain what the improvement means.

## Hidden Limitations

**Problem:** Burying or omitting important limitations.

**Common hidden limitations:**
- Computational cost
- Dataset-specific assumptions
- Failure modes
- Scalability issues

**Fix:** Dedicate a paragraph to limitations. Reviewers respect honesty.

## Writing Issues

### Passive Voice Overuse
**Bad:** "The model was trained and evaluated."
**Better:** "We trained the model on X and evaluated on Y."

### Vague Quantifiers
**Bad:** "significantly better," "much faster," "many cases"
**Better:** "4.2% better," "3.1x faster," "73% of cases"

### Missing Transitions
**Fix:** Start paragraphs with transition phrases:
- "Building on this..."
- "In contrast..."
- "To address this..."
- "We now turn to..."

## Submission Checklist

Before submitting:
- [ ] All claims have supporting evidence
- [ ] Baselines include recent strong methods
- [ ] Ablations isolate each contribution
- [ ] Related work is comprehensive and fair
- [ ] Notation is consistent throughout
- [ ] Contributions are specific with numbers
- [ ] Limitations are honestly discussed
- [ ] Figures are readable at print size
- [ ] Supplementary material is referenced
