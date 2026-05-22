# Higgsfield MCP Portability Experiment — Conference Booth Backdrop Rerun Comparison

## Run

- Date: 2026-05-22
- Asset type: conference booth backdrop
- Status: internal/private rerun and comparison; not a public asset
- Comparison baseline: `../2026-05-22-conference-booth-backdrop/`

## Source inputs

- `brands/ostium/brand.md`
- `docs/future-integrations/higgsfield-mcp-visual-video-portability.md`
- First booth-backdrop prompt and review packet
- Two-step workflow guardrail from the prior research-cover pass

## Generation metadata

- Tool path: Higgsfield MCP via local/direct MCP script
- Requested model: `nano_banana_pro`
- Returned job model: `nano_banana_2`
- Job ID: `69796228-94a7-4038-a2d3-be4fc2c30a30`
- Requested aspect ratio: `16:9`
- Requested resolution: `2k`
- Completed output dimensions reported by job status: `2752x1536`

## Local outputs

- Prompt: `prompt.txt`
- Generated composition layer: `higgsfield-composition-layer.png`
- Deterministic overlay source: `overlay.html`
- Deterministic overlay composite: `deterministic-overlay-composite.png`
- Side-by-side comparison source: `comparison.html`
- Side-by-side comparison image: `comparison-pass01-vs-rerun.png`

## Prompt strategy

This rerun intentionally differs from pass 01. Pass 01 asked the model to render the final booth graphic, including the headline and support copy. This rerun asked the model for only the booth wall, environmental lighting, product/data atmosphere, and a large clean safe area. Exact headline, support copy, and signature were applied afterward with deterministic HTML/Chromium rendering.

## Comparison to pass 01

### Pass 01 — `z_image`, single-pass text

Strengths:

- Directionally dark/orange/institutional.
- Had a simple booth-scale headline read.
- Avoided overt crypto cliches.

Failures / limitations:

- Supporting copy typo: `foex` instead of `forex`.
- Generic trading-platform drift; weak Ostium/product specificity.
- Microtext and dashboard details were not credible enough for close review.
- Average score: 3.65/5.

### Rerun — requested `nano_banana_pro`, returned `nano_banana_2`, composition + deterministic overlay

Strengths:

- Much stronger booth physicality: wall frame, lighting, floor reflection, and large-format signage feel.
- Better safe-area control: left side supports exact headline overlay cleanly.
- Main copy is exact and typo-free because it is deterministic, not generated.
- Right-side product/market atmosphere is stronger and more premium: chart panels, map/routing motif, warm orange gateway energy.
- Color semantics are directionally correct: orange as heat/identity, no obvious orange-as-P&L misuse.

Remaining issues:

- The generated right-side panels include tiny pseudo-readable/gibberish UI text. It is acceptable as background texture at booth distance but not production product UI.
- Ostium specificity is still mostly overlay + brand atmosphere; for a real production booth, the product panels should be deterministic or sourced from a real app/product screenshot.
- The `OSTIUM` text in overlay is a provisional wordmark surrogate, not official logo geometry.
- The bottom internal-testing footer should be removed for public use.

## Rubric scores — rerun composite

1. Ostium recognizability: 4.0 / 5
2. Market specificity: 4.0 / 5
3. Proof/product hierarchy: 4.0 / 5
4. Color semantics: 4.5 / 5
5. Typography behavior: 4.75 / 5
6. Logo restraint: 4.0 / 5
7. Claim discipline: 5.0 / 5
8. Modality fit: 4.5 / 5
9. Production taste: 4.25 / 5
10. Spec traceability: 4.5 / 5

Average: 4.35 / 5

Minimum useful-result check:

- Average score >= 4: pass
- No claim-discipline failure: pass
- No obvious generic crypto/SaaS drift: pass, with remaining generic product-UI caveat
- At least one concrete lesson for improving the workflow: pass

## Conclusion

The booth rerun is a clear improvement over the first version and validates the two-step workflow for this asset type. The main failure mode moved from visible text errors and generic single-pass output to a narrower issue: generated background UI details are still not trustworthy as real product UI. For production, use the generative model for booth environment/atmosphere and use deterministic/source-approved overlays for headline, logo, and product screens.

## Recommended next step

Run a third booth/product-specific pass using either:

1. deterministic product UI overlay on the right-side panels; or
2. an approved source app screenshot/reference image as input to Higgsfield.

Do not update public GitHub until Chris explicitly approves publication after internal review.
