#!/usr/bin/env python3
"""Generate deterministic Ostium-style SVG + PNG social assets.

This is a downstream proof that `brands/ostium/brand.md` can constrain asset
generation. It intentionally uses local SVG + headless Chromium only.

The generator is template-based because current official Ostium social assets are
not generic abstract brand posters. They cluster into market-event and
trade-proof formats: campaign banners, cost breakdowns, trade-result cards,
product-position overlays, and earnings/market briefings.
"""
from __future__ import annotations

import argparse
import html
import math
import re
import subprocess
import tempfile
from pathlib import Path

DEFAULT = {
    "ink": "#050403",
    "panel": "#080808",
    "panel2": "#111111",
    "paper": "#FFF0E8",
    "white": "#FFFFFF",
    "muted": "#CFC5C0",
    "muted2": "#8E8782",
    "orange": "#FF5A19",
    "burnt": "#C43B12",
    "copper": "#8A3518",
    "deep": "#2B130C",
    "green": "#16D47B",
    "red": "#F04444",
    "red_bg": "#3A0D12",
    "green_bg": "#073B24",
}


def read_sources(brand_dir: Path) -> str:
    chunks: list[str] = []
    for rel in ["brand.md", "brand-guide.md"]:
        p = brand_dir / rel
        if p.exists():
            chunks.append(p.read_text(encoding="utf-8", errors="ignore"))
    guide_dir = brand_dir / "brand-guide"
    if guide_dir.exists():
        for p in sorted(guide_dir.glob("*.md"))[:3]:
            chunks.append(p.read_text(encoding="utf-8", errors="ignore"))
    return "\n\n".join(chunks)


def extract_hexes(text: str) -> dict[str, str]:
    colors = DEFAULT.copy()
    found = list(dict.fromkeys(re.findall(r"#[0-9A-Fa-f]{6}", text)))

    def rgb(c: str) -> tuple[int, int, int]:
        return int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)

    darks = [c for c in found if max(rgb(c)) < 40]
    lights = [c for c in found if min(rgb(c)) > 200]
    oranges = [c for c in found if rgb(c)[0] > 200 and 45 <= rgb(c)[1] <= 125 and rgb(c)[2] < 70]
    coppers = [c for c in found if rgb(c)[0] > 100 and rgb(c)[1] < 80 and rgb(c)[2] < 60]
    muted = [c for c in found if abs(rgb(c)[0] - rgb(c)[1]) < 28 and rgb(c)[0] > 150 and rgb(c)[2] > 130]
    if darks:
        colors["ink"] = darks[0]
    if len(darks) > 1:
        colors["panel"] = darks[1]
    if lights:
        colors["paper"] = lights[0]
    if muted:
        colors["muted"] = muted[0]
    if oranges:
        colors["orange"] = oranges[0]
    if coppers:
        colors["copper"] = coppers[0]
    return colors


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def num(s: str, fallback: str = "") -> str:
    return s.strip() if s and s.strip() else fallback


def wrap_words(text: str, max_chars: int, max_lines: int = 3) -> list[str]:
    text = " ".join(text.strip().split())
    if not text:
        return []
    words = text.split()
    lines: list[str] = []
    cur: list[str] = []
    for w in words:
        candidate = " ".join(cur + [w])
        if cur and len(candidate) > max_chars:
            lines.append(" ".join(cur))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(" ".join(cur))
    if len(lines) > max_lines:
        kept = lines[: max_lines - 1]
        rest = " ".join(lines[max_lines - 1 :])
        kept.append(rest)
        lines = kept
    return lines


def fit_font(text: str, max_width: float, starting: float, minimum: float, weight_factor: float = 0.56) -> float:
    longest = max([len(line) for line in text.split("\n")] or [1])
    size = starting
    while size > minimum and longest * size * weight_factor > max_width:
        size -= 2
    return size


def text_block(
    text: str,
    x: float,
    y: float,
    max_width: float,
    font_size: float,
    min_size: float,
    fill: str,
    weight: int | str = 400,
    anchor: str = "start",
    max_lines: int = 3,
    line_height: float = 1.08,
    opacity: float = 1.0,
    letter_spacing: float = 0,
    chars_factor: float = 0.56,
) -> tuple[str, float]:
    max_chars = max(6, int(max_width / (font_size * chars_factor)))
    lines = wrap_words(text, max_chars=max_chars, max_lines=max_lines)
    joined = "\n".join(lines)
    fitted = fit_font(joined, max_width=max_width, starting=font_size, minimum=min_size, weight_factor=chars_factor)
    max_chars = max(6, int(max_width / (fitted * chars_factor)))
    lines = wrap_words(text, max_chars=max_chars, max_lines=max_lines)
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else fitted * line_height
        tspans.append(f'<tspan x="{x:.1f}" dy="{dy:.1f}">{esc(line)}</tspan>')
    height = fitted * (1 + max(0, len(lines) - 1) * line_height)
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{fill}" opacity="{opacity}" '
        f'font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{fitted:.1f}" '
        f'font-weight="{weight}" letter-spacing="{letter_spacing}">{"".join(tspans)}</text>',
        height,
    )


