# Ostium Brand Spec Portability Test

Date: 2026-05-21

## Purpose

Validate whether `brands/ostium/brand.md` can guide a new Ostium-branded asset outside the current deterministic SVG generator templates.

## Method

A downstream agent was given only:

1. `brands/ostium/brand.md`
2. `brands/ostium/source-inventory.md`
3. `docs/BRAND_PROVENANCE.md`
4. `docs/EVIDENCE_TRACEABILITY_MATRIX.md`

The agent was explicitly not given `scripts/brand_svg_asset.py` or existing generated outputs.

## Unsupported asset type tested

Ostium-branded conference booth backdrop.

## Result

**Pass with minor production gaps.**

The spec provided enough portable brand intelligence to construct a credible unsupported asset concept without relying on hidden generator coordinates, existing output examples, or deterministic template defaults.

## Proposed asset concept

A 10ft x 8ft conference booth backdrop for a crypto/trading/infrastructure event.

Core message:

> Onchain Access to Global Markets

Visual direction:

- dark/charcoal booth wall with warm orange/copper atmospheric glow;
- restrained Ostium logo/wordmark as a signature, not the hero;
- hero emphasis on product/trading-terminal proof module;
- supporting copy around self-custody, USDC settlement, and markets spanning stocks, commodities, forex, indices, and crypto;
- no unsupported partner, performance, or institutional claims.

## Downstream prompt/spec

Create a premium conference booth backdrop for Ostium, an onchain gateway to global markets.

Format: wide physical event-booth wall, approximately 10ft x 8ft, viewed straight-on with slight perspective.

Visual style:

- Dark black/charcoal foundation with subtle copper and burnt-orange atmospheric gradient.
- Serious, institutional, trader-native, execution-focused.
- Avoid playful crypto, neon cyberpunk, coin piles, mascots, rockets, or generic SaaS blue/purple gradients.

Composition:

- One dominant headline in clean modern sans-serif type: “Onchain Access to Global Markets”.
- Use short, confident, high-contrast typography.
- Keep headline large but safely inset from edges.
- Place a small white Ostium wordmark/logo as a restrained signature near the upper-left or lower-left.
- Do not make the logo the main focal object.
- Center/right area should feature a credible trading-terminal/product UI module:
  - dark near-black cards;
  - subtle borders;
  - compact labels;
  - chart panel;
  - market rows for stocks, commodities, forex, indices, crypto;
  - tabular numerals;
  - green only for long/up/profit/success;
  - red/pink only for short/down/loss/risk;
  - orange only for brand/action/accent/atmosphere.
- Include a concise supporting line: “Trade perpetual exposure across stocks, commodities, forex, indices, and crypto — settled in USDC.”
- Optional small proof/feature chips: “Self-custodial”, “Transparent”, “Real market liquidity”, “USDC settlement”.
- Treat all UI values as demo/synthetic unless sourced; avoid exact performance claims.

Imagery:

- Use abstracted but market-specific background texture: terminal screens, chart grids, macro-market panels, commodity/equity/forex references.
- Avoid third-party logos, fake endorsements, real exchange logos, or unsupported partner claims.

Overall feel:

- Premium, dark, precise, data-dense, orange-accented, global, infrastructure-grade.

## What `brand.md` made clear

- Positioning: Ostium should be framed as an onchain gateway to global markets.
- Tone: serious, precise, trader-native, infrastructure-grade, proof-led.
- Color system: black/charcoal base, orange as brand/action/atmosphere, green/red reserved for market semantics.
- Typography behavior: clean sans-serif for headlines, tabular/mono numerals for data.
- Layout behavior: product/proof surfaces should show dense trading UI rather than vague finance abstraction.
- Logo behavior: restrained signature placement; avoid making the logo the hero unless the asset is explicitly a lockup piece.
- Imagery rules: use market/product-specific context, not generic crypto visuals.
- Claim discipline: avoid unsupported performance, partner, or investment claims.
- Portability guidance: Section 14 supports unsupported new asset types by constructing from principles.

## Ambiguities / remaining gaps

- Physical booth-specific guidance: large-format viewing distance, environmental mockups, and booth hierarchy are not yet explicit.
- Logo production specs: clearspace, minimum size, and formal media-kit rules remain open decisions.
- Exact typefaces: font behavior is clear, but production font stack/licensing remains provisional.
- Large-format copy density: the spec emphasizes dense product proof, while booth signage requires distance-readable simplification.
- Compliance/event-context guidance: no explicit rules for conference/event disclaimers, jurisdictional limits, or booth collateral claims.
- Product screenshot realism: the spec says UI should look real and credible, but exact demo-data policy remains lightweight.

## Assessment

The portability test supports the claim that `brand.md` is now operational beyond the current deterministic social-template generator. The remaining gaps are production-context details, not core brand intelligence failures.
