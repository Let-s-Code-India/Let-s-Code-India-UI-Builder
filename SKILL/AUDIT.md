# Audit: original `Skill.md` (741 lines) -> v2.0.0

The original is kept untouched in `_backup/Skill.original.md`.

## 1. Problems found and how they were fixed
| # | problem in the original | consequence | fix in v2.0.0 |
|---|-------------------------|-------------|---------------|
| 1 | ~80% of the file was catalogues (50 palettes, 50 fonts, 50 layouts, 50 components, 50 blueprints) loaded into context every time | the model skims, picks a few items, the rest is noise; making it 7000 lines would make this 10x worse | `SKILL.md` is a 134-line playbook; catalogues moved to `references/` and are opened only when a step needs them |
| 2 | Palettes had only 3 colours (60/30/10) | text, border, muted, error and hover colours had to be invented, contradicting the rule "never invent hex" | every palette now has 13 tokens (canvas, surface, raised, line, line-strong, fg, muted, accent, accent-fg, success, warning, danger, info) in dark AND light, all contrast-verified |
| 3 | Some "30%" colours were not usable as card colours (palette 01: bright emerald `#10B981`; 02: `#047857`) and some canvas/surface pairs were almost identical (30, 49) | text on cards fails or layers do not show | surfaces derived from the canvas; the vivid colour kept as decorative `--brand-2`; 30 and 49 now use white cards on a tinted canvas |
| 4 | Fonts: Satoshi, General Sans, Cabinet Grotesk, Clash Display were described as Google Fonts; weights were never checked | those 4 families load from Fontshare, not Google; Google Fonts returns HTTP 400 (no fonts at all) if one weight does not exist | `font_links.py` emits the right host per family and only valid weights; body weight raised from 300 to 400 (pairs 5 and 12); leading raised to 1.5 where it was 1.4-1.45 (pairs 41-43, 49) |
| 5 | Invalid or meaningless class guidance (`hover:bg-zinc-850`; Prohibition 19 gives `bg-zinc-900 dark:bg-zinc-900` as its theming example, which is the same colour in both modes) | classes silently do nothing | invalid shades caught by `lint_ui.py`; every class in the references is compiled by the real Tailwind v4 compiler (`check_classes.mjs`) |
| 6 | `outline-none` appears in 9 snippets (input recipes 11-20): recipes 13 and 18 have no replacement focus style at all, and others rely on a border colour change such as `focus:border-white/30`, which does not reach 3:1 | keyboard users lose a clear focus indicator | state contract with a 2px `focus-visible` outline in the verified accent colour; `lint_ui.py` rule `focus-removed` |
| 7 | Stage 5 forced deployment, Supabase and Termux guidance into every reply | simple requests got essays; the actual design got less attention | output contract: rationale, code, verified line, next steps; deployment/backend only when asked |
| 8 | Promotional language ("elite", "zero tolerance", "400 rules", "100x") and a long frontmatter `description` | no measurable effect on output; long description hurts triggering | concrete rules with a reason each; 574-character trigger-focused description |
| 9 | No workflow, no examples, no self-check, no tests | the model had no way to know if it did well | design plan step, worked examples, final checklist, linters, `evals/prompts.md` with a rubric |
| 10 | Organisation name written three ways: `LET-S-CODE-INDIA`, `Let-S-Code-India`, `lets-code-india` | wrong name in outputs | one spelling everywhere: **Let-s-Code-India** (title `Let-s-Code-India-UI-Builder`, name `let-s-code-india-ui-builder`); `selftest.sh` fails if a wrong spelling appears |
| 11 | Motion: `transition-all` appears 18 times (animates layout properties) and reduced motion is mentioned only once | jank on low-end phones; motion-sensitive users not handled | transform/opacity only, listed transitions, reduced motion handled per element (`motion.md`); lint warns on `transition-all` |
| 12 | Prohibition 14 demands manual focus trapping for modals; menus and dialogs are typical custom-ARIA output | more code, more keyboard bugs | native `<dialog>`, `popover`, `<details>` (the browser provides focus containment, Esc and focus return); the starter's `Dialog` is tested |

