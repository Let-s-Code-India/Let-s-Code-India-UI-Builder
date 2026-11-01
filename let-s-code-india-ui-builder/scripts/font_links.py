#!/usr/bin/env python3
"""font_links.py - correct <link> tags and CSS font stacks for the 50 shipped type pairings.

Why this exists: Google Fonts returns HTTP 400 (and NO fonts at all) if a request names a weight a
family does not have (e.g. wght@700 for Bebas Neue). Several pairings also use Fontshare families
(Satoshi, General Sans, Cabinet Grotesk, Clash Display) which are NOT on Google Fonts. This script
only requests weights that exist, and uses the right host for each family.

Examples
  python3 scripts/font_links.py --list
  python3 scripts/font_links.py 12                 # by number or id: <link> tags + @theme font variables
  python3 scripts/font_links.py inter-minimalist --hindi   # adds a Devanagari companion font
  python3 scripts/font_links.py --build            # regenerate references/typography.md + assets/tokens/fonts.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent.parent

R = lambda a, b: list(range(a, b + 1, 100))  # noqa: E731  (variable-font weight range)

# family -> (host, category, allowed weights)
FAMILIES: dict[str, tuple[str, str, list[int]]] = {
    # sans
    "Inter": ("g", "sans", R(100, 900)), "Geist": ("g", "sans", R(100, 900)),
    "Outfit": ("g", "sans", R(100, 900)), "Plus Jakarta Sans": ("g", "sans", R(200, 800)),
    "Space Grotesk": ("g", "sans", R(300, 700)), "Syne": ("g", "sans", R(400, 800)),
    "DM Sans": ("g", "sans", R(100, 900)), "Lato": ("g", "sans", [100, 300, 400, 700, 900]),
    "Montserrat": ("g", "sans", R(100, 900)), "Open Sans": ("g", "sans", R(300, 800)),
    "Source Sans 3": ("g", "sans", R(200, 900)), "Roboto": ("g", "sans", [100, 300, 400, 500, 700, 900]),
    "Ubuntu": ("g", "sans", [300, 400, 500, 700]), "Ubuntu Condensed": ("g", "sans", [400]),
    "Red Hat Display": ("g", "sans", R(300, 900)), "Work Sans": ("g", "sans", R(100, 900)),
    "Nunito": ("g", "sans", R(200, 900)), "Quicksand": ("g", "sans", R(300, 700)),
    "Mulish": ("g", "sans", R(200, 900)), "Poppins": ("g", "sans", R(100, 900)),
    "Manrope": ("g", "sans", R(200, 800)), "IBM Plex Sans": ("g", "sans", R(100, 700)),
    # serif
    "Playfair Display": ("g", "serif", R(400, 900)), "Cormorant Garamond": ("g", "serif", R(300, 700)),
    "Cinzel": ("g", "serif", R(400, 900)), "Instrument Serif": ("g", "serif", [400]),
    "Bodoni Moda": ("g", "serif", R(400, 900)), "Prata": ("g", "serif", [400]),
    "Lora": ("g", "serif", R(400, 700)), "EB Garamond": ("g", "serif", R(400, 800)),
    "Source Serif 4": ("g", "serif", R(200, 900)), "Fraunces": ("g", "serif", R(100, 900)),
    "Merriweather": ("g", "serif", R(300, 900)),
    # mono
    "Geist Mono": ("g", "mono", R(100, 900)), "Fira Code": ("g", "mono", R(300, 700)),
    "JetBrains Mono": ("g", "mono", R(100, 800)), "Space Mono": ("g", "mono", [400, 700]),
    "IBM Plex Mono": ("g", "mono", R(100, 700)), "Source Code Pro": ("g", "mono", R(200, 900)),
    "Inconsolata": ("g", "mono", R(200, 900)), "Anonymous Pro": ("g", "mono", [400, 700]),
    "Share Tech Mono": ("g", "mono", [400]), "Red Hat Mono": ("g", "mono", R(300, 700)),
    # display
    "Bebas Neue": ("g", "display", [400]), "Oswald": ("g", "display", R(200, 700)),
    "Anton": ("g", "display", [400]), "Abril Fatface": ("g", "display", [400]),
    "Alfa Slab One": ("g", "display", [400]), "Staatliches": ("g", "display", [400]),
    "Righteous": ("g", "display", [400]), "Chakra Petch": ("g", "display", [300, 400, 500, 600, 700]),
    "Teko": ("g", "display", R(300, 700)), "Permanent Marker": ("g", "script", [400]),
    # Fontshare (Indian Type Foundry) - NOT on Google Fonts
    "Satoshi": ("fs", "sans", [300, 400, 500, 700, 900]),
    "General Sans": ("fs", "sans", [200, 300, 400, 500, 600, 700]),
    "Cabinet Grotesk": ("fs", "display", [100, 200, 300, 400, 500, 700, 800, 900]),
    "Clash Display": ("fs", "display", [200, 300, 400, 500, 600, 700]),
}

STACKS = {
    "sans": 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
    "serif": 'Georgia, "Times New Roman", serif',
    "mono": 'ui-monospace, "SFMono-Regular", Menlo, Consolas, "Liberation Mono", monospace',
    "display": 'system-ui, -apple-system, "Segoe UI", Arial, sans-serif',
    "script": '"Comic Sans MS", "Marker Felt", cursive',
}
HINDI = {"sans": "Noto Sans Devanagari", "display": "Noto Sans Devanagari", "mono": "Noto Sans Devanagari",
         "script": "Noto Sans Devanagari", "serif": "Noto Serif Devanagari"}

# (n, id, name, group, heading family, weight, italic, body family, body weight, base px, body leading, best for)
PAIRS = [
    (1, "inter-minimalist", "Inter Minimalist", "sans", "Inter", 700, False, "Inter", 400, 16, 1.5, "any product UI, dashboards"),
    (2, "geist-developer", "Geist Developer", "sans", "Geist Mono", 600, False, "Geist", 400, 15, 1.6, "developer tools, docs"),
    (3, "outfit-creative", "Outfit Creative", "sans", "Outfit", 800, False, "Plus Jakarta Sans", 400, 16, 1.5, "creative agencies, apps"),
    (4, "plus-jakarta-pro", "Plus Jakarta Pro", "sans", "Plus Jakarta Sans", 700, False, "Inter", 400, 16, 1.55, "SaaS marketing, fintech"),
    (5, "space-grotesk-cyber", "Space Grotesk Cyber", "sans", "Space Grotesk", 700, False, "Inter", 400, 16, 1.6, "AI / web3 / cyber"),
    (6, "cabinet-grotesk-bold", "Cabinet Grotesk Bold", "sans", "Cabinet Grotesk", 700, False, "General Sans", 400, 16, 1.5, "bold brands, studios"),
    (7, "syne-futuristic", "Syne Futuristic", "sans", "Syne", 800, False, "DM Sans", 400, 16, 1.6, "art, music, experimental"),
    (8, "clash-display-tech", "Clash Display Tech", "sans", "Clash Display", 700, False, "Satoshi", 400, 16, 1.5, "tech launches, hero-led pages"),
    (9, "satoshi-minimal", "Satoshi Minimal", "sans", "Satoshi", 700, False, "Inter", 400, 16, 1.5, "minimal brands, portfolios"),
    (10, "general-sans-corporate", "General Sans Corporate", "sans", "General Sans", 600, False, "Plus Jakarta Sans", 400, 16, 1.55, "corporate, B2B"),
    (11, "playfair-editorial", "Playfair Editorial", "serif", "Playfair Display", 700, False, "Lato", 400, 18, 1.7, "magazines, fashion"),
    (12, "cormorant-luxury", "Cormorant Luxury", "serif", "Cormorant Garamond", 600, False, "Montserrat", 400, 17, 1.75, "jewellery, hotels, luxury"),
    (13, "cinzel-royal", "Cinzel Royal", "serif", "Cinzel", 700, False, "Open Sans", 400, 16, 1.6, "heritage, events, wine"),
    (14, "instrument-serif-noir", "Instrument Serif Noir", "serif", "Instrument Serif", 400, True, "Plus Jakarta Sans", 400, 16, 1.6, "editorial, restaurants"),
    (15, "bodoni-classic", "Bodoni Classic", "serif", "Bodoni Moda", 700, False, "Inter", 400, 16, 1.6, "fashion, galleries"),
    (16, "prata-elegant", "Prata Elegant", "serif", "Prata", 400, False, "DM Sans", 400, 17, 1.65, "architecture, boutique"),
    (17, "lora-warm-editorial", "Lora Warm Editorial", "serif", "Lora", 700, False, "Inter", 400, 16, 1.7, "blogs, long reads, cafes"),
    (18, "eb-garamond-vintage", "EB Garamond Vintage", "serif", "EB Garamond", 500, False, "Source Serif 4", 400, 18, 1.75, "books, heritage, journals"),
    (19, "fraunces-modern-serif", "Fraunces Modern Serif", "serif", "Fraunces", 600, False, "Plus Jakarta Sans", 400, 16, 1.6, "friendly editorial, food"),
    (20, "merriweather-classic", "Merriweather Classic", "serif", "Merriweather", 700, False, "Open Sans", 400, 16, 1.65, "news, education"),
    (21, "fira-code-terminal", "Fira Code Terminal", "mono", "Fira Code", 700, False, "Inter", 400, 15, 1.6, "terminals, dev blogs"),
    (22, "jetbrains-mono-coder", "JetBrains Mono Coder", "mono", "JetBrains Mono", 600, False, "Plus Jakarta Sans", 400, 15, 1.65, "IDE-like products"),
    (23, "space-mono-hacker", "Space Mono Hacker", "mono", "Space Mono", 700, False, "DM Sans", 400, 15, 1.6, "retro-tech, hackathons"),
    (24, "ibm-plex-tech", "IBM Plex Tech", "mono", "IBM Plex Mono", 700, False, "IBM Plex Sans", 400, 16, 1.55, "engineering, enterprise tech"),
    (25, "source-code-pro", "Source Code Pro", "mono", "Source Code Pro", 700, False, "Source Sans 3", 400, 15, 1.6, "docs, code-heavy pages"),
    (26, "inconsolata-clean", "Inconsolata Clean", "mono", "Inconsolata", 700, False, "Inter", 400, 16, 1.5, "light terminal looks"),
    (27, "anonymous-pro-retro", "Anonymous Pro Retro", "mono", "Anonymous Pro", 700, False, "Roboto", 400, 15, 1.55, "retro computing"),
    (28, "ubuntu-tech-vibe", "Ubuntu Tech Vibe", "mono", "Ubuntu", 700, False, "Ubuntu Condensed", 400, 16, 1.5, "linux, open-source communities"),
    (29, "share-tech-mono", "Share Tech Mono", "mono", "Share Tech Mono", 400, False, "Inter", 400, 15, 1.6, "HUD, sci-fi interfaces"),
    (30, "red-hat-mono", "Red Hat Mono", "mono", "Red Hat Mono", 700, False, "Red Hat Display", 400, 16, 1.55, "cloud, infrastructure"),
    (31, "roboto-standard", "Roboto Standard", "sans", "Roboto", 500, False, "Roboto", 400, 16, 1.5, "neutral utility apps"),
    (32, "open-sans-corporate", "Open Sans Corporate", "sans", "Open Sans", 700, False, "Open Sans", 400, 16, 1.6, "government, NGOs, legal"),
    (33, "montserrat-clean", "Montserrat Clean", "sans", "Montserrat", 700, False, "Inter", 400, 16, 1.5, "agencies, startups"),
    (34, "lato-professional", "Lato Professional", "sans", "Lato", 700, False, "Lato", 400, 16, 1.6, "professional services"),
    (35, "poppins-vibrant", "Poppins Vibrant", "sans", "Poppins", 600, False, "Open Sans", 400, 16, 1.55, "consumer apps, education (Devanagari-capable heading)"),
    (36, "work-sans-modern", "Work Sans Modern", "sans", "Work Sans", 700, False, "Work Sans", 400, 16, 1.5, "modern business sites"),
    (37, "nunito-rounded", "Nunito Rounded", "sans", "Nunito", 700, False, "Nunito", 400, 16, 1.6, "kids, health, friendly apps"),
    (38, "quicksand-soft", "Quicksand Soft", "sans", "Quicksand", 700, False, "Mulish", 400, 16, 1.6, "wellness, soft brands"),
    (39, "dm-sans-clean", "DM Sans Clean", "sans", "DM Sans", 700, False, "DM Sans", 400, 16, 1.5, "clean product pages"),
    (40, "manrope-sharp", "Manrope Sharp", "sans", "Manrope", 800, False, "Inter", 400, 16, 1.5, "fintech, VC, sharp UI"),
    (41, "bebas-neue-headline", "Bebas Neue Headline", "display", "Bebas Neue", 400, False, "Montserrat", 400, 18, 1.5, "posters, sports, events"),
    (42, "oswald-impact", "Oswald Impact", "display", "Oswald", 700, False, "Open Sans", 400, 17, 1.5, "news, fitness, bold headers"),
    (43, "anton-bold-banner", "Anton Bold Banner", "display", "Anton", 400, False, "Roboto", 400, 18, 1.5, "banners, campaigns"),
    (44, "abril-fatface-bold", "Abril Fatface Bold", "display", "Abril Fatface", 400, False, "Lato", 400, 18, 1.6, "fashion, beauty, bold editorial"),
    (45, "alfa-slab-one-heavy", "Alfa Slab One Heavy", "display", "Alfa Slab One", 400, False, "Open Sans", 400, 17, 1.5, "retro, food trucks, crafts"),
    (46, "staatliches-poster", "Staatliches Poster", "display", "Staatliches", 400, False, "Inter", 400, 16, 1.5, "posters, events"),
    (47, "righteous-futuristic", "Righteous Futuristic", "display", "Righteous", 400, False, "DM Sans", 400, 16, 1.5, "games, retro-future"),
    (48, "chakra-petch-cyber", "Chakra Petch Cyber", "display", "Chakra Petch", 700, False, "Inter", 400, 16, 1.55, "cyber, esports, HUD"),
    (49, "teko-sharp-tech", "Teko Sharp Tech", "display", "Teko", 700, False, "Roboto", 400, 17, 1.5, "motorsport, industrial tech"),
    (50, "permanent-marker-fun", "Permanent Marker Fun", "display", "Permanent Marker", 400, False, "Poppins", 400, 16, 1.6, "playful, kids, street culture"),
]


def clamp_weight(family: str, w: int) -> int:
    allowed = FAMILIES[family][2]
    return min(allowed, key=lambda a: (abs(a - w), a))


def weights_for(pair) -> dict[str, dict]:
    """family -> {'w': sorted weights, 'italic': bool}"""
    _, _, _, _, hf, hw, hit, bf, bw, *_ = pair
    out: dict[str, dict] = {}
    out.setdefault(hf, {"w": set(), "italic": False})["w"].add(clamp_weight(hf, hw))
    out[hf]["italic"] |= hit
    b = out.setdefault(bf, {"w": set(), "italic": False})["w"]
    b.update({clamp_weight(bf, bw), clamp_weight(bf, 500), clamp_weight(bf, 700)})
    for fam in out:
        out[fam]["w"] = sorted(out[fam]["w"])
    return out


def google_url(fams: dict[str, dict], extra: list[str] | None = None) -> str | None:
    parts = []
    for fam in sorted(f for f in fams if FAMILIES[f][0] == "g"):
        spec = fams[fam]
        name = quote_plus(fam)
        if spec["italic"]:
            tuples = [f"0,{w}" for w in spec["w"]] + [f"1,{w}" for w in spec["w"]]
            parts.append(f"family={name}:ital,wght@{';'.join(tuples)}")
        else:
            parts.append(f"family={name}:wght@{';'.join(map(str, spec['w']))}")
    for e in extra or []:
        parts.append(e)
    if not parts:
        return None
    return "https://fonts.googleapis.com/css2?" + "&".join(parts) + "&display=swap"


def fontshare_url(fams: dict[str, dict]) -> str | None:
    parts = []
    for fam in sorted(f for f in fams if FAMILIES[f][0] == "fs"):
        slug = fam.lower().replace(" ", "-")
        parts.append(f"f[]={slug}@{','.join(map(str, fams[fam]['w']))}")
    if not parts:
        return None
    return "https://api.fontshare.com/v2/css?" + "&".join(parts) + "&display=swap"


def find_pair(key: str):
    for p in PAIRS:
        if key == p[1] or key == str(p[0]) or key == f"{p[0]:02d}":
            return p
    return None


def stack(family: str, hindi: bool) -> str:
    cat = FAMILIES[family][1]
    parts = [f'"{family}"']
    if hindi:
        parts.append(f'"{HINDI[cat]}"')
    parts.append(STACKS[cat])
    return ", ".join(parts)


def render(pair, hindi: bool) -> str:
    n, pid, name, group, hf, hw, hit, bf, bw, px, lh, best = pair
    fams = weights_for(pair)
    extra = []
    if hindi:
        cat = FAMILIES[hf][1]
        extra.append(f"family={quote_plus(HINDI[cat])}:wght@400;500;700")
    g = google_url(fams, extra)
    f = fontshare_url(fams)
    out = [f"<!-- {n:02d} {name}: heading {hf} {hw}{' italic' if hit else ''}, body {bf} {bw}, {px}px / {lh} -->"]
    if g:
        out += ['<link rel="preconnect" href="https://fonts.googleapis.com" />',
                '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />',
                f'<link href="{g}" rel="stylesheet" />']
    if f:
        out += ['<link rel="preconnect" href="https://api.fontshare.com" />',
                '<link rel="preconnect" href="https://cdn.fontshare.com" crossorigin />',
                f'<link href="{f}" rel="stylesheet" />']
    out += ["", "/* Tailwind v4 (index.css) */", "@theme {",
            f"  --font-display: {stack(hf, hindi)};",
            f"  --font-body: {stack(bf, hindi)};",
            "}", f"/* body: font-size {px / 16:g}rem, line-height {lh}; heading weight {hw}"
            f"{', italic' if hit else ''} */"]
    return "\n".join(out)


def build_files() -> None:
    rows = []
    loads = []
    data = []
    for p in PAIRS:
        n, pid, name, group, hf, hw, hit, bf, bw, px, lh, best = p
        src = "+".join(sorted({"Fontshare" if FAMILIES[f][0] == "fs" else "Google" for f in (hf, bf)}))
        head = f"{hf} {hw}{' italic' if hit else ''}"
        rows.append(f"| {n:02d} | `{pid}` | {head} | {bf} {bw} | {FAMILIES[hf][1]}/{FAMILIES[bf][1]} | {src} | {px}/{lh} | {best} |")
        fams = weights_for(p)
        g, f = google_url(fams), fontshare_url(fams)
        loads.append(f"### {n:02d} {pid}")
        if g:
            loads.append(f"`{g}`")
        if f:
            loads.append(f"`{f}`")
        data.append({"n": n, "id": pid, "name": name, "group": group, "heading": {"family": hf, "weight": hw, "italic": hit},
                     "body": {"family": bf, "weight": bw}, "base_px": px, "leading": lh, "best_for": best,
                     "google_url": g, "fontshare_url": f,
                     "display_stack": stack(hf, False), "body_stack": stack(bf, False)})
    md = ["# Typography (50 pairings, verified loading)",
          "",
          "Pick ONE pairing (max two families). Choose by the product's voice, not by habit: an",
          "Inter + purple-gradient look is the generic default. Serif/display faces carry personality;",
          "use them for headings and keep a quiet sans for body text.",
          "",
          "## Rules",
          "- Body text weight >= 400 and size >= 16px (15px only for dense developer UIs). Light (300) is for large display text only.",
          "- Body line-height 1.5-1.7, measure <= 70ch (`max-w-prose`). Serif body gets slightly more leading than sans.",
          "- Fluid headings with `clamp()`: h1 `clamp(2.25rem, 1.2rem + 4.5vw, 4.5rem)`, h2 `clamp(1.75rem, 1.1rem + 2.4vw, 3rem)`,",
          "  h3 `clamp(1.25rem, 1rem + 1vw, 1.75rem)`. Never `vw` alone. Tight tracking only on large display sizes (`tracking-tight`).",
          "- Load at most 2 families and ~4 weights, with `display=swap`. Preconnect to the font hosts.",
          "- Fontshare families (Satoshi, General Sans, Cabinet Grotesk, Clash Display) are NOT on Google Fonts: use the Fontshare URL.",
          "- Google Fonts returns HTTP 400 for a weight a family lacks (e.g. Bebas Neue has only 400): use the URLs below or",
          "  `python3 scripts/font_links.py <id>`; never hand-write the weights.",
          "- Hindi / Devanagari: append `\"Noto Sans Devanagari\"` (serif pairings: `\"Noto Serif Devanagari\"`) after the Latin family in the stack,",
          "  set `lang=\"hi\"` on the element, and give Devanagari body text line-height >= 1.7. `font_links.py <id> --hindi` does this.",
          "- Avoid typographic tells: accenting a single headline word, tracked ALL-CAPS eyebrow above every heading, `A · B · C` meta strings.",
          "",
          "## Pairings",
          "",
          "| # | id | heading | body | type | source | px/leading | best for |",
          "|---|----|---------|------|------|--------|-----------|----------|",
          *rows,
          "",
          "Stacks: sans `" + STACKS["sans"] + "`; serif `" + STACKS["serif"] + "`; mono `" + STACKS["mono"] + "`.",
          "Use `\"Family\", <stack of its type>` for `--font-display` / `--font-body`.",
          "",
          "## Load strings (copy as `<link href=\"...\" rel=\"stylesheet\">`)",
          "",
          *loads, ""]
    (ROOT / "references/typography.md").write_text("\n".join(md), encoding="utf-8")
    (ROOT / "assets/tokens/fonts.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote references/typography.md and assets/tokens/fonts.json ({len(PAIRS)} pairings)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pair", nargs="?", help="pairing number or id")
    ap.add_argument("--hindi", action="store_true", help="add a Devanagari companion font")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--build", action="store_true", help="regenerate references/typography.md and fonts.json")
    a = ap.parse_args()
    for p in PAIRS:  # self-check: every family known
        for fam in (p[4], p[7]):
            assert fam in FAMILIES, f"unknown family {fam}"
    if a.build:
        build_files()
        return 0
    if a.list:
        for p in PAIRS:
            print(f"{p[0]:02d} {p[1]:<26} {p[4]} / {p[7]:<20} {p[11]}")
        return 0
    if not a.pair:
        ap.print_help()
        return 2
    pair = find_pair(a.pair)
    if not pair:
        print(f"unknown pairing {a.pair!r}; use --list", file=sys.stderr)
        return 2
    print(render(pair, a.hindi))
    return 0


if __name__ == "__main__":
    sys.exit(main())
