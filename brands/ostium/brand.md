# Brand Spec: Ostium

## Status

- Version: 0.3 portability revision
- Date: 2026-05-21
- Owner/reviewer: Chris Lee
- Status: Strong first-pass synthesis with portability-oriented generation rules; source-backed, inferred, and operationalized rules are labeled for iteration
- Source posture: current official public sources only; additional official resources may be added later

## 1. Source Inventory

See `brands/ostium/source-inventory.md` for the full inventory.

Core source families:

| ID range | Source family | Role |
|---|---|---|
| S01-S06 | Official website, visual assets, and app/product surfaces | Brand positioning, visual system, product UI language |
| S07-S13 | Official docs | Product claims, terminology, infrastructure architecture |
| S14-S18 | Official X/Twitter | Social voice, proof patterns, visual/video grammar |
| S19-S20 | Owned blog and media kit reference | Editorial voice and future official asset expansion |

## 2. Authority Hierarchy

- Primary explicit sources: official website, official app surfaces, official docs, official logo/assets.
- Primary observed sources: official website visuals, app screenshots/assets, official X images/videos.
- Social behavior sources: official X posts and media, useful for voice, cadence, hooks, and proof patterns.
- Derived synthesis: local notes and contact sheets in `brands/ostium/notes/` and `brands/ostium/resources/`.

Conflict rules:

- Official docs and website copy outrank social shorthand for product facts.
- Social posts can define voice and content behavior, but do not establish exact product/legal claims by themselves.
- Logo/clearspace rules should only be treated as candidate rules until the full media kit is reviewed.
- Visual directions are stronger when they recur across website, app, and social assets.

## 3. Brand Essence

- Observable positioning: Ostium is the onchain gateway to global markets: a self-custodial, transparent venue for trading perpetual exposure across stocks, ETFs, commodities, indices, forex, and crypto.
- Emotional tone: serious, liquid, precise, trader-native, global, confident, infrastructure-grade.
- Visual adjectives: dark, premium, kinetic, data-dense, orange-accented, institutional, execution-focused, gateway-like.
- Avoided adjectives: playful, meme-first, soft consumer fintech, generic DeFi, neon cyberpunk, mascot-led, abstract without proof.
- Evidence: S01-S04, S07-S09, S14-S18.
- Confidence: high for direction; source-backed first pass.

## 4. Colors

| Token | Value | Usage | Evidence | Confidence |
|---|---|---|---|---|
| ostium-orange | `#FF5A19` | Primary brand accent, CTAs, active states, social emphasis | S02, S04, S16-S18 | High direction / high observed value |
| ink-black | `#080909` / `#0C0C0D` | App/page backgrounds, terminal foundation | S03-S06 | High direction / medium exact value |
| charcoal-panel | `#111111` / `#151515` / `#222222` | Cards, panels, borders, UI hierarchy | S02, S04, S06 | High direction / medium exact value |
| soft-white | `#FFE8E2` / near-white | Logo, headlines, high-priority text | S02-S05 | High direction / medium exact value |
| muted-gray | `#D0DBDA` and darker gray variants | Secondary labels, UI copy, subdued text | S02, S04, S06 | Medium-high |
| copper-deep | `#9E200E` / `#450B05` | Cinematic gradients, identity atmospherics | S02-S03 | Medium-high |
| market-green | observed green range | Long/up/profit/success semantics | S04, S06 | High semantic direction |
| market-red | observed red/pink range | Short/down/loss/risk semantics | S04, S06 | High semantic direction |

Rules:

- Use orange as the Ostium identity/action layer.
- Keep green and red reserved for market semantics, P&L, long/short, and chart movement.
- Pair orange with black/charcoal and off-white rather than bright white-on-orange everywhere.
- Use copper/burnt gradients for cinematic identity moments, not dense UI tables.
- Avoid blue/purple SaaS gradients as a default brand field.

## 5. Typography

