#!/bin/sh
# selftest.sh - run every automated check of the skill.
#   sh scripts/selftest.sh            # full run (Node checks run when assets/starter/node_modules exists)
# Exit code 0 = all good. Safe to use in CI (see assets/ci/skill-ci.yml).
cd "$(dirname "$0")/.." || exit 1
fail=0
step() { printf '\n== %s\n' "$1"; }
run() { "$@" || fail=1; }

step "generated libraries rebuild and verify"
run python3 scripts/build_palettes.py
run python3 scripts/contrast_check.py --palettes
run python3 scripts/font_links.py --build
run python3 scripts/build_blueprints.py
run python3 scripts/sync_quickpicks.py --check

step "SKILL.md frontmatter and size"
run python3 - <<'PY'
import re, sys
from pathlib import Path
root = Path(".")
text = (root / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"---\n(.*?)\n---\n", text, re.S)
assert m, "missing frontmatter"
fm = m.group(1)
name = re.search(r"^name:\s*(.+)$", fm, re.M).group(1).strip()
desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1).strip()
assert name == root.resolve().name == "let-s-code-india-ui-builder", f"name/folder mismatch: {name} vs {root.resolve().name}"
assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) and len(name) <= 64, "invalid name"
assert len(desc) <= 1024, f"description too long: {len(desc)}"
assert ": " not in desc, "description contains ': ' (breaks plain YAML scalars)"
lines = text.count("\n")
assert lines <= 500, f"SKILL.md too long: {lines} lines"
bad = [p for p in text.split() if p in ("LET-S-CODE-INDIA", "Let-S-Code-India", "lets-code-india")]
assert not bad, f"wrong organisation spelling: {bad}"
print(f"ok: name={name}, description={len(desc)} chars, {lines} lines")
PY

step "organisation name spelling (must be Let-s-Code-India everywhere)"
if grep -rIn --include='*.md' --include='*.py' --include='*.tsx' --include='*.html' --include='*.json' --include='*.sh' --include='*.mjs' --include='*.yml' -e 'LET-S-CODE-INDIA' -e 'Let-S-Code-India' -e 'lets-code-india' . --exclude-dir=node_modules --exclude-dir=dist --exclude-dir=_backup | grep -v 'selftest.sh'; then
  echo "found a wrong spelling"; fail=1
else
  echo "ok"
fi

step "lint the starter and the reference code examples"
run python3 scripts/lint_ui.py assets/starter/src assets/starter/index.html
run python3 scripts/check_refs.py

if command -v node >/dev/null 2>&1 && [ -d assets/starter/node_modules ]; then
  step "real Tailwind v4 class check + type-check + production build (starter)"
  ( cd assets/starter && run node ../../scripts/check_classes.mjs src index.html && run npx tsc --noEmit && run npx vite build )
else
  echo; echo "(skipped Node checks: run 'npm install' in assets/starter first)"
fi

step "result"
if [ "$fail" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED"; fi
exit "$fail"
