# Prioritization (Vectoring)

How to decide what to investigate first.

## The Core Idea

You can't resolve all uncertainties at once. Identify the MOST IMPORTANT unknown and focus entirely on answering it before moving to the next.

## The Vectoring Algorithm

1. **List uncertainties**: What don't you know? What could go wrong?
2. **Rank by importance**: Which unknowns would kill the project if wrong?
3. **Pick ONE**: Select the highest-importance unknown
4. **Scope to ~1 week**: Break down if too big
5. **Execute**: Answer that ONE question
6. **Re-vector**: Update list, pick next most important

## The Prioritization Grid

```
            IMPORTANT
                ↑
     Known +    │    Unknown +
     Important  │    Important
     (leverage) │    (TARGET)
                │
   ←────────────┼────────────→
     Known      │      Unknown
                │
     Known +    │    Unknown +
     Unimportant│    Unimportant
     (ignore)   │    (defer)
                │
                ↓
            UNIMPORTANT
```

**Target the Unknown + Important quadrant.**

## Types of Vectors

| Type | Question | How to Answer |
|------|----------|---------------|
| Feasibility | Will this work at all? | Minimal prototype, synthetic data |
| Scale | Will this work at realistic size? | Test with real workload |
| Theory | Does a fundamental limit exist? | Proof or counterexample |
| Design | What should this look like? | Low-fi mockup, user feedback |

## Core vs. Periphery

For each vector, distinguish:

**Core**: What MUST work to answer this specific question
- Cannot be faked or assumed
- Directly tests the uncertainty

**Periphery**: Everything else
- Can use synthetic/mock data
- Can assume other components work
- Can ignore edge cases
- Can use rough approximations

## Scoping

Each vector should be answerable in ~1 week.

**Too big?** Break into sub-questions:
- "Will users like this?" → "Will users understand the core interaction?"

**Too small?** You might be rescaling, not vectoring:
- Rescaling: Same question, smaller scope
- Vectoring: Different question entirely

## After Each Vector

1. What did you learn?
2. What's now known that was unknown?
3. What new unknowns emerged?
4. What's the next most important unknown?

Repeat until core uncertainties are resolved.
