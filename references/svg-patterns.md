# SVG Asset Patterns

Use these patterns when hand-coding deterministic brand graphics.

## Square launch/social graphic

- Canvas: `1080x1080`.
- Background: brand light neutral or dark neutral.
- Frame: subtle 1–2px border at 48–64px inset when the brand uses editorial restraint.
- Top metadata: brand name left, campaign/context right.
- Main headline: centered or left-aligned with generous whitespace.
- Supporting line: one short line near bottom or under headline.
- Brand energy: use gradients/motifs around edges or behind empty space; keep the headline field clean.

## Common structure

```svg
<svg width="1080" height="1080" viewBox="0 0 1080 1080" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="heat" ...>...</linearGradient>
    <filter id="blur">...</filter>
  </defs>
  <rect width="1080" height="1080" fill="#FDFCF8"/>
  <!-- background energy away from headline -->
  <!-- content panel/headline -->
</svg>
```

## Legibility rule

Do not place abstract marks, gradients, contour lines, or UI details directly behind headline text unless opacity is very low and contrast remains excellent. Prefer a clean panel or clear negative space behind primary copy.

## Crypto/DeFi anti-patterns

Avoid: blue-purple gradients, holographic coins, neon grids, lasers, token piles, fantasy mascots, trading candles as decoration, excessive glitch, fake metrics, fake product screenshots.
