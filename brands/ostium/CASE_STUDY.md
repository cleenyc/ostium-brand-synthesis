# Ostium Brand Synthesis Case Study

## 1. Project context

This repo adapts a source-grounded `brand.md` synthesis workflow to Ostium. The goal is not to produce a generic design mood board. The goal is to convert current official Ostium source material into an auditable creative operating spec that downstream agents and scripts can use without inventing unsupported brand rules.

## 2. Research challenge

The first-pass source set is intentionally scoped to current official public material:

- official website and Webflow/CSS assets exist;
- official docs provide strong product and infrastructure claims;
- public app/product surfaces show UI behavior but may be jurisdiction-gated;
- official X/Twitter provides active social voice, metrics-led trade proof, and visual/video examples;
- the website links to an official media kit, but complete media-kit rules were not incorporated in this first pass;
- exact logo clearspace, min-size, and font licensing remain open decisions.

The synthesis challenge is to create a strong first-pass spec while labeling provisional rules cleanly and preserving a path for future official resources.

## 3. Source set

| Source area | Repo artifact | Role |
|---|---|---|
| Website / homepage | `brands/ostium/resources/website/` | Positioning, visuals, CSS-derived tokens, official assets |
| Docs | `brands/ostium/resources/docs/` | Product facts, protocol terminology, architecture, claims |
| App/product UI | `brands/ostium/resources/app/` and website UI frame | Trading-terminal visual language and product proof |
| Official X/Twitter | `brands/ostium/resources/x/` | Voice, social proof patterns, high-signal images/videos |
| Source inventory | `brands/ostium/source-inventory.md` | Authority hierarchy and source IDs |
| Visual synthesis | `brands/ostium/notes/visual-synthesis-analysis.md` | Cross-source visual/motion rules |
| Social writing | `brands/ostium/notes/social-writing-analysis.md` | Copy voice and social content grammar |
| Final spec | `brands/ostium/brand.md` | Canonical structured Ostium spec inside this repo |

## 4. Method

The build followed the reusable `docs/brand-md-workflow/` process:

1. **Intake** — collect current official website, docs, app, assets, and X/Twitter evidence.
2. **Source inventory** — assign source IDs and authority levels.
3. **Explicit extraction** — capture stated product claims and positioning from website/docs.
4. **Visual observation** — analyze website assets, product UI, social images, and video contact sheets.
5. **Voice analysis** — analyze official X copy for hooks, cadence, proof structure, and avoid-list.
6. **Synthesis** — convert evidence into source-backed and provisional creative rules.
7. **Spec writing** — write `brand.md` using the evidence-backed template.
8. **Downstream proof** — generate a deterministic SVG/PNG asset from the spec.

## 5. Example transformation

Raw observation:

> Official UI and social posts repeatedly show exact market metrics: open interest, volume, notional size, slippage, price impact, settlement, and liquidation details.

Synthesized rule:

> Ostium creative should use product proof and exact market mechanics instead of generic finance hype.

Spec output:

> `brand.md` → Copy / Voice and Generation Constraints → evidence S04, S06, S15-S17 → confidence high.

This pattern is the core of the repo: observed evidence becomes a sourced, confidence-rated creative rule.

## 6. Key brand conclusions

High-confidence or medium-high-confidence outputs:

- Ostium should feel like a serious, liquid, global-market trading infrastructure brand.
- The visual system is dark/charcoal with a vivid orange identity/action accent.
- Product UI should preserve dense trader-native mechanics rather than hiding complexity.
- Green/red are market semantics, not general brand decoration.
- Copy should be concise, proof-led, product-native, and exact about assets/execution.
- Social assets can lean on record-sized trades, liquidity routing, and institutional milestones.
- Motion/video can use direct talking-head education with bold caption emphasis.

## 7. What remains provisional

The spec intentionally does not invent:

- formal logo clearspace rules;
- exact minimum logo size;
- final production font licensing;
- complete media-kit usage rules;
- full motion system beyond selected official X videos;
- public redistribution policy for every raw source artifact.

These are labeled as open decisions or provisional rules in `brand.md`, keeping the public spec polished while preserving review paths.

## 8. Downstream test

The prototype script `scripts/brand_svg_asset.py` reads `brands/ostium/brand.md` and optional guide files, extracts usable palette constraints, and generates SVG/PNG output.

This demonstrates the downstream value of the spec: once Ostium is represented as evidence-backed constraints, a tool can generate directionally on-brand assets while avoiding unsupported claims or fake official details.

## 9. Why this is reusable

Ostium is one worked example, but the workflow is brand-agnostic. For another brand, an agent should:

1. start with `docs/brand-md-workflow/workflow.md`,
2. collect references using `intake-checklist.md`,
3. analyze sources using `analysis-prompts.md`,
4. write the spec with `template.md`,
5. preserve evidence IDs, authority, confidence, open decisions, and provenance.

The reusable artifact is not an Ostium-specific renderer. It is the source-grounded `brand.md` synthesis method.