def ostium_logo(x: float, y: float, width: float, colors: dict[str, str], anchor: str = "start", opacity: float = 1.0) -> str:
    # Deterministic approximation of the white Ostium mark + spaced wordmark.
    mark_w = width * 0.18
    word_size = width * 0.118
    if anchor == "middle":
        x = x - width / 2
    return f'''
  <g transform="translate({x:.1f},{y:.1f})" opacity="{opacity}">
    <path d="M0 0 C{mark_w*0.22:.1f} {mark_w*0.08:.1f} {mark_w*0.22:.1f} {mark_w*0.92:.1f} 0 {mark_w:.1f} M{mark_w*0.48:.1f} 0 L{mark_w*0.48:.1f} {mark_w:.1f} M{mark_w:.1f} 0 C{mark_w*0.78:.1f} {mark_w*0.08:.1f} {mark_w*0.78:.1f} {mark_w*0.92:.1f} {mark_w:.1f} {mark_w:.1f}" fill="none" stroke="{colors['white']}" stroke-width="{max(1.5, width*0.018):.1f}" stroke-linecap="round"/>
    <text x="{mark_w*1.35:.1f}" y="{mark_w*0.78:.1f}" fill="{colors['white']}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{word_size:.1f}" font-weight="600" letter-spacing="{word_size*0.28:.1f}">OSTIUM</text>
  </g>'''


def defs(colors: dict[str, str]) -> str:
    return f'''
  <defs>
    <radialGradient id="warmGlow" cx="82%" cy="18%" r="78%">
      <stop offset="0" stop-color="{colors['orange']}" stop-opacity="0.52"/>
      <stop offset="0.42" stop-color="{colors['copper']}" stop-opacity="0.26"/>
      <stop offset="1" stop-color="{colors['ink']}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="orangeField" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#4B1608"/>
      <stop offset="0.48" stop-color="#B8320D"/>
      <stop offset="1" stop-color="#E24B12"/>
    </linearGradient>
    <linearGradient id="darkToOrange" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#000000" stop-opacity="0.96"/>
      <stop offset="0.55" stop-color="#160804" stop-opacity="0.82"/>
      <stop offset="1" stop-color="{colors['burnt']}" stop-opacity="0.58"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="18" stdDeviation="24" flood-color="#000" flood-opacity="0.55"/></filter>
    <filter id="softBlur"><feGaussianBlur stdDeviation="10"/></filter>
    <pattern id="grain" width="64" height="64" patternUnits="userSpaceOnUse">
      <circle cx="7" cy="9" r="1" fill="#fff" opacity="0.10"/><circle cx="29" cy="18" r="1.2" fill="#fff" opacity="0.06"/><circle cx="51" cy="42" r="1" fill="#000" opacity="0.18"/><circle cx="17" cy="55" r="0.8" fill="#fff" opacity="0.08"/>
    </pattern>
  </defs>'''


def svg_open(w: int, h: int, colors: dict[str, str]) -> str:
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">\n{defs(colors)}\n'


def svg_close() -> str:
    return "\n</svg>\n"


def abstract_market_background(w: int, h: int, colors: dict[str, str], theme: str = "macro") -> str:
    # Stylized, rights-safe stand-in for market/event imagery.
    theme = theme.lower()
    elements = [f'<rect width="{w}" height="{h}" fill="{colors["ink"]}"/>']
    elements.append(f'<rect width="{w}" height="{h}" fill="url(#darkToOrange)"/>')
    elements.append(f'<rect width="{w}" height="{h}" fill="url(#grain)" opacity="0.38"/>')
    if any(t in theme for t in ["silicon", "chip", "nvidia", "gpu", "server"]):
        # GPU/server rack silhouettes.
        for i in range(5):
            x = w * (0.38 + i * 0.115)
            y = h * 0.58 + (i % 2) * h * 0.035
            elements.append(f'<g opacity="0.34" transform="translate({x:.1f},{y:.1f}) rotate({-7+i*2})"><rect x="0" y="0" width="{w*0.16:.1f}" height="{h*0.28:.1f}" rx="10" fill="#D6CCC8"/><rect x="{w*0.02:.1f}" y="{h*0.035:.1f}" width="{w*0.12:.1f}" height="{h*0.20:.1f}" fill="#24110B" opacity="0.85"/><g opacity="0.5">' + ''.join(f'<line x1="{w*0.035 + k*w*0.02:.1f}" y1="{h*0.05:.1f}" x2="{w*0.035 + k*w*0.02:.1f}" y2="{h*0.225:.1f}" stroke="#E7D8CE" stroke-width="2"/>' for k in range(5)) + '</g></g>')
        elements.append(f'<circle cx="{w*0.55:.1f}" cy="{h*0.23:.1f}" r="{h*0.15:.1f}" fill="#111" opacity="0.34"/>')
    elif any(t in theme for t in ["cpi", "print", "macro", "inflation"]):
        elements.append(f'<g transform="translate({w*0.56:.1f},{h*0.10:.1f}) rotate(-11)" opacity="0.30"><rect width="{w*0.48:.1f}" height="{h*0.52:.1f}" rx="8" fill="#F2E8DE"/><text x="{w*0.035:.1f}" y="{h*0.08:.1f}" fill="#190904" font-size="{h*0.035:.1f}" font-weight="700">Consumer prices</text>' + ''.join(f'<rect x="{w*0.04:.1f}" y="{h*(0.13+i*0.055):.1f}" width="{w*(0.18+0.035*i):.1f}" height="{h*0.012:.1f}" fill="#2A130C" opacity="0.65"/>' for i in range(7)) + '</g>')
    else:
        # Commodity/liquid texture.
        for i in range(9):
            y = h * (0.15 + i * 0.09)
            elements.append(f'<path d="M{-w*0.08:.1f} {y:.1f} C {w*0.18:.1f} {y-h*0.13:.1f}, {w*0.36:.1f} {y+h*0.15:.1f}, {w*0.58:.1f} {y:.1f} S {w*0.92:.1f} {y-h*0.09:.1f}, {w*1.08:.1f} {y+h*0.06:.1f}" fill="none" stroke="{colors["burnt"]}" stroke-width="{h*0.018:.1f}" opacity="{0.16 + (i%3)*0.08:.2f}"/>')
        elements.append(f'<path d="M{w*0.48:.1f} {h*0.50:.1f} l{w*0.20:.1f} {h*0.06:.1f} l{-w*0.04:.1f} {h*0.055:.1f} l{-w*0.22:.1f} {-h*0.05:.1f} z" fill="#E8D6CA" opacity="0.70" transform="rotate(-18 {w*0.58:.1f} {h*0.53:.1f})"/>')
    # Vignette/dark safe zones.
    elements.append(f'<rect width="{w}" height="{h}" fill="url(#warmGlow)"/>')
    elements.append(f'<rect width="{w}" height="{h}" fill="#000" opacity="0.22"/>')
    elements.append(f'<radialGradient id="vig" cx="50%" cy="50%" r="70%"><stop offset="60%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity="0.72"/></radialGradient><rect width="{w}" height="{h}" fill="url(#vig)"/>')
    return "\n".join(elements)


