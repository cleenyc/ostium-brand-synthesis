# Future Spec: Higgsfield MCP + Visual/Video Portability

## Status

Local v1 operating spec for Higgsfield-backed brand portability experiments. Static-image workflow has been validated through internal conference-booth and research-cover passes; video and Virality Predictor loops are ready as next test tracks.

## Goal

Use `brands/ostium/brand.md` as a portable control layer for generating Ostium-branded visual and video assets through richer generative tools, including a potential Higgsfield MCP integration.

The purpose is to extend the deterministic SVG generator with a richer generative workflow and test how far the evidence-backed brand spec can travel across:

- new asset types;
- richer photographic or cinematic imagery;
- short-form video/motion outputs;
- tools that do not share the deterministic generator's hardcoded templates.

## Why this matters

The current deterministic generator proves that known social-template families can be encoded and rendered repeatably. Higgsfield adds a more ambitious portability layer: the same source-backed brand system can drive unsupported formats, cinematic imagery, booth/report concepts, and short-form motion directions.

A Higgsfield-style integration would test a stronger form of portability:

> Can a downstream creative model receive the source-backed Ostium brand spec and produce recognizable, claim-safe, market-specific assets without hidden generator assumptions?

## Candidate integration architecture

```text
brand.md
  + source-inventory.md
  + provenance / traceability docs
  + optional approved reference frames
        ↓
portability prompt builder
        ↓
Higgsfield MCP or comparable visual/video generation tool
        ↓
asset candidates
        ↓
brand-fidelity evaluator
        ↓
iterative self-loop: compare, classify failures, revise one variable, rerun within budget
        ↓
review packet with pass/fail notes, comparison summary, and spec/workflow improvement suggestions
```

For the full local operating procedure, see `docs/future-integrations/higgsfield-iterative-self-loop-operating-procedure.md`.

## Private iteration posture

This integration should remain **local/private until explicitly approved for public update**.

- Do not push Higgsfield experiment outputs, review packets, prompts, model choices, or workflow revisions to the public GitHub repo until Chris explicitly says to update the public repo.
- Run several internal passes first and use them as proof-building packets for the workflow.
- Public-facing docs should be updated once the strongest v1 story is selected and Chris approves publication.

## Preferred model policy

For Higgsfield image-generation tests, use **`nano_banana_pro`** by default.

Rationale:

- It is listed in the Higgsfield MCP catalog as `Nano Banana Pro` with “Ultimate quality, text and diagrams.”
- The first live smoke test used `z_image` and exposed text-fidelity problems, including a rendered typo in the supporting copy.
- Brand portability tests often depend on typography, diagrams, UI-like panels, and exact claims; use the strongest available text/diagram-oriented image model unless a specific experiment requires another model.

Fallbacks / alternatives:

- Use `gpt_image_2` when the primary test is exact typography or text-heavy layout.
- Use `flux_2` when prompt adherence / visual direction matters more than text accuracy.
- Use `z_image` only for fast rough sketches, not serious brand-fidelity evaluation.

## Production asset workflow principle

Higgsfield-style generation can use `brand.md` directionally, but production-grade assets should use a two-step flow:

1. **Generate the atmospheric/product composition first** — market-specific background, product atmosphere, composition, lighting, booth/report/video direction, and safe areas.
2. **Overlay exact typography, logo, and data separately** — use deterministic tooling or a text-accurate model/pass for headlines, microcopy, logo placement, chart labels, figures, product numbers, and compliance-sensitive claims.

For high-stakes text, logo geometry, and data values, the v1 production pattern is the two-step composition + exact-overlay workflow. Text-rendering failures become useful prompt-builder/workflow signals rather than dead ends.

## Inputs

Required:

- `brands/ostium/brand.md`
- `brands/ostium/source-inventory.md`
- `docs/BRAND_PROVENANCE.md`
- `docs/EVIDENCE_TRACEABILITY_MATRIX.md`

Optional:

- `docs/PORTABILITY_TEST.md`
- selected official Ostium reference frames or contact sheets;
- formal media-kit assets if reviewed later;
- approved output brief, such as campaign, launch, booth, app-store, video ad, or explainer.

## Prompt builder responsibilities

The prompt builder should translate `brand.md` into tool-ready instructions while preserving source discipline.

It should include:

- asset type and format;
- audience/context;
- dominant message;
- required market/product anchor;
- visual style constraints;
- typography behavior;
- semantic color rules;
- logo usage constraints;
- allowed/forbidden claims;
- negative prompt / avoid-list;
- evidence labels or provisionality notes;
- output checklist.

It should not include:

- hidden deterministic SVG coordinates;
- exact renderer-specific hacks;
- unsupported partner/performance claims;
- fake official brand rules;
- third-party logos unless explicitly approved.

