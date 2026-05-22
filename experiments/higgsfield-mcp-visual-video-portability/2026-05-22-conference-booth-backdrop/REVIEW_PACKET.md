# Higgsfield MCP Portability Experiment — Conference Booth Backdrop

Date: 2026-05-22
Status: first live Higgsfield MCP smoke test; output generated and reviewed

## Purpose

Test whether `brands/ostium/brand.md` can act as a portable control layer for a richer text-to-image model without using the deterministic SVG generator or existing template code.

This is a spec-level + output-level smoke test for the future integration described in `docs/future-integrations/higgsfield-mcp-visual-video-portability.md`.

## Source inputs used

- `brands/ostium/brand.md` v0.3 portability revision
- `docs/BRAND_PROVENANCE.md`
- `docs/future-integrations/higgsfield-mcp-visual-video-portability.md`

No deterministic SVG generator output was used as an image reference.

## Generation metadata

- Tool path: Higgsfield MCP direct call through local MCP connection
- Model: `z_image`
- Job ID: `941be5b5-56ae-432f-90df-849ff8a685ef`
- Aspect ratio: `16:9`
- Output file: `higgsfield-z-image-conference-booth-backdrop.png`
- Source URL at generation time: `[REDACTED PUBLIC URL]`

## Prompt

See `prompt.txt`.

## Output review

### Overall result

Useful first smoke test, but not a pass under the spec's minimum useful-result bar.

The image follows the broad dark/orange institutional trading direction and works compositionally as a booth backdrop, but it exposes three important portability issues:

1. Text fidelity is not reliable enough for final brand assets: the supporting line renders “foex” instead of “forex”.
2. Ostium-specific identity is weak: the small wordmark exists, but the asset could mostly be any dark fintech/trading platform.
3. Market/product specificity is suggested through generic terminal panels rather than a concrete Ostium product mechanic or market anchor.

### Rubric scores

Scores use the 1–5 rubric from the future-integration spec.

- Ostium recognizability: 3/5
  - Recognizable only through the tiny `OSTIUM` label and dark/orange trading mood. Needs stronger Ostium-specific product/gateway cues.
- Market specificity: 3/5
  - Includes market tables/charts, but mostly generic. No specific commodity/equity/forex catalyst or concrete product proof.
- Proof/product hierarchy: 3.5/5
  - One dominant headline works at booth distance. Product/data support exists but is decorative and illegible rather than credible proof.
- Color semantics: 4/5
  - Strong black/orange atmosphere. Green/red are mostly confined to small market data values. Good directional adherence.
- Typography behavior: 2.5/5
  - Headline is strong and readable; supporting text has a material typo (`foex`) and generated dashboard microtext is nonsensical.
- Logo restraint: 4/5
  - Logo/signature is restrained. It may be too weak for a conference backdrop, but it follows the spec.
- Claim discipline: 5/5
  - No unsupported partner/performance/investment claims observed.
- Modality fit: 4/5
  - The wide, high-contrast layout fits a booth/backdrop format. The large headline reads well from distance.
- Production taste: 3.5/5
  - Professional at a glance, but generic terminal details and bad microtext reduce credibility.
- Spec traceability: 4/5
  - Most visual decisions trace to `brand.md`: dark foundation, orange heat, data modules, restrained logo, global-market framing.

Average score: 3.65/5

Minimum useful-result check:

- Average score >= 4: fail
- No claim-discipline failure: pass
- No obvious generic crypto/SaaS drift: partial pass; avoids crypto cliches, but drifts toward generic trading-platform backdrop
- At least one concrete lesson for improving `brand.md`: pass

## Lessons for `brand.md` / prompt builder

1. For generated image tools, text should be treated as fragile unless the model is explicitly strong at text rendering. The prompt builder should either:
   - keep generated text minimal and verify it after generation;
   - use post-generation compositing for exact headlines/microcopy; or
   - choose a model/tool with stronger text accuracy for text-heavy assets.
2. Unsupported booth/report/app-store assets need a stronger concrete anchor than “global markets.” The prompt should require one visible proof/product module such as:
   - a specific market category row;
   - a simplified Ostium app/order-ticket module;
   - a gateway-to-markets visual metaphor tied to the product;
   - or one sourced product mechanic: USDC settlement, self-custody, transparent execution, long/short global markets.
3. The prompt builder should separate:
   - image-generation instructions for atmosphere/layout;
   - exact text/logo overlay instructions for a deterministic or editing pass.
4. `brand.md` is directionally portable, but production-grade asset creation likely needs a two-step pipeline: generate background/composition first, then overlay exact typography/logo/data with deterministic tooling.

## Recommended next test

Run a second Higgsfield MCP test with less text burden and stronger product specificity:

- Asset: research report cover or app-store-style product screenshot.
- Prompt strategy: ask Higgsfield for the atmospheric/product composition only, with a clear empty safe area for later exact text overlay.
- Evaluation: compare whether reduced text reliance improves production taste and Ostium recognizability.

## Current conclusion

The integration works technically: Higgsfield MCP accepted a prompt derived from `brand.md` and produced an asset candidate. The first output is valuable as a failure/learning packet, not as a release-ready brand asset.
