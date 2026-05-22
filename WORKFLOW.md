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

## Visual/video portability workflow

For richer image/video tools such as Higgsfield MCP, `brand.md` should act as the directional control layer, not as a promise that a single generative pass will handle everything production needs.

The working rule:

> Higgsfield-style generation can use `brand.md` directionally, but production-grade assets should use a two-step flow: generate the atmospheric/product composition first, then overlay exact typography, logo, and data with deterministic tooling or a text-accurate model/pass.

Use this split whenever exact text, logo geometry, data values, product claims, or compliance-sensitive copy matter:

1. **Composition pass** — generate the market/product atmosphere, visual framing, safe areas, lighting, UI/product mood, and motion direction.
2. **Exact overlay pass** — add or correct headlines, microcopy, logo placement, chart labels, figures, UI numbers, and sourced claims with deterministic tooling or a model chosen for text accuracy.
3. **Iterative self-loop** — compare candidates and prior passes, classify failures, revise the smallest useful variable, and rerun within a bounded iteration budget before selecting a winner.
4. **Review packet** — store prompt, output, model metadata, rubric scores, failures, comparison notes, and spec improvement suggestions under `experiments/`.
5. **Spec feedback** — patch `brand.md` only when the failure reveals missing portable brand guidance; do not hide failures with one-off prompt tricks.

The self-loop procedure is specified locally in `docs/future-integrations/higgsfield-iterative-self-loop-operating-procedure.md`. The operating pattern is: first generation → visual/rubric review → failure diagnosis → targeted workflow/prompt adjustment → rerun → side-by-side comparison → stop or repeat within budget.

For video generation, use the dedicated local procedure in `docs/future-integrations/higgsfield-seedance-virality-video-loop-operating-procedure.md`: Seedance 2.0 generation → manual brand/video review → Higgsfield Virality Predictor → combined diagnosis → targeted prompt/storyboard revision → bounded rerun. Virality feedback is advisory and must never override source truth, claim discipline, or brand fit.

Video subtypes are optional planning/review aids, not a hard gate: product/UI motion, market-event motion, conference/brand hero motion, founder/operator narrative, or hybrid narrative + product/UI. In this v1 workflow, a “CEO video” example means testing a founder/operator-style script, hook, scope, and concept before a shoot. Actual-person likeness/voice work belongs to a separate approved-reference production track.

For Higgsfield image-generation tests, default to `nano_banana_pro`. Use other models only when the experiment calls for a specific tradeoff.

Internal testing policy: keep Higgsfield experiment workflow changes and outputs local/private until Chris explicitly approves updating the public GitHub repo.
