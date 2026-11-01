#!/usr/bin/env python3
"""sync_quickpicks.py - keep the inline "Quick picks" rows of SKILL.md identical to the generated libraries.

SKILL.md must be useful on its own (some tools load only that file), so it embeds a few palette rows and font
URLs. They are copied from assets/tokens/palettes.json and assets/tokens/fonts.json by this script:

  python3 scripts/sync_quickpicks.py          # rewrite the blocks in SKILL.md
  python3 scripts/sync_quickpicks.py --check  # exit 1 if SKILL.md is out of sync (used by selftest.sh)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"

QUICK_PALETTES = [
    ("clean-minimalist-saas", "default product UI, light-first"),
    ("midnight-slate", "dashboards and analytics, dark-first"),
    ("warm-sand", "hospitality, wellness, craft, light-first"),
    ("royal-velvet", "luxury, jewellery, hotels, dark-first"),
]
QUICK_TYPES = [1, 4, 39, 11]

P_START, P_END = "<!-- quickpicks:palettes:start -->", "<!-- quickpicks:palettes:end -->"
T_START, T_END = "<!-- quickpicks:types:start -->", "<!-- quickpicks:types:end -->"


def palette_block() -> str:
    data = json.loads((ROOT / "assets/tokens/palettes.json").read_text(encoding="utf-8"))
    order = data["token_order"]
    lines = [P_START]
    for pid, use in QUICK_PALETTES:
        p = next(x for x in data["palettes"] if x["id"] == pid)
        for mode, tk in p["modes"].items():
            tag = "native" if mode == p["native"] else "twin"
            row = " ".join(f"--{k}:{tk[k]};" for k in order)
            lines.append(f"- `{pid}` {mode} ({tag}; {use}): `{row}`")
    lines.append(P_END)
    return "\n".join(lines)


def type_block() -> str:
    fonts = json.loads((ROOT / "assets/tokens/fonts.json").read_text(encoding="utf-8"))
    lines = [T_START, "| id | heading / body | `<link href=\"...\" rel=\"stylesheet\">` |", "|----|----------------|------|"]
    for n in QUICK_TYPES:
        f = next(x for x in fonts if x["n"] == n)
        h, b = f["heading"], f["body"]
        lines.append(f"| `{f['id']}` | {h['family']} {h['weight']} / {b['family']} {b['weight']} | `{f['google_url']}` |")
    lines.append(T_END)
    return "\n".join(lines)


def replace(text: str, placeholder: str, start: str, end: str, block: str) -> str:
    if placeholder in text:
        return text.replace(placeholder, block)
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        raise SystemExit(f"markers {start} not found in SKILL.md")
    return pat.sub(lambda _m: block, text)


def main() -> int:
    text = SKILL.read_text(encoding="utf-8")
    new = replace(text, "@@PALETTE_ROWS@@", P_START, P_END, palette_block())
    new = replace(new, "@@TYPE_ROWS@@", T_START, T_END, type_block())
    if "--check" in sys.argv:
        if new != text:
            print("SKILL.md quick picks are out of sync: run python3 scripts/sync_quickpicks.py")
            return 1
        print("SKILL.md quick picks are in sync")
        return 0
    SKILL.write_text(new, encoding="utf-8")
    print("SKILL.md quick picks updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