def icon_row(x_right: float, y: float, diameter: float, labels: list[str], colors: dict[str, str]) -> str:
    gap = diameter * 0.18
    start = x_right - len(labels) * diameter - (len(labels) - 1) * gap
    palette = ["#76B900", "#ED1C24", "#0067B1", "#00A6D6", "#F7931A", "#DDB431"]
    out = ['<g>']
    for i, label in enumerate(labels):
        cx = start + diameter / 2 + i * (diameter + gap)
        cy = y
        fill = palette[i % len(palette)]
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{diameter/2:.1f}" fill="{fill}" opacity="0.96"/>')
        fs = diameter * (0.30 if len(label) <= 3 else 0.22)
        out.append(f'<text x="{cx:.1f}" y="{cy+fs*0.32:.1f}" text-anchor="middle" fill="#fff" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{fs:.1f}" font-weight="800">{esc(label[:6])}</text>')
    out.append('</g>')
    return "\n".join(out)



def campaign_banner(args, colors: dict[str, str], w: int, h: int) -> str:
    logo_w = w * 0.150
    campaign_headline = args.headline or "Silicon Week"
    campaign_subhead = args.subhead or "2x Points This Week"
    is_hot = any(t in (campaign_headline + ' ' + args.background_theme).lower() for t in ['hot', 'print', 'cpi', 'inflation'])
    bg_theme = args.background_theme or ('macro print' if is_hot else 'silicon chips gpu servers')
    hx = w * (0.355 if is_hot else 0.50)
    hy = h * 0.445
    headline, hgt = text_block(campaign_headline, hx, hy, w * 0.70, h * 0.136, h * 0.060, colors["paper"], weight=300, anchor="middle", max_lines=2, line_height=1.02, chars_factor=0.50)
    subtitle, _ = text_block(campaign_subhead, hx, hy + hgt + h * 0.075, w * 0.62, h * 0.052, h * 0.030, colors["muted"], weight=300, anchor="middle", max_lines=2, line_height=1.08)
    icons = [s.strip() for s in (args.icons or "NVDA,AMD,MU,ARM,BTC").split(",") if s.strip()]
    # More visible, source-like backdrop accents: Jensen silhouette / CPI document / server racks.
    extra = []
    if is_hot:
        bars = ''.join([f'<rect x="{w*0.04:.1f}" y="{h*(0.15+i*0.058):.1f}" width="{w*(0.20+0.035*(i%4)):.1f}" height="{h*0.011:.1f}" fill="#3A1609" opacity="0.62"/>' for i in range(7)])
        extra.append(f'<g transform="translate({w*0.56:.1f},{h*0.07:.1f}) rotate(9)" opacity="0.18"><rect width="{w*0.40:.1f}" height="{h*0.54:.1f}" rx="14" fill="#F3E1D1"/><text x="{w*0.035:.1f}" y="{h*0.085:.1f}" fill="#260D05" font-size="{h*0.034:.1f}" font-weight="700">Consumer prices rose 0.3%</text>{bars}</g>')
    else:
        extra.append(f'<ellipse cx="{w*0.55:.1f}" cy="{h*0.22:.1f}" rx="{w*0.095:.1f}" ry="{h*0.16:.1f}" fill="#D8C8BB" opacity="0.13"/>')
        for i in range(4):
            x=w*(0.38+i*0.135); y=h*(0.62+(i%2)*0.035)
            extra.append(f'<g opacity="0.24" transform="translate({x:.1f},{y+h*0.035:.1f}) rotate({-8+i*3})"><rect width="{w*0.17:.1f}" height="{h*0.28:.1f}" rx="8" fill="#DCCABE"/><rect x="{w*0.018:.1f}" y="{h*0.035:.1f}" width="{w*0.132:.1f}" height="{h*0.20:.1f}" fill="#170A06" opacity="0.78"/></g>')
    return svg_open(w, h, colors) + abstract_market_background(w, h, colors, bg_theme) + '\n'.join(extra) + f'''
  <rect width="{w}" height="{h}" fill="#000" opacity="0.14"/>
  <ellipse cx="{hx:.1f}" cy="{hy+h*0.060:.1f}" rx="{w*0.31:.1f}" ry="{h*0.18:.1f}" fill="#000" opacity="0.18" filter="url(#softBlur)"/>
  {headline}
  {subtitle}
  {ostium_logo(w*0.050, h*0.850, logo_w, colors)}
  {icon_row(w*0.955, h*0.875, h*0.085, icons[:6], colors)}
''' + svg_close()

