#!/usr/bin/env python3
"""build_palettes.py - regenerate every palette artefact from the seed table below.

Outputs (paths relative to the skill root):
  assets/tokens/palettes.json        machine-readable tokens (both modes)
  assets/tokens/palettes.css         [data-palette] theme blocks, ready to import
  references/palettes.md             index used for choosing a palette
  references/palette-tokens.md       one block per palette with exact token values

Seeds keep the original three colours (canvas / surface / accent) of the 50
palettes. Everything else (text, muted, borders, raised surface, status colours,
the opposite-mode twin) is derived and contrast-verified by colorlib.

Usage:  python3 scripts/build_palettes.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colorlib import (TOKEN_ORDER, derive_tokens, is_dark, norm, twin_seeds,  # noqa: E402
                      verify_tokens)

ROOT = Path(__file__).resolve().parent.parent

GROUPS = {
    "tech": "Cyberpunk & tech - AI start-ups, crypto protocols, developer tools, web3",
    "luxury": "Luxury & premium - jewellery, architecture studios, boutique hotels, fashion",
    "saas": "Modern SaaS & fintech - enterprise SaaS, analytics, neobanks, finance portals",
    "creative": "Creative, art & Gen-Z - portfolios, indie games, music, streetwear",
    "organic": "Warm, minimal & organic - wellness, eco start-ups, meditation, craft coffee",
}

# (n, id, name, group, canvas, surface, accent, accent name, mood)
SEEDS = [
    (1, "cyber-black-green", "Cyber Black-Green", "tech", "#0B0B0B", "#10B981", "#EF4444", "Crimson Red", "security / ops, red alert accent"),
    (2, "neon-matrix", "Neon Matrix", "tech", "#050505", "#047857", "#22C55E", "Bright Lime", "matrix green, hacker culture"),
    (3, "cyberpunk-void", "Cyberpunk Void", "tech", "#09090B", "#27272A", "#A855F7", "Neon Purple", "neon purple, web3, gaming"),
    (4, "hacker-terminal", "Hacker Terminal", "tech", "#0D1117", "#161B22", "#3FB950", "GitHub Green", "GitHub-dark feel, dev tools, docs"),
    (5, "dark-synthwave", "Dark Synthwave", "tech", "#120A2A", "#2D1B69", "#FF007F", "Neon Pink", "retro pink-violet, music, events"),
    (6, "glitch-violet", "Glitch Violet", "tech", "#0A0A12", "#1E1B4B", "#6366F1", "Indigo Glow", "indigo glow, AI products"),
    (7, "quantum-teal", "Quantum Teal", "tech", "#030712", "#1F2937", "#14B8A6", "Teal Pop", "calm teal, data and science tools"),
    (8, "electric-horizon", "Electric Horizon", "tech", "#020617", "#0F172A", "#38BDF8", "Sky Blue", "sky blue, cloud and infrastructure"),
    (9, "laser-amber", "Laser Amber", "tech", "#090D16", "#1E293B", "#F59E0B", "Amber Laser", "amber on navy, monitoring, ops"),
    (10, "plasma-orange", "Plasma Orange", "tech", "#0F0505", "#260D0D", "#F97316", "Plasma Flame", "hot orange on black, energy, gaming"),
    (11, "royal-velvet", "Royal Velvet", "luxury", "#1C1412", "#2D2320", "#D4AF37", "Champagne Gold", "champagne gold, jewellery, hotels"),
    (12, "midnight-bronze", "Midnight Bronze", "luxury", "#141210", "#26221D", "#E2A03F", "Antique Bronze", "bronze, fine dining, spirits"),
    (13, "espresso-copper", "Espresso Copper", "luxury", "#1A1110", "#33221E", "#D97706", "Warm Copper", "copper warmth, cafe and craft"),
    (14, "sleek-mahogany", "Sleek Mahogany", "luxury", "#1A0F0D", "#3D231E", "#FBBF24", "Golden Yellow", "golden yellow on mahogany, heritage"),
    (15, "onyx-platinum", "Onyx Platinum", "luxury", "#0E0E10", "#232329", "#E5E7EB", "Platinum Silver", "silver monochrome, watches, tech luxury"),
    (16, "dark-truffle", "Dark Truffle", "luxury", "#1C1917", "#292524", "#D97706", "Warm Ochre", "ochre on warm black, galleries"),
    (17, "classic-noir", "Classic Noir", "luxury", "#0A0A0A", "#1F1F1F", "#F5F5F4", "Pure Ivory", "ivory on black, fashion, editorial"),
    (18, "titanium-gold", "Titanium Gold", "luxury", "#111827", "#1F2937", "#FBBF24", "Rich Gold", "navy and gold, private banking"),
    (19, "royal-emerald-gold", "Royal Emerald Gold", "luxury", "#062E1C", "#0D4A2D", "#FDE047", "Bright Gold", "emerald and gold, heritage brands"),
    (20, "deep-burgundy-gold", "Deep Burgundy Gold", "luxury", "#2A0808", "#4A0E0E", "#FCD34D", "Gold Accent", "burgundy and gold, wine, events"),
    (21, "midnight-slate", "Midnight Slate", "saas", "#0F172A", "#334155", "#06B6D4", "Cyan Spark", "slate and cyan, analytics"),
    (22, "deep-fintech", "Deep FinTech", "saas", "#0A0F1D", "#1E293B", "#3B82F6", "Trust Blue", "trust blue, neobank, payments"),
    (23, "emerald-growth", "Emerald Growth", "saas", "#121212", "#1E1E1E", "#34D399", "Success Emerald", "neutral dark with green, growth"),
    (24, "crypto-obsidian", "Crypto Obsidian", "saas", "#0B0F19", "#172033", "#10B981", "Profit Green", "profit green, trading"),
    (25, "saas-indigo", "SaaS Indigo", "saas", "#030712", "#111827", "#6366F1", "Indigo Pop", "indigo, B2B SaaS"),
    (26, "cloud-violet", "Cloud Violet", "saas", "#0F071E", "#1E1B4B", "#8B5CF6", "Vivid Purple", "violet, cloud and AI SaaS"),
    (27, "enterprise-navy", "Enterprise Navy", "saas", "#090D16", "#1E293B", "#2563EB", "Royal Blue", "royal blue, enterprise, HR"),
    (28, "analytics-teal", "Analytics Teal", "saas", "#042F2E", "#134E4A", "#2DD4BF", "Bright Teal", "deep teal, BI dashboards"),
    (29, "dashboard-rose", "Dashboard Rose", "saas", "#18181B", "#27272A", "#F43F5E", "Alert Rose", "rose alerts, admin and ops"),
    (30, "clean-minimalist-saas", "Clean Minimalist SaaS", "saas", "#FAFAFA", "#F4F4F5", "#2563EB", "Action Blue", "light, action blue, default product UI"),
    (31, "obsidian-fuchsia", "Obsidian Fuchsia", "creative", "#18181B", "#27272A", "#EC4899", "Hot Fuchsia", "hot fuchsia, creators, fashion"),
    (32, "electric-sunset", "Electric Sunset", "creative", "#110C1D", "#221738", "#F43F5E", "Sunset Coral", "coral on violet, music, events"),
    (33, "neon-peach", "Neon Peach", "creative", "#0F172A", "#1E293B", "#FB923C", "Neon Peach", "peach on navy, playful apps"),
    (34, "retro-vaporwave", "Retro Vaporwave", "creative", "#1A0E2E", "#2D1654", "#00F5D4", "Mint Neon", "mint neon on purple, retro games"),
    (35, "cyber-lime", "Cyber Lime", "creative", "#09090B", "#18181B", "#84CC16", "Electric Lime", "electric lime, streetwear, indie"),
    (36, "urban-violet", "Urban Violet", "creative", "#13111C", "#231F33", "#A855F7", "Electric Purple", "electric purple, nightlife"),
    (37, "neon-tangerine", "Neon Tangerine", "creative", "#0D0D0D", "#1A1A1A", "#FF5722", "Deep Tangerine", "tangerine on black, sports, energy"),
    (38, "creative-cyan-dark", "Creative Cyan Dark", "creative", "#080C14", "#131C2E", "#00E5FF", "Vivid Cyan", "vivid cyan, motion and design studios"),
    (39, "midnight-neon-red", "Midnight Neon Red", "creative", "#050505", "#141414", "#FF1744", "Sharp Red", "sharp red, security, events"),
    (40, "cyber-lemon", "Cyber Lemon", "creative", "#0C0A09", "#1C1917", "#EAB308", "Neon Lemon", "lemon on warm black, bold brands"),
    (41, "terracotta-minimal", "Terracotta Minimal", "organic", "#FAF9F5", "#E7E5E4", "#C2410C", "Deep Terracotta", "light cream + terracotta, wellness, craft"),
    (42, "warm-sand", "Warm Sand", "organic", "#FDFBF7", "#F5F2EB", "#B45309", "Warm Ochre", "sand and ochre, hospitality"),
    (43, "olive-organic", "Olive Organic", "organic", "#171A16", "#262A24", "#84CC16", "Fresh Olive", "dark olive, farm, eco"),
    (44, "forest-sage", "Forest Sage", "organic", "#0F1410", "#1C241E", "#10B981", "Sage Glow", "forest green, sustainability"),
    (45, "desert-dune", "Desert Dune", "organic", "#1F1A17", "#332A25", "#D97706", "Dune Gold", "dune gold, travel, outdoor"),
    (46, "warm-minimalist-gray", "Warm Minimalist Gray", "organic", "#F4F4F5", "#E4E4E7", "#7C3AED", "Deep Violet", "light gray + violet, portfolio, blog"),
    (47, "cozy-latte", "Cozy Latte", "organic", "#FAF7F2", "#EFECE6", "#92400E", "Rich Coffee", "latte and coffee, bakery, cafe"),
    (48, "autumn-rust", "Autumn Rust", "organic", "#1C1210", "#2B1D1A", "#EA580C", "Rust Accent", "rust on brown-black, craft, seasonal"),
    (49, "clean-slate-light", "Clean Slate Light", "organic", "#F8FAFC", "#F1F5F9", "#0F172A", "Dark Slate", "light slate, docs, legal, tax"),
    (50, "earthy-moss", "Earthy Moss", "organic", "#111412", "#1E2420", "#65A30D", "Moss Green", "moss green, agriculture, outdoor"),
]


def build() -> dict:
    palettes = []
    problems = []
    for n, pid, name, group, canvas, surface, accent, accent_name, mood in SEEDS:
        native = "dark" if is_dark(canvas) else "light"
        other = "light" if native == "dark" else "dark"
        nat_tokens, nat_notes = derive_tokens(canvas, surface, accent, native)
        tw_canvas, tw_surface, tw_accent, _ = twin_seeds(canvas, native, accent)
        tw_tokens, tw_notes = derive_tokens(tw_canvas, tw_surface, tw_accent, other)
        for mode, tk in ((native, nat_tokens), (other, tw_tokens)):
            bad = verify_tokens(tk)
            if bad:
                problems.append((pid, mode, bad))
        extra = {}
        # a vivid 30% seed (not usable as a card colour) is kept as a decorative colour
        from colorlib import contrast  # local import keeps top clean
        if contrast(canvas, surface) > 2.2 and native == "dark":
            extra["brand-2"] = norm(surface)
        palettes.append({
            "n": n, "id": pid, "name": name, "group": group, "native": native,
            "mood": mood, "accent_name": accent_name,
            "seed": {"canvas": norm(canvas), "surface": norm(surface), "accent": norm(accent)},
            "modes": {native: nat_tokens, other: tw_tokens},
            "extra": extra,
            "notes": {native: nat_notes, other: tw_notes},
        })
    return {"version": "2.0.0", "token_order": TOKEN_ORDER, "groups": GROUPS,
            "palettes": palettes, "problems": problems}


def css_vars(tokens: dict, extra: dict | None = None, indent: str = "  ") -> str:
    lines = [f"{indent}--{k}: {tokens[k]};" for k in TOKEN_ORDER]
    for k, v in (extra or {}).items():
        lines.append(f"{indent}--{k}: {v};")
    return "\n".join(lines)


def write_json(data: dict) -> None:
    out = ROOT / "assets/tokens/palettes.json"
    payload = {k: v for k, v in data.items() if k != "problems"}
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def write_css(data: dict) -> None:
    parts = ["/* palettes.css - generated by scripts/build_palettes.py. Do not edit by hand.\n"
             "   Usage: <html data-palette=\"cyber-black-green\" data-theme=\"dark|light\">\n"
             "   Without data-theme the palette's native mode is used. */\n"]
    for p in data["palettes"]:
        nat = p["native"]
        oth = "light" if nat == "dark" else "dark"
        parts.append(f"/* {p['n']:02d} {p['name']} */")
        parts.append(f"[data-palette=\"{p['id']}\"] {{\n  color-scheme: {nat};\n"
                     f"{css_vars(p['modes'][nat], p['extra'])}\n}}")
        parts.append(f"[data-palette=\"{p['id']}\"][data-theme=\"{nat}\"] {{\n  color-scheme: {nat};\n"
                     f"{css_vars(p['modes'][nat], p['extra'])}\n}}")
        parts.append(f"[data-palette=\"{p['id']}\"][data-theme=\"{oth}\"] {{\n  color-scheme: {oth};\n"
                     f"{css_vars(p['modes'][oth], p['extra'])}\n}}\n")
    (ROOT / "assets/tokens/palettes.css").write_text("\n".join(parts), encoding="utf-8")


def inline(tokens: dict, extra: dict) -> str:
    body = " ".join(f"--{k}:{tokens[k]};" for k in TOKEN_ORDER)
    for k, v in extra.items():
        body += f" --{k}:{v};"
    return f"`{body}`"


def write_markdown(data: dict) -> None:
    idx = ["# Palettes (50) - index",
           "",
           "Pick **one** palette per product. Choose by the brief's subject and audience,",
           "not by the first row that looks plausible. Every palette ships with a dark and a light",
           "theme (native mode + a derived twin); every token pair is contrast-verified.",
           "",
           "How to get the tokens:",
           "1. Shell available: `python3 scripts/tokens_to_tailwind.py --palette <id> --out src/theme.css`",
           "2. No shell: open `references/palette-tokens.md`, search for the id, copy the one-line",
           "   `--token:value;` strings into `:root` (dark) and `:root[data-theme=\"light\"]` (or the reverse).",
           "3. User has brand colours: `python3 scripts/tokens_to_tailwind.py --brand \"#HEX\" --mode dark|light`",
           "   derives a full verified token set from one brand colour.",
           "",
           "Token meaning: `canvas` page background (~60% of area), `surface` cards/panels (~30%),",
           "`raised` menus/dialogs, `line` decorative borders, `line-strong` input borders (3:1),",
           "`fg` body text, `muted` secondary text, `accent` (<=10%: primary action, active state, key data),",
           "`accent-fg` text on accent, `success|warning|danger|info` status (always with icon + text).",
           ""]
    tok = ["# Palette tokens (exact values)",
           "",
           "Look up ONE palette by id (search the `###` heading). Do not read the whole file.",
           "Copy the values verbatim; never nudge a hex by eye (contrast was verified for these exact values).",
           "`brand-2` (when present) is a decorative second colour - never for text or card backgrounds.",
           ""]
    for gkey, gdesc in GROUPS.items():
        idx.append(f"## {gdesc}")
        idx.append("")
        idx.append("| # | id | native | canvas | accent | mood |")
        idx.append("|---|----|--------|--------|--------|------|")
        for p in data["palettes"]:
            if p["group"] != gkey:
                continue
            nat = p["native"]
            t = p["modes"][nat]
            idx.append(f"| {p['n']:02d} | `{p['id']}` | {nat} | `{t['canvas']}` | `{t['accent']}` {p['accent_name']} | {p['mood']} |")
        idx.append("")
        for p in data["palettes"]:
            if p["group"] != gkey:
                continue
            nat = p["native"]
            oth = "light" if nat == "dark" else "dark"
            tok.append(f"### {p['n']:02d} {p['id']}  ({p['name']}, native: {nat})")
            tok.append(f"- {nat} (native): {inline(p['modes'][nat], p['extra'])}")
            tok.append(f"- {oth} (twin): {inline(p['modes'][oth], p['extra'])}")
            tok.append("")
    idx.append("All 100 theme rows verified by `scripts/contrast_check.py --palettes`: `fg` >= 7:1, `muted`, `accent`,")
    idx.append("status colours and `accent-fg` on `accent` >= 4.5:1, `line-strong` >= 3:1, against canvas, surface and raised.")
    (ROOT / "references/palettes.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    (ROOT / "references/palette-tokens.md").write_text("\n".join(tok) + "\n", encoding="utf-8")


def main() -> int:
    data = build()
    write_json(data)
    write_css(data)
    write_markdown(data)
    adjusted = sum(1 for p in data["palettes"] for m in p["notes"].values() for n in m if n.startswith("accent"))
    derived = sum(1 for p in data["palettes"] for m in p["notes"].values() for n in m if n.startswith(("surface", "canvas")))
    print(f"palettes: {len(data['palettes'])}  themes: {len(data['palettes']) * 2}  "
          f"accent-nudged: {adjusted}  surface/canvas-derived: {derived}")
    if data["problems"]:
        for pid, mode, bad in data["problems"]:
            print(f"FAIL {pid} [{mode}]: {', '.join(bad)}")
        return 1
    print("all theme rows pass contrast verification")
    return 0


if __name__ == "__main__":
    sys.exit(main())