- Primary behavior: clean, modern sans-serif for UI and marketing; uppercase/wide tracking for wordmark and concise labels.
- Data behavior: use tabular numerals or monospace for prices, sizes, market stats, code/API examples, and proof metrics.
- Observed font families: `Ppmori Variable`, `Ttfirsneue`, `IBM Plex Mono`, `Ppmondwest`, app usage of IBM Plex Sans/Mono patterns.
- Heading style: short, confident, high-contrast; often title-case for marketing and uppercase for social/milestone assets.
- Body style: direct, product-led, economical; avoid ornamental copy blocks.
- Social caption style: bold all-caps, high-contrast white with orange/red emphasis words.
- Evidence: S02, S04, S06, S16-S18.
- Confidence: high for typography behavior; provisional for exact licensed font usage until full media kit review.

## 6. Logo & Marks

- Approved observed usage: Ostium wordmark and gateway-like mark appear in official website assets, OG image, app header, favicon/webclip, and social milestone visuals.
- Conceptual motif: gateway, portal, threshold, market access point.
- Background rules: observed mark/wordmark works on black/charcoal, orange, and cinematic dark/copper backgrounds.
- Clear space: open decision pending full media kit review.
- Minimum size: open decision pending full media kit review.
- Misuse / don'ts: do not redraw the mark, stretch the wordmark, invent alternate logo systems, or overclaim official clearspace/token rules.
- Evidence: S03, S05, S06, S16.
- Confidence: high for observed mark direction; provisional for formal usage rules.

## 7. Layout & Grid

- Grid system: product UI uses a dense desktop trading-terminal grid with chart, market stats, recent trades, order ticket, and position tables.
- Margins: marketing identity assets use broad cinematic negative space; product assets use tight gutters and compact cards.
- Alignment: precise rectangular modules, left-aligned data labels, tabular numeric columns, clear panel boundaries.
- Density: high for product proof; low-to-medium for brand identity moments.
- Whitespace: use spacious hero/identity scenes, but do not hide product complexity in product surfaces.
- Hierarchy: chart/asset/proof message first, supporting metrics second, CTA/action state third.
- Evidence: S03-S06, S16-S18.
- Confidence: high.

## 8. Composition

- Common framing: market-specific background or product proof first; one strong focal object, proof number, campaign phrase, or UI module; orange atmospheric treatment; concrete market/product detail.
- Balance: pair atmospheric brand space with hard product proof; avoid decorative visuals without execution evidence.
- Cropping: social images can use large billboard/product/proof crops; videos can use tight talking-head crops with caption rhythm.
- Scale relationships: in social assets, the logo is usually restrained while the market event, number, question, or product UI module is dominant; metrics should be prominent in trade-proof assets.
- Focal point behavior: either brand gateway/wordmark, product UI/chart, or one proof headline; avoid competing headline stacks.
- Evidence: S03-S04, S16-S18.
- Confidence: high direction.


## 8A. Ostium Social Asset System — observed from recent official posts

Ostium social assets should not collapse into a generic dark fintech launch-card style. The observed system is template-driven, market-event-specific, and proof-led.

High-confidence social templates:

1. **Campaign/event banner** — 16:9 or wide landscape; full-bleed market/news/technology imagery; heavy black-to-burnt-orange overlay; huge 1–3 word campaign headline; smaller muted subtitle; white Ostium logo bottom-left; circular market/asset icons bottom-right. Examples: CPI/“Hot Print”, semiconductor/“Silicon Week”.
2. **Cost breakdown card** — square/portrait orange-red gradient; top-left Ostium logo; large question headline with the dollar amount as the dominant line; trade descriptor row with Long/Short pill, pair, leverage; minimalist fee table with horizontal dividers; large rounded total-cost callout at bottom.
3. **Trade result / commodity proof card** — 16:9 landscape; cinematic asset-specific background such as oil/tanker/liquid texture; huge notional amount top-left; short context line (“in WTI shorts.”); black PNL module on the right with green/red numeric semantics; small white Ostium logo bottom-center.
4. **Product-position overlay** — square; full-bleed real-world financial or gritty macro collage background; central near-black product UI card with one or two open-position modules; pair, direction/leverage pills, size, price, price impact, status, and “View more”; small white Ostium logo bottom-center.
5. **Earnings / market briefing card** — 4:5 portrait; dark brown-to-orange gradient with grain; subject/company logo or text at top-center; stacked data sections with thin dividers; Street/market/Ostium-positioning/largest-trade/promotion modules; bottom-center Ostium logo.