def cost_breakdown(args, colors: dict[str, str], w: int, h: int) -> str:
    """Ostium cost-breakdown template tuned to the supplied official reference."""
    margin = w * 0.058
    right = w - margin
    pos = num(args.position_size, "$9,699,990")
    pair = num(args.market, "NDX/USD")
    direction = num(args.direction, "Long").title()
    leverage = num(args.leverage, "100x")
    lines = ["How much does a", pos, "trade cost on Ostium?"] if pos in (args.headline or pos) else wrap_words(args.headline, 18, 3)

    headline_svg = []
    y = h * 0.188
    for i, line in enumerate(lines):
        if i == 1:
            start_fs, minimum, factor, weight = h * 0.099, h * 0.072, 0.505, 850
        else:
            start_fs, minimum, factor, weight = h * 0.061, h * 0.043, 0.505, 650
        fs = fit_font(line, w - margin * 1.85, start_fs, minimum, factor)
        headline_svg.append(
            f'<text x="{margin:.1f}" y="{y:.1f}" fill="{colors["white"]}" '
            f'font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{fs:.1f}" '
            f'font-weight="{weight}" letter-spacing="{-fs*0.035:.1f}">{esc(line)}</text>'
        )
        if i == 0:
            # Cost-breakdown headlines often put a large dollar amount on the
            # second line; give that line enough ascender space so the `$` and
            # first digits do not collide with "How much does a".
            y += fs * 1.62
        elif i == 1:
            y += fs * 0.90
        else:
            y += fs * 1.10

    pill_color = colors["green"] if direction.lower() == "long" else colors["red"]
    pill_bg = colors["green_bg"] if direction.lower() == "long" else colors["red_bg"]
    trade_y = h * 0.432
    table_y = h * 0.512
    row_h = h * 0.073
    rows = [
        ("Position Size", "", pos),
        ("Opening Fee", num(args.opening_fee_pct, "0.03%"), num(args.opening_fee, "$2,910")),
        ("Slippage", num(args.slippage_pct, "0.0017%"), num(args.slippage, "$164.9")),
        ("Closing Fee", num(args.closing_fee_pct, "0.00%"), num(args.closing_fee, "$0")),
        ("Rollover Fee", "", num(args.rollover_fee, "−5.64%/year")),
    ]
    table = []
    for i, (label, pct, value) in enumerate(rows):
        yy = table_y + i * row_h
        fs = h * 0.0245
        table.append(f'<text x="{margin:.1f}" y="{yy:.1f}" fill="{colors["paper"]}" opacity="0.76" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{fs:.1f}" font-weight="300">{esc(label)}</text>')
        if pct:
            table.append(f'<text x="{w*0.575:.1f}" y="{yy:.1f}" text-anchor="middle" fill="{colors["paper"]}" opacity="0.88" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{fs:.1f}" font-weight="300">{esc(pct)}</text>')
        table.append(f'<text x="{right:.1f}" y="{yy:.1f}" text-anchor="end" fill="{colors["paper"]}" opacity="0.88" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{fs:.1f}" font-weight="300">{esc(value)}</text>')
        if i < len(rows)-1:
            table.append(f'<line x1="{margin:.1f}" y1="{yy+h*0.030:.1f}" x2="{right:.1f}" y2="{yy+h*0.030:.1f}" stroke="{colors["paper"]}" stroke-opacity="0.36" stroke-width="1.1"/>')

    total = num(args.total_cost, "$3,074.9")
    total_text = f"Total Cost to Open: {total}"
    total_fs = fit_font(total_text, w - margin*2 - 38, h*0.044, h*0.031, 0.52)
    cta_y = h * 0.858
    cta_h = h * 0.067
    return svg_open(w, h, colors) + f'''
  <rect width="{w}" height="{h}" fill="#812207"/>
  <rect width="{w}" height="{h}" fill="url(#orangeField)" opacity="0.94"/>
  <circle cx="{w*0.82:.1f}" cy="{h*0.12:.1f}" r="{w*0.45:.1f}" fill="{colors['orange']}" opacity="0.16" filter="url(#softBlur)"/>
  <circle cx="{w*0.52:.1f}" cy="{h*0.72:.1f}" r="{w*0.55:.1f}" fill="#2b0903" opacity="0.18" filter="url(#softBlur)"/>
  <rect width="{w}" height="{h}" fill="url(#grain)" opacity="0.20"/>
  <rect width="{w}" height="{h}" fill="#000" opacity="0.045"/>
  {ostium_logo(margin+2, h*0.054, w*0.215, colors, opacity=0.96)}
  {''.join(headline_svg)}
  <g transform="translate({margin:.1f},{trade_y:.1f})">
    <rect x="0" y="{-h*0.026:.1f}" width="{w*0.148:.1f}" height="{h*0.046:.1f}" rx="{h*0.014:.1f}" fill="{pill_bg}" opacity="0.70"/>
    <text x="{w*0.074:.1f}" y="{h*0.009:.1f}" text-anchor="middle" fill="{pill_color}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{h*0.035:.1f}" font-weight="800">{esc(direction)}</text>
    <text x="{w*0.205:.1f}" y="{h*0.009:.1f}" fill="{colors['white']}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{h*0.036:.1f}" font-weight="800">{esc(pair)}</text>
    <text x="{w*0.410:.1f}" y="{h*0.006:.1f}" fill="{colors['paper']}" opacity="0.80" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{h*0.034:.1f}" font-weight="500">·</text>
    <text x="{w*0.463:.1f}" y="{h*0.009:.1f}" fill="{colors['paper']}" opacity="0.67" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{h*0.035:.1f}" font-weight="700">{esc(leverage)}</text>
  </g>
  {''.join(table)}
  <rect x="{margin:.1f}" y="{cta_y:.1f}" width="{w-margin*2:.1f}" height="{cta_h:.1f}" rx="{h*0.015:.1f}" fill="{colors['orange']}" opacity="0.13" stroke="{colors['paper']}" stroke-opacity="0.24" stroke-width="1.15"/>
  <text x="{margin+18:.1f}" y="{cta_y+cta_h*0.67:.1f}" fill="{colors['white']}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{total_fs:.1f}" font-weight="800" letter-spacing="{-total_fs*0.030:.1f}">{esc(total_text)}</text>
''' + svg_close()



