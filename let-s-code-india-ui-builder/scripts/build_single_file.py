#!/usr/bin/env python3
"""build_single_file.py - bundle the whole skill into ONE markdown file.

Use the bundle only where a tool cannot load multiple files (paste into a chat, a single custom-instruction
slot with a large limit). Where multi-file skills are supported (Claude Skills, VS Code / GitHub Copilot agent skills,
Claude Code) use the folder: SKILL.md stays small and loads the references only when a step needs them.

Output: dist/Let-s-Code-India-UI-Builder.single-file.md
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist/Let-s-Code-India-UI-Builder.single-file.md"

REFS = ["palettes.md", "palette-tokens.md", "typography.md", "surfaces.md", "components.md", "motion.md",
        "accessibility.md", "blueprints.md", "anti-generic.md", "examples.md"]
STARTER = ["src/index.css", "src/theme.css", "src/lib/cn.ts", "src/components/Button.tsx", "src/components/Field.tsx",
           "src/components/Card.tsx", "src/components/Badge.tsx", "src/components/Alert.tsx",
           "src/components/Dialog.tsx", "src/components/ThemeToggle.tsx", "src/components/Skeleton.tsx",
           "src/components/EmptyState.tsx", "src/react-augment.d.ts", "index.html"]


def fence(path: Path, lang: str) -> str:
    return f"```{lang}\n{path.read_text(encoding='utf-8').rstrip()}\n```"


def main() -> int:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    parts = [skill.rstrip(), "",
             "---", "",
             "# SINGLE-FILE BUNDLE NOTE",
             "This file contains the whole skill. Wherever the playbook above says to open a file under `references/` or "
             "`assets/starter/`, find that file's section below (each starts with `## FILE:`). Scripts cannot run from a single file: "
             "use the tables and the component source below instead, and state in your delivery that scripted checks were not run.",
             ""]
    for name in REFS:
        body = (ROOT / "references" / name).read_text(encoding="utf-8").rstrip()
        parts += ["---", "", f"## FILE: references/{name}", "", body, ""]
    parts += ["---", "", "## FILE: assets/starter (source to copy)", ""]
    for rel in STARTER:
        p = ROOT / "assets/starter" / rel
        lang = {"css": "css", "ts": "ts", "tsx": "tsx", "html": "html"}[p.suffix.lstrip(".")]
        parts += [f"### assets/starter/{rel}", "", fence(p, lang), ""]
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    lines = OUT.read_text(encoding="utf-8").count("\n")
    print(f"wrote {OUT.relative_to(ROOT)} ({lines} lines, {OUT.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
