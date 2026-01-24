---
name: stanford-gsb-negotiation
description: "Negotiation preparation using Stanford GSB frameworks. Use when user mentions negotiating salary, job offers, contracts, vendor deals, real estate, disputes, difficult conversations, asking for a raise, making deals, or reaching agreement. Helps with preparation, market research, response scripts, and handling difficult negotiators."
---

# Negotiation Preparation Workflow

**Context:** User will negotiate later. This workflow prepares them with research, strategy, and scripts.

## Route by User Intent

| User says | Action |
|-----------|--------|
| Preparing for negotiation | Run preparation workflow below |
| Needs market data | WebSearch → output specific numbers with sources |
| "They just said X" (mid-negotiation) | Give response script from `references/tactics.md` |
| Difficult negotiator / manipulative tactic | See `references/difficult-tactics.md` |
| Emotional / relationship conflict | See `references/emotion-scripts.md` |

## Preparation Workflow

### Step 1: Understand Their Situation

Ask:
- "What are you negotiating?"
- "Who's the other party?"
- "What's your deadline?"
- "What outcome would make you happy?"
- "What's the minimum you'd accept?"

### Step 2: Uncover BATNA and Leverage

**BATNA** = Best Alternative to Negotiated Agreement (their walkaway power)

Ask:
- "What will you do if this deal falls through?" ← Their BATNA
- "Do you have other options? Can you create more?"
- "What are their alternatives if you walk away?" ← Their BATNA
- "Who makes the final decision on their side?"

See `references/frameworks.md` for Seven Elements analysis.

### Step 3: Research Market Data

WebSearch for relevant data. See `references/research-templates.md` for search queries.

Output:
```
Market range: $X - $Y (median: $Z)
Sources: [with links]
```

### Step 4: Find Value Creation Opportunities

Ask:
- "What do you think they really care about?"
- "What could you offer that's easy for you but valuable to them?"
- "Are there differences in timing, preferences, or priorities?"

### Step 5: Output Strategy

```
Target: $X (based on market data)
Walk-away point: $Y (based on BATNA)
Opening: $Z

Opening script: "[exact words]"

If they push back: "[response script]"
```

## Quick Response Table

When user reports what the other side said:

| They said | User should say |
|-----------|-----------------|
| Anchored high/low | "How did you arrive at that number?" |
| "Final offer" | "What would need to change for flexibility?" |
| Got emotional | "It seems like this is really important to you." |
| Went silent | "What would help you decide?" |
| Something unexpected | Mirror last 2-3 words: "...think about it?" |
| Using manipulative tactic | See `references/difficult-tactics.md` |

## References

Load as needed based on situation:

| File | When to load |
|------|--------------|
| `references/frameworks.md` | Deep preparation, analyzing complex negotiations, understanding BATNA/interests |
| `references/tactics.md` | Mid-negotiation responses, specific scripts by situation |
| `references/difficult-tactics.md` | User facing manipulative tactics, difficult negotiators |
| `references/emotion-scripts.md` | Relationship strain, difficult conversations, high emotions |
| `references/research-templates.md` | Need to WebSearch for market data |
| `references/examples.md` | Looking for reference outcomes from similar negotiations |
