---
name: let-s-code-india-ui-builder
description: Design and build distinctive, accessible, production-ready web UI (landing pages, dashboards, forms, components, themes) with React and Tailwind CSS v4 or plain HTML/CSS. Use whenever the user asks to design, build, restyle, theme or review a web interface, page or component, including Hindi or Indian-audience products. Chooses a verified palette, type pairing and surface style, writes design tokens first, builds state-complete accessible components, then self-reviews against a checklist. Do not use for backend-only work, native mobile apps, or copywriting without UI.
license: MIT
compatibility: Tailwind CSS v4 with React 18/19 and TypeScript, or plain HTML/CSS. Scripts need Python 3.9+ (standard library only) and Node 20+ for the class checker. Works without a shell by reading the reference tables.
metadata:
  author: Ayush Giri
  organization: Let-s-Code-India
  version: "2.0.0"
---

# Let-s-Code-India-UI-Builder

Author: Ayush Giri, Founder, Let-s-Code-India. Version 2.0.0.

Build web UI that looks designed by a person with a point of view, works for everyone, and runs well on a mid-range
Android phone. Quality here comes from decisions made in a fixed order with **verified building blocks** (palettes,
type pairings, components, scripts), not from stronger adjectives. Read this file fully; open other files only when a step needs them.

## 0. Where things are (load on demand)
| need | open |
|------|------|
| choose a palette | `references/palettes.md` (index) -> exact tokens in `references/palette-tokens.md` (search the id) or run `scripts/tokens_to_tailwind.py` |
| choose type | `references/typography.md` or `python3 scripts/font_links.py <n> [--hindi]` |
| surface style, layout recipes, shape, icons, imagery | `references/surfaces.md` |
| components, states, forms | `references/components.md`; working code in `assets/starter/src/components/` |
| motion / accessibility | `references/motion.md` / `references/accessibility.md` |
| start from an archetype | `references/blueprints.md` |
| avoid the generic look | `references/anti-generic.md` |
| worked examples / measuring quality | `references/examples.md` / `evals/prompts.md` |

## 1. Workflow (always in this order)
1. **Ground the brief.** Extract product, audience, primary job, constraints (stack, languages, devices, brand colours, existing code).
   If something essential is missing, state your assumption in one line and continue. Ask at most ONE question, and only if the answer changes the architecture.
   Editing existing code: read it first, keep its conventions, tokens and component names, improve inside them.