What was **consolidated, not copied one by one**: the 50 layout snippets and 50 component snippets became 6 surface styles
(variables), 12 layout recipes and about 20 accessible component recipes plus working starter components. Anything you
want back from the old lists is in `_backup/Skill.original.md`.

## 2. Corrections to my earlier message
- I said `border-3` and `z-60` do not exist in Tailwind. That is true for **Tailwind v3**. In **v4** (what this skill targets) both are valid, so they are no longer treated as errors. `hover:bg-zinc-850` is invalid in every version.
- Because of that, "arbitrary z-index vs z-60" was not a real contradiction under v4. The remaining z-index advice is about something else: never use z-index wars (`z-[9999]`); modals, menus and toasts belong in the browser's top layer (`<dialog>`, `popover`).

## 3. Palette changes you should know about
- To make text/links on tinted backgrounds (`bg-accent/10 text-accent`) and button hover states pass WCAG AA, accents were nudged lighter (dark themes) or darker (light themes) where needed.
  In the **native** mode this changed the accent of 26 of the 50 palettes slightly: 01, 03, 05, 06, 07, 13, 16, 21, 22, 25, 26, 27, 28, 29, 30, 31, 32, 36, 37, 39, 41, 42, 45, 46, 48, 50. The hue is kept; the exact original hex is stored under `seed` in `assets/tokens/palettes.json`.
- Native modes: 44 dark, 6 light. Every palette also has a derived twin (light twin for dark palettes and the reverse), so a theme toggle always works.
- Greys (palette 30 and similar) get a quiet tint from the accent hue in their dark twin instead of a red cast.

## 4. What was verified (and how)
| check | result |
|-------|--------|
| `contrast_check.py --palettes`: 100 themes (50 palettes x 2) | all pass: `fg` >= 7:1; `muted`, `accent` (also on its own 12% tint), status colours (also on tint), `accent-fg` on `accent` and on its hover/active colour >= 4.5:1; `line-strong` >= 3:1 |
| Starter project: `tsc --noEmit` and `vite build` (React 19, Vite 8, Tailwind 4.3, TypeScript 7) | pass |
| `check_classes.mjs`: every Tailwind class in the starter and in all 18 code fences of `references/` compiled with the real Tailwind v4 compiler | 0 invalid |
| `lint_ui.py` on the starter and on the reference code | 0 errors, 0 warnings; fixtures with known bugs are detected |
| Headless Chromium on the built starter: 320, 360 and 1280px wide, light and dark | no horizontal overflow; no JavaScript errors |
| Native modal dialog | opens via `command`/`commandfor`, centred in light and dark, initial focus on the safe action, Esc closes |
| `SKILL.md` | frontmatter valid, name equals folder, 574-character description, 134 lines; quick-pick rows identical to the generated JSON |
| Organisation spelling | only `Let-s-Code-India` outside `_backup/` |
Run it all again any time: `sh scripts/selftest.sh`.

## 5. Not verified (be honest with users)
- Whether the skill improves a given AI tool's output. That needs the evals: run `evals/prompts.md` with and without the skill in your tool.
- Font hosts were not reachable from the build sandbox. The Google Fonts URL format and the Fontshare format (`https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap`) are well-known patterns, and the per-family weight tables were written from knowledge of those families. Open the pages once in a real browser; if any family fails, fix its entry in `scripts/font_links.py` and rebuild.
- Firefox, Safari, real Android devices, and screen readers (TalkBack, VoiceOver, NVDA) were not tested. The accessibility reference says how to test them.
- Anchor-positioned popovers (`position-area`) are not available everywhere yet; the recipe documents the fallback (the panel is centred).
