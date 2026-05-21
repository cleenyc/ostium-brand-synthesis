# Workflow Narrative: Source-Grounded Brand Specs for AI Agents

## The problem

AI creative tools often fail at brand work because the prompt asks for “on brand” output without giving the model a trustworthy definition of the brand.

When the source material is messy or evolving, agents tend to:

- invent exact hex codes,
- fake logo rules,
- overgeneralize from one visual example,
- ignore copy voice,
- make unsupported product or performance claims,
- collapse official, observed, and guessed rules into the same confidence level.

That is not a rendering problem. It is a brand-operating-system problem.

## The insight

Traditional brand guides are written for humans. They are useful, but they often assume judgment, institutional memory, and access to files that an AI agent may not have.

A `brand.md` is different. It is a machine-readable creative spec designed for downstream agents. It tells the agent:

- what sources exist,
- which sources outrank others,
- which rules are explicit vs observed,
- how confident each rule is,
- what must not be invented,
- which open decisions require review.

The goal is not just prettier generated assets. The goal is safer creative execution under uncertainty.

## The method

```text
Brand references
→ source inventory
→ authority hierarchy
→ visual / voice extraction
→ confidence-rated rules
→ open decisions
→ canonical brand.md
→ downstream asset generation
```

The reusable procedure lives in `docs/brand-md-workflow/`:

1. `workflow.md` — operating process and quality bar.
2. `intake-checklist.md` — how to collect and label references.
3. `analysis-prompts.md` — prompts for PDFs, images, videos, URLs, and social feeds.
4. `template.md` — strict `brand.md` output contract.
5. `build-summary.md` — package summary and handoff.

## The provenance model

Every major brand rule should answer:

- **Where did this come from?** Source ID or file.
- **How authoritative is it?** Official guide, observed design evidence, social copy, derivative synthesis, etc.
- **How confident are we?** High, medium, low, or split confidence such as “high direction / medium exact values.”
- **What is open?** Logo package, exact tokens, font licensing, contradictory assets, stale examples.

This lets downstream agents distinguish between:

- “Use this exactly.”
- “Use this directionally.”
- “Route this for review before production.”
- “Do not invent this.”

## Ostium as the worked example

The Ostium case study demonstrates the method on a real, evolving source set:

- official website and Webflow/CSS evidence,
- official docs and product claims,
- public app/product UI surfaces,
- official X/Twitter voice and media,
- representative source artifacts and contact sheets,
- open media-kit/logo/font decisions.

The final `brands/ostium/brand.md` includes source IDs, authority hierarchy, confidence labels, open decisions, and generation constraints.

## Output contract

A good `brand.md` should let a future agent generate assets that feel unmistakably on-brand without copying prior assets or hallucinating unavailable details.

It should include:

- source inventory,
- authority hierarchy,
- brand essence,
- color rules,
- typography rules,
- logo/mark caveats,
- layout and composition rules,
- imagery and motion guidance,
- copy voice,
- content formats,
- generation constraints,
- negative prompts / avoid-list,
- open decisions,
- review status.

## Downstream proof

The SVG generator in this repo is deliberately small. It proves that once a `brand.md` exists, downstream tools can consume it and produce constrained output.

The interesting artifact is not the renderer. The interesting artifact is the evidence-backed spec that keeps the renderer from making things up.
