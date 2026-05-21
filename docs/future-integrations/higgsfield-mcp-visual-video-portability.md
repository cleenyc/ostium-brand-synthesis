# Future Spec: Higgsfield MCP + Visual/Video Portability

## Status

Rough future-integration spec. Not implemented in v1.

## Goal

Use `brands/ostium/brand.md` as a portable control layer for generating Ostium-branded visual and video assets through richer generative tools, including a potential Higgsfield MCP integration.

The purpose is not to replace the deterministic SVG generator. The purpose is to test whether the evidence-backed brand spec can generalize across:

- new asset types;
- richer photographic or cinematic imagery;
- short-form video/motion outputs;
- tools that do not share the deterministic generator's hardcoded templates.

## Why this matters

The current deterministic generator proves that known social-template families can be encoded and rendered repeatably. It does not fully prove that `brand.md` alone is sufficient for high-quality visual or video generation across unsupported formats.

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
review packet with pass/fail notes and spec improvement suggestions
```

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

## Open questions

- Which Higgsfield MCP tools/endpoints are available and what asset formats do they support?
- Can the integration supply reference frames without overfitting to a single official example?
- How should generated videos be stored or linked in a public repo?
- Should the output evaluator be model-based, human-reviewed, or both?
- What minimum media-kit/logo/font inputs are needed before calling an output production-ready?

## Suggested first implementation slice

1. Build a prompt-packet generator that reads `brand.md` plus provenance docs.
2. Generate one unsupported static asset prompt: conference booth, app-store screenshot, or report cover.
3. Run the prompt through Higgsfield MCP or a comparable visual model.
4. Score the result against the rubric above.
5. Save the review packet under a future `experiments/` directory.
6. Patch `brand.md` only when the failure reveals missing portable brand guidance.

## Non-goals for first integration

- Do not replace the deterministic SVG generator.
- Do not claim official Ostium approval.
- Do not optimize only for a single good-looking prompt.
- Do not silently fix failures with hidden prompt tricks; feed them back into `brand.md`.
