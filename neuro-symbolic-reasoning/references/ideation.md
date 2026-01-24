# Ideation Mode

Open-ended exploration of neuro-symbolic approaches. NO code, NO file creation.

## Discussion Prompts

Help the user think through:
- What problem are they trying to solve?
- Why might symbolic reasoning help here?
- What are the tradeoffs they care about?

## Solver Landscape

| Solver | Good For | Limitation |
|--------|----------|------------|
| Prover9 (FOL) | Expressive reasoning | May timeout |
| Z3 (SMT) | Constraints, planning | Less expressive |
| Pyke (Rules) | Simple rule chains | Only propositional |

## Key Reference

Logic-LM (Pan et al., EMNLP 2023) - The main reference for NL→logic pipelines with self-refinement. See the paper and repo for established patterns.

## Avoid

- Prescribing a specific research design
- Forcing experimental templates
- Creating files or writing code
