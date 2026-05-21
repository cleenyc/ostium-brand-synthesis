# Ostium Brand Provenance

This document explains how `brands/ostium/brand.md` was generated, what source artifacts support it, and which rules remain provisional for future review.

## Outcome files

- `brands/ostium/source-inventory.md` — official source map and authority hierarchy.
- `brands/ostium/brand.md` — canonical structured Ostium spec within this repo.
- `brands/ostium/notes/source-extraction-summary.md` — extraction notes across website/docs/app/social.
- `brands/ostium/notes/social-writing-analysis.md` — official X voice and content patterns.
- `brands/ostium/notes/visual-synthesis-analysis.md` — visual and motion synthesis.
- `docs/EVIDENCE_TRACEABILITY_MATRIX.md` — selected final rules mapped to source evidence.
- `docs/PORTABILITY_TEST.md` — generator-independent test showing how `brand.md` guides an unsupported asset type without using the deterministic renderer or existing outputs.
- `outputs/ostium-cost-breakdown-v5.svg/png`, `outputs/ostium-silicon-week-v5.svg/png`, `outputs/ostium-wti-proof-v5.svg/png`, `outputs/ostium-position-overlay-v5.svg/png`, `outputs/ostium-hot-print-v5.svg/png`, and `outputs/ostium-briefing-v5.svg/png` — deterministic downstream proofs generated from the corrected social-template spec.

## Source hierarchy

1. Official website and product/app assets.
2. Official documentation and docs exports.
3. Official verified X/Twitter account and owned social media.
4. Derived local source notes and contact sheets.

No third-party coverage or screenshots were used as brand evidence. The prior Ostium Social Volatility Research Kit was intentionally excluded from brand synthesis evidence because it is narrower than this project.

## Generation process

1. Mirrored the source-grounded exemplar repo's method and structure.
2. Rebuilt the source inventory around official Ostium surfaces.
3. Downloaded representative official website/docs/assets/social artifacts for auditability.
4. Extracted product positioning, product claims, voice patterns, visual tokens, and UI behaviors.
5. Converted repeated evidence into confidence/provenance-labeled creative rules.
6. Wrote `brand.md` as a strong first-pass spec with polished provisional labels.
7. Rebuilt a deterministic SVG/PNG generator as a downstream proof consumer.
8. Added portability rules to `brand.md` so unsupported new asset types can be constructed from principles rather than hidden generator defaults.
9. Ran a generator-independent portability test and hygiene checks before review.

## Strongest source-backed areas

- Positioning: onchain gateway to global markets.
- Product scope: stocks, ETFs, commodities, indices, forex, crypto; USDC settlement; self-custody; transparency.
- Visual palette: dark/charcoal foundation, orange brand accent, off-white text, green/red market semantics.
- Product UI language: dense trading terminal, chart/order-ticket/table grid, execution/risk proof.
- Social voice: exact notional proof, liquidity/execution language, market-native timing.

## Provisional / open-decision areas

- Formal logo clearspace, minimum size, and complete media-kit usage rules.
- Exact production font licensing and final type tokens.
- Full motion system beyond selected official X videos.
- Whether to package full raw videos or only contact sheets/selected frames in the public repo.

## External-agent use

A downstream agent should start with:

1. `brands/ostium/brand.md`
2. `brands/ostium/source-inventory.md`
3. `docs/EVIDENCE_TRACEABILITY_MATRIX.md`
4. `brands/ostium/notes/visual-synthesis-analysis.md`
5. `brands/ostium/notes/social-writing-analysis.md`
6. Representative artifacts under `brands/ostium/resources/`
7. `docs/PORTABILITY_TEST.md` when evaluating whether the spec generalizes beyond supported templates

Do not invent official logo rules, font licensing, partnership claims, trading-performance claims, or public asset usage rights. If an output depends on open decisions, label it as directional/provisional and route it for review.
