#!/usr/bin/env python3
"""contrast_check.py - WCAG 2.x contrast checks (stdlib only).

Examples
  python3 scripts/contrast_check.py "#F0F0F0" "#0B0B0B"        # one pair
  python3 scripts/contrast_check.py --palettes                 # verify all 100 shipped themes
  python3 scripts/contrast_check.py --css src/theme.css        # verify a generated/hand-made theme

Exit code 0 = everything passes, 1 = at least one failure (usable in CI).
Thresholds: body text 4.5:1 (AA) - large text and UI components 3:1 - fg 7:1 (AAA).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colorlib import TOKEN_ORDER, contrast, norm, verify_tokens  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def grade(r: float) -> str:
    if r >= 7:
        return "AAA"
    if r >= 4.5:
        return "AA"
    if r >= 3:
        return "AA-large / UI only"
    return "FAIL"


def cmd_pair(a: str, b: str) -> int:
    r = contrast(a, b)
    print(f"{norm(a)} on {norm(b)} = {r:.2f}:1  ->  {grade(r)}")
    print("  normal text (4.5):", "pass" if r >= 4.5 else "FAIL",
          "| large text / UI (3.0):", "pass" if r >= 3 else "FAIL",
          "| AAA body (7.0):", "pass" if r >= 7 else "no")
    return 0 if r >= 4.5 else 1


def cmd_palettes(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    bad = 0
    themes = 0
    for p in data["palettes"]:
        for mode, tk in p["modes"].items():
            themes += 1
            fails = verify_tokens(tk)
            if fails:
                bad += 1
                print(f"FAIL {p['id']} [{mode}]: {'; '.join(fails)}")
    print(f"checked {themes} themes in {len(data['palettes'])} palettes: "
          f"{'all pass' if not bad else str(bad) + ' failing'}")
    return 1 if bad else 0


_BLOCK = re.compile(r"([^{}]+)\{([^{}]*)\}")
_VAR = re.compile(r"--([a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\s*;")


def cmd_css(path: Path) -> int:
    text = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.S)
    bad = checked = 0
    for sel, body in _BLOCK.findall(text):
        tokens = {k: norm(v) for k, v in _VAR.findall(body)}
        if not all(k in tokens for k in TOKEN_ORDER):
            continue
        checked += 1
        fails = verify_tokens(tokens)
        label = " ".join(sel.split())
        if fails:
            bad += 1
            print(f"FAIL {label}: {'; '.join(fails)}")
        else:
            print(f"ok   {label}")
    if checked == 0:
        print("no complete token block found (need all 13 tokens: " + ", ".join(TOKEN_ORDER) + ")")
        return 1
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("colors", nargs="*", help="foreground and background hex")
    ap.add_argument("--palettes", nargs="?", const=str(ROOT / "assets/tokens/palettes.json"),
                    help="verify a palettes.json (default: the shipped one)")
    ap.add_argument("--css", help="verify theme CSS blocks containing all 13 tokens")
    a = ap.parse_args()
    if a.palettes:
        return cmd_palettes(Path(a.palettes))
    if a.css:
        return cmd_css(Path(a.css))
    if len(a.colors) == 2:
        return cmd_pair(*a.colors)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
