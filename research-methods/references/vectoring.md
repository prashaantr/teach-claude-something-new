# Vectoring

## Definition

**Vectoring** = Identifying the biggest dimension of risk/uncertainty in your project RIGHT NOW and focusing all effort there.

## The Core Problem

Research is iterative exploration, not linear execution. The "project spec" mindset (figure everything out → execute → publish) wastes resources on non-critical dimensions.

## The Vectoring Algorithm

1. **Generate questions**: List all untested hunches, risky decisions, high-level unknowns
2. **Rank questions**: Prioritize by importance/impact
3. **Pick ONE and answer it rapidly**: Address only the most critical question in 1-2 weeks
4. **Re-vector**: After answering, repeat with the next most important question

## Assumption Mapping

Plot assumptions on a 2x2 grid:

```
                Important
                    ↑
                    |
    IGNORE     |    TARGET
    (known +   |    (unknown +
    unimportant)|   important)
                    |
   ←----------------+----------------→
    Known                      Unknown
                    |
    IGNORE     |    DEFER
    (known +   |    (unknown +
    unimportant)|   unimportant)
                    |
                    ↓
                Unimportant
```

**Target the Unknown + Important quadrant.**

## Example Vectors

| Vector Type | Question | Approach |
|-------------|----------|----------|
| Piloting | Will this technique work at all? | Basic prototype + mocked data |
| Engineering | Will this scale to real workloads? | Test harness with realistic data |
| Proving | Does a theoretical limit exist? | Simple mathematical proof |
| Design | What does this look like to users? | Low-fi prototype, paper sketches |

## Core vs. Periphery

**Core**: What MUST work to answer your vector question
**Periphery**: Everything else (can be faked, assumed, mocked, subsetted)

### Examples of Peripheral Work to Defer
- Perfect data preprocessing (use subset)
- Complete UI (use mockups)
- All edge cases (handle happy path only)
- Full evaluation (test one metric)
- Production code quality (prototype is fine)

## Scoping Vectors

Each vector should be achievable in ~1 week:
- If too big: Break into sub-questions
- If too small: You're probably rescaling, not vectoring

**Rescaling vs. Vectoring:**
- Rescaling: "Can users troll online?" → "Can users troll CNN.com?" (same question, smaller)
- Vectoring: "Can users troll online?" → "Do users understand what trolling is?" (different question)

## Re-Vectoring

After answering one vector:
1. Update your assumption map
2. Some unknowns are now known
3. New unknowns may have emerged
4. Pick the next Unknown + Important question

## Common Mistakes

- Trying to solve everything at once
- Not distinguishing core from periphery
- Spending too long on one vector (should take ~1 week)
- Pivoting too early when stuck (iterate, don't abandon)
