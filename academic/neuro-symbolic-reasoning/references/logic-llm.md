# Logic-LM Reference

Pan et al., "Logic-LM: Empowering Large Language Models with Symbolic Solvers" (EMNLP 2023)

Source: https://github.com/teacherpeterpan/Logic-LLM

## Pipeline

```
NL Problem → LLM (few-shot) → Logic Program → Symbolic Solver → Answer
                   ↑                               |
                   └──── Self-Refinement ←─────────┘
                              (on errors)
```

## Dataset-Solver Mapping

| Dataset | Logic Type | Solver | Answer Format |
|---------|------------|--------|---------------|
| FOLIO | First-order logic | Prover9 | True/False/Unknown |
| ProntoQA | Propositional | Pyke | True/False |
| ProofWriter | Propositional | Pyke | True/False |
| LogicalDeduction | Constraints | CSP | A/B/C/D/E |
| AR-LSAT | Satisfiability | Z3 | A/B/C/D/E |

## Logic Program Format

Programs use `:::` to annotate each line with natural language explanation.

**FOL (FOLIO-style):**
```
Predicates:
PredicateName(x) ::: description

Premises:
∀x (P(x) → Q(x)) ::: description
P(constant) ::: description

Conclusion:
Q(constant) ::: description
```

**Constraints (AR-LSAT-style):**
```
# Declarations
sort_name = EnumSort([member1, member2, ...])
function_name: sort -> type

# Constraints
constraint_expression ::: description

# Options
(A): is_valid(expr) / is_sat(expr) / is_exception(expr)
```

See actual prompt templates in the repo: `models/prompts/`

## Self-Refinement

When solver returns an error, retry with:
```
Original program:
[[PROGRAM]]

Error: [[ERROR]]

Fix the program.
```

Max rounds: 3 (configurable)

## Backup Strategy

When solver fails after all refinement rounds:
- `random`: Random guess from options
- `LLM`: Chain-of-thought fallback

## Performance

| Method | FOLIO | ProntoQA | ProofWriter | AR-LSAT |
|--------|-------|----------|-------------|---------|
| Standard | 56.4 | 47.6 | 35.8 | 20.9 |
| CoT | 63.1 | 78.2 | 51.0 | 21.7 |
| Logic-LM | **66.5** | **84.4** | **58.8** | **25.2** |

+39% over standard, +18% over CoT.