def trade_result(args, colors: dict[str, str], w: int, h: int) -> str:
    value = num(args.position_size, "$75,908,000")
    context = args.subhead or f"in {num(args.market, 'WTI')} {num(args.direction, 'shorts').lower()}."
    pnl = num(args.pnl, "$1,328,633.46")
    pnl_color = colors["green"] if not pnl.strip().startswith("-") else colors["red"]
    fs_value = fit_font(value, w*0.72, h*0.158, h*0.088, 0.52)
    context_svg, _ = text_block(context, w*0.055, h*0.325, w*0.50, h*0.064, h*0.038, colors["white"], weight=800, max_lines=2, line_height=1.03)
    # stylized oil slick + tanker stand-in, closer to source than abstract contour waves
    slick = ''.join(f'<path d="M{w*(-0.05+i*0.10):.1f} {h*(0.02+i*0.09):.1f} C {w*(0.18+i*0.04):.1f} {h*(0.13+i*0.07):.1f}, {w*(0.36+i*0.02):.1f} {h*(0.02+i*0.08):.1f}, {w*(0.58+i*0.03):.1f} {h*(0.16+i*0.06):.1f}" fill="none" stroke="#F05A22" stroke-width="{h*0.035:.1f}" opacity="{0.16+i*0.018:.2f}"/>' for i in range(7))
    return svg_open(w, h, colors) + f'''
  <rect width="{w}" height="{h}" fill="#05222A"/>
  <rect width="{w}" height="{h}" fill="url(#darkToOrange)" opacity="0.55"/>
  {slick}
  <path d="M{w*0.43:.1f} {h*0.48:.1f} l{w*0.20:.1f} {h*0.08:.1f} l{-w*0.035:.1f} {h*0.070:.1f} l{-w*0.23:.1f} {-h*0.07:.1f} z" fill="#E8D6CA" opacity="0.58" transform="rotate(-20 {w*0.52:.1f} {h*0.53:.1f})"/>
  <rect width="{w}" height="{h}" fill="#000" opacity="0.20"/>
  <text x="{w*0.055:.1f}" y="{h*0.260:.1f}" fill="{colors['paper']}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{fs_value:.1f}" font-weight="850" letter-spacing="{-fs_value*0.04:.1f}">{esc(value)}</text>
  {context_svg}
  <g filter="url(#shadow)">
    <rect x="{w*0.585:.1f}" y="{h*0.505:.1f}" width="{w*0.292:.1f}" height="{h*0.158:.1f}" fill="{colors['panel']}" opacity="0.94"/>
    <text x="{w*0.615:.1f}" y="{h*0.568:.1f}" fill="{colors['muted']}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{h*0.039:.1f}" font-weight="400">{esc(num(args.pnl_label, 'Unrealized PNL'))}</text>
    <text x="{w*0.615:.1f}" y="{h*0.645:.1f}" fill="{pnl_color}" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{h*0.052:.1f}" font-weight="850">{esc(pnl)}</text>
  </g>
  {ostium_logo(w*0.5, h*0.925, w*0.120, colors, anchor='middle', opacity=0.92)}
''' + svg_close()

