# Operating Procedure: Higgsfield Seedance 2.0 Video + Virality Predictor Iterative Loop

## Status

Local/private v1 operating procedure for Seedance 2.0 video generation plus Higgsfield Virality Predictor feedback. Ready for Chris-approved video test runs and kept private until selected for public publication.

## Purpose

Define an agent-operated video-generation workflow for Ostium brand portability using:

1. Higgsfield MCP video generation with `seedance_2_0`;
2. optional source-approved start frames or deterministic visual overlays;
3. Higgsfield Virality Predictor feedback;
4. a bounded self-iterative loop that improves the next prompt/video direction from actual video + virality feedback.

The desired loop is:

> video brief → start-frame/composition plan → Seedance 2.0 generation → visual/brand review → Virality Predictor review → failure/feedback classification → targeted prompt/storyboard revision → rerun within budget → comparison summary.

This is the video analogue of the still-image self-loop, with Virality Predictor added as an additional evaluator rather than the sole judge.

## Model/tool facts to preserve

Observed through Higgsfield MCP model discovery:

- Video model: `seedance_2_0`
- Name: Seedance 2.0
- Provider: Bytedance
- Purpose: reference-driven video with image/video/audio reference inputs, consistent identity, product/multi-SKU support
- Supported durations: 4–15 seconds
- Supported aspect ratios: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
- Optional parameters:
  - `resolution`: `480p`, `720p`, `1080p`; default `720p`
  - `mode`: `std`, `fast`; default `std`
  - `genre`: `auto`, `action`, `horror`, `comedy`, `noir`, `drama`, `epic`; default `auto`
- Media roles include: `image`, `start_image`, `end_image`, `video`, `audio`
- Do not pass `generate_audio`; Seedance 2.0 accepts audio via media input only.

Virality Predictor:

- Use Higgsfield MCP `virality_predictor` after a generated video completes.
- Input should be a completed generated video job ID or confirmed uploaded video media ID.
- Treat Virality Predictor as a creative-performance evaluator: hook strength, attention, engagement, retention risk, audience response, and creative performance.
- Use virality feedback to sharpen hooks, pacing, and audience clarity while keeping source truth, claim discipline, and brand fit as the creative foundation.

## Recommended first video format

Default internal smoke-test settings:

- Duration: 4–6 seconds.
- Aspect ratio: `16:9` for brand/booth/report hero motion, or `9:16` for short-form social testing.
- Resolution: `720p` for exploration; `1080p` for stronger candidate review when cost/time allow.
- Mode: `std` unless speed is the goal.
- Genre: `auto` or `drama`; avoid genre values that create off-brand tonal drift.
- Text burden: minimal. Do not ask the video model to render exact paragraphs, product numbers, or dense UI text.
- Captions: if exact captions are required, plan deterministic/text-accurate post overlay rather than relying on generated video text.

## Video subtype taxonomy

This workflow is not limited to product videos. Subtypes are a recommended planning aid, not a required gate. Use one when it clarifies risks, inputs, and review criteria; otherwise let the brief remain free-form and infer the closest subtype only for review/checklist purposes.

### 1. Product / UI motion

Use for app screens, order tickets, open-position modules, market access demos, settlement/execution explainers, or product-led social clips.

Default strategy:

- use a source-approved app screenshot, deterministic UI reconstruction, or clean start frame;
- keep generated UI text abstract unless it is overlaid later;
- show product state clearly before cinematic motion;
- use deterministic overlays for exact prices, labels, trade sizes, and claims.

Primary risks:

- fake UI numbers or labels;
- generated pseudo-text;
- generic trading-platform drift;
- product mechanics that do not match the source docs;
- over-cinematic motion that obscures the product.

### 2. Market-event motion

Use for CPI, earnings, commodities, indices, forex, crypto, macro catalysts, or campaign moments.

Default strategy:

- lead with the market/catalyst in the first second;
- use market-specific imagery from the `brand.md` mapping;
- keep the motion clear enough to understand muted;
- add exact event labels/captions deterministically after generation.

Primary risks:

- generic finance montage;
- unsupported market claims;
- fake news/partner/exchange visuals;
- weak or delayed hook;
- overuse of green/red/orange outside their semantic roles.

### 3. Conference / brand hero motion

Use for booth screens, website hero loops, event backdrops, report hero motion, or non-verbal brand atmosphere.

Default strategy:

- start from a strong still composition or deterministic overlay composite;
- use subtle parallax, light routing, product-panel motion, and atmosphere;
- keep exact text/logo separate unless using a text-accurate overlay pass;
- preserve safe areas for booth/web layout.

Primary risks:

- becoming a generic crypto conference wall;
- illegible generated background UI;
- excessive cinematic complexity;
- weak connection to global markets/onchain gateway positioning.

### 4. Founder / operator narrative

Use for in-person narrative concepts that feel like a founder, CEO, trader, or operator explaining Ostium, without attempting to generate a one-to-one likeness of a specific real executive. In this workflow, a “CEO video” example usually means testing the script, hook, framing, and market-native concept before anything is actually shot — not optimizing a synthetic CEO likeness.

Default strategy:

