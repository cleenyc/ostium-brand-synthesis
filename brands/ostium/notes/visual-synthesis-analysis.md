# Ostium Visual Synthesis Analysis

Date: 2026-05-21
Sources: S01-S06, S16-S18

## Core visual thesis

Ostium's visual system combines three modes:

1. **Cinematic gateway identity** — dark landscapes, copper/orange glow, sparse monumental logo/wordmark.
2. **Dense trading terminal** — black/charcoal UI, market tables, candlesticks, order ticket, green/red semantics.
3. **Social proof assets** — orange/black announcement graphics, exact trade metrics, founder/operator video clips with bold captions.

The system should not be reduced to generic orange-on-black crypto design. Its stronger pattern is **precision market infrastructure with a warm gateway accent**.

## Palette

Observed recurring roles:

- Near-black / charcoal foundation: `#080909`, `#0C0C0D`, `#111111`, `#151515`, `#222222`.
- Brand orange: `#FF5A19` / `#FF5A1F` range.
- Deep red-brown / copper: `#9E200E`, `#450B05`, burnt umber gradients.
- Off-white/beige: `#FFE8E2`, soft white logo/text.
- Muted pale gray/green-gray: `#D0DBDA`, UI labels and secondary text.
- Market green/red: green for long/profit/up; red/pink for short/loss/down.

Rule: orange is brand energy/action; green/red remain market semantics.

## Typography

Website CSS references `Ppmori Variable`, `Ttfirsneue`, `IBM Plex Mono`, and `Ppmondwest`; app UI uses `IBM Plex Sans` and `IBM Plex Mono` patterns. Observed behavior:

- uppercase, widely tracked wordmark;
- compact UI labels and data tables;
- tabular/monospace numeric behavior for prices and market data;
- bold uppercase captions for social video;
- condensed uppercase headline treatment for milestone graphics.

## Layout / composition

Use:

- dark spacious hero compositions for identity moments;
- high-density grid/table/card layouts for product proof;
- one dominant proof message per social asset;
- clear separation between brand layer, market semantics, and product mechanics;
- visible metrics and execution details when making product claims.

Avoid:

- generic neon cyberpunk grids;
- random token/coin piles;
- abstract DeFi blobs with no product proof;
- overusing orange where green/red market semantics are needed;
- soft consumer-fintech minimalism that hides trading complexity.

## Motion / video

Observed social video patterns:

- talking-head educational clips;
- burned-in all-caps captions;
- orange/red emphasis words;
- fast caption cadence rather than complex camera motion;
- founder/operator credibility over polished ad production;
- product/infrastructure concepts explained conversationally.

Motion rules:

- Use captions as a primary motion layer.
- Keep key phrases short and readable in-feed.
- Use orange emphasis for semantic anchors, not every word.
- Where product UI is shown, maintain legibility and real market-data grammar.


## Owner-provided recent social samples — generator correction pass

Chris supplied recent official Ostium social examples after the first generated sample looked too close to the exemplar workflow repo and failed text wrapping. The samples sharpen the actual social grammar:

- **Campaign banners:** 16:9/wide, full-bleed macro or technology imagery, heavy black/orange grade, large light-weight headline, smaller muted subtitle, logo bottom-left, icon row bottom-right.
- **Cost breakdown cards:** square/portrait orange-red gradient, top-left logo, question headline with the dollar amount as the largest line, Long/Short pill + pair + leverage row, thin-divider fee table, large rounded total-cost callout.
- **Trade proof cards:** cinematic asset-specific backgrounds; huge notional number; concise market/direction line; black PNL module with green/red semantics; small logo bottom-center.
- **Position overlays:** real trading floor or gritty macro collage background; central black product UI card; one/two position cards with pair, direction/leverage, size, price, price impact, and view-more row; logo bottom-center.
- **Briefing cards:** 4:5 orange/brown gradient, subject/company header, stacked market/positioning/trade/promo sections, thin dividers, bottom-center Ostium signature.

Correction to generator requirements:

- Generated examples must use one of the Ostium-native social templates, not a generic abstract brand poster.
- Headline and subtitle layout must enforce max width, wrapping, and dynamic font sizing.
- Logo must be restrained and placed according to template, not used as a dominant centerpiece.
- Public example copy should be externally legible and should not include internal phrases like “source-grounded spec.”