def position_card(x: float, y: float, ww: float, hh: float, p: dict[str, str], colors: dict[str, str]) -> str:
    direction = p.get("direction", "Long").title()
    is_long = direction.lower() == "long"
    badge_bg = colors["green_bg"] if is_long else colors["red_bg"]
    badge_fg = colors["green"] if is_long else colors["red"]
    return f'''
  <g transform="translate({x:.1f},{y:.1f})">
    <rect width="{ww:.1f}" height="{hh:.1f}" rx="16" fill="#0A0A0A" stroke="#242424" stroke-width="1.4"/>
    <circle cx="{ww*0.060:.1f}" cy="{hh*0.205:.1f}" r="{hh*0.095:.1f}" fill="#171717" stroke="#2A2A2A"/>
    <text x="{ww*0.060:.1f}" y="{hh*0.228:.1f}" text-anchor="middle" fill="#fff" font-size="{hh*0.070:.1f}" font-weight="800" font-family="Inter, Helvetica Neue, Arial, sans-serif">{esc(p.get('icon','NDX'))}</text>
    <text x="{ww*0.115:.1f}" y="{hh*0.180:.1f}" fill="#fff" font-size="{hh*0.115:.1f}" font-weight="800" font-family="Inter, Helvetica Neue, Arial, sans-serif">{esc(p.get('pair','US100/USD'))}</text>
    <rect x="{ww*0.345:.1f}" y="{hh*0.105:.1f}" width="{ww*0.145:.1f}" height="{hh*0.135:.1f}" rx="6" fill="{badge_bg}" opacity="0.82"/>
    <text x="{ww*0.417:.1f}" y="{hh*0.197:.1f}" text-anchor="middle" fill="{badge_fg}" font-size="{hh*0.070:.1f}" font-weight="750" font-family="Inter, Helvetica Neue, Arial, sans-serif">{esc(direction)} {esc(p.get('leverage','25.0x'))}</text>
    <text x="{ww*0.115:.1f}" y="{hh*0.305:.1f}" fill="#A0A0A0" font-size="{hh*0.070:.1f}" font-weight="400" font-family="Inter, Helvetica Neue, Arial, sans-serif">{esc(p.get('time','19/05 08:33 pm'))}</text>
    <text x="{ww*0.915:.1f}" y="{hh*0.180:.1f}" text-anchor="end" fill="#fff" font-size="{hh*0.085:.1f}" font-weight="800" font-family="Inter, Helvetica Neue, Arial, sans-serif">Open</text>
    <text x="{ww*0.915:.1f}" y="{hh*0.285:.1f}" text-anchor="end" fill="#A0A0A0" font-size="{hh*0.070:.1f}" font-weight="500" font-family="Inter, Helvetica Neue, Arial, sans-serif">Market</text>
    <line x1="{ww*0.045:.1f}" y1="{hh*0.405:.1f}" x2="{ww*0.955:.1f}" y2="{hh*0.405:.1f}" stroke="#292929"/>
    <text x="{ww*0.045:.1f}" y="{hh*0.585:.1f}" fill="#8F8F8F" font-size="{hh*0.064:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">Size</text>
    <text x="{ww*0.045:.1f}" y="{hh*0.725:.1f}" fill="#fff" font-size="{hh*0.088:.1f}" font-weight="800" font-family="IBM Plex Mono, Menlo, monospace">{esc(p.get('size','$24.81M'))}</text>
    <text x="{ww*0.360:.1f}" y="{hh*0.585:.1f}" fill="#8F8F8F" font-size="{hh*0.064:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">Price</text>
    <text x="{ww*0.360:.1f}" y="{hh*0.725:.1f}" fill="#fff" font-size="{hh*0.088:.1f}" font-weight="800" font-family="IBM Plex Mono, Menlo, monospace">{esc(p.get('price','$28,732.64'))}</text>
    <text x="{ww*0.670:.1f}" y="{hh*0.585:.1f}" fill="#8F8F8F" font-size="{hh*0.064:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">Price Impact</text>
    <text x="{ww*0.670:.1f}" y="{hh*0.725:.1f}" fill="#fff" font-size="{hh*0.088:.1f}" font-weight="800" font-family="IBM Plex Mono, Menlo, monospace">{esc(p.get('impact','0.12 bps'))}</text>
    <line x1="{ww*0.045:.1f}" y1="{hh*0.805:.1f}" x2="{ww*0.955:.1f}" y2="{hh*0.805:.1f}" stroke="#292929"/>
    <text x="{ww*0.500:.1f}" y="{hh*0.918:.1f}" text-anchor="middle" fill="#8F8F8F" font-size="{hh*0.064:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">View more⌄</text>
  </g>'''



def position_overlay(args, colors: dict[str, str], w: int, h: int) -> str:
    panel_w, panel_h = w*0.86, h*0.47
    px, py = (w-panel_w)/2, h*0.255
    direction = num(args.direction, "Long").title()
    p1 = {"pair": num(args.market, "US500/USD"), "direction": direction, "leverage": num(args.leverage, "22.0x"), "size": num(args.position_size, "$21.85M"), "price": num(args.price, "$7,354.98"), "impact": num(args.price_impact, "0.52 bps"), "icon": num(args.icon, "SPY")}
    p2 = {"pair": num(args.market2, "US100/USD"), "direction": direction, "leverage": num(args.leverage2, "25.0x"), "size": num(args.position_size2, "$24.81M"), "price": num(args.price2, "$28,732.64"), "impact": num(args.price_impact2, "0.12 bps"), "icon": num(args.icon2, "NDX")}
    long_count = "2L" if direction.lower() == "long" else "0L"
    short_count = "0S" if direction.lower() == "long" else "2S"
    bg = []
    # trading-floor/collage-like rights-safe backdrop
    bg.append(f'<rect width="{w}" height="{h}" fill="#100906"/>')
    bg.append(f'<rect width="{w}" height="{h}" fill="url(#darkToOrange)" opacity="0.45"/>')
    for i in range(7):
        x=w*(0.05+i*0.14); y=h*(0.10+(i%3)*0.16)
        bg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w*0.10:.1f}" height="{h*0.08:.1f}" fill="#DAD0C6" opacity="0.18" transform="rotate({-8+i*3} {x:.1f} {y:.1f})"/>')
    for i in range(10):
        bg.append(f'<circle cx="{w*(0.08+i*0.10):.1f}" cy="{h*(0.76+(i%2)*0.08):.1f}" r="{w*0.030:.1f}" fill="#CFC6BD" opacity="0.08"/>')
    bg.append(f'<rect width="{w}" height="{h}" fill="#000" opacity="0.38"/>')
    return svg_open(w, h, colors) + '\n'.join(bg) + f'''
  <g filter="url(#shadow)">
    <rect x="{px:.1f}" y="{py:.1f}" width="{panel_w:.1f}" height="{panel_h:.1f}" rx="14" fill="{colors['panel']}" opacity="0.985" stroke="#1D1D1D"/>
    <text x="{px+panel_w*0.030:.1f}" y="{py+panel_h*0.065:.1f}" fill="#A8A8A8" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{panel_h*0.043:.1f}" font-weight="750">OPEN POSITIONS</text>
    <text x="{px+panel_w*0.970:.1f}" y="{py+panel_h*0.065:.1f}" text-anchor="end" fill="#BFBFBF" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{panel_h*0.043:.1f}" font-weight="750">Size: {esc(num(args.summary_size, '$46.66M'))} <tspan fill="{colors['green']}">{long_count}</tspan> / <tspan fill="{colors['red']}">{short_count}</tspan></text>
    {position_card(px+panel_w*0.025, py+panel_h*0.118, panel_w*0.95, panel_h*0.375, p1, colors)}
    {position_card(px+panel_w*0.025, py+panel_h*0.540, panel_w*0.95, panel_h*0.375, p2, colors)}
  </g>
  {ostium_logo(w*0.5, h*0.925, w*0.150, colors, anchor='middle', opacity=0.92)}
''' + svg_close()


