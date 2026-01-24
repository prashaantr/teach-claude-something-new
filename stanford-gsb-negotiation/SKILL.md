---
name: stanford-gsb-negotiation
description: Negotiation preparation workflow. Use when user mentions: negotiating salary, job offers, contracts, vendor deals, real estate, disputes, difficult conversations, asking for a raise, making deals, reaching agreement, or "what should I ask for." Provides structured preparation, market research, and response scripts.
---

# Negotiation Workflow

## Route by User Intent

| User intent | Action |
|-------------|--------|
| Preparing for negotiation | Run preparation workflow |
| Needs market data | WebSearch → output number with sources |
| Mid-negotiation ("they said X") | Give response script |
| Emotional/relationship conflict | Ask about feelings first, then strategize |

## Preparation Workflow

### 1. Ask Context

Ask:
- "What are you negotiating?"
- "Who's the other party?"
- "What's your deadline?"
- "What outcome would make you happy?"
- "What's your minimum acceptable outcome?"

### 2. Research Market Data

WebSearch for relevant data. See `references/research-templates.md` for search queries by negotiation type.

Output format:
```
Market range: $X - $Y (median: $Z)
Sources: [list with links]
```

### 3. Ask About Leverage

Ask:
- "What will you do if this deal falls through?" (their BATNA - backup plan)
- "What are their alternatives if you walk away?"
- "Who makes the final decision on their side?"
- "What do you think they really care about?"
- "What could you offer that's easy for you but valuable to them?"

### 4. Output Strategy

```
Target: $X (justify with market data)
Walk-away: $Y
Opening: $Z

Script: "[what to say]"

If they push back, say: "[response]"
```

## Mid-Negotiation Response

When user says "they just said X":

| Situation | Tell user to say |
|-----------|------------------|
| They anchored high/low | "What range were you thinking?" |
| "Final offer" | "If [X] is fixed, what flexibility is there on [Y]?" |
| They got angry | "I can see this is important to you. Help me understand." |
| They went silent | "What would help you decide by [date]?" |
| They added last-minute asks | "If we're reopening terms, I'd want to revisit [Y] too." |

## Emotional Situations

When user shows frustration or relationship strain:

1. Ask: "What happened?" and "How are you feeling about this?"
2. Ask: "What might they say happened?" (reframe perspective)
3. Give opening script: "We seem to see this differently. I'd like to understand your perspective."

See `references/emotion-scripts.md` for more scripts.

## References

Load as needed:
- `references/research-templates.md` - WebSearch queries by negotiation type
- `references/emotion-scripts.md` - Scripts for difficult conversations
- `references/examples.md` - Reference outcomes for similar negotiations
