---
name: cs-research-methodology
description: Framework for investigating research problems using the "bit flip" method - identifying assumptions and proposing alternatives. Use when analyzing why current approaches fail, finding gaps in existing solutions, or structuring a research argument.
---

# CS Research Methodology

A reasoning framework for investigating problems based on Stanford CS197.

## Core Concept: The Bit Flip

Every research contribution follows this pattern:
1. **The Bit**: What does everyone assume?
2. **The Flip**: What's the alternative?
3. **The Proof**: Why does the alternative work better?

## The Investigation Process

### Step 1: Identify the Bit (Current Assumption)

Given a problem, ask:
- How do existing solutions approach this?
- What do they all have in common?
- What do they take for granted?

The assumption is often implicit—look for patterns across approaches.

→ See [references/framing.md](references/framing.md) for detailed process and examples.

### Step 2: Find Where the Bit Fails

Ask:
- When does this assumption break down?
- What cases does it handle poorly?
- What has changed that might invalidate it?

Evidence of limitation:
- Edge cases where current approaches fail
- New capabilities that weren't available when assumption was made
- Adjacent fields that solve similar problems differently

→ See [references/landscape.md](references/landscape.md) for mapping existing approaches.

### Step 3: Propose the Flip (Alternative)

Articulate clearly:
- "Current approaches assume X. Instead, consider Y."
- The alternative must be specific and testable
- Explain WHY the flip addresses the limitation

→ See [references/prioritization.md](references/prioritization.md) for deciding what to investigate.

### Step 4: Identify Evidence for the Proof

What would prove the flip works?
- What comparison would be convincing?
- What would demonstrate improvement?
- What would show this isn't just different but better?

→ See [references/validation.md](references/validation.md) for designing evaluation.

## Output Template

After investigation, you should have:

```
THE BIT: Current approaches assume [X].
THE LIMITATION: This fails when [evidence].
THE FLIP: Instead, [Y].
THE PROOF: This works because [mechanism], demonstrated by [evidence type].
```
