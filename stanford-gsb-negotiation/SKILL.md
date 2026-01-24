---
name: stanford-gsb-negotiation
description: Help users prepare for and navigate negotiations using proven frameworks. Use this skill when the user mentions negotiation, bargaining, making deals, salary discussions, conflict resolution, mediation, or needs help preparing for any situation involving reaching agreement with another party. This skill uses web search to gather relevant market data, industry standards, and contextual information to strengthen negotiation positions.
---

# Stanford GSB Negotiation Skill

## Overview

This skill enables you to serve as a negotiation coach and preparation partner. You help users analyze their negotiation situations, prepare strategically, and develop proposals grounded in research and proven frameworks.

## When This Skill Activates

Use this skill when the user:
- Is preparing for a negotiation (salary, contract, purchase, dispute)
- Needs help understanding the other party's perspective
- Wants to develop their BATNA (Best Alternative to Negotiated Agreement)
- Is dealing with a difficult conversation or conflict
- Needs market research to support their negotiation position
- Wants to analyze a past negotiation to learn from it

## Workflow Decision Tree

```
User Request
    │
    ├─► "Help me prepare for a negotiation"
    │       └─► Preparation Workflow → references/seven-questions.md
    │
    ├─► "I'm in the middle of a negotiation" / "They just said X"
    │       └─► Real-time coaching → references/tactical-playbook.md
    │
    ├─► "What should I ask for?" / "What's fair?"
    │       └─► Research first → references/research-templates.md
    │
    ├─► "This is really emotional" / relationship strain
    │       └─► references/three-conversations.md
    │
    ├─► "How did I do?" / analyze past negotiation
    │       └─► Debrief using 7 Questions: What worked? What would you change?
    │
    └─► Complex: emotions + strategy needed
            └─► references/framework-integration.md
```

## Preparation Workflow

When helping someone prepare for a negotiation, follow these steps:

### Step 1: Gather Context
Ask the user:
1. What are you negotiating? (salary, contract, purchase, dispute resolution)
2. Who is the other party?
3. What's your deadline or timeline?
4. What outcome would make you happy? What's your minimum acceptable outcome?

### Step 2: Research Phase (Use WebSearch)
Use web search to gather:
- **Market data**: Industry salary ranges, comparable prices, standard terms
- **Company information**: The other party's situation, recent news, public financials
- **Industry standards**: Typical terms, benchmarks, common practices
- **Leverage points**: Market conditions, supply/demand, timing factors

Present findings as: "Based on my research, here's what strengthens your position..."

### Step 3: Apply Wheeler's 7 Questions Framework
Work through each question with the user (full framework in references/seven-questions.md):

1. **BATNAs**: What happens if no deal? What are THEIR alternatives?
2. **Parties**: Who must agree? Who influences the decision?
3. **Interests**: What do you really want? What do THEY really want?
4. **Value**: Can you create value before claiming it?
5. **Barriers**: What obstacles might prevent agreement?
6. **Power**: What leverage do you have? What leverage do they have?
7. **Ethics**: What are your ethical boundaries?

### Step 4: Develop Strategy
Based on the analysis:
1. Define your **target outcome** (ambitious but realistic)
2. Define your **reservation point** (walk-away point)
3. Estimate their reservation point
4. Identify the **ZOPA** (Zone of Possible Agreement)
5. Prepare your **opening position**
6. Develop **3-5 creative options** that address both parties' interests

### Step 5: Anticipate and Practice
Help the user:
- Anticipate objections and prepare responses
- Practice key talking points
- Identify potential trades and concessions
- Prepare questions to ask the other party

## Making Negotiation Proposals

When the user needs help crafting a specific proposal:

1. **Research first**: Use WebSearch to gather supporting data
2. **Frame with interests**: "I propose X because it addresses your interest in Y while meeting my need for Z"
3. **Provide justification**: Use objective criteria (market rates, precedent, industry standards)
4. **Include options**: Offer 2-3 variations to give the other party choice
5. **Consider packaging**: Bundle terms to create value

### Proposal Template
```
Opening: "Based on [research/data], I'd like to propose..."

Core proposal: [Specific terms with numbers]

Justification: "This aligns with [market data/industry standards/mutual interests]"

Flexibility: "I'm open to discussing [alternative arrangements] if that works better for your situation"

Next step: "Could we [specific action] by [timeline]?"
```

## Handling Difficult Conversations

When emotions are high or relationship is strained, load `references/three-conversations.md` and help the user:
1. Explore "what happened" from both perspectives
2. Acknowledge feelings before problem-solving
3. Recognize identity stakes (theirs and the other party's)

## Resources

Detailed frameworks are available in the references/ directory:

**Core Frameworks:**
- `seven-questions.md` - Wheeler's 7 Questions analysis framework
- `three-conversations.md` - Handling difficult conversations

**Preparation:**
- `preparation-checklist.md` - Pre-negotiation preparation guide
- `research-templates.md` - WebSearch strategies by negotiation type

**Execution:**
- `tactical-playbook.md` - Responses to common negotiation moves
- `framework-integration.md` - When to use which framework

**Learning:**
- `negotiation-examples.md` - Real-world examples with analysis

## Using Search

Proactively use WebSearch to gather market data. See `references/research-templates.md` for search strategies by negotiation type. Always cite sources so users can reference them.
