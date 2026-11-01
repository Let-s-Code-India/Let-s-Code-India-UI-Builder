# Evals: how to know the skill actually got better

"100x more powerful" is not measurable; pass rates are. Run these ten prompts **without** the skill (baseline) and
**with** it, in the same tool and model, save each output, and score with the rubric. Re-run after every change to
`SKILL.md` or the references. Keep the skill change only if the score improves and nothing regresses.

## How to run
1. Fresh chat/session per prompt (no memory of earlier outputs). Same model for both runs.
2. Save the code. If the tool cannot save files, paste the code into `src/App.tsx` of `assets/starter`.
3. Automated checks (a few seconds each):
   - `python3 scripts/lint_ui.py <path>`: expect 0 errors
   - `node scripts/check_classes.mjs <path>`: expect 0 invalid (run inside a project with Tailwind v4)
   - `python3 scripts/contrast_check.py --css <theme.css>`: expect all `ok`
   - `npm run build` in the starter: expect success
4. Manual checks (10 minutes per output): keyboard pass, 360px and 320px viewport, 200% zoom, dark and light theme.
5. Score: each rubric item is 1 (pass) or 0 (fail). Record in the table at the bottom.

## Global rubric (applies to every prompt, 12 points)
| id | item |
|----|------|
| G1 | A design plan (<= 12 lines) exists before the code: palette id, type pairing, surface style, layout, ONE signature move |
| G2 | All colours come from tokens (no stray hex / `bg-white` / `text-black`); contrast verified or tokens from the library |
| G3 | Typography follows a pairing: fluid headings (`clamp`), body >= 16px (15px for dense dev UI), line-height 1.5-1.7, measure <= 70ch |
| G4 | Every interactive element has visible `focus-visible`, hover, active, disabled (and loading where async) |
| G5 | Semantic HTML: one `<h1>`, landmarks, native `button`/`a`/`dialog`/`details`; no `div onClick` |
| G6 | Forms: real labels, hint/error text with icon, `aria-invalid`/`aria-describedby`, correct `type`/`autocomplete` |
| G7 | Loading, empty and error states exist for every data view |
| G8 | Responsive: no horizontal scroll at 320px and 360px, `dvh` not `vh`, touch targets >= 44px |
| G9 | Light and dark themes both work (`color-scheme`, tokens, no-flash script if a toggle exists) |
| G10 | Motion: at most one orchestrated entrance; only transform/opacity; per-element reduced-motion handling |
| G11 | Not generic: passes the swap test and the squint test in `references/anti-generic.md` |
| G12 | Delivery: 3-5 line rationale + complete runnable code + <= 3 next steps; states what was verified; no unrequested deployment/backend essay |

## The ten prompts (each adds specific checks, 3 points each)

**P1 - Marketing landing page.** "Build a landing page for a project-management tool for small construction firms."
- S1 hero has a product-specific focal element (not a stock gradient)  - S2 pricing section with a visually distinct recommended plan that is not colour-only  - S3 one CTA verb repeated consistently

**P2 - Dashboard.** "Create an analytics dashboard for an online tutoring marketplace."
- S1 one hero metric + quiet secondary strip (not 6 equal KPI cards)  - S2 every chart has a text/table alternative  - S3 numbers use `tabular-nums` and show comparison period

**P3 - Auth form.** "Make a sign-up form with email, password and phone (India)."
- S1 `autocomplete`, `inputMode`, `+91` prefix; paste allowed; show/hide password button with `aria-pressed`  - S2 errors appear after blur/submit, with a summary that moves focus  - S3 loading state on submit, no double submit

**P4 - Pricing component.** "Pricing section with three plans and a monthly/yearly switch."
- S1 switch is a real radio group or switch with keyboard support and announces state  - S2 prices formatted for INR with `Intl.NumberFormat('en-IN')`  - S3 recommended plan marked with text, not just border colour

**P5 - Modal.** "A delete-confirmation dialog for a project."
- S1 native `<dialog>` + `showModal()`/`command` (no custom focus trap, no `role="dialog"`)  - S2 safest action first in DOM order; Esc and backdrop dismiss work  - S3 consequence restated in the body; destructive button named "Delete project"

**P6 - Portfolio, bold direction.** "Neo-brutalist portfolio for a photographer."
- S1 one surface style used consistently (brutal)  - S2 accessible despite the noise: contrast >= 4.5, visible focus, no motion-only information  - S3 hover effect disabled/softened under `prefers-reduced-motion`

**P7 - Theme.** "Add dark mode to this React app and a toggle." (provide the starter or a small app)
- S1 `color-scheme` + `<meta name="color-scheme">`, tokens swap, no `bg-white` hard-codes  - S2 no flash of wrong theme (inline script before paint, `try/catch` around storage)  - S3 toggle exposes state (`aria-pressed`) and respects OS preference when nothing is saved

**P8 - Restyle.** "Restyle this plain HTML page to look premium." (provide a 60-line unstyled page)
- S1 content and semantics preserved, not rewritten away  - S2 introduces tokens and one type pairing instead of ad-hoc values  - S3 states what changed and why in 3-5 lines

**P9 - Hindi-first.** "Landing page for a Hindi-first online tuition service, mostly mobile users."
- S1 Devanagari font stack, `lang="hi"`, line-height >= 1.7  - S2 360x800 first, light assets, no autoplay media  - S3 WhatsApp or call CTA as a real link with the right protocol

**P10 - Review.** "Review this UI code for accessibility and design problems." (provide code with 6 planted issues: `div onClick`, `outline-none`, `img` without alt, low-contrast grey text, `100vh` hero, colour-only error)
- S1 finds >= 5 of 6 planted issues  - S2 gives the concrete fix for each (code, not advice)  - S3 does not invent issues that are not there

## Scoring sheet
Max per prompt = 12 (global) + 3 (specific) = 15. Total = 150.

| prompt | baseline (no skill) | with skill | notes / regressions |
|--------|--------------------|-----------|---------------------|
| P1 | /15 | /15 | |
| P2 | /15 | /15 | |
| P3 | /15 | /15 | |
| P4 | /15 | /15 | |
| P5 | /15 | /15 | |
| P6 | /15 | /15 | |
| P7 | /15 | /15 | |
| P8 | /15 | /15 | |
| P9 | /15 | /15 | |
| P10 | /15 | /15 | |
| **total** | /150 | /150 | |

Target: with-skill >= 135/150 (90%) and at least +30% over baseline. Any prompt scoring below 11/15 is a bug in the skill:
find the rubric item that failed, find which instruction was missing, ambiguous or buried, fix it, re-run the whole set.
Record each change and its score in `CHANGELOG` (date, change, before -> after).

## When an output is "normal level" (diagnosis)
| symptom | likely cause in the skill | fix |
|---------|---------------------------|-----|
| ignores the palette/type library | host loaded only `SKILL.md` and not the references | use the Quick picks inline in `SKILL.md`, or the single-file bundle |
| writes essays before code | output contract not followed | tighten the contract wording; check that nothing in the skill demands long preambles |
| generic look despite the skill | plan step skipped | make sure the plan is the first thing in the reply; strengthen the swap test |
| invalid Tailwind classes | host uses Tailwind v3 | state the version up front; run `check_classes.mjs`; add v3 note if the project is on v3 |
| broken dialogs/menus | custom ARIA instead of native elements | point to `components.md` sections 8 and the starter `Dialog` |
