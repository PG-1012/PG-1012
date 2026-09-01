#!/usr/bin/env python3
"""Generate the profile banner SVG, in light and dark variants.

Self-hosted rather than pulled from a widget service: no third-party
dependency, no rate limit, and it renders identically forever. The README
swaps variants with <picture> + prefers-color-scheme.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent

W, H = 1000, 260

THEMES = {
    "dark": {
        "bg": "#0D1117", "panel": "#161B22", "border": "#30363D",
        "text": "#E6EDF3", "dim": "#8B949E", "accent": "#58A6FF",
        "green": "#3FB950", "amber": "#D29922", "red": "#F85149",
        "grid": "#21262D",
    },
    "light": {
        "bg": "#FFFFFF", "panel": "#F6F8FA", "border": "#D0D7DE",
        "text": "#1F2328", "dim": "#636C76", "accent": "#0969DA",
        "green": "#1A7F37", "amber": "#9A6700", "red": "#CF222E",
        "grid": "#EAEEF2",
    },
}

# A stylised trace: the recall curve from the cytology project, rising fast
# then flattening. Decorative, but it is the shape of a real result.
TRACE = [
    (0, 62), (6, 40), (12, 28), (18, 21), (25, 17), (33, 14),
    (42, 12), (52, 10), (63, 9), (75, 8), (88, 7), (100, 6),
]


def polyline(points, x0, y0, w, h):
    out = []
    for px, py in points:
        out.append(f"{x0 + px / 100 * w:.1f},{y0 + py / 100 * h:.1f}")
    return " ".join(out)


def build(theme_name: str) -> str:
    c = THEMES[theme_name]

    grid = "".join(
        f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{c["grid"]}" stroke-width="1"/>'
        for x in range(0, W, 40)
    ) + "".join(
        f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{c["grid"]}" stroke-width="1"/>'
        for y in range(0, H, 40)
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Panshul Gera — building things that make a decision easier">
  <defs>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c['bg']}" stop-opacity="0"/>
      <stop offset="1" stop-color="{c['bg']}" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="trace" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c['accent']}"/>
      <stop offset="1" stop-color="{c['green']}"/>
    </linearGradient>
    <style>
      .mono {{ font-family: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, monospace; }}
      .cursor {{ animation: blink 1.1s steps(1) infinite; }}
      @keyframes blink {{ 50% {{ opacity: 0; }} }}
      /* The curve is drawn solid and merely fades in. An initial
         stroke-dashoffset would leave it invisible in any renderer that
         does not run CSS animations, which is most static previews. */
      .draw {{ animation: fade 1.6s ease-out 1; }}
      @keyframes fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    </style>
  </defs>

  <rect width="{W}" height="{H}" fill="{c['bg']}"/>
  <g opacity="0.55">{grid}</g>

  <!-- terminal panel -->
  <rect x="28" y="28" width="{W - 56}" height="{H - 56}" rx="10"
        fill="{c['panel']}" stroke="{c['border']}" stroke-width="1"/>

  <!-- title bar -->
  <line x1="28" y1="66" x2="{W - 28}" y2="66" stroke="{c['border']}" stroke-width="1"/>
  <circle cx="52" cy="47" r="5.5" fill="{c['red']}"/>
  <circle cx="72" cy="47" r="5.5" fill="{c['amber']}"/>
  <circle cx="92" cy="47" r="5.5" fill="{c['green']}"/>
  <text class="mono" x="118" y="51" font-size="12" fill="{c['dim']}">panshul — zsh — 100×28</text>

  <!-- prompt -->
  <text class="mono" x="56" y="108" font-size="14"><tspan fill="{c['green']}">\u279c</tspan><tspan fill="{c['accent']}" xml:space="preserve">  ~/panshul </tspan><tspan fill="{c['dim']}">git:(</tspan><tspan fill="{c['red']}">main</tspan><tspan fill="{c['dim']}">)</tspan><tspan fill="{c['text']}" xml:space="preserve"> whoami</tspan></text>

  <text class="mono" x="56" y="150" font-size="27" font-weight="700" fill="{c['text']}">Panshul Gera<tspan class="cursor" fill="{c['accent']}">_</tspan></text>

  <text class="mono" x="56" y="182" font-size="13" fill="{c['dim']}">Fintech engineer in Toronto.</text>
  <text class="mono" x="56" y="202" font-size="13" fill="{c['dim']}">I build things that make a decision easier — usually by finding</text>
  <text class="mono" x="56" y="222" font-size="13" fill="{c['dim']}">the constraint everyone assumed was fixed.</text>

  <!-- A real result, used as ornament: recall against decision threshold. -->
  <g transform="translate(700, 104)">
    <polyline class="draw" points="{polyline(TRACE, 0, 0, 232, 74)}"
              fill="none" stroke="{c['accent']}" stroke-width="2.5"
              stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="232" cy="4.4" r="3.5" fill="{c['green']}"/>
    <line x1="0" y1="86" x2="232" y2="86" stroke="{c['border']}" stroke-width="1"/>
    <text class="mono" x="0" y="104" font-size="10" fill="{c['dim']}">threshold</text>
    <text class="mono" x="160" y="104" font-size="10" fill="{c['green']}">99% recall</text>
  </g>
</svg>
'''


def main() -> None:
    for name in THEMES:
        path = OUT / f"banner-{name}.svg"
        path.write_text(build(name))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