- frame as a credible founder/operator talking-head or walk-and-talk scene;
- keep the script direct, market-native, and proof-led;
- use deterministic captions for exact wording;
- add product/market cutaways only when they clarify the message;
- evaluate voice, body language, pacing, and first-second hook in addition to brand visuals.

Primary risks:

- generic AI-founder-ad feel;
- unnatural face, mouth, hands, or body motion;
- overpolished lifestyle/startup staging;
- vague hype instead of concrete market/product language;
- captions or speech drifting from approved copy.

### 5. Hybrid narrative + product/UI

Use when a founder/operator or CEO-style narrative is combined with product screenshots, market panels, or UI cutaways.

Default strategy:

- separate responsibilities: person/narrative motion from deterministic product/caption overlays;
- use product cutaways to clarify, not distract;
- keep exact claims/captions/source data outside the generative pass where possible.

Primary risks:

- both the person and product UI becoming uncanny or inaccurate;
- generated cutaways inventing product details;
- hook becoming too complex for a 4–6 second first pass.

### Separate production track: real-person likeness

This v1 loop is focused on hook/script/concept testing for founder/operator-style narratives. If a future production workflow needs actual-person likeness or voice work, handle it as a separate approved-reference media process with its own consent, review, and release controls.

## Inputs

Required:

- `brands/ostium/brand.md`
- `docs/BRAND_PROVENANCE.md`
- `docs/EVIDENCE_TRACEABILITY_MATRIX.md`
- `docs/future-integrations/higgsfield-mcp-visual-video-portability.md`
- `docs/future-integrations/higgsfield-iterative-self-loop-operating-procedure.md`
- a video brief: audience, platform/aspect ratio, desired action, duration, market/product or narrative anchor, and whether the output is internal exploratory or candidate-public. A subtype is recommended when useful, but not required.

Recommended:

- source-approved start frame or deterministic composition image;
- official product screenshot or approved UI reconstruction;
- exact text/caption overlay plan;
- prior experiment folder if extending an existing visual direction.

## Output folder structure

Use a loop folder so all iterations remain auditable:

```text
experiments/higgsfield-mcp-visual-video-portability/YYYY-MM-DD-<video-asset>-seedance-virality-loop/
  brief.md
  iteration-01/
    seedance-prompt.txt
    start-frame.png                 # optional
    generated-video.mp4
    job-metadata.json
    virality-predictor.json         # or dashboard/job notes
    REVIEW_PACKET.md
  iteration-02/
    seedance-prompt.txt
    generated-video.mp4
    job-metadata.json
    virality-predictor.json
    REVIEW_PACKET.md
  comparison-summary.md
```

If the Virality Predictor returns an interactive dashboard rather than plain JSON, record the predictor job ID, key surfaced scores/notes, and screenshots/exported summaries where possible.

## Video prompt packet

A Seedance prompt should be storyboard-like, not just aesthetic adjectives.

When helpful, declare or infer a subtype from the taxonomy: product/UI motion, market-event motion, conference/brand hero motion, founder/operator narrative, or hybrid narrative + product/UI. Do not block prompt writing just because a brief does not fit neatly into one subtype.

Include:

- duration and aspect ratio;
- first frame / start-frame description;
- motion arc in 2–4 beats;
- camera movement;
- product/market anchor;
- desired hook in the first 1–2 seconds;
- visual hierarchy and safe areas;
- what text/captions are generated versus overlaid later;
- brand color semantics;
- what must not appear.

Avoid:

- dense generated captions;
- fake exchange/partner logos;
- fake product performance;
- fake live dashboards or exact numbers unless they are deterministic/source-approved overlays;
- overproduced crypto/cyberpunk motion;
- random coins/tokens/rocket/moon imagery;
- unsupported calls to invest or promises of profit.

## Autonomous loop

### 1. Prepare the video brief

Start with a tight creative objective, for example:

- “4-second 16:9 brand hero motion for conference booth screen.”
- “6-second 9:16 market-event social clip about global markets moving onchain.”
- “5-second product UI motion showing market access and transparent execution.”

Define the first-frame strategy:

- generate a start frame with the image workflow;
- use a deterministic composite from a prior pass;
- use an approved product screenshot/reference;
- or text-only generation if no reference is available.

Prefer start-frame/reference-driven video for Ostium because identity and product specificity matter.

### 2. Generate with Seedance 2.0

Call Higgsfield MCP `generate_video` with:

- `model: seedance_2_0`
- `duration`: 4–6 seconds for first pass, within the 4–15s supported range
- `aspect_ratio`: selected by brief
- `resolution`: `720p` for smoke tests or `1080p` for stronger review candidates
- `mode`: `std` by default
- optional `medias`:
  - start frame role: `start_image`
  - end frame role: `end_image` when needed
  - audio role: `audio` only if using an audio reference

Record:

- job ID;
- returned model and adjusted params;
- duration/aspect/resolution;
- prompt;
- input media IDs;
- output URL/local file path.

### 3. Review the generated video manually/visually

Before Virality Predictor, the agent should review the video against brand and production constraints.

Score:

