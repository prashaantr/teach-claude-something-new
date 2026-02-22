# Karpathy Coding Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**Core principle:** These guidelines prioritize thoughtfulness over speed. Apply judgment for simpler tasks.

## 1. Think Before Coding

Surface uncertainties rather than masking them.

- State assumptions explicitly
- Present multiple interpretations when they exist
- If something is unclear, **stop** - name what's confusing, ask
- Don't assume. Don't hide confusion. Surface tradeoffs.

## 2. Simplicity First

Write minimal code addressing the actual request.

- No features beyond what was asked
- No abstractions for single-use code
- No unrequested error handling
- No speculative configurability

**Self-check:** Would a senior engineer call this approach overcomplicated?

## 3. Surgical Changes

Modify only what the request demands.

- Don't "improve" adjacent code, comments, or formatting
- Preserve existing code style
- Remove only dependencies your changes created
- Preserve pre-existing dead code unless explicitly requested

## 4. Goal-Driven Execution

Transform vague requests into measurable success criteria.

- Define concrete, testable outcomes
- Create multi-step plans with verification checkpoints
- Loop until verified complete

**Template:**
```
Goal: [specific outcome]
Steps:
1. [action] → verify by [check]
2. [action] → verify by [check]
Success: [measurable criteria]
```

## Effectiveness Indicators

You're applying these guidelines well when you see:
- Fewer unnecessary diff changes
- Reduced rewrites from overengineering
- Clarifying questions preceding implementation (not following mistakes)
- Minimal code that solves exactly what was asked

## Integration with Other Skills

This skill complements:
- **coding-agent**: Apply these principles when delegating coding tasks
- **skill-creator**: Use surgical changes when modifying existing skills

---

*Based on [Andrej Karpathy's LLM coding observations](https://github.com/forrestchang/andrej-karpathy-skills)*
