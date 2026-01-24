# Ideation Mode

NO code, NO file creation.

## Questions to Ask

- Is this a deduction task (derive conclusions) or satisfaction task (find assignments)?
- Do they need guarantees (correctness) or just better performance?
- Is the logic expressible in FOL, or do they need constraints/arithmetic?

## Common Pitfalls

- FOL is undecidable - Prover9 may not terminate
- NL→Logic translation is the hard part, not the solving
- "Faithful" translation is undefined - how will they measure it?
- Small benchmark gains may not generalize

## Tradeoffs

| Choice | Upside | Downside |
|--------|--------|----------|
| More expressive logic | Captures more meaning | Harder to solve, may timeout |
| Simpler logic | Fast, decidable | May lose nuance |
| Few-shot prompting | Easy to try | Brittle, dataset-specific |
| Fine-tuned parser | More robust | Expensive, needs training data |

## Reference

Logic-LM paper details in [logic-llm.md](logic-llm.md).
