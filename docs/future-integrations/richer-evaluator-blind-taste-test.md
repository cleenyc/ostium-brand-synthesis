# Future Spec: Richer Evaluator / Blind Taste Test

## Status

Rough future-integration spec. Not implemented in v1.

## Goal

Build an evaluator that tests whether generated Ostium-branded assets are close enough to official Ostium assets that a reviewer or model cannot trivially identify the generated item.

This is not a replacement for human brand review. It is a pressure test for whether `brand.md` and downstream generation workflows are producing assets that preserve real brand behavior rather than superficial color/style cues.

## Core hypothesis

If `brand.md` is an effective operational brand spec, then generated assets created from it should:

- preserve recognizable Ostium visual and voice patterns;
- avoid generic DeFi/fintech drift;
- maintain product/market specificity;
- preserve semantic color and data hierarchy;
- avoid unsupported claims;
- be harder to distinguish from real official examples than weakly prompted assets.

## Evaluation modes

### 1. Blind identification test

Give an evaluator a small set of assets:

- several official Ostium assets;
- one generated candidate;
- optionally one weak baseline generated from a generic prompt.

Ask:

> Which asset is generated, and why?

Useful outcome:

- If the generated candidate is obvious, the evaluator's reason becomes a concrete improvement target.
- If the generated candidate is not obvious, inspect whether it passed for the right reasons rather than because the official examples were weak or mismatched.

### 2. Rubric scoring

Score each candidate against a fixed brand-fidelity rubric:

1. Ostium recognizability.
2. Market/product specificity.
3. Proof-led hierarchy.
4. Dark/orange institutional visual language.
5. Correct green/red market semantics.
6. Logo restraint.
7. Typography/data treatment.
8. Claim discipline.
9. Production taste.
10. Source/spec traceability.

### 3. Pairwise comparison

Compare generated candidate A vs candidate B:

- Which is more Ostium-native?
- Which better follows `brand.md`?
- Which failure mode is more severe?
- Which would be safer to route for human review?

### 4. Baseline comparison

Compare three outputs:

1. generic prompt only: “make an Ostium-style finance ad”;
2. `brand.md` prompt packet;
3. `brand.md` plus selected official reference frames.

This helps isolate whether `brand.md` materially improves output quality compared with generic prompting.

## Inputs

Required:

- official Ostium asset set or contact sheets;
- generated candidate assets;
- `brands/ostium/brand.md`;
- source inventory and provenance docs;
- candidate prompt packets.

Optional:

- asset metadata: source URL, post date, context, format;
- model/tool metadata;
- reviewer notes;
- generated baseline assets;
- image embeddings or visual similarity features.

## Dataset structure

A future implementation could store evaluation packets like this:

```text
experiments/
└── evaluator-runs/
    └── YYYY-MM-DD-run-name/
        ├── README.md
        ├── official/
        │   ├── asset-01.jpg
        │   ├── asset-02.jpg
        │   └── manifest.json
        ├── generated/
        │   ├── candidate-a.png
        │   ├── candidate-b.png
        │   └── prompts.md
        ├── baseline/
        │   └── generic-prompt-output.png
        ├── evaluator-results.json
        └── findings.md
```

The public repo does not need to store every raw asset. It can store manifests, contact sheets, selected representative examples, or redacted review packets depending on artifact policy.

## Evaluator prompt shape

Blind identification:

```text
You are evaluating brand fidelity. You will see N assets. Most are official Ostium assets; one may be generated.

Do not rely only on resolution, compression, or obvious rendering artifacts. Judge by brand system, composition, proof hierarchy, typography, color semantics, market specificity, and claim discipline.

Tasks:
1. Pick the asset most likely to be generated.
2. Give the top five reasons.
3. Score each asset from 1–5 for Ostium brand fidelity.
4. Identify what the generated asset would need to improve.
5. Identify whether the failure points imply missing guidance in `brand.md` or only poor generation execution.
```

Rubric scoring:

```text
Evaluate this asset against `brand.md`.

Return JSON:
{
  "ostium_recognizability": 1-5,
  "market_specificity": 1-5,
  "proof_hierarchy": 1-5,
  "color_semantics": 1-5,
  "typography_data_treatment": 1-5,
  "logo_restraint": 1-5,
  "claim_discipline": 1-5,
  "production_taste": 1-5,
  "spec_traceability": 1-5,
  "likely_generated": true/false,
  "failure_reasons": [...],
  "brand_md_missing_guidance": [...],
  "generation_execution_issues": [...]
}
```

## Metrics

Possible run-level metrics:

- generated-identification rate;
- average rubric score;
- lowest required score;
- claim-discipline failure count;
- generic-drift failure count;
- missing-guidance count;
- improvement from generic baseline to `brand.md`-conditioned prompt.

A useful first target:

- generated candidate average rubric score >= 4.0;
- claim discipline >= 5;
- color semantics >= 4;
- market specificity >= 4;
- generated asset not identified for core brand-system reasons more than half the time.

## Failure taxonomy

Classify failures into:

1. **Spec gap** — `brand.md` does not say enough.
2. **Prompt translation gap** — `brand.md` says it, but prompt builder lost it.
3. **Generation model limitation** — prompt was good, output tool could not execute.
4. **Asset-policy gap** — output depends on logo/font/media-kit rules not yet formalized.
5. **Taste gap** — follows rules but still feels weak or amateur.
6. **Claim-safety gap** — output invents unsupported financial/partner/performance claims.
7. **Overfit gap** — output copies a reference asset too closely instead of generalizing.

Only spec gaps should automatically feed back into `brand.md`. Other gaps should update prompt builder, evaluator, asset policy, or model/tool choice.

## Human review loop

The evaluator should not decide public readiness alone. It should produce a review packet that a human can inspect:

- visual candidates;
- evaluator ranking;
- rubric scores;
- likely generated pick;
- failure taxonomy;
- recommended next action:
  - patch `brand.md`;
  - patch prompt builder;
  - change generation tool;
  - discard candidate;
  - approve for further design review.

## Suggested first implementation slice

1. Select 5–7 official Ostium social assets or contact-sheet frames.
2. Generate one unsupported asset from `brand.md` only.
3. Generate one weak generic baseline.
4. Run a blind identification prompt through a vision-capable evaluator.
5. Save `findings.md` and `evaluator-results.json`.
6. Patch `brand.md` only if the failure points are true spec gaps.

## Evaluator positioning

- Use evaluator runs as directional creative evidence that strengthens the brand-system case over time.
- Optimize for source-backed recognizability, claim discipline, and credible creative transfer — not evaluator gaming.
- Separate compression/render artifacts from true brand-system gaps.
- Use third-party assets only when explicitly allowed and clearly sourced.
- Present generated assets as brand-system prototypes and creative workflow evidence unless/until Ostium approves them as official communications.
