# brand.md Workflow

## Goal
Create a high-fidelity, evidence-backed `brand.md` creative spec from user-provided brand references only.

## Output Boundary
The workflow ends at `brand.md`. Presentations, ads, decks, videos, or other assets are downstream uses.

## Operating Principles
1. User-provided references only.
2. No rule without evidence.
3. Explicit brand guide rules override inferred patterns.
4. Official, owner-provided, and owner-approved sources outrank older or lower-authority references.
5. Contradictions are flagged, not guessed through.
6. Every important rule gets evidence + confidence.
7. The owner/reviewer reviews the draft before it becomes canonical.

## Source Authority
1. Official brand guide / design system
2. Official templates / brand hub exports
3. Recent official marketing assets
4. Official social/campaign assets
5. Owner-approved contextual examples, clearly labeled as context rather than brand authority

## Workflow

### 1. Intake
Collect provided references and create a source inventory:
- asset ID
- filename/URL
- type
- date if known
- source/origin
- authority level
- notes/known limitations

### 2. Extract Explicit Rules
From PDFs, brand guides, decks, and docs:
- colors
- typography
- logo usage
- spacing/grid
- imagery rules
- motion rules
- copy/voice rules
- dos/don’ts

### 3. Analyze Visual / Motion References
Use image/video analysis for observable patterns only:
- composition
- color behavior
- type scale
- density/whitespace
- photo treatment
- icon/illustration style
- motion pacing/transitions
- recurring layouts

### 4. Synthesize Rules
Convert observations into strict creative rules:
- Use / avoid / only-if statements
- Evidence IDs attached
- Confidence: high / medium / low
- Separate explicit rules from inferred rules

### 5. Draft `brand.md`
Use `template.md`. Include:
- source inventory
- authority hierarchy
- brand-specific creative constraints
- prompt-ready guidance
- open decisions
- review checklist

### 6. Human Review
The owner/reviewer reviews for accuracy. Feedback becomes versioned changes in `brand.md`.

## Quality Bar
A good `brand.md` should let a future agent generate assets that feel unmistakably on-brand without copying specific prior assets.
