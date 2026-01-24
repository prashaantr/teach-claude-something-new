# The Bit Flip Framework

## Definition

A **bit flip** is the core research move: identifying an implicit assumption in prior work and proposing an alternative.

## The Three-Step Pattern

Every major research contribution follows this structure:

1. **Articulate the bit**: State what everyone currently assumes
2. **Flip it**: Propose the alternative nobody considered
3. **Prove it**: Demonstrate your approach is superior

## Historical Examples

### RISC Architecture (Hennessy & Patterson, Turing Award)
- **Bit**: Complex instruction sets are better
- **Flip**: Simple instruction sets enable faster execution
- **Proof**: Led to ARM, MIPS, major Silicon Valley companies

### Interactive Computing (Engelbart)
- **Bit**: Computers are for batch processing
- **Flip**: Computers can be interactive personal tools
- **Proof**: Invented the mouse, hypertext, influenced the Mac

### Deep Learning (LeCun, Hinton, Bengio, Turing Award)
- **Bit**: Neural networks are a failed approach
- **Flip**: With GPUs + data + algorithms, they work
- **Proof**: Foundation of modern ML

## Applying the Framework

### Step 1: Find the Bit
Ask: "What does everyone in this field take for granted?"
- Read 5-10 papers in the area
- Notice repeated assumptions
- Look for phrases like "traditionally...", "the standard approach...", "it is well known that..."

### Step 2: Question the Bit
Ask: "What if this assumption is wrong?"
- Consider edge cases where assumption fails
- Look at adjacent fields with different assumptions
- Think about what new capabilities might invalidate the assumption

### Step 3: Propose the Flip
Articulate clearly:
- "Prior work assumes X. We propose Y instead."
- The flip should be specific and testable
- One flip per project (avoid multiple simultaneous flips)

### Step 4: Design the Proof
Your evaluation must directly test whether the flip works:
- Compare against approaches that use the old assumption
- Measure outcomes that matter for the problem
- Show when/why your flip is better

## Common Mistakes

- **Flipping multiple bits**: Higher risk, harder to attribute success
- **Vague flips**: "We use a better approach" (not specific enough)
- **Obvious flips**: If everyone already knows, it's not research
- **Unstestable flips**: Must be able to compare old vs. new

## Bit Flip Neighborhoods

- **Single-paper flip**: Change one axis relative to nearest neighbor
- **Literature-level flip**: Unique across broader literature (stronger novelty)
- Larger neighborhoods = more impactful contributions
