# Ideation Mode

Conceptual guidance for neuro-symbolic research design. NO code, NO file creation.

## Key Design Questions

1. **What reasoning task needs symbolic verification?**
   - Why can't an LLM do this reliably alone?
   - What guarantees does symbolic reasoning provide?

2. **Which logic formalism fits?**
   - First-order logic: expressive but undecidable
   - Propositional: decidable but limited expressiveness
   - SMT/Constraints: good for scheduling, planning, finite domains

3. **What's the NL→Logic translation strategy?**
   - Few-shot prompting with examples
   - Fine-tuned semantic parser
   - Hybrid with human verification

4. **How will you evaluate faithfulness?**
   - Does the logic actually represent the NL meaning?
   - How do you detect translation errors?

## Tradeoffs

| Approach | Pro | Con |
|----------|-----|-----|
| Prover9 (FOL) | Expressive | May timeout, undecidable |
| Z3 (SMT) | Fast, decidable | Less expressive |
| Pyke (Rules) | Simple, fast | Only propositional |
| Pure LLM | Flexible | Unreliable on strict logic |

## Experimental Design

```
Research Question: Can [approach] improve [task] over [baseline]?
Dataset: [FOLIO, ProntoQA, AR-LSAT, or custom]
Metrics: Accuracy, faithfulness, [domain-specific]
Baselines: LLM-only, Logic-LM, LINC, chain-of-thought
Ablations: [components to isolate]
```

## Related Work to Consider

- Logic-LM (Pan et al., EMNLP 2023) - Few-shot NL→logic with self-refinement
- LINC - Logical inference via neurosymbolic computation
- SatLM - Satisfiability-aided language models
- Faithful CoT - Chain-of-thought with verification
