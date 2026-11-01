# Let-s-Code-India-UI-Builder (v2.0.0)

An AI skill that makes any capable coding assistant produce **distinctive, accessible, production-ready web UI**:
a fixed workflow, verified building blocks and checks, instead of a very long list of adjectives.

Author: Ayush Giri, Founder, Let-s-Code-India.

## What is inside
```
let-s-code-india-ui-builder/
  SKILL.md                    the playbook (read first, ~130 lines, self-sufficient with quick picks)
  references/                 loaded on demand
    palettes.md  palette-tokens.md   50 palettes x dark+light, every pair contrast-verified (generated)
    typography.md                    50 pairings with correct Google/Fontshare loading, Hindi support (generated)
    surfaces.md                      6 surface styles, shape/elevation rules, 12 layout recipes, icons, imagery
    components.md                    state contract + accessible recipes (switch, tabs, popover, toast, table ...)
    motion.md  accessibility.md  anti-generic.md  examples.md  blueprints.md (54 blueprints, 4 India-first)
  scripts/                    standard-library Python (+1 Node script)
    tokens_to_tailwind.py     theme from a palette id OR from one brand colour
    contrast_check.py  font_links.py  lint_ui.py  check_classes.mjs  check_refs.py  selftest.sh
    build_*.py  sync_quickpicks.py  build_single_file.py      (regenerate the generated files)
  assets/starter/             Vite + React + TypeScript + Tailwind v4 project (type-checks, builds, passes the linters)
  assets/tokens/              palettes.json, palettes.css, fonts.json
  assets/ci/skill-ci.yml      GitHub Actions workflow that runs selftest.sh
  evals/prompts.md            10 prompts + rubric to MEASURE improvement (baseline vs with skill)
  dist/                       single-file bundle for tools that cannot load multiple files
  _backup/Skill.original.md   your original file, untouched
  AUDIT.md  CHANGELOG.md
```

## Install
| tool | how |
|------|-----|
| GitHub Copilot (VS Code, Codespaces) | copy this folder to `.github/skills/let-s-code-india-ui-builder/` in your repo, open Copilot Chat in **Agent** mode, then ask for a UI task. The skill is picked by its `description`. (VS Code also reads `.claude/skills/` and `.agents/skills/`.) |
| Claude Code | `.claude/skills/let-s-code-india-ui-builder/` in the project, or `~/.claude/skills/` for all projects |
| Claude (claude.ai) | zip the folder so that `let-s-code-india-ui-builder/` is the zip's top level, then add it in the Skills settings |
| Tools without skill support (chat, custom-instruction boxes) | paste `dist/Let-s-Code-India-UI-Builder.single-file.md` (large) or just `SKILL.md` (small, already contains quick picks) |

## Use
Ask normally: "Build a landing page for ...", "Add dark mode to this app", "Review this component for accessibility".
New project? Copy `assets/starter`, then:
```bash
cd assets/starter && npm install
python3 ../../scripts/tokens_to_tailwind.py --palette midnight-slate --out src/theme.css   # or --brand "#7C3AED" --mode dark
npm run dev            # npm run check = lint + exact class check + type-check + build
```

## Verify and measure
```bash
sh scripts/selftest.sh          # every automated check (needs: python3; node + `npm install` in assets/starter for the Node checks)
```
Then run `evals/prompts.md`: ten prompts, with and without the skill, scored 0/1 per rubric item.

## Change it safely
Edit the *seeds* (`scripts/build_palettes.py`, `scripts/font_links.py`, `scripts/build_blueprints.py`), then run the build scripts and `selftest.sh`.
Do not hand-edit the generated files (`palettes.md`, `palette-tokens.md`, `typography.md`, `blueprints.md`, `assets/tokens/*`).
Organisation name everywhere: **Let-s-Code-India**. Skill name: `let-s-code-india-ui-builder`. Display title: `Let-s-Code-India-UI-Builder`.
