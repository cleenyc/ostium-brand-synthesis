---
name: ostium-brand-workflow
description: Generate constrained Ostium assets and run source-backed visual/video portability experiments from the Ostium brand.md spec.
version: 0.3.0
author: Chris Lee
license: MIT
---

# Ostium brand workflow

Use this skill when an agent needs to work from the Ostium brand synthesis package in this repo.

The repo has two operating modes:

1. deterministic SVG/PNG asset generation;
2. Higgsfield MCP visual/video portability experiments.

Both modes start from the same source-backed brand system. The point is not to make an AI tool guess what "on brand" means. The point is to give the agent a spec it can read, cite, and apply.

## Required reading

Read these before generating or reviewing any asset:

1. `brands/ostium/brand.md`
2. `brands/ostium/source-inventory.md`
3. `docs/EVIDENCE_TRACEABILITY_MATRIX.md`
4. `docs/BRAND_PROVENANCE.md`
5. `WORKFLOW.md`

For Higgsfield or other generative portability work, also read:

1. `docs/future-integrations/higgsfield-mcp-visual-video-portability.md`
2. `docs/future-integrations/higgsfield-iterative-self-loop-operating-procedure.md`
3. `docs/future-integrations/higgsfield-seedance-virality-video-loop-operating-procedure.md` when the task involves video or hook testing
4. `docs/HIGGSFIELD_MCP_CASE_STUDY.md` for the worked example

## Core rules

1. Treat `brand.md` as the operating spec.
2. Use source IDs and confidence labels when explaining why an output fits Ostium.
3. Keep the work product-led: global markets, liquidity, transparent settlement, self-custody, execution, and exact sourced proof when available.
4. Use orange as atmosphere and brand heat. Keep green and red for market semantics.
5. Avoid generic crypto neon, token piles, moon/rocket imagery, blue-purple SaaS gradients, vague launch posters, unsupported hype, and invented partner/performance claims.
6. Do not invent official logo rules, font licensing, partner claims, trading-performance claims, or market data.
7. Keep renderer-specific workarounds and model quirks out of `brand.md` unless they reveal a real portable brand-spec gap.

## Mode A: deterministic SVG/PNG assets

Use this mode for repeatable static social assets from the local renderer.

Use one of the Ostium-native templates:

- `campaign-banner`
- `cost-breakdown`
- `trade-result`
- `position-overlay`
- `briefing`

Example:

```bash
python3 scripts/brand_svg_asset.py \
  --brand-dir ./brands/ostium \
  --template campaign-banner \
  --headline "Silicon Week" \
  --subhead "2x Points This Week" \
  --background-theme "silicon chips gpu servers" \
  --icons "NVDA,AMD,MU,ARM,BTC" \
  --out ./outputs/ostium-silicon-week-v5.png
```

Review checklist:

- Uses an Ostium-native template, not a generic abstract brand poster.
- Text wraps and scales within safe margins.
- Uses a dark/charcoal foundation and orange atmosphere.
- Copy is concise, product-led, and source-grounded.
- Green/red appear only as market semantics.
- No unsupported financial-performance or partner/endorsement claims.
- SVG and PNG were generated locally.

## Mode B: Higgsfield MCP portability experiments

Use this mode when testing whether the Ostium brand spec can guide richer image/video tools across unsupported formats.

Good candidates:

- conference booth backdrop;
- research/report cover;
- app-store or product screenshot concept;
- market-event motion;
- founder/operator narrative hook;
- hybrid narrative plus product/UI concept;
- launch campaign direction.

### Image workflow

1. Build a prompt packet from `brand.md`, provenance, and the asset brief.
2. Request `nano_banana_pro` by default for Higgsfield image tests.
3. Record the actual returned model, job ID, dimensions, prompt, and output files.
4. Score the result against the brand-fidelity rubric in the Higgsfield spec.
5. If exact text, logo geometry, data values, or claim language matter, use the two-step workflow:
   - generate the atmosphere/composition first;
   - overlay exact typography, logo, product UI, numbers, and claims with deterministic tooling or a text-accurate pass.
6. Save a review packet with the prompt, output, model metadata, rubric scores, critique, and next iteration decision.

### Iteration loop

Run a bounded loop rather than stopping at the first decent result:

```text
brief -> generate -> review -> compare -> classify failure -> revise one variable -> rerun -> select or escalate
```

Default bounds:

- 1 candidate is fine for smoke tests.
- 2-4 candidates per iteration when budget allows.
- 3 iterations per asset type unless a human approves more.
- Stop early when the best candidate clears the useful-result bar and the remaining improvements need source assets or human taste.

### Video and hook testing

For video, use the Seedance 2.0 procedure:

```text
video brief -> start-frame/composition plan -> Seedance 2.0 generation -> brand/video review -> Higgsfield Virality Predictor -> targeted prompt/storyboard revision -> bounded rerun
```

Use Virality Predictor to sharpen hooks, pacing, and audience clarity. Keep source truth, claim discipline, and Ostium brand fit as the foundation.

A "CEO video" or founder narrative example means testing the hook, script, framing, and campaign concept before a shoot. It does not require generating a one-to-one likeness. Actual-person likeness or voice work belongs to a separate approved-reference production track.

## Review packet checklist

Every Higgsfield experiment should capture:

- asset brief and goal;
- source docs used;
- prompt packet;
- generated asset(s);
- model/tool metadata;
- rubric scores;
- comparison against prior candidates when available;
- failure classification;
- next prompt/workflow change;
- whether `brand.md` needs a real spec update or the issue belongs to prompt-building, overlays, or model behavior.