Social composition rules:

- Start with the market event or trade proof, not an abstract brand shape.
- Use backgrounds that explain the market: CPI documents, earnings/company imagery, trading floors, commodity visuals, political/macro collage, GPUs/servers/chips, or product UI screenshots.
- Orange is usually atmospheric heat: overlay, glow, gradient, or print-like block. It is not merely a small accent line.
- Typography should be very large and simple. Use one hero phrase or number, then one supporting line/module.
- Logo usage is restrained: small white lockup at bottom-left, bottom-center, or top-left depending on template. The logo is a signature, not the focal object.
- Product proof modules must look like real trading UI: black cards, subtle borders, compact labels, tabular numbers, Long green, Short red/pink, P&L green/red.
- Text must wrap and scale to safe areas. Headlines should never run near an edge; use max-width, balanced line breaks, and font-size reduction for long figures or questions.
- Avoid generic abstract gateway geometry as the default social template unless paired with specific source-backed market/product context.
- Avoid placeholder/internal proof chips such as “source-grounded spec” in generated public-facing examples.

Evidence: S16-S18 plus owner-provided recent official Ostium social samples reviewed on 2026-05-21.
Confidence: high for social-template direction; production details remain open for full official media-kit/font review.

## 9. Imagery / Photography

- Subject matter: product UI, market data, institutional milestone moments, traders/operators, global market references, commodities/equities/forex/crypto context.
- Lighting: dark, high-contrast, warm orange/copper accents; official social milestone photography can be bright real-world institutional context.
- Color grading: black/charcoal with orange/copper warmth; keep institutional photography clean and credible.
- Camera/framing: cinematic wides for identity; exchange-terminal screenshots for product; low/wide proof photography for large public milestones; tight talking-head for explainers.
- Texture: subtle atmospheric grain/haze acceptable in identity visuals; UI should stay crisp.
- People/product treatment: people signal credibility in founder/operator or milestone contexts, not lifestyle stock photography.
- Avoid: generic skyscraper stock, random coins/tokens, fantasy finance abstractions, overpolished lifestyle scenes without product relevance.
- Evidence: S03-S04, S16-S18.
- Confidence: medium-high.

## 10. Illustration & Iconography

- Stroke/fill: simple geometric iconography; orange brand mark; market/pair icons in app context.
- Geometry: portal/gateway-like mark, square/boxed logo containers, terminal cards, chart/grid lines.
- Complexity: keep icons simple; reserve complexity for real product UI, charts, and tables.
- Metaphors: gateway, routing, liquidity, global markets, execution rails, transparent settlement.
- Icon usage rules: pair/category icons should support market identity, not become decorative clutter.
- Evidence: S05-S06, S16.
- Confidence: medium-high.

## 11. Motion / Video Language

- Motion principles: explain complex market-structure ideas through direct, caption-led clips; use product proof and exact examples where possible.
- Pacing: fast caption cadence; short phrase chunks; minimal visual lag.
- Transitions: keep simple unless showing product/UI or market movement; do not overproduce at the expense of clarity.
- Camera movement: talking-head clips can be static; product videos can use direct screen/demo motion.
- Text animation: bold all-caps captions with orange/red emphasis words; captions should be legible when muted.
- Audio/VO/music cues: human explanation and market/operator credibility matter more than cinematic sound design in educational clips.
- Evidence: S18.
- Confidence: medium-high for social video; provisional for broader motion system.

## 12. Copy / Voice