def briefing(args, colors: dict[str, str], w: int, h: int) -> str:
    margin = w*0.082
    company = num(args.company, "NVIDIA")
    ticker = num(args.ticker, "NVDA")
    y = h*0.108
    sections = []
    # logo-like header block; text approximation stays deterministic without Nvidia marks
    sections.append(f'<text x="{w/2:.1f}" y="{y:.1f}" text-anchor="middle" fill="#fff" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{h*0.060:.1f}" font-weight="900" letter-spacing="0.5">{esc(company)}</text>')
    sections.append(f'<text x="{w/2:.1f}" y="{y+h*0.042:.1f}" text-anchor="middle" fill="{colors["paper"]}" opacity="0.82" font-family="Inter, Helvetica Neue, Arial, sans-serif" font-size="{h*0.015:.1f}" font-weight="700" letter-spacing="1.1">{esc(args.context.upper() if args.context else "Q1 FY27 PRE-EARNINGS BRIEFING")}</text>')
    y = h*0.245
    sections.append(f'<text x="{margin:.1f}" y="{y:.1f}" fill="#fff" font-size="{h*0.028:.1f}" font-weight="800" font-family="Inter, Helvetica Neue, Arial, sans-serif">Street Consensus</text>')
    labels = [("Revenue", "$78.0B"), ("EPS", "$1.77"), ("Data Center", "$73B"), ("Q2 Guide Bar", "$86B")]
    colw=(w-margin*2)/4
    for i,(lab,val) in enumerate(labels):
        x = margin + i*colw
        sections.append(f'<text x="{x:.1f}" y="{y+h*0.058:.1f}" fill="{colors["muted"]}" opacity="0.70" font-size="{h*0.017:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">{lab}</text>')
        sections.append(f'<text x="{x:.1f}" y="{y+h*0.087:.1f}" fill="#fff" font-size="{h*0.027:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">{val}</text>')
    y += h*0.152
    sections.append(f'<text x="{margin:.1f}" y="{y:.1f}" fill="#fff" font-size="{h*0.027:.1f}" font-weight="800" font-family="Inter, Helvetica Neue, Arial, sans-serif">Options Market</text>')
    sections.append(f'<text x="{w*0.54:.1f}" y="{y:.1f}" fill="#fff" font-size="{h*0.027:.1f}" font-weight="800" font-family="Inter, Helvetica Neue, Arial, sans-serif">Polymarket</text>')
    sections.append(f'<text x="{margin:.1f}" y="{y+h*0.049:.1f}" fill="{colors["muted"]}" opacity="0.70" font-size="{h*0.017:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">Implied Move</text><text x="{margin:.1f}" y="{y+h*0.087:.1f}" fill="#fff" font-size="{h*0.033:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">±7%</text><text x="{margin:.1f}" y="{y+h*0.111:.1f}" fill="{colors["muted"]}" opacity="0.75" font-size="{h*0.013:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">on the print</text>')
    sections.append(f'<text x="{w*0.54:.1f}" y="{y+h*0.049:.1f}" fill="{colors["muted"]}" opacity="0.70" font-size="{h*0.017:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">Beat Probability</text><text x="{w*0.54:.1f}" y="{y+h*0.087:.1f}" fill="#fff" font-size="{h*0.033:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">90%</text>')
    y += h*0.125
    sections.append(f'<line x1="{margin:.1f}" y1="{y:.1f}" x2="{w-margin:.1f}" y2="{y:.1f}" stroke="#fff" stroke-opacity="0.35"/>')
    # special positioning section with two small columns, closer to original
    y += h*0.065
    sections.append(f'<text x="{margin:.1f}" y="{y:.1f}" fill="#fff" font-size="{h*0.029:.1f}" font-weight="800" font-family="Inter, Helvetica Neue, Arial, sans-serif">Ostium Positioning</text>')
    sections.append(f'<text x="{margin:.1f}" y="{y+h*0.052:.1f}" fill="{colors["muted"]}" opacity="0.70" font-size="{h*0.017:.1f}">Long</text><text x="{margin:.1f}" y="{y+h*0.088:.1f}" fill="#fff" font-size="{h*0.031:.1f}">99.31%</text>')
    sections.append(f'<text x="{w*0.33:.1f}" y="{y+h*0.052:.1f}" fill="{colors["muted"]}" opacity="0.70" font-size="{h*0.017:.1f}">Positions</text><text x="{w*0.33:.1f}" y="{y+h*0.088:.1f}" fill="#fff" font-size="{h*0.031:.1f}">69</text>')
    y += h*0.135
    for label, value, right in [(f"Largest Open {ticker} Trade", f"One wallet built a {num(args.position_size, '$3.31M')} {ticker} long across 7 positions over the past week, currently up $224k", num(args.position_size, '$3.31M')), (num(args.headline, "Silicon Week"), num(args.subhead, f"2x points on {ticker}, AMD, MU, ARM\\nFees lowered up to 75%"), "")]:
        sections.append(f'<line x1="{margin:.1f}" y1="{y:.1f}" x2="{w-margin:.1f}" y2="{y:.1f}" stroke="#fff" stroke-opacity="0.35"/>')
        sections.append(f'<text x="{margin:.1f}" y="{y+h*0.058:.1f}" fill="#fff" font-size="{h*0.028:.1f}" font-weight="800" font-family="Inter, Helvetica Neue, Arial, sans-serif">{esc(label)}</text>')
        wrapped, hh = text_block(value, margin, y+h*0.091, w*0.62, h*0.019, h*0.014, "#fff", weight=400, max_lines=2, line_height=1.05)
        sections.append(wrapped)
        if right:
            sections.append(f'<text x="{w-margin:.1f}" y="{y+h*0.085:.1f}" text-anchor="end" fill="#fff" font-size="{h*0.030:.1f}" font-family="Inter, Helvetica Neue, Arial, sans-serif">{esc(right)}</text>')
        y += h*(0.125 if right else 0.104)
    return svg_open(w, h, colors) + f'''
  <rect width="{w}" height="{h}" fill="#6A1B09"/>
  <rect width="{w}" height="{h}" fill="url(#orangeField)" opacity="0.82"/>
  <rect width="{w}" height="{h}" fill="#000" opacity="0.13"/>
  <rect width="{w}" height="{h}" fill="url(#grain)" opacity="0.18"/>
  {''.join(sections)}
  {ostium_logo(w*0.5, h*0.958, w*0.180, colors, anchor='middle')}
''' + svg_close()

