# Higgsfield MCP Visual/Video Portability — Review Packet

## Run

- Date: 2026-05-22
- Asset type: research report cover / website hero background
- Status: internal/private pass; not a public asset
- Purpose: test the two-step workflow: generate the atmospheric/product composition with Higgsfield, then apply exact typography/logo/data with deterministic overlay tooling.

## Source inputs

- `brands/ostium/brand.md`
- `docs/future-integrations/higgsfield-mcp-visual-video-portability.md`
- Prior smoke-test lesson from `2026-05-22-conference-booth-backdrop`

## Model/tool metadata

- Tool path: Higgsfield MCP via local Hermes MCP config / direct MCP client script
- Requested model: `nano_banana_pro`
- Returned job model: `nano_banana_2`
- Job ID: `1031298d-9649-4e1a-8770-cb4c17061387`
- Requested aspect ratio: `16:9`
- Requested resolution: `2k`
- Completed output dimensions reported by job status: `2752x1536`
- Output URL: see local saved file; do not treat remote URL as source of truth for review

## Local outputs

- Prompt: `prompt.txt`
- Higgsfield composition layer: `higgsfield-composition-layer.png`
- Deterministic overlay source: `overlay.html`
- Deterministic overlay composite: `deterministic-overlay-composite.png`

## Prompt strategy

This pass intentionally asked Higgsfield for a composition/background layer only:

- dark/charcoal institutional foundation;
- orange/copper gateway/routing atmosphere;
- credible product/UI and market panels;
- left-side safe negative space;
- no exact headline, paragraph text, logo, or exact metrics in the generated layer.

Exact copy and signature treatment were applied separately in `overlay.html`.

## Visual review

### Higgsfield composition layer

Strengths:

- Strong left-side negative space for overlay.
- Dark premium / institutional trading feel is much stronger than the first `z_image` booth-backdrop pass.
- Concrete market/product anchors are present: world map, UI panel, chart modules, market categories.
- Orange is used as gateway/connection heat rather than P&L.
- Green/red chart semantics are restrained and market-like.

Issues:

- The generated layer still produced readable category labels (`Commodities`, `Equities`, `Forex`, `Crypto`) despite the prompt asking for no readable text.
- The labels were accurate enough and not typoed, but this confirms that exact text must remain outside the generative pass for production assets.
- The UI panels are credible but still generic; stronger Ostium specificity would require either a reference UI/image input or deterministic product UI reconstruction.
- No official logo geometry should be inferred from this pass.

### Deterministic overlay composite

Strengths:

- Exact headline and support copy are legible and controlled.
- Safe-area strategy worked: generated composition supports the copy instead of competing with it.
- Overall output reads as a credible Ostium/global-markets/onchain report-cover direction.
- Two-step workflow solved the previous text-fidelity problem for the main message.

Issues:

- The deterministic `OSTIUM` text is a provisional wordmark surrogate, not a verified official logo lockup.
- Headline is large and clean, but a final production asset should use approved fonts/wordmark assets once available.
- The lower internal-testing module is useful for review but should be removed for any public-facing version.

## Rubric scores

1. Ostium recognizability: 4.0 / 5
2. Market specificity: 4.5 / 5
3. Proof/product hierarchy: 4.5 / 5
4. Color semantics: 4.5 / 5
5. Typography behavior: 4.5 / 5
6. Logo restraint: 4.0 / 5
7. Claim discipline: 5.0 / 5
8. Modality fit: 4.5 / 5
9. Production taste: 4.0 / 5
10. Spec traceability: 4.5 / 5

Average: 4.4 / 5

Minimum useful result: PASS for internal workflow validation.

## Lessons

1. The two-step workflow is materially better than asking the image model to render the final asset in one pass.
2. `brand.md` provided enough portable direction for a stronger global-markets/onchain composition than the first smoke test.
3. Even with explicit “no readable text” instructions, the model may emit readable labels; exact typography and data should remain deterministic or use a text-accurate edit/pass.
4. The next spec/prompt-builder improvement is not a `brand.md` patch. The brand guidance was adequate; the generator pipeline needs a stricter composition-only mode and/or masking/reference-image workflow.
5. For higher Ostium specificity, next pass should add a source-approved app/product screenshot or deterministic UI overlay rather than rely on generated UI details.

## Recommendation

Keep this as the first successful internal two-step visual portability pass. Next internal pass should test either:

- app-store/product screenshot composition using a deterministic UI overlay; or
- short 4–6s video from this composite/start frame, avoiding text-heavy generated video.

Do not update public GitHub until Chris explicitly approves publication after additional internal passes.
