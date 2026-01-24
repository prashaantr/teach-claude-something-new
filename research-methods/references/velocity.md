# Velocity

## Definition

**Velocity** = How much you learn in a given time period. Rapid reduction of risk in a chosen dimension.

## The Velocity Equation

```
velocity = distance / time
```

- Increasing distance (doing more) is rarely possible—you're already maxed out
- Decreasing time (doing faster) is often possible via focused prototyping

## The Velocity Algorithm

1. Articulate the question you're answering (from vectoring)
2. Decide what's absolutely CORE
3. Decide what's PERIPHERY (can be faked)
4. Determine minimum necessary fidelity
5. Execute—remain open to reevaluating
6. Loop with new question

## Core vs. Periphery

**Core**: Goals essential to answering THIS WEEK's question
**Periphery**: Goals that can be:
- Faked (use dummy data)
- Assumed (pretend it works)
- Subsetted (use 100 examples instead of 10,000)
- Mocked (simulate the component)

## Tactics for High Velocity

### Strip Everything Non-Essential
- Your approach should feel "necessarily incomplete"
- If it feels complete, you're probably over-engineering

### Mock Data and Components
- Don't wait for real data—generate synthetic data
- Don't wait for teammates—mock their components
- Don't wait for infrastructure—use local approximations

### Lower Fidelity Expectations
- Any draft beats no draft
- Any prototype beats no prototype
- Rough numbers beat no numbers

### Parallelize Work
- Team members work on different vectors simultaneously
- Use mocked interfaces to avoid blocking each other

### Research Engineering
- Do minimal engineering to answer your vector
- Find workarounds when plans take too long
- Delete code freely—it's a prototype

## The Swamp

**Every project gets stuck.** Extended periods where:
- Models don't work
- Designs fail
- Engineering breaks

**Response to the swamp:**
- Don't pivot after one week (fatal flaw fallacy)
- Iterate out, don't abandon
- Try multiple approaches in parallel
- Reduce scope of current vector

## Velocity Signals

**Low velocity signals (you're stuck):**
- Checking email/social media frequently
- "Just one more feature before testing"
- Perfectionism on non-core components
- Waiting for dependencies

**Diagnosis:**
- If too broad: Refocus on tighter question
- If too perfectionist: Lower expectations dramatically

## Why Velocity Matters

If you prototype 5x faster than peers:
- You explore more of the design space
- You fail faster and learn faster
- You can pursue riskier, higher-impact ideas
- You iterate before committing to publication

## Technical Debt

- Build debt intentionally during high-velocity phases
- Pay it down during creative cycle downtime
- Never let debt slow down vectoring
