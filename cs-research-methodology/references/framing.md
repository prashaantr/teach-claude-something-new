# Problem Framing (Finding the Bit)

How to identify the assumption worth challenging—the "bit" you'll flip.

## Process

### 1. List Existing Approaches

For the problem at hand, identify 3-5 existing approaches:
- What methods/solutions currently exist?
- How do practitioners typically solve this?

### 2. Find the Common Thread

Ask: "What do ALL these approaches share?"

Look for:
- Same input representation
- Same problem decomposition
- Same optimization target
- Same constraints they accept
- Same tradeoffs they make

The assumption is what they all take for granted.

### 3. Question the Assumption

For each shared element, ask:
- "Why does everyone do it this way?"
- "What if this wasn't necessary?"
- "When does this break down?"

### 4. Identify the Limitation

Find evidence the assumption causes problems:
- Cases where current approaches fail
- Performance ceilings nobody can break
- User complaints that never get addressed
- Workarounds people use

### 5. Propose the Alternative

State clearly:
```
Current approaches assume [X].
This causes [limitation] because [reason].
Instead, we could [Y].
This would enable [benefit] because [mechanism].
```

## Checking Your Work

Good assumption challenges:
- **Specific**: Not "use a better approach" but "use representation X instead of Y"
- **Non-obvious**: The assumption must actually be believed by practitioners
- **Testable**: You can design an experiment comparing old vs. new
- **Singular**: One assumption per investigation (changing multiple = confounded results)

## Examples

**Example 1: Search Engines**
- Assumption: Rank documents by keyword matching
- Limitation: Misses semantic relevance
- Alternative: Rank by meaning similarity using embeddings
- Benefit: Finds relevant documents even without exact keywords

**Example 2: Image Classification**
- Assumption: Need large labeled datasets
- Limitation: Expensive annotation, limited domains
- Alternative: Learn from image-text pairs from the web
- Benefit: Broader coverage without manual labeling

## Output Template

After completing this process, you should have:

1. **The assumption**: What everyone currently takes for granted
2. **The evidence it's limiting**: Specific failures or constraints it causes
3. **The alternative**: What to do instead
4. **Why it's better**: The mechanism by which the alternative solves the limitation
