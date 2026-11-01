# Let-s-Code-India-UI-Builder (v2.0.0)

An AI skill that makes any capable coding assistant produce **distinctive, accessible, production-ready web UI**:
a fixed workflow, verified building blocks and checks, instead of a very long list of adjectives.

Author: Ayush Giri, Founder, Let-s-Code-India. License: MIT.

## Repository layout
```
Let-s-Code-India-UI-Builder/                  <- this GitHub repository
├── README.md                                 you are reading it
├── LICENSE
├── CHANGELOG.md
├── .gitignore
├── .github/workflows/skill-ci.yml            GitHub Actions: runs every check on each push
└── let-s-code-india-ui-builder/              <- THE SKILL (this folder is what you install)
    ├── SKILL.md                              the playbook, read first
    ├── references/                           opened on demand by SKILL.md
    │   ├── palettes.md, palette-tokens.md    50 palettes x dark+light, contrast-verified (generated)
    │   ├── typography.md                     50 font pairings, Hindi support (generated)
    │   ├── surfaces.md                       surface styles, 12 layout recipes, icons, imagery
    │   ├── components.md                     state contract + accessible component recipes
    │   ├── motion.md, accessibility.md, anti-generic.md, examples.md
    │   └── blueprints.md                     54 blueprints, 4 India-first (generated)
    ├── scripts/                              Python (standard library) + one Node script
    │   ├── tokens_to_tailwind.py, contrast_check.py, font_links.py, lint_ui.py, check_classes.mjs
    │   ├── build_palettes.py, build_blueprints.py, sync_quickpicks.py, build_single_file.py
    │   └── check_refs.py, colorlib.py, selftest.sh
    ├── assets/
    │   ├── starter/                          Vite + React + TypeScript + Tailwind v4 starter project
    │   └── tokens/                           palettes.json, palettes.css, fonts.json
    └── evals/prompts.md                      10 prompts + rubric to measure improvement
```

## Install (copy the folder `let-s-code-india-ui-builder/`, not the whole repo)
| Your tool | What to do |
|-----------|-----------|
| **Claude Code** | Copy the folder to `.claude/skills/let-s-code-india-ui-builder/` in your project, or to `~/.claude/skills/let-s-code-india-ui-builder/` for all projects. |
| **Claude (claude.ai)** | Zip the folder `let-s-code-india-ui-builder/` so that this folder is the zip's top level, then Settings > Skills > add the zip. |
| **GitHub Copilot (VS Code / Codespaces)** | Copy the folder to `.github/skills/let-s-code-india-ui-builder/`, open Copilot Chat in **Agent** mode. (VS Code also reads `.claude/skills/` and `.agents/skills/`.) |
| **Any tool without skill support** | Paste the contents of `let-s-code-india-ui-builder/SKILL.md` into the chat or custom-instruction box. It is self-sufficient (contains quick picks). For the full bundle run `python3 scripts/build_single_file.py` and paste `dist/Let-s-Code-India-UI-Builder.single-file.md`. |

The skill is picked automatically from its `description`. Then just ask:
"Build a landing page for ...", "Add dark mode to this app", "Review this component for accessibility".

## Starting a new project
```bash
cd let-s-code-india-ui-builder/assets/starter && npm install
python3 ../../scripts/tokens_to_tailwind.py --palette midnight-slate --out src/theme.css   # or --brand "#7C3AED" --mode dark
npm run dev        # npm run check = lint + exact class check + type-check + build
```

## Verify and measure
```bash
cd let-s-code-india-ui-builder
sh scripts/selftest.sh      # every automated check (needs python3; Node checks need `npm install` in assets/starter)
```
Then run `evals/prompts.md`: ten prompts, with and without the skill, scored 0/1 per rubric item.

## Change it safely
Edit the seeds (`scripts/build_palettes.py`, `scripts/font_links.py`, `scripts/build_blueprints.py`), run the build scripts, then `selftest.sh`.
Do not hand-edit generated files (`palettes.md`, `palette-tokens.md`, `typography.md`, `blueprints.md`, `assets/tokens/*`).
Naming: organisation **Let-s-Code-India**, skill folder and name `let-s-code-india-ui-builder`, display title `Let-s-Code-India-UI-Builder`.
