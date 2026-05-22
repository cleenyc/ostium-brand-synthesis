# Operating Procedure: Higgsfield Iterative Self-Loop for Brand Portability

## Status

Local/private v1 operating procedure for agent-run Higgsfield iteration. The loop is specified and already reflected in internal static-image tests; public publication remains Chris-approved.

## Purpose

Define an agent-operated creative QA loop for Higgsfield-style image/video generation where the agent does not stop after the first acceptable image. Instead, it:

1. generates a small candidate set;
2. reviews each candidate against the source-backed Ostium brand rubric;
3. compares candidates against prior passes;
4. identifies concrete failure modes;
5. revises the prompt/pipeline only where evidence supports a change;
6. reruns a bounded number of iterations;
7. selects the best candidate with a documented rationale.

The observed pattern from the booth-backdrop work is the model:

> first generation → visual/rubric review → failure diagnosis → workflow/prompt adjustment → rerun → comparison packet → next recommendation.

This procedure makes that loop explicit so a future agent can operate it autonomously within guardrails.

## Operating boundaries

- Keep the loop bounded so the agent produces momentum instead of open-ended generation.
- Optimize for repeatable brand portability, not a one-off pretty image.
- Preserve failure evidence so each rerun strengthens the workflow.
- Patch `brand.md` when a result reveals missing portable brand guidance; route model-specific quirks to prompt-builder, overlay, or evaluator improvements.
- Keep outputs, prompts, model choices, and review packets local/private until Chris approves publication.
- Use deterministic/source-approved verification for exact text, logo geometry, product numbers, and claims.

## Inputs

Required:

- `brands/ostium/brand.md`
- `docs/BRAND_PROVENANCE.md`
- `docs/EVIDENCE_TRACEABILITY_MATRIX.md`
- `docs/future-integrations/higgsfield-mcp-visual-video-portability.md`
- asset brief: asset type, audience/context, desired message, output format, and whether the asset is exploratory, internal, or candidate-public.

Optional:

- previous experiment folders for the same asset type;
- approved reference frames or official product screenshots;
- deterministic overlay/template files;
- formal media-kit assets once reviewed.

## Iteration budget

Default bounds for an autonomous agent:

- Candidate set per iteration: 2–4 generated candidates when credits/time allow; 1 candidate only for smoke tests or constrained budgets.
- Maximum iterations per asset type: 3.
- Stop early if a candidate passes the minimum useful-result bar and the remaining failures are only production-polish issues that require source assets rather than more generation.
- Escalate to Chris instead of continuing when a decision is aesthetic/strategic rather than objectively scored by the rubric.

Recommended iteration labels:

```text
experiments/higgsfield-mcp-visual-video-portability/YYYY-MM-DD-<asset-type>-loop/
  iteration-01/
    prompt.txt
    candidates/
      candidate-01.png
      candidate-02.png
    REVIEW_PACKET.md
  iteration-02/
    prompt.txt
    candidates/
    REVIEW_PACKET.md
  comparison-summary.md
```

If only one candidate is generated per iteration, preserve the same structure with one candidate file.

## Autonomous loop

### 1. Build the initial prompt packet

Use only source-backed brand rules and the asset brief.

The prompt packet should specify:

- asset type and format;
- desired dominant read;
- market/product anchor;
- composition and safe-area needs;
- color semantics;
- logo/text/data treatment;
- claim constraints;
- negative prompt / avoid-list;
- whether the pass is a composition-only pass or a final-copy/text pass.

For assets with exact copy, logo, data, or compliance-sensitive claims, default to the two-step workflow:

1. generate composition/atmosphere/product environment;
2. overlay exact typography, logo, product UI, figures, and claims deterministically or with a text-accurate model/pass.

### 2. Generate a bounded candidate set

Use the preferred model policy from the Higgsfield integration spec:

- default image model request: `nano_banana_pro`;
- record the model actually returned by Higgsfield, because the backend may return a fallback such as `nano_banana_2`;
- record job IDs, dimensions, aspect ratio, prompt, and any fallback/adjustment notices.

Do not mutate `brand.md` between candidates in the same iteration.

### 3. Review each candidate independently

For every candidate, inspect the actual pixels/output. Do not rely on the model's prompt or job metadata.

Score each candidate 1–5 on the standard rubric:

1. Ostium recognizability
2. Market specificity
3. Proof/product hierarchy
4. Color semantics
5. Typography behavior
6. Logo restraint
7. Claim discipline
8. Modality fit
9. Production taste
10. Spec traceability

Also record hard failures:

- misspelled or unreadable generated text;
- fake logos, fake partners, fake endorsements;
- fabricated exact metrics/claims;
- green/red/orange semantic misuse;
- generic DeFi/SaaS/cyberpunk drift;
- low product/UI credibility;
- unsafe logo/font assumptions;
- poor safe-area behavior for overlay;
- video captions illegible when muted.

