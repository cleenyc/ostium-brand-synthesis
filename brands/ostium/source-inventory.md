# Ostium Source Inventory

Version: 0.2
Date: 2026-05-21
Status: current official public surfaces plus owner-provided official social samples for generator correction and portability review

## Source policy

This inventory uses only official Ostium-owned public surfaces for v1. It does not use third-party coverage, third-party screenshots, or the prior Ostium Social Volatility Research Kit as brand evidence. The owner/reviewer may add more official resources later; this inventory is designed to accept additional source IDs without rewriting the method.

## Authority hierarchy

1. **Official brand/product surfaces** — official website, app/product UI, official assets and media kit links.
2. **Official documentation** — docs pages and llms exports for product/infrastructure claims and terminology.
3. **Official X/Twitter** — verified account voice, social proof patterns, visual/video grammar, and public market-facing phrasing.
4. **Derived local notes** — contact sheets, source extraction notes, visual synthesis, and writing analysis produced from the above.

If sources conflict, explicit product/docs claims outrank social copy. Visual rules should be treated as source-backed when they recur across official website/app/social assets, and as observed when they appear strongly in one source family.

## Sources

| ID | Source | Type | URL / local artifact | Authority | Notes |
|---|---|---|---|---|---|
| S01 | Ostium homepage | Website / positioning | https://www.ostium.com/; `brands/ostium/resources/website/homepage.html` | Primary | Hero, positioning, CTAs, footer copy, official brand visuals. |
| S02 | Ostium homepage CSS extract | Website / visual tokens | `brands/ostium/resources/website/homepage-css-extract.md` | Primary | Selected official CSS evidence for observed font-family names and color values; full raw CSS is not packaged in this pass. |
| S03 | Homepage OG image | Official visual asset | `brands/ostium/resources/website/og-image.png` | Primary | Cinematic dark/copper brand image with logo/wordmark and gateway-like motif. |
| S04 | Website product UI frame | Official product visual | `brands/ostium/resources/website/product-ui-frame.png` | Primary | High-density trading UI screenshot used for product visual language. |
| S05 | Boxed logo SVG | Official logo asset | `brands/ostium/resources/website/boxed-logo.svg` | Primary | Publicly downloadable website logo mark/wordmark asset. |
| S06 | App product surface | Public app UI | https://app.ostium.com/trade?restricted=true&from=SPX&to=USD; `brands/ostium/resources/app/*` | Primary | Restricted-jurisdiction banner appeared, but UI metadata/assets and product layout were observable. |
| S07 | Docs welcome | Documentation | https://docs.ostium.com/traders/welcome.md; local copy | Primary | Product positioning, asset classes, leverage, settlement, transparency. |
| S08 | Protocol: how Ostium works | Documentation | https://docs.ostium.com/protocol/how-ostium-works.md; local copy | Primary | Settlement/hedging architecture and infrastructure language. |
| S09 | Markets reference | Documentation | https://docs.ostium.com/traders/reference/markets.md; local copy | Primary | Market breadth, leverage ranges, fees, traditional/crypto market-hour distinction. |
| S10 | Fees reference | Documentation | https://docs.ostium.com/traders/reference/fees.md; local copy | Primary | Opening/oracle/rollover/liquidation fee framing. |
| S11 | Connect account | Documentation | https://docs.ostium.com/traders/getting-started/connect-account.md; local copy | Primary | Email smart account and Web3 wallet onboarding, non-custodial framing. |
| S12 | Builder API overview | Documentation | https://docs.ostium.com/developer/builder-api/overview.md; local copy | Primary | Developer endpoint surface and API positioning. |
| S13 | Docs llms exports | Documentation bundle | https://docs.ostium.com/llms.txt and `/llms-full.txt`; local copies | Primary | Broad docs corpus for terminology and claims. |
| S14 | Official X account profile | Social identity | https://x.com/Ostium; `brands/ostium/resources/x/ostium_x_profile_full.json` | Primary social | Verified business account metadata, bio, website, pinned tweet. |
| S15 | Recent official X posts | Social voice/content | `brands/ostium/resources/x/ostium_x_findings.md` | Primary social | Curated read-only digest of recent post text, metrics, and media candidates from the official account. |
| S16 | Nasdaq partnership visual | Social visual | https://x.com/Ostium/status/2056388734283911442; local image | Primary social | Institutional credibility, orange billboard, concise headline. |
| S17 | Large-trade proof visuals | Social visual | local `largest-us100-long.jpg`, `largest-oil-trade.jpg`, `no-funding-rates.jpg` | Primary social | Metrics-led trade proof, liquidity/execution framing. |
| S18 | X video contact sheets | Social video | local contact sheets from official X MP4s | Primary social | Talking-head caption grammar and liquidity-routing explainer style. |
| S19 | Blog index | Owned content | https://www.ostium.com/blog | Primary/owned | Market Outlook format and editorial trader voice; individual posts not deeply ingested in this pass. |
| S20 | Media Kit link | Official linked asset pack | Google Drive link observed from website footer | Primary but not downloaded | Official `Ostium Media Kit.zip` exists; add as future source if provided/downloaded for public packaging review. |
| S21 | Owner-provided recent official social samples | Social visual reference set | `brands/ostium/resources/owner-provided/recent-social-samples/*` | Primary social / owner-provided | Seven recent Ostium-posted assets supplied by the owner/reviewer to correct the generator: campaign banners, cost breakdown, trade proof, position overlays, and briefing card. Review redistribution before public release. |

## Access notes

- `ostium.io` redirects to `https://www.ostium.com/`.
- `docs.ostium.com` is the working docs host. `docs.ostium.io` did not resolve during source gathering.
- `app.ostium.com` loaded but showed a restricted-jurisdiction banner. Public UI metadata and static assets remained useful for visual analysis.
- `trade.ostium.com` and `blog.ostium.com` returned TLS/525 errors during discovery; `www.ostium.com/blog` loaded as owned blog surface.

## Local artifact policy

The repo includes representative artifacts for auditability: website/docs snapshots, official asset images/SVGs, official X export files, selected social images, owner-provided recent social samples, and contact sheets for official video posts. Full raw video and owner-provided social samples should remain curated rather than dumped broadly; include only assets/contact sheets that materially support visual or motion rules and review redistribution before public release.