- Tone: direct, confident, market-native, proof-led, precise.
- Sentence style: short declarative lines; use exact figures when substantiated; favor active verbs.
- Vocabulary: gateway, global markets, onchain, liquidity, execution, self-custody, USDC settlement, transparent, real market liquidity, stocks, commodities, forex, indices, crypto.
- Claims/positioning: connect traditional asset exposure to onchain infrastructure; show settlement/transparency/self-custody clearly; use official docs for product facts.
- Social proof style: “New record,” “Largest…,” exact notional, asset, direction, price impact/slippage, “one wallet,” “this trader.”
- Avoid: vague hype, unsupported performance claims, investment advice, compliance overreach, overclaiming institutional relationships, generic “future of finance” copy without proof.
- Evidence: S01, S07-S15, S17-S18.
- Confidence: high.

## 13. Generation Constraints

Prompt-ready rules for future asset generation:

- Must include: a specific Ostium social template or an explicit reason for constructing a new asset type from core principles; one dominant message/number/module; safe-area text wrapping; orange/black atmospheric treatment or orange-red field; concrete market/product vocabulary; and no unsupported claims.
- Should include: market-event imagery or product/data UI modules; exact sourced metrics when available; Long/Short/P&L semantic colors; restrained white Ostium logo placement; circular market/asset icon rows where campaign-relevant.
- May include: cinematic commodity/technology/macro backdrops, gritty editorial collage, trading-floor imagery, fee tables, open-position UI overlays, earnings briefing sections, caption-led talking-head style.
- Must avoid: generic abstract launch-poster geometry as the default; third-party logos/partners unless source evidence and usage rights are explicit; investment advice; fake official logo rules; random crypto token piles; blue/purple SaaS gradients; mascot imagery; unsupported profit/performance claims; internal/process proof text in public examples.
- Negative prompt / exclusions: generic DeFi neon, cyberpunk city grids, coin piles, moon/rocket memes, soft pastel fintech, fake exchange endorsements, illegible chart clutter, orange used as P&L color, single-line headlines that overflow safe margins.

Operational generation rules:

- **Logo as signature, not hero:** unless the requested asset is explicitly an identity/brand-lockup piece, the Ostium logo should be small and restrained. The hero should be the market event, proof number, product UI module, or campaign phrase.
- **One dominant read:** each asset should have one immediate read at thumbnail size: a large figure, a short phrase, a product state, or a briefing subject. Secondary modules can add credibility, but should not compete with the first read.
- **Market specificity before decoration:** if the asset references CPI, semiconductors, oil, indices, forex, or earnings, the background and modules should visually explain that market. Do not substitute generic financial abstraction for market context.
- **Data hierarchy:** use tabular/monospace numerals for prices, sizes, price impact, fees, P&L, and product table values. Use sans-serif display type for campaign phrases, questions, and section labels.
- **Semantic color discipline:** green is for long/up/profit/success; red/pink is for short/down/loss/risk; orange is brand/action/heat/atmosphere. Do not use orange as a substitute P&L color.
- **Proof before hype:** exact notional, direction, market, fee, slippage, price impact, or positioning data should outrank vague claims. If metrics are not sourced, label the output as hypothetical/demo or avoid exact claims.
- **Safe-area behavior:** large figures and questions should wrap and scale before they approach edges. Dollar amounts and dense numerals need extra vertical spacing and should never collide with surrounding copy.
- **Product UI credibility:** product-proof modules should look like real trading UI: black/near-black cards, subtle borders, compact labels, tight gutters, tabular numbers, status labels, and Long/Short badges.
- **Tool independence:** coordinates, exact font-size multipliers, renderer-specific spacing, and placeholder SVG geometry are implementation details, not brand truths. Preserve the composition logic across tools, but do not treat deterministic-renderer workarounds as official design rules.

## 14. Asset Generation Portability

The goal of this spec is not only to describe existing Ostium surfaces, but to carry enough brand intelligence for other tools or agents to create new Ostium-branded outputs without relying on hidden generator assumptions.

### 14.1 Asset-type decision tree

Use the lightest archetype that fits the requested message:

1. **Market event / campaign moment** → campaign/event banner.
   - Use for CPI, earnings weeks, semiconductor weeks, macro events, promotions, or time-boxed market themes.
   - Lead with a huge 1–3 word phrase, a concise subtitle, market-specific background imagery, restrained logo, and optional asset icon row.
