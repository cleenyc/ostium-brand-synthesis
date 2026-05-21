---
name: ostium-brand-asset-generator
description: Generate constrained Ostium-style SVG/PNG assets from the source-grounded Ostium brand.md spec.
version: 0.2.0
author: Chris Lee
license: MIT
---

# Ostium Brand Asset Generator

Use this skill when you need to generate a deterministic static asset using the Ostium brand synthesis package in this repo.

## Required reading

1. `brands/ostium/brand.md`
2. `brands/ostium/source-inventory.md`
3. `docs/EVIDENCE_TRACEABILITY_MATRIX.md`
4. `docs/BRAND_PROVENANCE.md`

## Rules

1. Treat `brand.md` as the operating spec.
2. Use official source IDs and confidence labels when explaining why an asset is on-brand.
3. Do not invent official logo rules, font licensing, partner claims, trading-performance claims, or market data.
4. Keep output product-led: global markets, liquidity, transparent settlement, self-custody, execution, and exact sourced proof when available.
5. Use one of the Ostium-native social templates: campaign banner, cost breakdown, trade result/proof, product-position overlay, or briefing card.
6. Use orange as atmosphere/brand heat; keep green/red for market semantics.
7. Enforce safe-area text wrapping/scaling. Headlines must not run near an edge.
8. Avoid generic abstract launch-card geometry, generic crypto neon, token piles, moon/rocket memes, blue-purple SaaS gradients, internal/process proof text, and unsupported hype.

## Examples

Campaign banner:

```bash
python3 scripts/brand_svg_asset.py \
  --brand-dir ./brands/ostium \
  --template campaign-banner \
  --headline "Silicon Week" \
  --subhead "2x Points This Week" \
  --background-theme "silicon chips gpu servers" \
  --icons "NVDA,AMD,MU,ARM,BTC" \
  --out ./outputs/ostium-silicon-week-v5.png
```

Cost breakdown:

```bash
python3 scripts/brand_svg_asset.py \
  --brand-dir ./brands/ostium \
  --template cost-breakdown \
  --position-size '$9,699,990' \
  --market NDX/USD \
  --direction Long \
  --leverage 100x \
  --total-cost '$3,074.9' \
  --out ./outputs/ostium-cost-breakdown-v5.png
```

## Review checklist

- Asset uses an Ostium-native social template, not a generic abstract brand poster.
- Text wraps/scales within safe margins.
- Asset uses dark/charcoal foundation and orange atmosphere/accent.
- Copy is concise, product-led, and source-grounded.
- No unsupported financial performance claims.
- No invented partner/endorsement claims.
- SVG and PNG were generated locally.