1. Ostium recognizability
2. Market specificity
3. Proof/product hierarchy
4. Color semantics
5. Caption/text behavior
6. Logo restraint
7. Claim discipline
8. Motion clarity
9. First-2-second hook
10. Production taste
11. Spec traceability

Check video-specific hard failures:

- illegible or hallucinated captions;
- fake product UI numbers;
- camera motion that obscures product clarity;
- generic crypto hype visuals;
- orange used as P&L semantics;
- distracting transitions;
- unsupported claims;
- hook too slow or unclear in first 1–2 seconds;
- video not understandable muted.

### 4. Run Virality Predictor

After a video candidate is generated and locally reviewed, run Higgsfield MCP Virality Predictor using the completed generated video job ID or uploaded video media ID.

Capture:

- Virality Predictor job ID;
- overall predicted virality/creative-performance readout;
- hook strength;
- retention/attention risk;
- engagement/audience response notes;
- scene-level or moment-level issues if exposed;
- dashboard screenshot/export/summary when available.

Important: Virality Predictor is advisory. It can suggest a stronger hook, pacing, or retention structure, but it must not authorize off-brand claims, fake urgency, or unsupported performance promises.

### 5. Merge brand review and virality feedback

Create a combined diagnosis:

- **Brand-critical failures** — must fix before any further virality optimization.
- **Production-critical failures** — text, logo, UI, audio, or visual clarity issues.
- **Virality/hook opportunities** — stronger first second, clearer transformation, more specific market/event, faster visual payoff.
- **Retention risks** — slow start, too much visual ambiguity, no action beat, weak final frame.
- **Prompt/pipeline changes** — what to change in the next generation.

Decision priority:

1. Claim discipline and source truth.
2. Brand recognizability and market/product specificity.
3. Video clarity and exact text/UI handling.
4. Virality/hook/retention optimization.
5. Polish.

### 6. Rerun with targeted changes

Revise only the smallest useful variable per iteration:

- shorten/strengthen the first visual hook;
- introduce the market/product anchor in the first second;
- simplify motion or camera path;
- use a stronger start frame;
- move captions to deterministic overlay;
- add clearer final frame / end card;
- switch aspect ratio for platform fit;
- switch duration within 4–15s;
- use official product UI/reference input;
- adjust prompt away from generic crypto/DeFi motifs.

Do not make five major changes at once unless the prior iteration was structurally wrong.

### 7. Compare iterations

For each iteration after the first, write a comparison:

- video job IDs;
- thumbnail/contact sheet or keyframes if available;
- brand score delta;
- Virality Predictor delta;
- hook/retention delta;
- what improved;
- what regressed;
- selected candidate and why.

If Virality Predictor improves while brand score worsens, do not select the higher-virality output unless Chris explicitly chooses that tradeoff.

## Stop conditions

Stop the loop when any of these are true:

- the candidate passes brand/claim discipline and Virality Predictor feedback no longer reveals a high-priority hook/retention failure;
- the iteration budget is exhausted;
- the next improvement requires official source media, product screenshots, voiceover, or Chris's creative judgment;
- further changes would optimize for virality at the expense of Ostium source discipline;
- tool/auth/credit issues make additional video runs noisy or expensive.

Default budget:

- 1–2 Seedance candidates for a smoke test;
- up to 3 iterations for a serious internal pass;
- Virality Predictor after each completed candidate selected for possible continuation.

## Review packet fields

Each iteration `REVIEW_PACKET.md` should include:

- brief and intended platform;
- Seedance prompt;
- model/job metadata;
- start/end/reference media used;
- generated video file/link;
- brand/video rubric scores;
- manual review notes;
- Virality Predictor job ID and feedback summary;
- combined diagnosis;
- next prompt revision;
- stop/continue decision.

The loop-level `comparison-summary.md` should include:

- all candidate job IDs;
- final selected video;
- score deltas;
- Virality Predictor deltas;
- best-candidate rationale;
- remaining risks;
- whether a `brand.md`, prompt-builder, or pipeline change is recommended.

## Example video loop

Hypothetical 6-second 16:9 Ostium conference-screen video:

1. Start from the deterministic booth backdrop composite.
2. Seedance prompt: slow parallax over booth wall, orange gateway/routing lines animate across global market panels, product UI comes into focus, final frame holds safe area for exact overlay.
3. Manual review finds motion good but hook too slow and generated UI text messy.
4. Virality Predictor flags weak first-second hook and retention risk from slow payoff.
5. Iteration 02 uses a sharper first beat: orange routing pulse starts immediately, market panels snap into alignment by second 1.5, product UI remains abstract and exact text stays out of video generation.
6. If brand score and virality/hook improve, stop and plan deterministic caption/end-card overlay.

## Guardrails

- Keep all video prompts, outputs, predictor results, and review packets local/private until Chris approves public publication.
- Do not treat Virality Predictor as a source of truth about brand, compliance, or product facts.
- Do not create artificial urgency, financial promises, or unsupported performance claims for virality.
- Do not use official-looking product UI or logo geometry unless sourced/approved.
- Prefer short, clear, muted-understandable videos over overproduced cinematic complexity.
- Preserve job IDs and model-return metadata for auditability.
