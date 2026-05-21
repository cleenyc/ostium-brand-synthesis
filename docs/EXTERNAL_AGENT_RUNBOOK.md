# External Agent Runbook: Ostium Brand Synthesis

This runbook tells an external agent how to use the Ostium brand synthesis package without drifting from the source-grounded workflow.

## Read first

1. `brands/ostium/brand.md`
2. `brands/ostium/source-inventory.md`
3. `docs/BRAND_PROVENANCE.md`
4. `docs/EVIDENCE_TRACEABILITY_MATRIX.md`
5. `brands/ostium/notes/visual-synthesis-analysis.md`
6. `brands/ostium/notes/social-writing-analysis.md`

## Core constraints

- Use only official/source-approved evidence.
- Do not invent official logo clearspace, minimum size, exact production font licensing, or partner claims.
- Do not make investment advice or unsupported performance claims.
- Treat open decisions in `brand.md` as review items.
- Use source IDs when making brand-rule claims.

## Asset generation

Run:

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

The script emits both SVG and PNG.

## Good output should feel

- template-specific rather than generic abstract launch art;
- dark and precise;
- orange as atmosphere/brand heat, while green/red remain market semantics;
- trader-native;
- global-market oriented;
- execution/proof led;
- safe-wrapped inside social-card margins;
- careful about claims.

## Stop conditions

Stop and request review if asked to:

- publish or push the repo;
- use third-party brand evidence;
- use unreconciled private sources;
- claim official endorsement;
- make a trading/investment recommendation;
- formalize logo/font rules without the full media kit.
