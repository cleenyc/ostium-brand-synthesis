# Higgsfield MCP experiment summary

This folder contains internal proof packets for testing whether `brands/ostium/brand.md` can guide Higgsfield MCP image generation outside the deterministic SVG templates.

The useful pattern was the loop, not a single image:

```text
prompt from brand.md -> generate -> review -> classify failure -> revise workflow/prompt -> rerun -> compare
```

## Runs

### 1. Conference booth backdrop, first pass

Path: `2026-05-22-conference-booth-backdrop/`

- Model: `z_image`
- Job: `941be5b5-56ae-432f-90df-849ff8a685ef`
- Result: directionally useful but failed exact text fidelity (`foex` instead of `forex`) and drifted toward generic trading-platform visuals.
- Score: `3.65/5`

### 2. Research/report cover, two-step pass

Path: `2026-05-22-research-report-cover-nano-banana/`

- Requested model: `nano_banana_pro`
- Returned model: `nano_banana_2`
- Job: `1031298d-9649-4e1a-8770-cb4c17061387`
- Result: strong dark/orange market-infrastructure composition with exact deterministic overlay.
- Score: `4.4/5`

### 3. Conference booth backdrop, rerun

Path: `2026-05-22-conference-booth-backdrop-rerun-nano-banana/`

- Requested model: `nano_banana_pro`
- Returned model: `nano_banana_2`
- Job: `69796228-94a7-4038-a2d3-be4fc2c30a30`
- Result: stronger physical booth read, cleaner brand hierarchy, exact overlaid headline and supporting copy.
- Score: `4.35/5`

![Booth comparison](2026-05-22-conference-booth-backdrop-rerun-nano-banana/comparison-pass01-vs-rerun.png)

## Main lesson

For Ostium assets, the best v1 pattern is:

1. use Higgsfield for composition, atmosphere, product environment, and campaign direction;
2. use deterministic or text-accurate overlays for exact copy, logo geometry, product UI, figures, and claims;
3. preserve review packets so the next agent can improve the workflow instead of starting from scratch.