2. **Write the design plan (max 12 lines) BEFORE any code:**
   ```
   Subject / audience / job : ...
   Direction (one sentence) : ...
   Palette (id, mode)       : ...        Type pairing (id): ...
   Surface style            : ...        Layout recipes   : ...
   Signature move (ONE)     : ...
   Generic-risk check       : which tell did I avoid / what structural decision did I change?
   ```
   Choose from the libraries by the brief, not by habit (do not reuse last project's combination). For a known archetype start from `references/blueprints.md`,
   then change one structural decision. Run the swap and squint tests in `references/anti-generic.md`.
3. **Tokens first.** Generate or copy the theme: `python3 scripts/tokens_to_tailwind.py --palette <id> --out src/theme.css`
   (brand colours: `--brand "#HEX" --mode dark|light`). No shell: copy a row from section 3 or from `palette-tokens.md`. Set fonts and `data-style`.
   From here on components contain **no raw hex colours**.
4. **Build** small, typed components (copy from `assets/starter/src/components/`, adapt from `components.md`). Order: semantics, layout, states, polish. Mobile first. Real content, no lorem.
5. **Self-review** with section 7; run the scripts when a shell exists; fix what they report before delivering.
6. **Deliver** exactly as section 6 says.

## 2. Rules (each with its reason)
1. **Tokens, not hex.** Use `bg-canvas bg-surface bg-raised border-line border-line-strong text-fg text-muted bg-accent text-accent-fg` and the status colours `success warning danger info`. Reason: every pair is contrast-verified; ad-hoc hex is where accessibility fails.
2. **Area ratio about 60/30/10**: canvas / surfaces / accent. Accent (<= 10%) marks the primary action, the active state and key data. Reason: accent loses meaning when it is everywhere.
3. **One palette, one type pairing (<= 2 families, <= 4 weights), one surface style per product.** Mixing only if the brief asks for the clash. Reason: coherence is what reads as "designed".
4. **Type.** Fluid headings with `clamp()`, body >= 16px (15px dense dev UI), line-height 1.5-1.7, measure <= 70ch, `text-balance` on headings. Body weight >= 400. Hindi: Devanagari companion font, `lang="hi"`, line-height >= 1.7.
5. **Spacing** on the Tailwind scale (multiples of 4); section rhythm `py-16 sm:py-24`; consistent gaps. Reason: rhythm is most of what "polish" means.
6. **State contract** for every interactive element: hover, `focus-visible` (2px accent outline, 2px offset), active, disabled, loading; 44px touch targets. Never remove an outline without a replacement.
7. **Native first.** `button`, `a`, `dialog`, `details`, `popover`, `select`, `progress`. A modal is a native `<dialog>` (no `role="dialog"`, `aria-modal`, or custom focus trap). No `div onClick`. Reason: the browser already solved focus, Esc and semantics.
8. **Colour is never the only signal**: status, selected, error, chart series get icon + text or a pattern.
9. **Forms**: real label, hint, error text + icon, `aria-invalid`/`aria-describedby`, correct `type`/`autocomplete`/`inputMode`, validate on blur and submit.
10. **Five states** for every data view: loading, empty, error, partial, success.
11. **Motion**: one orchestrated entrance, `transform`/`opacity` only, no `transition-all`, reduced motion handled per element. Never the global `animation-duration: 0.01ms` hack.
12. **Responsive**: mobile first; check 320, 360, 768, 1280; `dvh` not `vh`; container queries for reusable cards; no horizontal scroll; `min-w-0`, `truncate`, `break-words` for user content.
13. **Themes**: `<meta name="color-scheme" content="light dark">`, `color-scheme` per theme, no-flash inline script, no hard-coded `bg-white`/`text-black`, storage access in `try/catch`.
14. **Performance**: <= 2 font families, `display=swap`, preconnect; hero image `fetchpriority="high"`, others lazy, with width/height; blur on <= 2 surfaces.
15. **Honest content**: no invented metrics, logos or testimonials; label sample data; specific, plain copy; buttons name actions ("Save changes").
16. **Scope**: build what was asked. No unrequested deployment, backend, auth or database; list them as next steps at most.

## 3. Quick picks (self-sufficient fallback when only this file is available)
Copy a row verbatim into `:root` (and `:root[data-theme="..."]` for the other mode). Never nudge a hex by eye. Full library: 50 palettes in `references/`.
<!-- quickpicks:palettes:start -->
- `clean-minimalist-saas` light (native; default product UI, light-first): `--canvas:#F4F4F5; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDFDF; --line-strong:#8A8A8A; --fg:#171717; --muted:#6B6B6B; --accent:#225BD8; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`
- `clean-minimalist-saas` dark (twin; default product UI, light-first): `--canvas:#101113; --surface:#191A1D; --raised:#202124; --line:#37383B; --line-strong:#6D6E70; --fg:#EEEFF1; --muted:#919294; --accent:#6B95F1; --accent-fg:#0E0F11; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- `midnight-slate` dark (native; dashboards and analytics, dark-first): `--canvas:#0F172A; --surface:#334155; --raised:#39475A; --line:#4D596B; --line-strong:#8F949F; --fg:#ECEEF3; --muted:#B3B6BF; --accent:#79D8E8; --accent-fg:#0C0E12; --success:#6DDFB6; --warning:#FBBF24; --danger:#FCBBBB; --info:#A9CEFC;`
- `midnight-slate` light (twin; dashboards and analytics, dark-first): `--canvas:#F1F3F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#86898D; --fg:#12161C; --muted:#676A6F; --accent:#046D7F; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`
- `warm-sand` light (native; hospitality, wellness, craft, light-first): `--canvas:#FDFBF7; --surface:#F5F2EB; --raised:#FFFFFF; --line:#D7D4CD; --line-strong:#8C8A84; --fg:#1C1912; --muted:#686660; --accent:#9E4908; --accent-fg:#FAFAF9; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`
- `warm-sand` dark (twin; hospitality, wellness, craft, light-first): `--canvas:#18140C; --surface:#241E11; --raised:#2B2518; --line:#413C30; --line-strong:#74716A; --fg:#F3F1EC; --muted:#97948E; --accent:#CE8D5D; --accent-fg:#12100C; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- `royal-velvet` dark (native; luxury, jewellery, hotels, dark-first): `--canvas:#1C1412; --surface:#2D2320; --raised:#332A27; --line:#493F3D; --line-strong:#7B7472; --fg:#F3EEEC; --muted:#A19B99; --accent:#D4AF37; --accent-fg:#120D0C; --success:#34D399; --warning:#FBBF24; --danger:#F97F7F; --info:#60A5FA;`
- `royal-velvet` light (twin; luxury, jewellery, hotels, dark-first): `--canvas:#F5F3F2; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8C8987; --fg:#1A1614; --muted:#6D6A68; --accent:#77621F; --accent-fg:#FAFAF9; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`
<!-- quickpicks:palettes:end -->

Type (Google Fonts URLs only request weights that exist; use these exact strings):
<!-- quickpicks:types:start -->
| id | heading / body | `<link href="..." rel="stylesheet">` |
|----|----------------|------|
| `inter-minimalist` | Inter 700 / Inter 400 | `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap` |
| `plus-jakarta-pro` | Plus Jakarta Sans 700 / Inter 400 | `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Plus+Jakarta+Sans:wght@700&display=swap` |
| `dm-sans-clean` | DM Sans 700 / DM Sans 400 | `https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap` |
| `playfair-editorial` | Playfair Display 700 / Lato 400 | `https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Playfair+Display:wght@700&display=swap` |
<!-- quickpicks:types:end -->
Stacks: sans `system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif`; serif `Georgia, "Times New Roman", serif`. Hindi: add `"Noto Sans Devanagari"` after the Latin family.
Tailwind v4 wiring: `@theme inline { --color-canvas: var(--canvas); --color-fg: var(--fg); ... }` (one line per token, see `assets/starter/src/theme.css`).

## 4. Environment adapters
- **Agent with a shell (Copilot agent mode, Claude Code, Cursor, Codex):** new project -> copy `assets/starter`; run the scripts; finish with `npm run check` (lint + class check + build).
- **Chat with artifacts or canvas:** one self-contained file (React or HTML), tokens inlined as CSS variables, no `localStorage` (theme follows the OS plus an in-memory toggle), no external images, system font stack if fonts cannot load. No scripts available: apply the section 7 checklist by reasoning and say so.
- **Plain HTML/CSS:** same tokens as CSS variables in `:root`, native elements, one `<style>`. Tailwind only if asked (prototype: `<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>`).
- **Existing Tailwind v3 project:** keep the tokens as CSS variables and map them in `tailwind.config` (`colors: { canvas: 'var(--canvas)', ... }`); replace `@theme inline`. Check class names with `check_classes.mjs` only on v4.

## 5. India-first defaults (when the audience is in India or the user writes Hindi)
- Primary viewport 360x800 Android, test 320. Assume mid-range devices and variable 4G: small JS, images <= 80 KB, lazy loading, no autoplay media, light blur and parallax.
- Hindi/Indic text: companion font + `lang`, line-height >= 1.7, no fixed heights on text blocks, test long strings. Language switch (hi/en) persists and is reachable on every page.
- Money and numbers: `new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 })` gives Rs 1,23,456 grouping. Dates `12 Mar 2026`, time labelled IST.
- Inputs: phone `+91` with `inputMode="tel" autoComplete="tel-national"`; PIN `inputMode="numeric"` 6 digits; one "Full name" field; UPI ID with a verify state.
- Contact: real `https://wa.me/<number>` and `tel:` links; do not machine-translate legal text silently.

## 6. Output contract
1. **Rationale (3-5 lines):** palette id + mode, type pairing, surface style, layout, the signature move.
2. **Code:** complete and runnable, with file paths; no placeholders or ellipses; install/run commands only when it is a project.
3. **Verified:** one line saying what you ran or checked, and what you could not.
4. **Next steps:** at most three bullets.
Do not open with a long explanation, do not restate these rules, do not narrate the process. Deployment/backend/auth guidance only on request.

## 7. Final checklist (self-review before delivering)
- [ ] Plan written; the signature move exists and works
- [ ] Every colour comes from a token; contrast at least AA (library or `contrast_check.py`)
- [ ] One `<h1>`, landmarks, skip link, `lang`
- [ ] Focus visible everywhere; whole flow works by keyboard; Esc closes overlays
- [ ] hover / active / disabled / loading defined; loading, empty and error views exist
- [ ] Forms labelled; errors have text + icon
- [ ] No horizontal scroll at 320 and 360; `dvh`; targets >= 44px
- [ ] Light and dark both checked; no theme flash
- [ ] Motion: one entrance, reduced motion handled
- [ ] No fake content; copy is specific
- [ ] `lint_ui.py` 0 errors, `check_classes.mjs` 0 invalid, build passes (when a shell exists)

## 8. Scripts (`scripts/`, standard library only unless noted)
`tokens_to_tailwind.py` theme from palette or brand colour | `contrast_check.py` WCAG ratios, palette and CSS verification | `font_links.py` exact font `<link>` tags and stacks |
`lint_ui.py` static accessibility/theming/performance lint | `check_classes.mjs` exact Tailwind v4 class validity (Node) |
`build_palettes.py`, `build_blueprints.py` regenerate the generated references (never hand-edit `palettes.md`, `palette-tokens.md`, `typography.md`, `blueprints.md`) |
`build_single_file.py` one-file bundle for tools that cannot load references | `selftest.sh` runs every check.
