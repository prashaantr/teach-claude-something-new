# Landscape Mapping

How to understand prior work and find your unique position.

## The Search Process

### Step 1: Find Nearest Neighbor
Identify the single paper closest to your idea:
- Search keywords describing your approach
- Ask: What has the most similar goal AND method?

For this paper, extract:
- What assumption does it make? (its bit)
- What evidence supports it?
- What are its limitations?

### Step 2: Expand (3-5 Rounds)

**Backward** (influences on nearest neighbor):
- Check its Introduction and Related Work citations

**Forward** (influenced by nearest neighbor):
- Google Scholar "Cited By"
- Semantic Scholar similar papers

**Lateral** (related approaches):
- Connected Papers visualization
- ArXiv related papers
- elicit.org, researchrabbit.ai

### Step 3: Filter by Quality
Prioritize:
- Top venues in the field
- High citations relative to age
- Include industry research and international work

## Design Space Mapping

Create a 2D map where:
- Axes = key dimensions where approaches differ
- Each paper = a point
- Empty regions = potential opportunities

Example axes:
- Supervised ↔ Unsupervised
- Single-task ↔ Multi-task
- Domain-specific ↔ General

Your contribution should occupy a distinct position.

## Reading Strategy

Don't read every paper thoroughly. For each paper, extract:
1. The assumption it makes (its bit flip)
2. Key evidence it provides
3. Where it sits in design space

Goal: Map the landscape, not master every paper.

## Stopping Criteria

Track what you learn per paper:
- Papers 1-5: Most learning
- Papers 6-15: Filling gaps
- 15+: Diminishing returns

Stop when new papers mostly confirm what you already know.

## Output: Related Work Map

Group papers by shared thesis:
```
[Papers A, B, C] all assume X.
[Papers D, E] assume Y instead.
Our work differs by assuming Z.
```

Each group becomes a paragraph in Related Work, organized by argument rather than by listing papers.
