#!/usr/bin/env python3
"""Generate a self-hosted stats card from the GitHub API.

Replaces github-readme-stats, which returned HTTP 503 while this profile was
being built. A card that is sometimes a broken image is worse than one that is
occasionally a few weeks stale, and this repo already self-hosts its banner
for the same reason.

Re-run to refresh:  python3 assets/make_stats.py
"""

import collections
import json
import urllib.request
from pathlib import Path

USER = "PG-1012"
OUT = Path(__file__).resolve().parent
W, H = 480, 200

# Bytes-per-language is the honest measure; repo count over-weights small repos.
LANG_COLORS = {
    "Python": "#3572A5", "Swift": "#F05138", "TypeScript": "#3178C6",
    "Jupyter Notebook": "#DA5B0B", "JavaScript": "#F1E05A", "HTML": "#E34C26",
    "CSS": "#563D7C", "Shell": "#89E051", "Makefile": "#427819",
}

THEMES = {
    "dark": {"bg": "#161B22", "border": "#30363D", "text": "#E6EDF3",
             "dim": "#8B949E", "accent": "#58A6FF", "track": "#21262D"},
    "light": {"bg": "#F6F8FA", "border": "#D0D7DE", "text": "#1F2328",
              "dim": "#636C76", "accent": "#0969DA", "track": "#EAEEF2"},
}


def fetch() -> tuple[list[tuple[str, int]], int]:
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/repos?per_page=100",
        headers={"User-Agent": "profile-stats"},
    )
    repos = json.load(urllib.request.urlopen(req, timeout=30))
    repos = [r for r in repos if not r["fork"] and r["name"] != USER]

    totals: collections.Counter = collections.Counter()
    for repo in repos:
        lang_req = urllib.request.Request(
            repo["languages_url"], headers={"User-Agent": "profile-stats"}
        )
        try:
            for lang, count in json.load(urllib.request.urlopen(lang_req, timeout=30)).items():
                totals[lang] += count
        except Exception:
            continue
    return totals.most_common(6), len(repos)


def build(theme: str, langs: list[tuple[str, int]], repo_count: int) -> str:
    c = THEMES[theme]
    total = sum(v for _, v in langs) or 1

    rows = []
    y = 78
    for name, count in langs:
        share = count / total
        colour = LANG_COLORS.get(name, c["accent"])
        bar_w = max(4, share * 250)
        rows.append(
            f'<text class="mono" x="24" y="{y + 4}" font-size="11" fill="{c["text"]}">{name}</text>'
            f'<rect x="180" y="{y - 7}" width="250" height="9" rx="4.5" fill="{c["track"]}"/>'
            f'<rect x="180" y="{y - 7}" width="{bar_w:.1f}" height="9" rx="4.5" fill="{colour}"/>'
            f'<text class="mono" x="440" y="{y + 4}" font-size="10" fill="{c["dim"]}">{share * 100:.0f}%</text>'
        )
        y += 22

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Language distribution across {repo_count} repositories">
  <style>.mono {{ font-family: ui-monospace, "SF Mono", Menlo, monospace; }}</style>
  <rect width="{W}" height="{H}" rx="10" fill="{c['bg']}" stroke="{c['border']}"/>
  <text class="mono" x="24" y="34" font-size="13" font-weight="700" fill="{c['text']}">Languages by bytes written</text>
  <text class="mono" x="24" y="54" font-size="10.5" fill="{c['dim']}">across {repo_count} public repositories</text>
  {"".join(rows)}
</svg>
'''


def main() -> None:
    langs, repo_count = fetch()
    for theme in THEMES:
        path = OUT / f"stats-{theme}.svg"
        path.write_text(build(theme, langs, repo_count))
        print(f"wrote {path}")
    print(f"languages: {langs}")


if __name__ == "__main__":
    main()