### 4. Compare candidates and prior passes

For each iteration, write a comparison section:

- best candidate and why;
- second-best candidate and why it lost;
- what improved versus the previous pass;
- what regressed versus the previous pass;
- whether failures are prompt-level, pipeline-level, model-level, source-spec-level, or production-asset-level.

Classification rules:

- **Prompt-level failure:** The prompt omitted a needed instruction already present in `brand.md`.
- **Pipeline-level failure:** The workflow asked the model to do something it should not own, e.g. exact typography or product numbers.
- **Model-level failure:** The instruction was clear, but the model produced artifacts, typos, or pseudo-text anyway.
- **Source-spec-level failure:** The brand spec lacks portable guidance needed across tools, not just for one model.
- **Production-asset-level failure:** The output requires official logo/font/media-kit/product assets, not more prompt iteration.

### 5. Decide the next action

Use this decision tree:

1. **Candidate passes and remaining issues are overlay/source-asset issues** → stop generation; create deterministic/source-approved overlay task.
2. **Candidate fails because generated text/logo/data are unreliable** → move exact elements to overlay pass; do not keep asking the image model to fix exact copy.
3. **Candidate fails due to generic drift** → revise prompt to add stronger market/product anchor and compare against prior candidates.
4. **Candidate fails due to missing brand guidance across multiple tools/candidates** → propose a `brand.md` patch, with evidence.
5. **Candidate fails due to low production taste but follows the spec** → try one more model/prompt iteration within budget.
6. **Multiple candidates are close and preference is subjective** → produce comparison packet and ask Chris to choose.

### 6. Rerun with a targeted change

The next prompt should change only the smallest useful variable, such as:

- stronger product/market anchor;
- composition-only instead of text-rendering;
- explicit safe-area geometry;
- reference image input;
- alternate model for text/diagram fidelity;
- deterministic overlay of exact product UI.

Do not rewrite the entire prompt unless the comparison packet shows the first prompt was structurally wrong.

### 7. Finalize the loop

At the end of the bounded loop, save:

- all prompts;
- all generated candidates;
- deterministic overlay files if any;
- side-by-side comparison image or contact sheet;
- `REVIEW_PACKET.md` for each iteration;
- `comparison-summary.md` for the loop;
- local project checkpoint with job IDs, scores, chosen candidate, and remaining issues.

## Minimum final packet

A loop is complete only when the repo contains enough evidence for another agent or Chris to audit the decision:

```text
asset brief
prompt(s)
model/job metadata
candidate files
visual review notes
rubric scores
side-by-side comparison
best-candidate rationale
failure classification
next action
publication status
```

## Stop conditions

Stop the autonomous loop when any of these are true:

- a candidate meets the minimum useful-result bar: average score >= 4, no claim-discipline failure, no obvious generic drift, and at least one documented workflow/spec lesson;
- iteration budget is exhausted;
- the next improvement requires official assets, source screenshots, or Chris's aesthetic judgment;
- credit/tool/auth issues would make further attempts noisy rather than informative;
- a public-facing decision is needed.

## Escalation rules

Ask Chris before proceeding when:

- choosing between two subjectively different strong directions;
- publishing anything externally;
- using official-looking logos/product claims without verified source assets;
- changing the public repo;
- spending beyond the default iteration budget;
- moving from internal exploratory assets to candidate-public assets.

## Example from booth-backdrop passes

Pass 01:

- Model: `z_image`
- Approach: single-pass final asset with generated text
- Result: directionally on-brand but failed minimum useful bar
- Failure modes: `foex` typo, generic trading-platform drift, weak product specificity
- Score: 3.65/5

Pass 03 rerun:

- Requested model: `nano_banana_pro`; returned model: `nano_banana_2`
- Approach: composition generation + deterministic exact overlay
- Result: stronger booth physicality, typo-free headline/support copy, better booth-scale read
- Remaining issue: generated product panels still contain pseudo-readable/gibberish UI texture
- Score: 4.35/5

Loop lesson:

- The correct improvement was not “ask the image model harder to spell forex.”
- The correct improvement was to separate responsibilities: generative model for physical booth atmosphere and deterministic/source-approved overlays for exact typography, logo, and product UI.

## Implementation notes for future automation

A future agent can implement this as a local runner with these stages:

1. `build_prompt(asset_brief, brand_docs, prior_review)`
2. `generate_candidates(prompt, model_policy, count)`
3. `download_outputs(job_ids)`
4. `review_candidate(candidate, rubric)`
5. `compare_candidates(candidates, prior_passes)`
6. `classify_failures(review)`
7. `decide_next_action(review, iteration_budget)`
8. `write_review_packet()`
9. `write_project_checkpoint()`

The runner should keep secrets out of the repo and store only non-secret job metadata, prompts, outputs, and review notes.
