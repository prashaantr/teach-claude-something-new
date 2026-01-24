---
name: neuro-symbolic-reasoning
description: Neuro-symbolic AI combining LLMs with symbolic solvers. Two modes - IDEATION (research design, exploring tradeoffs - no code/files) and IMPLEMENTATION (solver integration, debugging). Triggers for ideation include "explore", "design experiment", "tradeoffs", "what approach". Triggers for implementation include "implement", "build", "code", "debug".
---

# Neuro-Symbolic Reasoning

## Mode Detection

Detect user intent and route accordingly:

**→ Ideation**: "How should I...", "What are the tradeoffs...", "Design an experiment..."
- NO code, NO file creation
- See [references/ideation.md](references/ideation.md)

**→ Implementation**: "Implement...", "Build...", "Write code...", "Debug..."
- See [references/solvers.md](references/solvers.md) for code
- See [references/logic-llm.md](references/logic-llm.md) for format
- See [references/packages.md](references/packages.md) for setup

## File Creation Policy

**Be conservative with files:**
- Prefer inline code snippets over creating files
- Ask before creating multiple files
- Only create files when: (1) user explicitly asks, (2) code is complex enough to warrant it, or (3) user needs to run it later
- One file is usually enough - avoid scaffolding project structures unless asked

## Core Pipeline

```
NL Problem → LLM Formulator → Logic Program → Symbolic Solver → Answer
                    ↑                              |
                    └──── Self-Refinement ←────────┘
```

## Solver Selection

| Logic Type | Solver | Use When |
|------------|--------|----------|
| First-order logic | Prover9 | Expressive reasoning, theorem proving |
| Constraints/SAT | Z3 | Scheduling, planning, satisfiability |
| Rule-based | Pyke | Simple propositional rules |
