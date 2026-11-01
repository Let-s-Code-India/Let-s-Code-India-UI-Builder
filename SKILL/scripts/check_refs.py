#!/usr/bin/env python3
"""check_refs.py - verify the code examples inside references/*.md.

Extracts every ```tsx / ```jsx / ```html fence (and the class strings in the layout table of surfaces.md)
into a temp folder, then runs lint_ui.py on it and - when Node and the starter's node_modules exist -
check_classes.mjs against the starter's CSS, i.e. the real Tailwind v4 compiler.

Usage: python3 scripts/check_refs.py
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STARTER = ROOT / "assets/starter"


def extract(tmp: Path) -> int:
    n = 0
    for md in sorted((ROOT / "references").glob("*.md")):
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r"```(tsx|jsx|html)\n(.*?)```", text, re.S):
            n += 1
            (tmp / f"{md.stem}-{n}.{'html' if m.group(1) == 'html' else 'tsx'}").write_text(m.group(2), encoding="utf-8")
    spans = []
    for line in (ROOT / "references/surfaces.md").read_text(encoding="utf-8").splitlines():
        if re.match(r"\| L\d+ ", line):
            spans += [s for s in re.findall(r"`([^`]+)`", line) if not s.startswith("<")]
    (tmp / "surfaces-layouts.tsx").write_text("\n".join(f'<div className="{s}" />' for s in spans), encoding="utf-8")
    return n


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="refcheck-"))
    try:
        n = extract(tmp)
        print(f"extracted {n} code fences from references/")
        rc = subprocess.call([sys.executable, str(ROOT / "scripts/lint_ui.py"), str(tmp)])
        if shutil.which("node") and (STARTER / "node_modules").exists():
            files = [str(p) for p in sorted(tmp.iterdir())]
            rc |= subprocess.call(["node", str(ROOT / "scripts/check_classes.mjs"), *files, "--css", "src/index.css"], cwd=STARTER)
        else:
            print("skipped class validation (needs Node and `npm install` in assets/starter)")
        return 1 if rc else 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