def svg_doc(args, colors: dict[str, str], w: int, h: int) -> str:
    template = args.template
    if template == "campaign-banner":
        return campaign_banner(args, colors, w, h)
    if template == "cost-breakdown":
        return cost_breakdown(args, colors, w, h)
    if template == "trade-result":
        return trade_result(args, colors, w, h)
    if template == "position-overlay":
        return position_overlay(args, colors, w, h)
    if template == "briefing":
        return briefing(args, colors, w, h)
    raise SystemExit(f"Unknown template: {template}")


def render_png(svg_path: Path, png_path: Path, width: int, height: int) -> None:
    chromium = "/usr/bin/chromium"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        html_path = Path(f.name)
        f.write(f'<html><body style="margin:0;background:#080909">{svg_path.read_text(encoding="utf-8")}</body></html>')
    try:
        subprocess.run([
            chromium,
            "--headless=new",
            "--no-sandbox",
            f"--window-size={width},{height}",
            f"--screenshot={png_path}",
            html_path.resolve().as_uri(),
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    finally:
        html_path.unlink(missing_ok=True)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Generate Ostium-native social SVG/PNG assets")
    ap.add_argument("--brand-dir", required=True, type=Path)
    ap.add_argument("--template", choices=["campaign-banner", "cost-breakdown", "trade-result", "position-overlay", "briefing"], default="campaign-banner")
    ap.add_argument("--headline", default="")
    ap.add_argument("--subhead", default="")
    ap.add_argument("--brand", default="Ostium")
    ap.add_argument("--context", default="")
    ap.add_argument("--background-theme", default="")
    ap.add_argument("--icons", default="")
    ap.add_argument("--market", default="")
    ap.add_argument("--market2", default="")
    ap.add_argument("--ticker", default="")
    ap.add_argument("--company", default="")
    ap.add_argument("--direction", default="")
    ap.add_argument("--leverage", default="")
    ap.add_argument("--leverage2", default="")
    ap.add_argument("--position-size", default="")
    ap.add_argument("--position-size2", default="")
    ap.add_argument("--summary-size", default="")
    ap.add_argument("--price", default="")
    ap.add_argument("--price2", default="")
    ap.add_argument("--price-impact", default="")
    ap.add_argument("--price-impact2", default="")
    ap.add_argument("--icon", default="")
    ap.add_argument("--icon2", default="")
    ap.add_argument("--pnl", default="")
    ap.add_argument("--pnl-label", default="")
    ap.add_argument("--opening-fee-pct", default="")
    ap.add_argument("--opening-fee", default="")
    ap.add_argument("--slippage-pct", default="")
    ap.add_argument("--slippage", default="")
    ap.add_argument("--closing-fee-pct", default="")
    ap.add_argument("--closing-fee", default="")
    ap.add_argument("--rollover-fee", default="")
    ap.add_argument("--total-cost", default="")
    ap.add_argument("--proof-line", action="append", default=[], help="Deprecated compatibility option; not used by Ostium-native templates")
    ap.add_argument("--size", type=int, default=None, help="Square size compatibility option. Prefer --width/--height.")
    ap.add_argument("--width", type=int, default=None)
    ap.add_argument("--height", type=int, default=None)
    ap.add_argument("--out", required=True, type=Path)
    return ap.parse_args()


def default_dimensions(args: argparse.Namespace) -> tuple[int, int]:
    if args.width and args.height:
        return args.width, args.height
    if args.size:
        return args.size, args.size
    if args.template in {"campaign-banner", "trade-result"}:
        return 1600, 900
    if args.template == "briefing":
        return 1080, 1350
    if args.template == "cost-breakdown":
        return 986, 1232
    return 1080, 1080


def main() -> None:
    args = parse_args()
    src = read_sources(args.brand_dir)
    if not src:
        raise SystemExit(f"No brand.md or brand-guide.md found in {args.brand_dir}")
    colors = extract_hexes(src)
    width, height = default_dimensions(args)
    png_path = args.out
    svg_path = png_path.with_suffix(".svg")
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text(svg_doc(args, colors, width, height), encoding="utf-8")
    render_png(svg_path, png_path, width, height)
    print(svg_path)
    print(png_path)


if __name__ == "__main__":
    main()