2. **Cost, fee, or slippage explanation** → cost breakdown card.
   - Lead with a question and a dominant position-size/dollar figure.
   - Include trade direction, pair, leverage, fee/slippage rows, and a total-cost callout.
3. **Trader action or performance proof** → trade-result / proof card.
   - Lead with large notional or P&L, followed by market + direction context.
   - Include a compact P&L/status module and an asset-specific backdrop.
4. **Open positions or product state** → product-position overlay.
   - Use a central near-black UI card over a market/trading/macro backdrop.
   - Include pair, direction/leverage badge, size, price, price impact, status, and “View more”/navigation affordance only when appropriate.
5. **Earnings, company, or macro briefing** → briefing card.
   - Use stacked data sections, thin dividers, concise labels, and one subject/company/market at the top.
   - Include market consensus, options/probability, Ostium positioning, largest trade, or promotion modules only when sourced or explicitly hypothetical.
6. **Education / explainer** → caption-led video or product-annotated diagram.
   - Use short phrase chunks, product proof, direct market examples, and restrained transitions. Clarity outranks cinematic treatment.
7. **Unsupported new asset type** → construct from principles.
   - Start with: market-specific context + one proof-led message + one credible data/product module + orange/black atmosphere + restrained logo.
   - If no concrete market/product/proof anchor exists, ask for one or label the output as exploratory.

### 14.2 Promptable composition recipes

For downstream image/video tools, describe each asset in terms of role, focal point, support modules, and constraints rather than renderer coordinates.

- **Campaign/event banner:** wide 16:9 or landscape. Full-bleed market/event imagery under black-to-burnt-orange heat overlay. Huge centered or slightly left-of-center phrase. One smaller muted subtitle. Small white Ostium signature near bottom-left. Circular asset/category icons near bottom-right when relevant. Avoid abstract geometry unless it supports the market/event.
- **Cost breakdown card:** square/portrait. Orange-red gradient field. Top-left small white Ostium signature. Three-line question structure where the position size/dollar line is dominant. Trade descriptor row with Long/Short pill, pair, leverage. Minimal fee table with horizontal dividers. Bottom rounded total-cost callout.
- **Trade-result proof card:** 16:9 landscape. Cinematic commodity/market-specific background. Huge notional top-left. Short context line beneath. Right-side or lower-right black P&L module with semantic green/red. Small bottom-center logo.
- **Product-position overlay:** square. Gritty macro/trading/product backdrop. Central near-black card containing one or two open-position modules. Compact labels, subtle borders, Long/Short badges, tabular values, status text. Small bottom-center logo.
- **Briefing card:** 4:5 portrait. Dark brown/orange gradient with grain. Subject/company/market label top-center. Stacked sections separated by thin dividers. Use short labels and numerical values, not long prose. Bottom-center logo.

### 14.3 Market imagery mapping

Use imagery that explains the specific market or catalyst:

- CPI / inflation / macro print: official-looking reports, printouts, documents, rate screens, economic calendar texture, newsroom or terminal context.
- Semiconductors / AI / chip weeks: chips, GPUs, server racks, data-center lighting, manufacturing/thermal textures; avoid generic sci-fi circuits.
- Commodities / WTI / oil: crude/liquid texture, tankers, rigs, industrial shipping, energy-market terminals; avoid random flame or coin imagery.
- Indices / equities / earnings: company/product context, exchange screens, option-chain/earnings-calendar motifs, terminal panels.
- Forex / rates / global macro: currency pairs, macro maps, central-bank/rate-calendar cues, institutional terminal imagery.
- Crypto / onchain: wallet/settlement/product UI context; avoid token piles, moon/rocket memes, or generic blockchain neon.

### 14.4 Copy and content archetypes

Reusable Ostium-native copy structures:

- “How much does a [position size] [market/pair] trade cost on Ostium?”
- “[Large notional] in [market] [direction].”
- “One wallet built a [notional] [ticker/market] [direction] across [count] positions…”
- “[Market event phrase]” + “[specific promotional/product context].”
- “[Subject] pre/post-[event] briefing” with sections for consensus, options/probability, Ostium positioning, largest trade, and promotion.
- “New record,” “largest open trade,” “price impact,” “slippage,” “fees,” and “one wallet” are stronger when paired with exact, sourced values.