## Candidate asset types to test

Start with unsupported or semi-supported formats:

1. **Conference booth backdrop**
   - Large-format physical signage.
   - Tests whether product/data density can simplify at viewing distance.
2. **App-store-style product screenshot**
   - Tests product UI credibility and copy hierarchy outside social templates.
3. **Short market-event video**
   - Tests motion language, caption cadence, and market imagery mapping.
4. **Research report cover**
   - Tests editorial/institutional design rather than social proof format.
5. **Founder/operator explainer clip**
   - Tests talking-head/caption-led motion principles.
6. **Launch announcement card**
   - Tests whether unsupported launch communication avoids generic crypto/SaaS drift.

## Output packet

Each generation run should produce a review packet:

- prompt used;
- source documents supplied;
- generated asset(s);
- model/tool metadata where available;
- pass/fail rubric scores;
- reviewer notes;
- missing guidance discovered in `brand.md`;
- recommended spec edits.

## Brand-fidelity rubric

Score each output from 1–5:

1. **Ostium recognizability** — feels like Ostium rather than generic fintech/DeFi.
2. **Market specificity** — imagery and copy clearly connect to a market, catalyst, or product mechanic.
3. **Proof/product hierarchy** — one dominant message plus credible product/data support.
4. **Color semantics** — orange/black brand atmosphere; green/red reserved for market semantics.
5. **Typography behavior** — confident sans-serif hierarchy; tabular/mono treatment for data.
6. **Logo restraint** — logo behaves as signature unless asset is a lockup/identity piece.
7. **Claim discipline** — avoids unsupported performance, partner, or investment claims.
8. **Modality fit** — uses the strengths of image/video rather than copying static SVG template logic.
9. **Production taste** — visually credible enough to review as an actual brand asset direction.
10. **Spec traceability** — output choices can be explained by `brand.md` and source docs.

Minimum useful result:

- average score >= 4;
- no claim-discipline failure;
- no obvious generic crypto/SaaS drift;
- at least one concrete lesson for improving `brand.md`.

## Video-specific requirements

For video outputs:

- captions should be legible when muted;
- phrase chunks should be short and direct;
- motion should clarify product/market ideas rather than add decorative complexity;
- product UI should stay crisp if shown;
- orange heat/light should support the scene, not overwhelm market semantics;
- avoid fake dashboards, fake exchange partnerships, and fabricated live performance.

For the full local Seedance 2.0 + Virality Predictor loop, see `docs/future-integrations/higgsfield-seedance-virality-video-loop-operating-procedure.md`.

Default video-test posture:

- Generate with Higgsfield MCP `seedance_2_0`.
- Optionally choose or infer a video subtype when it helps review: product/UI motion, market-event motion, conference/brand hero motion, founder/operator narrative, or hybrid narrative + product/UI. Subtypes are guidance, not a hard requirement. “CEO video” examples in this v1 loop mean testing founder/operator script, hook, and concept before a shoot, not generating or optimizing a one-to-one CEO likeness.
- Prefer short 4–6 second tests before longer cuts; model-supported duration range is 4–15 seconds.
- Use `start_image`/reference-driven generation when brand identity or product specificity matters.
- Run Higgsfield Virality Predictor on completed video candidates selected for continuation.
- Merge Virality Predictor feedback with brand/rubric review; virality never overrides source truth, claim discipline, or brand fit.
- Iterate by changing one high-leverage variable at a time: hook timing, first frame, market/product anchor, camera motion, caption/overlay handling, duration, aspect ratio, or reference input.

## Next expansion areas

- Turn the manual prompt-packet pattern into a reusable prompt-builder script or template.
- Add source-approved reference frames and product/UI overlays as richer inputs.
- Define a clean public-repo storage/linking pattern for generated videos.
- Combine model-based review with human creative judgment for stronger evaluator packets.
- Promote official media-kit/logo/font assets into the workflow when available.

## V1 implementation path

1. Build a prompt-packet generator that reads `brand.md` plus provenance docs.
2. Generate one unsupported static asset prompt: conference booth, app-store screenshot, or report cover.
3. Run the prompt through Higgsfield MCP or a comparable visual model.
4. Score the result against the rubric above.
5. Save the review packet under a future `experiments/` directory.
6. Patch `brand.md` only when the failure reveals missing portable brand guidance.

## V1 positioning

- Extends the deterministic SVG generator rather than competing with it.
- Presents internal generated assets as workflow evidence and creative direction, with publication controlled by Chris.
- Optimizes for repeatable prompt/review/iteration behavior, not one lucky generation.
- Converts failures into prompt-builder, overlay, evaluator, or source-spec improvements.