Do not invent exact live-market figures for public artifacts. For mockups, either use clearly synthetic/demo values or keep the asset private until values are sourced.

### 14.5 Evidence labels for generated outputs

When translating this spec into new assets, label rules by origin:

- **Observed:** directly visible in official Ostium website, app, docs, or owned social assets.
- **Inferred:** repeated pattern derived from multiple official examples.
- **Operationalized:** practical generation rule derived from observed/inferred behavior for portability.
- **Tool constraint:** limitation or workaround of a specific renderer/model; do not promote to brand truth.

A good output should preserve observed and inferred behavior, use operationalized rules to fill gaps, and avoid presenting tool constraints as official Ostium design guidance.

### 14.6 Portability test

To validate whether `brand.md` is operational rather than merely descriptive, test it with at least one asset request outside the current deterministic generator templates. The downstream tool or agent should receive this spec, provenance docs, and source inventory, but not hidden generator code or hardcoded layout defaults. Review the result for:

- recognizable Ostium tone and visual system;
- market-specific context rather than generic finance imagery;
- correct semantic colors and data hierarchy;
- restrained logo behavior;
- absence of unsupported claims;
- clear provisional labeling where source assets, exact fonts, or logo rules are unavailable.

Failures should be fed back into this spec as missing guidance, not silently fixed only in a renderer.

## 15. Do / Don't Summary

| Do | Don't | Evidence |
|---|---|---|
| Use orange as brand/action layer over black/charcoal | Use orange for market P&L semantics | S02, S04, S06 |
| Lead with product proof, exact metrics, and market specificity | Use vague finance/crypto hype | S07-S18 |
| Show dense trading UI when proving capability | Hide trading complexity behind generic app mockups | S04, S06 |
| Keep Nasdaq/partner language exact and careful | Overclaim endorsement or partnership scope | S16 |
| Use caption-led social clips for explainers | Make technical videos visually ornate but unclear | S18 |
| Preserve self-custody, transparency, and settlement framing | Make broker/custody claims not supported by docs | S07-S11 |

## 16. Open Decisions

| Issue | Sources | Recommendation | Needs Owner Review? |
|---|---|---|---|
| Full media-kit logo rules | S20 | Add media kit assets when the owner/reviewer provides or approves download/use; then formalize logo clearspace/min-size. | Yes |
| Exact font licensing and production font stack | S02, S04, S06 | Use observed font behavior now; do not imply public font rights until confirmed. | Yes |
| Full official video corpus | S15-S18 | Expand beyond selected high-signal posts if stronger motion spec is needed. | Optional |
| Public artifact weight | S03-S18 | Keep representative evidence and contact sheets; avoid bulky raw dumps unless they materially support the spec. | Yes before publication |
| Brand guide PDF generation | Derived | Markdown/HTML guide are enough for first local pass; PDF can be generated later if useful. | Optional |

## 17. Review Checklist

- [x] Source inventory created from official public sources
- [x] Major rules cite source families
- [x] Confidence/provisional labels assigned with polished language
- [x] Open decisions preserved without weak public-facing phrasing
- [x] No third-party coverage used as brand evidence
- [x] Generator-embedded brand rules reviewed and elevated where portable
- [ ] Owner/reviewer reviewed and corrected
- [ ] Full media kit reviewed if/when available

## 18. Version History

| Version | Date | Change | Reviewer |
|---|---|---|---|
| 0.3 | 2026-05-21 | Added portability revision: operational generation rules, asset-type decision tree, promptable recipes, market imagery mapping, content archetypes, evidence labels, and portability test | pending owner review |
| 0.2 | 2026-05-21 | Corrected social-template direction and generator-facing rules after official social sample review | pending owner review |
| 0.1 | 2026-05-21 | First-pass Ostium brand spec from official public sources | pending owner review |
