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

---

# SINGLE-FILE BUNDLE NOTE
This file contains the whole skill. Wherever the playbook above says to open a file under `references/` or `assets/starter/`, find that file's section below (each starts with `## FILE:`). Scripts cannot run from a single file: use the tables and the component source below instead, and state in your delivery that scripted checks were not run.

---

## FILE: references/palettes.md

# Palettes (50) - index

Pick **one** palette per product. Choose by the brief's subject and audience,
not by the first row that looks plausible. Every palette ships with a dark and a light
theme (native mode + a derived twin); every token pair is contrast-verified.

How to get the tokens:
1. Shell available: `python3 scripts/tokens_to_tailwind.py --palette <id> --out src/theme.css`
2. No shell: open `references/palette-tokens.md`, search for the id, copy the one-line
   `--token:value;` strings into `:root` (dark) and `:root[data-theme="light"]` (or the reverse).
3. User has brand colours: `python3 scripts/tokens_to_tailwind.py --brand "#HEX" --mode dark|light`
   derives a full verified token set from one brand colour.

Token meaning: `canvas` page background (~60% of area), `surface` cards/panels (~30%),
`raised` menus/dialogs, `line` decorative borders, `line-strong` input borders (3:1),
`fg` body text, `muted` secondary text, `accent` (<=10%: primary action, active state, key data),
`accent-fg` text on accent, `success|warning|danger|info` status (always with icon + text).

## Cyberpunk & tech - AI start-ups, crypto protocols, developer tools, web3

| # | id | native | canvas | accent | mood |
|---|----|--------|--------|--------|------|
| 01 | `cyber-black-green` | dark | `#0B0B0B` | `#F26969` Crimson Red | security / ops, red alert accent |
| 02 | `neon-matrix` | dark | `#050505` | `#22C55E` Bright Lime | matrix green, hacker culture |
| 03 | `cyberpunk-void` | dark | `#09090B` | `#C48BFA` Neon Purple | neon purple, web3, gaming |
| 04 | `hacker-terminal` | dark | `#0D1117` | `#3FB950` GitHub Green | GitHub-dark feel, dev tools, docs |
| 05 | `dark-synthwave` | dark | `#120A2A` | `#FF7ABC` Neon Pink | retro pink-violet, music, events |
| 06 | `glitch-violet` | dark | `#0A0A12` | `#9597F5` Indigo Glow | indigo glow, AI products |
| 07 | `quantum-teal` | dark | `#030712` | `#1DBBAA` Teal Pop | calm teal, data and science tools |
| 08 | `electric-horizon` | dark | `#020617` | `#38BDF8` Sky Blue | sky blue, cloud and infrastructure |
| 09 | `laser-amber` | dark | `#090D16` | `#F59E0B` Amber Laser | amber on navy, monitoring, ops |
| 10 | `plasma-orange` | dark | `#0F0505` | `#F97316` Plasma Flame | hot orange on black, energy, gaming |

## Luxury & premium - jewellery, architecture studios, boutique hotels, fashion

| # | id | native | canvas | accent | mood |
|---|----|--------|--------|--------|------|
| 11 | `royal-velvet` | dark | `#1C1412` | `#D4AF37` Champagne Gold | champagne gold, jewellery, hotels |
| 12 | `midnight-bronze` | dark | `#141210` | `#E2A03F` Antique Bronze | bronze, fine dining, spirits |
| 13 | `espresso-copper` | dark | `#1A1110` | `#E1953D` Warm Copper | copper warmth, cafe and craft |
| 14 | `sleek-mahogany` | dark | `#1A0F0D` | `#FBBF24` Golden Yellow | golden yellow on mahogany, heritage |
| 15 | `onyx-platinum` | dark | `#0E0E10` | `#E5E7EB` Platinum Silver | silver monochrome, watches, tech luxury |
| 16 | `dark-truffle` | dark | `#1C1917` | `#E19238` Warm Ochre | ochre on warm black, galleries |
| 17 | `classic-noir` | dark | `#0A0A0A` | `#F5F5F4` Pure Ivory | ivory on black, fashion, editorial |
| 18 | `titanium-gold` | dark | `#111827` | `#FBBF24` Rich Gold | navy and gold, private banking |
| 19 | `royal-emerald-gold` | dark | `#062E1C` | `#FDE047` Bright Gold | emerald and gold, heritage brands |
| 20 | `deep-burgundy-gold` | dark | `#2A0808` | `#FCD34D` Gold Accent | burgundy and gold, wine, events |

## Modern SaaS & fintech - enterprise SaaS, analytics, neobanks, finance portals

| # | id | native | canvas | accent | mood |
|---|----|--------|--------|--------|------|
| 21 | `midnight-slate` | dark | `#0F172A` | `#79D8E8` Cyan Spark | slate and cyan, analytics |
| 22 | `deep-fintech` | dark | `#0A0F1D` | `#7AAAF9` Trust Blue | trust blue, neobank, payments |
| 23 | `emerald-growth` | dark | `#121212` | `#34D399` Success Emerald | neutral dark with green, growth |
| 24 | `crypto-obsidian` | dark | `#0B0F19` | `#10B981` Profit Green | profit green, trading |
| 25 | `saas-indigo` | dark | `#030712` | `#8C8EF5` Indigo Pop | indigo, B2B SaaS |
| 26 | `cloud-violet` | dark | `#0F071E` | `#AE8DF9` Vivid Purple | violet, cloud and AI SaaS |
| 27 | `enterprise-navy` | dark | `#090D16` | `#85A8F4` Royal Blue | royal blue, enterprise, HR |
| 28 | `analytics-teal` | dark | `#042F2E` | `#7DE4D7` Bright Teal | deep teal, BI dashboards |
| 29 | `dashboard-rose` | dark | `#18181B` | `#F88095` Alert Rose | rose alerts, admin and ops |
| 30 | `clean-minimalist-saas` | light | `#F4F4F5` | `#225BD8` Action Blue | light, action blue, default product UI |

## Creative, art & Gen-Z - portfolios, indie games, music, streetwear

| # | id | native | canvas | accent | mood |
|---|----|--------|--------|--------|------|
| 31 | `obsidian-fuchsia` | dark | `#18181B` | `#F27FB8` Hot Fuchsia | hot fuchsia, creators, fashion |
| 32 | `electric-sunset` | dark | `#110C1D` | `#F66981` Sunset Coral | coral on violet, music, events |
| 33 | `neon-peach` | dark | `#0F172A` | `#FB923C` Neon Peach | peach on navy, playful apps |
| 34 | `retro-vaporwave` | dark | `#1A0E2E` | `#00F5D4` Mint Neon | mint neon on purple, retro games |
| 35 | `cyber-lime` | dark | `#09090B` | `#84CC16` Electric Lime | electric lime, streetwear, indie |
| 36 | `urban-violet` | dark | `#13111C` | `#C085F9` Electric Purple | electric purple, nightlife |
| 37 | `neon-tangerine` | dark | `#0D0D0D` | `#FF5E2B` Deep Tangerine | tangerine on black, sports, energy |
| 38 | `creative-cyan-dark` | dark | `#080C14` | `#00E5FF` Vivid Cyan | vivid cyan, motion and design studios |
| 39 | `midnight-neon-red` | dark | `#050505` | `#FF4A6D` Sharp Red | sharp red, security, events |
| 40 | `cyber-lemon` | dark | `#0C0A09` | `#EAB308` Neon Lemon | lemon on warm black, bold brands |

## Warm, minimal & organic - wellness, eco start-ups, meditation, craft coffee

| # | id | native | canvas | accent | mood |
|---|----|--------|--------|--------|------|
| 41 | `terracotta-minimal` | light | `#FAF9F5` | `#A3370A` Deep Terracotta | light cream + terracotta, wellness, craft |
| 42 | `warm-sand` | light | `#FDFBF7` | `#9E4908` Warm Ochre | sand and ochre, hospitality |
| 43 | `olive-organic` | dark | `#171A16` | `#84CC16` Fresh Olive | dark olive, farm, eco |
| 44 | `forest-sage` | dark | `#0F1410` | `#10B981` Sage Glow | forest green, sustainability |
| 45 | `desert-dune` | dark | `#1F1A17` | `#E49D4C` Dune Gold | dune gold, travel, outdoor |
| 46 | `warm-minimalist-gray` | light | `#F4F4F5` | `#6D33D1` Deep Violet | light gray + violet, portfolio, blog |
| 47 | `cozy-latte` | light | `#FAF7F2` | `#92400E` Rich Coffee | latte and coffee, bakery, cafe |
| 48 | `autumn-rust` | dark | `#1C1210` | `#EF8046` Rust Accent | rust on brown-black, craft, seasonal |
| 49 | `clean-slate-light` | light | `#F1F5F9` | `#0F172A` Dark Slate | light slate, docs, legal, tax |
| 50 | `earthy-moss` | dark | `#111412` | `#7BB02F` Moss Green | moss green, agriculture, outdoor |

All 100 theme rows verified by `scripts/contrast_check.py --palettes`: `fg` >= 7:1, `muted`, `accent`,
status colours and `accent-fg` on `accent` >= 4.5:1, `line-strong` >= 3:1, against canvas, surface and raised.

---

## FILE: references/palette-tokens.md

# Palette tokens (exact values)

Look up ONE palette by id (search the `###` heading). Do not read the whole file.
Copy the values verbatim; never nudge a hex by eye (contrast was verified for these exact values).
`brand-2` (when present) is a decorative second colour - never for text or card backgrounds.

### 01 cyber-black-green  (Cyber Black-Green, native: dark)
- dark (native): `--canvas:#0B0B0B; --surface:#1A1A1A; --raised:#212121; --line:#383838; --line-strong:#6B6B6B; --fg:#F0F0F0; --muted:#909090; --accent:#F26969; --accent-fg:#0F0F0F; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA; --brand-2:#10B981;`
- light (twin): `--canvas:#F4F3F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8A8989; --fg:#181616; --muted:#6C6A6A; --accent:#B13232; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8; --brand-2:#10B981;`

### 02 neon-matrix  (Neon Matrix, native: dark)
- dark (native): `--canvas:#050505; --surface:#191919; --raised:#222222; --line:#373737; --line-strong:#6C6C6C; --fg:#F0F0F0; --muted:#8D8D8D; --accent:#22C55E; --accent-fg:#0F0F0F; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA; --brand-2:#047857;`
- light (twin): `--canvas:#F3F4F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDFDE; --line-strong:#898A89; --fg:#161816; --muted:#6A6C6A; --accent:#147237; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8; --brand-2:#047857;`

### 03 cyberpunk-void  (Cyberpunk Void, native: dark)
- dark (native): `--canvas:#09090B; --surface:#27272A; --raised:#2D2D30; --line:#434346; --line-strong:#777779; --fg:#EEEEF1; --muted:#97979A; --accent:#C48BFA; --accent-fg:#0E0E11; --success:#34D399; --warning:#FBBF24; --danger:#F97F7F; --info:#66A9FA;`
- light (twin): `--canvas:#F3F3F4; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#89898A; --fg:#161618; --muted:#6A6A6C; --accent:#8342C1; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 04 hacker-terminal  (Hacker Terminal, native: dark)
- dark (native): `--canvas:#0D1117; --surface:#161B22; --raised:#1D2229; --line:#34393F; --line-strong:#6B6E73; --fg:#ECEFF3; --muted:#8E9297; --accent:#3FB950; --accent-fg:#0C0F12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F2F3F5; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#87898C; --fg:#14161A; --muted:#686A6D; --accent:#277332; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 05 dark-synthwave  (Dark Synthwave, native: dark)
- dark (native): `--canvas:#120A2A; --surface:#2D1B69; --raised:#33226E; --line:#48387C; --line-strong:#7C768A; --fg:#EEECF3; --muted:#A39FAF; --accent:#FF7ABC; --accent-fg:#0E0C12; --success:#34D399; --warning:#FBBF24; --danger:#F98585; --info:#6AAAFA;`
- light (twin): `--canvas:#F2F1F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#8C8A92; --fg:#14121C; --muted:#68676F; --accent:#BD005E; --accent-fg:#FAF9FA; --success:#127136; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 06 glitch-violet  (Glitch Violet, native: dark)
- dark (native): `--canvas:#0A0A12; --surface:#1E1B4B; --raised:#252250; --line:#3B3863; --line-strong:#72727A; --fg:#ECECF3; --muted:#96969E; --accent:#9597F5; --accent-fg:#0C0C12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F2F2F5; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#87878C; --fg:#14141A; --muted:#68686D; --accent:#5154C6; --accent-fg:#F9F9FA; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 07 quantum-teal  (Quantum Teal, native: dark)
- dark (native): `--canvas:#030712; --surface:#1F2937; --raised:#262F3D; --line:#3C4551; --line-strong:#787A82; --fg:#ECEEF3; --muted:#9D9FA6; --accent:#1DBBAA; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F98282; --info:#6AAAFA;`
- light (twin): `--canvas:#F1F2F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#8A8C92; --fg:#12141C; --muted:#67686F; --accent:#0C6E64; --accent-fg:#F9FAFA; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 08 electric-horizon  (Electric Horizon, native: dark)
- dark (native): `--canvas:#020617; --surface:#0F172A; --raised:#192033; --line:#2E3546; --line-strong:#696C78; --fg:#ECEEF3; --muted:#8A8D97; --accent:#38BDF8; --accent-fg:#0C0D12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F1F2F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#8A8C92; --fg:#12141C; --muted:#67686F; --accent:#1F6A8B; --accent-fg:#F9FAFA; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 09 laser-amber  (Laser Amber, native: dark)
- dark (native): `--canvas:#090D16; --surface:#1E293B; --raised:#252F41; --line:#3B4555; --line-strong:#767980; --fg:#ECEEF3; --muted:#96989F; --accent:#F59E0B; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F98282; --info:#6AAAFA;`
- light (twin): `--canvas:#F1F3F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#86898D; --fg:#12161C; --muted:#676A6F; --accent:#895806; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 10 plasma-orange  (Plasma Orange, native: dark)
- dark (native): `--canvas:#0F0505; --surface:#260D0D; --raised:#2F1717; --line:#432C2C; --line-strong:#6F6666; --fg:#F3ECEC; --muted:#938B8B; --accent:#F97316; --accent-fg:#120C0C; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F6F1F1; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#928A8A; --fg:#1C1212; --muted:#6F6767; --accent:#9F4A0E; --accent-fg:#FAF9F9; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 11 royal-velvet  (Royal Velvet, native: dark)
- dark (native): `--canvas:#1C1412; --surface:#2D2320; --raised:#332A27; --line:#493F3D; --line-strong:#7B7472; --fg:#F3EEEC; --muted:#A19B99; --accent:#D4AF37; --accent-fg:#120D0C; --success:#34D399; --warning:#FBBF24; --danger:#F97F7F; --info:#60A5FA;`
- light (twin): `--canvas:#F5F3F2; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8C8987; --fg:#1A1614; --muted:#6D6A68; --accent:#77621F; --accent-fg:#FAFAF9; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 12 midnight-bronze  (Midnight Bronze, native: dark)
- dark (native): `--canvas:#141210; --surface:#26221D; --raised:#2D2924; --line:#423F3A; --line-strong:#757472; --fg:#F1F0EE; --muted:#949391; --accent:#E2A03F; --accent-fg:#110F0E; --success:#34D399; --warning:#FBBF24; --danger:#F87777; --info:#60A5FA;`
- light (twin): `--canvas:#F4F4F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDFDE; --line-strong:#8A8A89; --fg:#181816; --muted:#6C6C6A; --accent:#835D25; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 13 espresso-copper  (Espresso Copper, native: dark)
- dark (native): `--canvas:#1A1110; --surface:#33221E; --raised:#392925; --line:#4E3E3B; --line-strong:#7E7675; --fg:#F3EDEC; --muted:#A19998; --accent:#E1953D; --accent-fg:#120D0C; --success:#34D399; --warning:#FBBF24; --danger:#F97F7F; --info:#63A7FA;`
- light (twin): `--canvas:#F5F3F2; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8C8987; --fg:#1A1614; --muted:#6D6A68; --accent:#985304; --accent-fg:#FAFAF9; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 14 sleek-mahogany  (Sleek Mahogany, native: dark)
- dark (native): `--canvas:#1A0F0D; --surface:#3D231E; --raised:#432A25; --line:#563F3B; --line-strong:#827A78; --fg:#F3EDEC; --muted:#A19997; --accent:#FBBF24; --accent-fg:#120D0C; --success:#34D399; --warning:#FBBF24; --danger:#F98888; --info:#6AAAFA;`
- light (twin): `--canvas:#F5F2F2; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8C8787; --fg:#1A1414; --muted:#6D6868; --accent:#7D5F12; --accent-fg:#FAF9F9; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 15 onyx-platinum  (Onyx Platinum, native: dark)
- dark (native): `--canvas:#0E0E10; --surface:#232329; --raised:#2A2A2F; --line:#404045; --line-strong:#767678; --fg:#EFEFF1; --muted:#9A9A9C; --accent:#E5E7EB; --accent-fg:#0E0E10; --success:#34D399; --warning:#FBBF24; --danger:#F87A7A; --info:#60A5FA;`
- light (twin): `--canvas:#F3F3F4; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#89898A; --fg:#161618; --muted:#6A6A6C; --accent:#606163; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 16 dark-truffle  (Dark Truffle, native: dark)
- dark (native): `--canvas:#1C1917; --surface:#292524; --raised:#2F2C2B; --line:#454140; --line-strong:#7A7776; --fg:#F1EFEE; --muted:#989594; --accent:#E19238; --accent-fg:#110F0E; --success:#34D399; --warning:#FBBF24; --danger:#F97F7F; --info:#63A7FA;`
- light (twin): `--canvas:#F4F3F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8A8989; --fg:#181616; --muted:#6C6A6A; --accent:#985304; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 17 classic-noir  (Classic Noir, native: dark)
- dark (native): `--canvas:#0A0A0A; --surface:#1F1F1F; --raised:#262626; --line:#3C3C3C; --line-strong:#6F6F6F; --fg:#F0F0F0; --muted:#8F8F8F; --accent:#F5F5F4; --accent-fg:#0F0F0F; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F4F4F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDFDE; --line-strong:#8A8A89; --fg:#181816; --muted:#6C6C6A; --accent:#626262; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 18 titanium-gold  (Titanium Gold, native: dark)
- dark (native): `--canvas:#111827; --surface:#1F2937; --raised:#262F3D; --line:#3C4551; --line-strong:#767A85; --fg:#ECEEF3; --muted:#999DA5; --accent:#FBBF24; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F98282; --info:#6AAAFA;`
- light (twin): `--canvas:#F1F3F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#86898D; --fg:#12161C; --muted:#676A6F; --accent:#7D5F12; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 19 royal-emerald-gold  (Royal Emerald Gold, native: dark)
- dark (native): `--canvas:#062E1C; --surface:#0D4A2D; --raised:#175135; --line:#2C6248; --line-strong:#82988E; --fg:#ECF3F0; --muted:#B0C0B9; --accent:#FDE047; --accent-fg:#0C1210; --success:#71E0B8; --warning:#FBBF24; --danger:#FCB8B8; --info:#ACD0FC;`
- light (twin): `--canvas:#F1F6F4; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDFDF; --line-strong:#868D8A; --fg:#121C18; --muted:#676F6C; --accent:#6F631F; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 20 deep-burgundy-gold  (Deep Burgundy Gold, native: dark)
- dark (native): `--canvas:#2A0808; --surface:#4A0E0E; --raised:#511818; --line:#622D2D; --line-strong:#867171; --fg:#F3ECEC; --muted:#A79595; --accent:#FCD34D; --accent-fg:#120C0C; --success:#34D399; --warning:#FBBF24; --danger:#F97F7F; --info:#60A5FA;`
- light (twin): `--canvas:#F6F1F1; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#928A8A; --fg:#1C1212; --muted:#6F6767; --accent:#746123; --accent-fg:#FAF9F9; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 21 midnight-slate  (Midnight Slate, native: dark)
- dark (native): `--canvas:#0F172A; --surface:#334155; --raised:#39475A; --line:#4D596B; --line-strong:#8F949F; --fg:#ECEEF3; --muted:#B3B6BF; --accent:#79D8E8; --accent-fg:#0C0E12; --success:#6DDFB6; --warning:#FBBF24; --danger:#FCBBBB; --info:#A9CEFC;`
- light (twin): `--canvas:#F1F3F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#86898D; --fg:#12161C; --muted:#676A6F; --accent:#046D7F; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 22 deep-fintech  (Deep FinTech, native: dark)
- dark (native): `--canvas:#0A0F1D; --surface:#1E293B; --raised:#252F41; --line:#3B4555; --line-strong:#767A84; --fg:#ECEEF3; --muted:#9699A2; --accent:#7AAAF9; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F98282; --info:#6AAAFA;`
- light (twin): `--canvas:#F1F2F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#8A8C92; --fg:#12141C; --muted:#67686F; --accent:#2C60B6; --accent-fg:#F9FAFA; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 23 emerald-growth  (Emerald Growth, native: dark)
- dark (native): `--canvas:#121212; --surface:#1E1E1E; --raised:#252525; --line:#3B3B3B; --line-strong:#6F6F6F; --fg:#F0F0F0; --muted:#939393; --accent:#34D399; --accent-fg:#0F0F0F; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F3F4F4; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDFDF; --line-strong:#898A8A; --fg:#161818; --muted:#6A6C6C; --accent:#1C7253; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 24 crypto-obsidian  (Crypto Obsidian, native: dark)
- dark (native): `--canvas:#0B0F19; --surface:#172033; --raised:#1E2739; --line:#353D4E; --line-strong:#6E7179; --fg:#ECEEF3; --muted:#8E9097; --accent:#10B981; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F2F3F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#87888D; --fg:#13151B; --muted:#68696E; --accent:#0A6F4D; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 25 saas-indigo  (SaaS Indigo, native: dark)
- dark (native): `--canvas:#030712; --surface:#111827; --raised:#1B2130; --line:#303644; --line-strong:#6A6D75; --fg:#ECEEF3; --muted:#8A8D94; --accent:#8C8EF5; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F1F2F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#8A8C92; --fg:#12141C; --muted:#67686F; --accent:#5154C6; --accent-fg:#F9FAFA; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 26 cloud-violet  (Cloud Violet, native: dark)
- dark (native): `--canvas:#0F071E; --surface:#1E1B4B; --raised:#252250; --line:#3B3863; --line-strong:#767080; --fg:#EFECF3; --muted:#9A95A2; --accent:#AE8DF9; --accent-fg:#0E0C12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F3F1F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#8D8A92; --fg:#16121C; --muted:#6A676F; --accent:#6F4AC5; --accent-fg:#FAF9FA; --success:#127136; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 27 enterprise-navy  (Enterprise Navy, native: dark)
- dark (native): `--canvas:#090D16; --surface:#1E293B; --raised:#252F41; --line:#3B4555; --line-strong:#767980; --fg:#ECEEF3; --muted:#96989F; --accent:#85A8F4; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F98282; --info:#6AAAFA;`
- light (twin): `--canvas:#F1F3F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#86898D; --fg:#12161C; --muted:#676A6F; --accent:#2159D4; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 28 analytics-teal  (Analytics Teal, native: dark)
- dark (native): `--canvas:#042F2E; --surface:#134E4A; --raised:#1A534F; --line:#316562; --line-strong:#869D9C; --fg:#ECF3F3; --muted:#B0C0C0; --accent:#7DE4D7; --accent-fg:#0C1212; --success:#81E4C0; --warning:#FCC843; --danger:#FCC1C1; --info:#B3D4FD;`
- light (twin): `--canvas:#F1F6F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDFDF; --line-strong:#868D8D; --fg:#121C1C; --muted:#676F6F; --accent:#176E63; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 29 dashboard-rose  (Dashboard Rose, native: dark)
- dark (native): `--canvas:#18181B; --surface:#27272A; --raised:#2D2D30; --line:#434346; --line-strong:#777779; --fg:#EFEFF1; --muted:#9D9DA0; --accent:#F88095; --accent-fg:#0E0E10; --success:#34D399; --warning:#FBBF24; --danger:#F97F7F; --info:#66A9FA;`
- light (twin): `--canvas:#F3F3F4; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#89898A; --fg:#161618; --muted:#6A6A6C; --accent:#B52F46; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 30 clean-minimalist-saas  (Clean Minimalist SaaS, native: light)
- light (native): `--canvas:#F4F4F5; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDFDF; --line-strong:#8A8A8A; --fg:#171717; --muted:#6B6B6B; --accent:#225BD8; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`
- dark (twin): `--canvas:#101113; --surface:#191A1D; --raised:#202124; --line:#37383B; --line-strong:#6D6E70; --fg:#EEEFF1; --muted:#919294; --accent:#6B95F1; --accent-fg:#0E0F11; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`

### 31 obsidian-fuchsia  (Obsidian Fuchsia, native: dark)
- dark (native): `--canvas:#18181B; --surface:#27272A; --raised:#2D2D30; --line:#434346; --line-strong:#777779; --fg:#EFEFF1; --muted:#9D9DA0; --accent:#F27FB8; --accent-fg:#0E0E10; --success:#34D399; --warning:#FBBF24; --danger:#F97F7F; --info:#66A9FA;`
- light (twin): `--canvas:#F3F3F4; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#89898A; --fg:#161618; --muted:#6A6A6C; --accent:#AA346E; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 32 electric-sunset  (Electric Sunset, native: dark)
- dark (native): `--canvas:#110C1D; --surface:#221738; --raised:#291E3E; --line:#3F3552; --line-strong:#726F7B; --fg:#EEECF3; --muted:#918E99; --accent:#F66981; --accent-fg:#0E0C12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F3F1F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#8D8A92; --fg:#16121C; --muted:#6A676F; --accent:#B52F46; --accent-fg:#FAF9FA; --success:#127136; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 33 neon-peach  (Neon Peach, native: dark)
- dark (native): `--canvas:#0F172A; --surface:#1E293B; --raised:#252F41; --line:#3B4555; --line-strong:#757A86; --fg:#ECEEF3; --muted:#989CA7; --accent:#FB923C; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F98282; --info:#6AAAFA;`
- light (twin): `--canvas:#F1F3F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#86898D; --fg:#12161C; --muted:#676A6F; --accent:#925523; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 34 retro-vaporwave  (Retro Vaporwave, native: dark)
- dark (native): `--canvas:#1A0E2E; --surface:#2D1654; --raised:#351F5B; --line:#48346A; --line-strong:#7C7489; --fg:#EFECF3; --muted:#9E98A8; --accent:#00F5D4; --accent-fg:#0F0C12; --success:#34D399; --warning:#FBBF24; --danger:#F97C7C; --info:#60A5FA;`
- light (twin): `--canvas:#F3F1F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#8D8A92; --fg:#16121C; --muted:#6A676F; --accent:#006C5D; --accent-fg:#FAF9FA; --success:#127136; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 35 cyber-lime  (Cyber Lime, native: dark)
- dark (native): `--canvas:#09090B; --surface:#18181B; --raised:#212124; --line:#363639; --line-strong:#6E6E70; --fg:#EEEEF1; --muted:#8E8E90; --accent:#84CC16; --accent-fg:#0E0E11; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F3F3F4; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#89898A; --fg:#161618; --muted:#6A6A6C; --accent:#476E0C; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 36 urban-violet  (Urban Violet, native: dark)
- dark (native): `--canvas:#13111C; --surface:#231F33; --raised:#2A2639; --line:#3F3C4E; --line-strong:#73717B; --fg:#EEECF3; --muted:#929099; --accent:#C085F9; --accent-fg:#0D0C12; --success:#34D399; --warning:#FBBF24; --danger:#F87474; --info:#60A5FA;`
- light (twin): `--canvas:#F3F2F5; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#89878C; --fg:#16141A; --muted:#6A686D; --accent:#8342C1; --accent-fg:#FAF9FA; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`

### 37 neon-tangerine  (Neon Tangerine, native: dark)
- dark (native): `--canvas:#0D0D0D; --surface:#1A1A1A; --raised:#212121; --line:#383838; --line-strong:#6C6C6C; --fg:#F0F0F0; --muted:#919191; --accent:#FF5E2B; --accent-fg:#0F0F0F; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F4F3F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8A8989; --fg:#181616; --muted:#6C6A6A; --accent:#AD3B17; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 38 creative-cyan-dark  (Creative Cyan Dark, native: dark)
- dark (native): `--canvas:#080C14; --surface:#131C2E; --raised:#1A2334; --line:#313A4A; --line-strong:#6C7076; --fg:#ECEFF3; --muted:#8C9095; --accent:#00E5FF; --accent-fg:#0C0E12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F1F3F6; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDEDF; --line-strong:#86898D; --fg:#12161C; --muted:#676A6F; --accent:#006E7A; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 39 midnight-neon-red  (Midnight Neon Red, native: dark)
- dark (native): `--canvas:#050505; --surface:#141414; --raised:#1D1D1D; --line:#333333; --line-strong:#686868; --fg:#F0F0F0; --muted:#8D8D8D; --accent:#FF4A6D; --accent-fg:#0F0F0F; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F4F3F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8A8989; --fg:#181616; --muted:#6C6A6A; --accent:#C21134; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 40 cyber-lemon  (Cyber Lemon, native: dark)
- dark (native): `--canvas:#0C0A09; --surface:#1C1917; --raised:#252220; --line:#3A3735; --line-strong:#716F6E; --fg:#F2EFEE; --muted:#918F8E; --accent:#EAB308; --accent-fg:#110F0D; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`
- light (twin): `--canvas:#F4F3F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8A8989; --fg:#181616; --muted:#6C6A6A; --accent:#7A5D04; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 41 terracotta-minimal  (Terracotta Minimal, native: light)
- light (native): `--canvas:#FAF9F5; --surface:#E7E5E4; --raised:#FFFFFF; --line:#CBC9C7; --line-strong:#82817A; --fg:#1C1A12; --muted:#5F5D56; --accent:#A3370A; --accent-fg:#FAFAF9; --success:#116932; --warning:#944407; --danger:#B21B1B; --info:#1C4CD4;`
- dark (twin): `--canvas:#16140E; --surface:#211F15; --raised:#28261C; --line:#3E3C33; --line-strong:#73716B; --fg:#F3F1EC; --muted:#96948F; --accent:#D98968; --accent-fg:#12110C; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`

### 42 warm-sand  (Warm Sand, native: light)
- light (native): `--canvas:#FDFBF7; --surface:#F5F2EB; --raised:#FFFFFF; --line:#D7D4CD; --line-strong:#8C8A84; --fg:#1C1912; --muted:#686660; --accent:#9E4908; --accent-fg:#FAFAF9; --success:#137337; --warning:#9E4908; --danger:#B91C1C; --info:#1D4ED8;`
- dark (twin): `--canvas:#18140C; --surface:#241E11; --raised:#2B2518; --line:#413C30; --line-strong:#74716A; --fg:#F3F1EC; --muted:#97948E; --accent:#CE8D5D; --accent-fg:#12100C; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`

### 43 olive-organic  (Olive Organic, native: dark)
- dark (native): `--canvas:#171A16; --surface:#262A24; --raised:#2D302B; --line:#424640; --line-strong:#767975; --fg:#EFF1EE; --muted:#9D9F9C; --accent:#84CC16; --accent-fg:#0F110E; --success:#34D399; --warning:#FBBF24; --danger:#F98585; --info:#6AAAFA;`
- light (twin): `--canvas:#F3F4F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDFDE; --line-strong:#898A89; --fg:#161816; --muted:#6A6C6A; --accent:#476E0C; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 44 forest-sage  (Forest Sage, native: dark)
- dark (native): `--canvas:#0F1410; --surface:#1C241E; --raised:#232B25; --line:#39413B; --line-strong:#717672; --fg:#EEF2EE; --muted:#909591; --accent:#10B981; --accent-fg:#0D110E; --success:#34D399; --warning:#FBBF24; --danger:#F87777; --info:#60A5FA;`
- light (twin): `--canvas:#F3F4F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDFDE; --line-strong:#898A89; --fg:#161816; --muted:#6A6C6A; --accent:#0A7350; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 45 desert-dune  (Desert Dune, native: dark)
- dark (native): `--canvas:#1F1A17; --surface:#332A25; --raised:#39302C; --line:#4E4641; --line-strong:#807C79; --fg:#F2EFED; --muted:#A29E9C; --accent:#E49D4C; --accent-fg:#120F0D; --success:#34D399; --warning:#FBBF24; --danger:#F98D8D; --info:#70AEFA;`
- light (twin): `--canvas:#F4F3F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8A8989; --fg:#181616; --muted:#6C6A6A; --accent:#985304; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 46 warm-minimalist-gray  (Warm Minimalist Gray, native: light)
- light (native): `--canvas:#F4F4F5; --surface:#E4E4E7; --raised:#FFFFFF; --line:#C7C7CA; --line-strong:#818182; --fg:#161618; --muted:#616163; --accent:#6D33D1; --accent-fg:#FAFAFA; --success:#116932; --warning:#944407; --danger:#AE1A1A; --info:#1C4CD4;`
- dark (twin): `--canvas:#101013; --surface:#19191D; --raised:#222226; --line:#37373B; --line-strong:#6D6D70; --fg:#EEEEF1; --muted:#919194; --accent:#AB81F3; --accent-fg:#0E0E11; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`

### 47 cozy-latte  (Cozy Latte, native: light)
- light (native): `--canvas:#FAF7F2; --surface:#EFECE6; --raised:#FFFFFF; --line:#D1CEC8; --line-strong:#87837E; --fg:#1C1812; --muted:#67645E; --accent:#92400E; --accent-fg:#FAFAF9; --success:#126E34; --warning:#9B4708; --danger:#B91C1C; --info:#1D4ED8;`
- dark (twin): `--canvas:#17130C; --surface:#231D12; --raised:#2A2419; --line:#403B31; --line-strong:#73706A; --fg:#F3F1EC; --muted:#97948E; --accent:#C09073; --accent-fg:#12100C; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`

### 48 autumn-rust  (Autumn Rust, native: dark)
- dark (native): `--canvas:#1C1210; --surface:#2B1D1A; --raised:#312421; --line:#473A37; --line-strong:#766E6C; --fg:#F3EDEC; --muted:#999190; --accent:#EF8046; --accent-fg:#120D0C; --success:#34D399; --warning:#FBBF24; --danger:#F87474; --info:#60A5FA;`
- light (twin): `--canvas:#F5F3F2; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DFDEDE; --line-strong:#8C8987; --fg:#1A1614; --muted:#6D6A68; --accent:#AD4109; --accent-fg:#FAFAF9; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

### 49 clean-slate-light  (Clean Slate Light, native: light)
- light (native): `--canvas:#F1F5F9; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDFDF; --line-strong:#868A8F; --fg:#12171C; --muted:#676B70; --accent:#0F172A; --accent-fg:#F9FAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`
- dark (twin): `--canvas:#0D1217; --surface:#131B22; --raised:#1A2229; --line:#31393F; --line-strong:#6B6F73; --fg:#ECF0F3; --muted:#858A8E; --accent:#9599A1; --accent-fg:#0C0F12; --success:#34D399; --warning:#FBBF24; --danger:#F87171; --info:#60A5FA;`

### 50 earthy-moss  (Earthy Moss, native: dark)
- dark (native): `--canvas:#111412; --surface:#1E2420; --raised:#252B27; --line:#3B413D; --line-strong:#727573; --fg:#EEF1EF; --muted:#919492; --accent:#7BB02F; --accent-fg:#0E110F; --success:#34D399; --warning:#FBBF24; --danger:#F87777; --info:#60A5FA;`
- light (twin): `--canvas:#F3F4F3; --surface:#FFFFFF; --raised:#FFFFFF; --line:#DEDFDE; --line-strong:#898A89; --fg:#161816; --muted:#6A6C6A; --accent:#456F09; --accent-fg:#FAFAFA; --success:#137337; --warning:#A24B08; --danger:#B91C1C; --info:#1D4ED8;`

---

## FILE: references/typography.md

# Typography (50 pairings, verified loading)

Pick ONE pairing (max two families). Choose by the product's voice, not by habit: an
Inter + purple-gradient look is the generic default. Serif/display faces carry personality;
use them for headings and keep a quiet sans for body text.

## Rules
- Body text weight >= 400 and size >= 16px (15px only for dense developer UIs). Light (300) is for large display text only.
- Body line-height 1.5-1.7, measure <= 70ch (`max-w-prose`). Serif body gets slightly more leading than sans.
- Fluid headings with `clamp()`: h1 `clamp(2.25rem, 1.2rem + 4.5vw, 4.5rem)`, h2 `clamp(1.75rem, 1.1rem + 2.4vw, 3rem)`,
  h3 `clamp(1.25rem, 1rem + 1vw, 1.75rem)`. Never `vw` alone. Tight tracking only on large display sizes (`tracking-tight`).
- Load at most 2 families and ~4 weights, with `display=swap`. Preconnect to the font hosts.
- Fontshare families (Satoshi, General Sans, Cabinet Grotesk, Clash Display) are NOT on Google Fonts: use the Fontshare URL.
- Google Fonts returns HTTP 400 for a weight a family lacks (e.g. Bebas Neue has only 400): use the URLs below or
  `python3 scripts/font_links.py <id>`; never hand-write the weights.
- Hindi / Devanagari: append `"Noto Sans Devanagari"` (serif pairings: `"Noto Serif Devanagari"`) after the Latin family in the stack,
  set `lang="hi"` on the element, and give Devanagari body text line-height >= 1.7. `font_links.py <id> --hindi` does this.
- Avoid typographic tells: accenting a single headline word, tracked ALL-CAPS eyebrow above every heading, `A · B · C` meta strings.

## Pairings

| # | id | heading | body | type | source | px/leading | best for |
|---|----|---------|------|------|--------|-----------|----------|
| 01 | `inter-minimalist` | Inter 700 | Inter 400 | sans/sans | Google | 16/1.5 | any product UI, dashboards |
| 02 | `geist-developer` | Geist Mono 600 | Geist 400 | mono/sans | Google | 15/1.6 | developer tools, docs |
| 03 | `outfit-creative` | Outfit 800 | Plus Jakarta Sans 400 | sans/sans | Google | 16/1.5 | creative agencies, apps |
| 04 | `plus-jakarta-pro` | Plus Jakarta Sans 700 | Inter 400 | sans/sans | Google | 16/1.55 | SaaS marketing, fintech |
| 05 | `space-grotesk-cyber` | Space Grotesk 700 | Inter 400 | sans/sans | Google | 16/1.6 | AI / web3 / cyber |
| 06 | `cabinet-grotesk-bold` | Cabinet Grotesk 700 | General Sans 400 | display/sans | Fontshare | 16/1.5 | bold brands, studios |
| 07 | `syne-futuristic` | Syne 800 | DM Sans 400 | sans/sans | Google | 16/1.6 | art, music, experimental |
| 08 | `clash-display-tech` | Clash Display 700 | Satoshi 400 | display/sans | Fontshare | 16/1.5 | tech launches, hero-led pages |
| 09 | `satoshi-minimal` | Satoshi 700 | Inter 400 | sans/sans | Fontshare+Google | 16/1.5 | minimal brands, portfolios |
| 10 | `general-sans-corporate` | General Sans 600 | Plus Jakarta Sans 400 | sans/sans | Fontshare+Google | 16/1.55 | corporate, B2B |
| 11 | `playfair-editorial` | Playfair Display 700 | Lato 400 | serif/sans | Google | 18/1.7 | magazines, fashion |
| 12 | `cormorant-luxury` | Cormorant Garamond 600 | Montserrat 400 | serif/sans | Google | 17/1.75 | jewellery, hotels, luxury |
| 13 | `cinzel-royal` | Cinzel 700 | Open Sans 400 | serif/sans | Google | 16/1.6 | heritage, events, wine |
| 14 | `instrument-serif-noir` | Instrument Serif 400 italic | Plus Jakarta Sans 400 | serif/sans | Google | 16/1.6 | editorial, restaurants |
| 15 | `bodoni-classic` | Bodoni Moda 700 | Inter 400 | serif/sans | Google | 16/1.6 | fashion, galleries |
| 16 | `prata-elegant` | Prata 400 | DM Sans 400 | serif/sans | Google | 17/1.65 | architecture, boutique |
| 17 | `lora-warm-editorial` | Lora 700 | Inter 400 | serif/sans | Google | 16/1.7 | blogs, long reads, cafes |
| 18 | `eb-garamond-vintage` | EB Garamond 500 | Source Serif 4 400 | serif/serif | Google | 18/1.75 | books, heritage, journals |
| 19 | `fraunces-modern-serif` | Fraunces 600 | Plus Jakarta Sans 400 | serif/sans | Google | 16/1.6 | friendly editorial, food |
| 20 | `merriweather-classic` | Merriweather 700 | Open Sans 400 | serif/sans | Google | 16/1.65 | news, education |
| 21 | `fira-code-terminal` | Fira Code 700 | Inter 400 | mono/sans | Google | 15/1.6 | terminals, dev blogs |
| 22 | `jetbrains-mono-coder` | JetBrains Mono 600 | Plus Jakarta Sans 400 | mono/sans | Google | 15/1.65 | IDE-like products |
| 23 | `space-mono-hacker` | Space Mono 700 | DM Sans 400 | mono/sans | Google | 15/1.6 | retro-tech, hackathons |
| 24 | `ibm-plex-tech` | IBM Plex Mono 700 | IBM Plex Sans 400 | mono/sans | Google | 16/1.55 | engineering, enterprise tech |
| 25 | `source-code-pro` | Source Code Pro 700 | Source Sans 3 400 | mono/sans | Google | 15/1.6 | docs, code-heavy pages |
| 26 | `inconsolata-clean` | Inconsolata 700 | Inter 400 | mono/sans | Google | 16/1.5 | light terminal looks |
| 27 | `anonymous-pro-retro` | Anonymous Pro 700 | Roboto 400 | mono/sans | Google | 15/1.55 | retro computing |
| 28 | `ubuntu-tech-vibe` | Ubuntu 700 | Ubuntu Condensed 400 | sans/sans | Google | 16/1.5 | linux, open-source communities |
| 29 | `share-tech-mono` | Share Tech Mono 400 | Inter 400 | mono/sans | Google | 15/1.6 | HUD, sci-fi interfaces |
| 30 | `red-hat-mono` | Red Hat Mono 700 | Red Hat Display 400 | mono/sans | Google | 16/1.55 | cloud, infrastructure |
| 31 | `roboto-standard` | Roboto 500 | Roboto 400 | sans/sans | Google | 16/1.5 | neutral utility apps |
| 32 | `open-sans-corporate` | Open Sans 700 | Open Sans 400 | sans/sans | Google | 16/1.6 | government, NGOs, legal |
| 33 | `montserrat-clean` | Montserrat 700 | Inter 400 | sans/sans | Google | 16/1.5 | agencies, startups |
| 34 | `lato-professional` | Lato 700 | Lato 400 | sans/sans | Google | 16/1.6 | professional services |
| 35 | `poppins-vibrant` | Poppins 600 | Open Sans 400 | sans/sans | Google | 16/1.55 | consumer apps, education (Devanagari-capable heading) |
| 36 | `work-sans-modern` | Work Sans 700 | Work Sans 400 | sans/sans | Google | 16/1.5 | modern business sites |
| 37 | `nunito-rounded` | Nunito 700 | Nunito 400 | sans/sans | Google | 16/1.6 | kids, health, friendly apps |
| 38 | `quicksand-soft` | Quicksand 700 | Mulish 400 | sans/sans | Google | 16/1.6 | wellness, soft brands |
| 39 | `dm-sans-clean` | DM Sans 700 | DM Sans 400 | sans/sans | Google | 16/1.5 | clean product pages |
| 40 | `manrope-sharp` | Manrope 800 | Inter 400 | sans/sans | Google | 16/1.5 | fintech, VC, sharp UI |
| 41 | `bebas-neue-headline` | Bebas Neue 400 | Montserrat 400 | display/sans | Google | 18/1.5 | posters, sports, events |
| 42 | `oswald-impact` | Oswald 700 | Open Sans 400 | display/sans | Google | 17/1.5 | news, fitness, bold headers |
| 43 | `anton-bold-banner` | Anton 400 | Roboto 400 | display/sans | Google | 18/1.5 | banners, campaigns |
| 44 | `abril-fatface-bold` | Abril Fatface 400 | Lato 400 | display/sans | Google | 18/1.6 | fashion, beauty, bold editorial |
| 45 | `alfa-slab-one-heavy` | Alfa Slab One 400 | Open Sans 400 | display/sans | Google | 17/1.5 | retro, food trucks, crafts |
| 46 | `staatliches-poster` | Staatliches 400 | Inter 400 | display/sans | Google | 16/1.5 | posters, events |
| 47 | `righteous-futuristic` | Righteous 400 | DM Sans 400 | display/sans | Google | 16/1.5 | games, retro-future |
| 48 | `chakra-petch-cyber` | Chakra Petch 700 | Inter 400 | display/sans | Google | 16/1.55 | cyber, esports, HUD |
| 49 | `teko-sharp-tech` | Teko 700 | Roboto 400 | display/sans | Google | 17/1.5 | motorsport, industrial tech |
| 50 | `permanent-marker-fun` | Permanent Marker 400 | Poppins 400 | script/sans | Google | 16/1.6 | playful, kids, street culture |

Stacks: sans `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`; serif `Georgia, "Times New Roman", serif`; mono `ui-monospace, "SFMono-Regular", Menlo, Consolas, "Liberation Mono", monospace`.
Use `"Family", <stack of its type>` for `--font-display` / `--font-body`.

## Load strings (copy as `<link href="..." rel="stylesheet">`)

### 01 inter-minimalist
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap`
### 02 geist-developer
`https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700&family=Geist+Mono:wght@600&display=swap`
### 03 outfit-creative
`https://fonts.googleapis.com/css2?family=Outfit:wght@800&family=Plus+Jakarta+Sans:wght@400;500;700&display=swap`
### 04 plus-jakarta-pro
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Plus+Jakarta+Sans:wght@700&display=swap`
### 05 space-grotesk-cyber
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Space+Grotesk:wght@700&display=swap`
### 06 cabinet-grotesk-bold
`https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@700&f[]=general-sans@400,500,700&display=swap`
### 07 syne-futuristic
`https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Syne:wght@800&display=swap`
### 08 clash-display-tech
`https://api.fontshare.com/v2/css?f[]=clash-display@700&f[]=satoshi@400,500,700&display=swap`
### 09 satoshi-minimal
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap`
`https://api.fontshare.com/v2/css?f[]=satoshi@700&display=swap`
### 10 general-sans-corporate
`https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700&display=swap`
`https://api.fontshare.com/v2/css?f[]=general-sans@600&display=swap`
### 11 playfair-editorial
`https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Playfair+Display:wght@700&display=swap`
### 12 cormorant-luxury
`https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Montserrat:wght@400;500;700&display=swap`
### 13 cinzel-royal
`https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Open+Sans:wght@400;500;700&display=swap`
### 14 instrument-serif-noir
`https://fonts.googleapis.com/css2?family=Instrument+Serif:ital,wght@0,400;1,400&family=Plus+Jakarta+Sans:wght@400;500;700&display=swap`
### 15 bodoni-classic
`https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@700&family=Inter:wght@400;500;700&display=swap`
### 16 prata-elegant
`https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Prata:wght@400&display=swap`
### 17 lora-warm-editorial
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Lora:wght@700&display=swap`
### 18 eb-garamond-vintage
`https://fonts.googleapis.com/css2?family=EB+Garamond:wght@500&family=Source+Serif+4:wght@400;500;700&display=swap`
### 19 fraunces-modern-serif
`https://fonts.googleapis.com/css2?family=Fraunces:wght@600&family=Plus+Jakarta+Sans:wght@400;500;700&display=swap`
### 20 merriweather-classic
`https://fonts.googleapis.com/css2?family=Merriweather:wght@700&family=Open+Sans:wght@400;500;700&display=swap`
### 21 fira-code-terminal
`https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Inter:wght@400;500;700&display=swap`
### 22 jetbrains-mono-coder
`https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600&family=Plus+Jakarta+Sans:wght@400;500;700&display=swap`
### 23 space-mono-hacker
`https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Mono:wght@700&display=swap`
### 24 ibm-plex-tech
`https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@700&family=IBM+Plex+Sans:wght@400;500;700&display=swap`
### 25 source-code-pro
`https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@700&family=Source+Sans+3:wght@400;500;700&display=swap`
### 26 inconsolata-clean
`https://fonts.googleapis.com/css2?family=Inconsolata:wght@700&family=Inter:wght@400;500;700&display=swap`
### 27 anonymous-pro-retro
`https://fonts.googleapis.com/css2?family=Anonymous+Pro:wght@700&family=Roboto:wght@400;500;700&display=swap`
### 28 ubuntu-tech-vibe
`https://fonts.googleapis.com/css2?family=Ubuntu:wght@700&family=Ubuntu+Condensed:wght@400&display=swap`
### 29 share-tech-mono
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Share+Tech+Mono:wght@400&display=swap`
### 30 red-hat-mono
`https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@400;500;700&family=Red+Hat+Mono:wght@700&display=swap`
### 31 roboto-standard
`https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap`
### 32 open-sans-corporate
`https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;700&display=swap`
### 33 montserrat-clean
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Montserrat:wght@700&display=swap`
### 34 lato-professional
`https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap`
### 35 poppins-vibrant
`https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;700&family=Poppins:wght@600&display=swap`
### 36 work-sans-modern
`https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;700&display=swap`
### 37 nunito-rounded
`https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;700&display=swap`
### 38 quicksand-soft
`https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;700&family=Quicksand:wght@700&display=swap`
### 39 dm-sans-clean
`https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap`
### 40 manrope-sharp
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Manrope:wght@800&display=swap`
### 41 bebas-neue-headline
`https://fonts.googleapis.com/css2?family=Bebas+Neue:wght@400&family=Montserrat:wght@400;500;700&display=swap`
### 42 oswald-impact
`https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;700&family=Oswald:wght@700&display=swap`
### 43 anton-bold-banner
`https://fonts.googleapis.com/css2?family=Anton:wght@400&family=Roboto:wght@400;500;700&display=swap`
### 44 abril-fatface-bold
`https://fonts.googleapis.com/css2?family=Abril+Fatface:wght@400&family=Lato:wght@400;700&display=swap`
### 45 alfa-slab-one-heavy
`https://fonts.googleapis.com/css2?family=Alfa+Slab+One:wght@400&family=Open+Sans:wght@400;500;700&display=swap`
### 46 staatliches-poster
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Staatliches:wght@400&display=swap`
### 47 righteous-futuristic
`https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Righteous:wght@400&display=swap`
### 48 chakra-petch-cyber
`https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@700&family=Inter:wght@400;500;700&display=swap`
### 49 teko-sharp-tech
`https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Teko:wght@700&display=swap`
### 50 permanent-marker-fun
`https://fonts.googleapis.com/css2?family=Permanent+Marker:wght@400&family=Poppins:wght@400;500;700&display=swap`

---

## FILE: references/surfaces.md

# Surfaces, shape, layout (replaces the old "50 layout classes")

Class strings below use the token utilities from `assets/starter/src/theme.css` (`bg-canvas`, `bg-surface`,
`bg-raised`, `border-line`, `border-line-strong`, `text-fg`, `text-muted`, `bg-accent`, `text-accent-fg`) and the style
utilities `rounded-ui`, `rounded-ui-lg`, `shadow-ui`, `ui-border` (all defined in the starter's `index.css`).
Tailwind v4. Every class here is checked against the real compiler.

## 1. Choose ONE surface style per product

A style is a set of CSS variables on `<html data-style="...">`. Components read the variables, so the whole
product changes consistently. Never mix two styles in one view (a brutalist hard-shadow card inside a frosted glass
dashboard looks like a bug). Mixing is allowed only when the brief asks for the clash.

| style | variables (`--ui-radius` / `--ui-radius-lg` / `--ui-border` / `--ui-shadow`) | personality | use for | extra rules |
|-------|------------------------------|-------------|---------|-------------|
| `soft` (default) | 0.75rem / 1.25rem / 1px / two-layer soft shadow | calm, modern product UI | SaaS, dashboards, fintech, most apps | one radius family; shadows only on raised things |
| `glass` | 1rem / 1.75rem / 1px / deep soft shadow | frosted layers over a rich backdrop | hero cards, music, AI, web3 | needs a colourful or gradient backdrop; blur on at most 2 surfaces (cost on low-end Android); keep text on the opaque part |
| `brutal` | 0 / 0 / 3px / `6px 6px 0 0 var(--fg)` | loud, flat, raw | agencies, indie games, streetwear | flat saturated fills, thick `fg` borders, hover = shift the shadow, bold type, never blur |
| `terminal` | 2px / 4px / 1px / none | precise, technical | dev tools, security, HUD | mono headings/labels, hairline borders, no shadows, optional dotted grid backdrop |
| `editorial` | 0 / 0 / 1px / none | print-like, quiet | studios, fashion, law, journals | hairline rules instead of boxes, serif headings, generous whitespace, asymmetric columns |
| `organic` | 1.25rem / 2rem / 1px / soft inset + drop | warm, tactile | wellness, food, craft, hospitality | asymmetric radii allowed on one hero shape, warm neutral palettes, imagery over icons |

`--ui-shadow` in dark themes: shadows are barely visible on dark canvases, so depth comes from lighter surfaces
(`canvas` < `surface` < `raised`) plus a `line` border, not from bigger shadows.

## 2. Shape rules
- One radius family per product. Nested radius = outer radius minus the padding between them (`rounded-ui-lg` card
  containing `rounded-ui` controls).
- Pill (`rounded-full`) for badges, avatars and a single primary hero button in `soft`/`organic` styles only.
- Do not give every element the same radius regardless of hierarchy: controls < cards < sheets/dialogs.
- Borders: `border-line` for decoration; inputs/controls that must be findable use `border-line-strong` (3:1).

## 3. Elevation and stacking
| layer | how |
|-------|-----|
| page content | normal flow, `z-0`/`z-10` only inside a local `isolate` stacking context |
| sticky header | `sticky top-0 z-40` plus `scroll-padding-top` on `html` so focused elements are not hidden behind it |
| skip link | `z-50`, off-screen until focused |
| modal, menu, tooltip, toast, popover | **top layer**: `<dialog>` / `popover` attribute. No z-index needed, nothing can sit above them |
Never write `z-[9999]`. If you need it, the element should be in the top layer.

## 4. Layout recipes (Tailwind v4)
Page container: `mx-auto w-full max-w-6xl px-4 sm:px-6 lg:px-8`. Section rhythm: `py-16 sm:py-24` (hero may use `py-24 sm:py-32`).
Mobile first; test 320, 360, 768, 1280. Spacing in multiples of 4 (`gap-4`, `gap-6`, `p-8`).

| id | recipe | classes |
|----|--------|---------|
| L1 split hero | copy left, live demo/visual right | `grid items-center gap-12 lg:grid-cols-[minmax(0,6fr)_minmax(0,5fr)]` |
| L2 bento | asymmetric feature grid | `grid gap-4 md:grid-cols-6 md:auto-rows-[minmax(10rem,auto)]`; cards `md:col-span-4 md:row-span-2`, `md:col-span-2`, `md:col-span-3` |
| L3 sticky split | left explains while right scrolls | `grid gap-12 lg:grid-cols-[minmax(0,5fr)_minmax(0,7fr)]`; left `lg:sticky lg:top-24 lg:self-start` |
| L4 dashboard shell | sidebar + content | `grid min-h-dvh grid-cols-1 lg:grid-cols-[16rem_minmax(0,1fr)]`; sidebar hidden below `lg` behind a menu button |
| L5 editorial columns | long-form + margin notes | `grid gap-x-12 gap-y-8 md:grid-cols-12`; body `md:col-span-7 md:col-start-2`; aside `md:col-span-3` |
| L6 narrow focus | auth, checkout, settings | `mx-auto flex min-h-dvh w-full max-w-md flex-col justify-center gap-6 px-4` |
| L7 card grid | collections, pricing | `grid gap-6 sm:grid-cols-2 lg:grid-cols-3` (use `grid-cols-[repeat(auto-fit,minmax(16rem,1fr))]` when counts vary) |
| L8 alternating rows | feature explanations | `grid items-center gap-10 md:grid-cols-2` with `md:[&>*:first-child]:order-2` on even rows |
| L9 timeline | real sequences only | `relative ms-4 border-s border-line-strong ps-8` with a dot per item |
| L10 masonry | galleries | `columns-1 gap-4 sm:columns-2 lg:columns-3 [&>*]:mb-4 [&>*]:break-inside-avoid` |
| L11 full-bleed hero | image/video first | `relative isolate grid min-h-[min(100dvh,56rem)] place-items-end overflow-hidden`; media `absolute inset-0 -z-10 size-full object-cover` |
| L12 data page | table + filters | `flex flex-col gap-4`; filters `flex flex-wrap gap-3`; table wrapper `overflow-x-auto rounded-ui-lg ui-border border-line` |

Component-level responsiveness: prefer container queries for cards that live in different-width slots:
`@container` on the wrapper and `@md:flex-row` / `@lg:grid-cols-2` on the card. Use `min-h-dvh` / `100dvh`, never `100vh`.
Use `aspect-video` / `aspect-square` + `object-cover` for media; give `<img>` width and height to prevent layout shift.

## 5. Overflow defence (user content breaks layouts)
Flex/grid children that hold text: `min-w-0`. Single line: `truncate`. Long words/URLs: `break-words` (or `[overflow-wrap:anywhere]`).
Previews: `line-clamp-2`. Tables and code: wrap in `overflow-x-auto`; the body never scrolls sideways.

## 6. Icons
One family per product (Lucide via `lucide-react` is the default: `size-5`, `strokeWidth={1.75}`, `aria-hidden="true"` when decorative).
Icon-only buttons need `aria-label`. Icons inherit colour (`currentColor`), sizes 16/20/24 only, never mix filled and outline.
Status icons always accompany colour (see Badge/Alert in `assets/starter/src/components`).

## 7. Imagery
Real product UI, simple SVG diagrams, or real photography beat generic gradient blobs and floating device mockups.
LCP image: `fetchpriority="high"`, no lazy. Others: `loading="lazy" decoding="async"`, `sizes`/`srcset`. No hot-linked
third-party images in artifacts or demos (they break offline and in sandboxes); use inline SVG or generated CSS shapes.
Alt text describes purpose (`alt=""` for decorative).

---

## FILE: references/components.md

# Components

Ready, tested components live in `assets/starter/src/components/`: `Button` (+ `buttonClass()`), `TextField` /
`TextAreaField`, `Card`, `Badge`, `Alert`, `Dialog` + `DialogTrigger`, `ThemeToggle`, `Skeleton`, `EmptyState`.
Copy them rather than re-inventing. This file gives (1) the state contract every component must meet and
(2) accessible recipes for the patterns the starter does not ship. All class strings use the token utilities and
compile on Tailwind v4 (checked with `scripts/check_classes.mjs`).

## 1. State contract (every interactive element)

| state | requirement | class recipe |
|-------|-------------|--------------|
| default | readable, obviously interactive (not only by colour) | border, underline or filled shape |
| hover | subtle, never the only cue | `hover:bg-fg/10` (ghost) or `hover:bg-accent-hover` (filled) |
| focus-visible | 2px outline, 2px offset, accent | `focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent` |
| active (pressed) | tiny physical response | `active:bg-accent-active` or `active:scale-[0.98] motion-reduce:active:scale-100` |
| disabled | not focusable if truly unavailable; explain why nearby | `disabled:opacity-50 disabled:cursor-not-allowed` |
| loading | keep the label, show progress, block double submit | `aria-busy`, `disabled`, spinner (see `Button`) |
| selected / current | not colour alone: weight, underline, check or indicator bar | `aria-[current=page]:underline aria-[current=page]:font-semibold`, `aria-selected:bg-accent/10` |
| invalid | text message + icon + `aria-invalid`, linked with `aria-describedby` | `aria-invalid:border-danger` (see `TextField`) |
Touch targets: 44x44px minimum on touch layouts (`min-h-11`); never below 24x24 (WCAG 2.2). Do not remove the focus outline without replacing it.

Every data view needs **five states**: loading (`Skeleton`, announce with `role="status"` on the container), empty
(`EmptyState`: say what is missing and offer the next action), error (`Alert tone="danger"` with a retry), partial, success.

## 2. Anything that must look like a button but navigates
```tsx
import { buttonClass } from './components/Button';
<a href="/pricing" className={buttonClass({ variant: 'primary', size: 'lg' })}>See pricing</a>
```
Navigates = `<a href>`. Performs an action = `<button>`. Never `<div onClick>`.

## 3. Icon-only button
```tsx
<button type="button" aria-label="Close panel"
  className="inline-flex size-11 items-center justify-center rounded-ui text-fg transition-colors hover:bg-fg/10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent">
  <svg className="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" /></svg>
</button>
```

## 4. Switch (native checkbox, `role="switch"`)
```tsx
<label className="flex min-h-11 cursor-pointer items-center justify-between gap-4">
  <span>Email notifications</span>
  <input type="checkbox" role="switch" className="peer sr-only" />
  <span aria-hidden="true"
    className="relative h-7 w-12 shrink-0 rounded-full bg-line-strong transition-colors peer-checked:bg-accent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-accent after:absolute after:start-1 after:top-1 after:size-5 after:rounded-full after:bg-canvas after:transition-transform peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none rtl:peer-checked:after:-translate-x-5" />
</label>
```
Checkbox / radio: keep native inputs (`className="size-5"`, label `min-h-11`); `accent-color` is already set on `html`.

## 5. Segmented control (radio group)
```tsx
<fieldset className="inline-flex rounded-ui ui-border border-line-strong p-1">
  <legend className="sr-only">Billing period</legend>
  {['Monthly', 'Yearly'].map((v) => (
    <label key={v}>
      <input type="radio" name="billing" value={v} defaultChecked={v === 'Monthly'} className="peer sr-only" />
      <span className="flex min-h-9 cursor-pointer items-center rounded-ui px-4 text-sm font-medium text-muted transition-colors peer-checked:bg-accent peer-checked:text-accent-fg peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-accent">{v}</span>
    </label>
  ))}
</fieldset>
```

## 6. Accordion / FAQ (native, no JS)
`<details name="faq">` makes the group exclusive (one open at a time). Keyboard and screen reader support is built in.
```html
<div class="divide-y divide-line rounded-ui-lg ui-border border-line bg-surface">
  <details name="faq" class="group p-5">
    <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 font-medium [&::-webkit-details-marker]:hidden">
      How do I choose a palette?
      <svg class="size-5 shrink-0 transition-transform group-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="m6 9 6 6 6-6" /></svg>
    </summary>
    <p class="mt-3 text-muted">Start from the product's subject and audience, then check the mood column.</p>
  </details>
</div>
```

## 7. Navigation: disclosure on mobile
A site nav is a **disclosure**, not an ARIA menu: button with `aria-expanded` + `aria-controls`, links in a list.
```tsx
function SiteNav() {
  const [open, setOpen] = useState(false);
  return (
    <nav aria-label="Main" className="flex flex-wrap items-center justify-between gap-3">
      <a href="/" className="font-display text-lg font-bold">Brand</a>
      <button type="button" aria-expanded={open} aria-controls="nav-links" onClick={() => setOpen((o) => !o)}
        className="min-h-11 rounded-ui ui-border border-line-strong px-4 text-sm font-medium lg:hidden">
        {open ? 'Close menu' : 'Menu'}
      </button>
      <ul id="nav-links" className={`w-full flex-col gap-1 lg:flex lg:w-auto lg:flex-row ${open ? 'flex' : 'hidden'}`}>
        <li><a href="/docs" aria-current="page"
          className="flex min-h-11 items-center rounded-ui px-3 hover:bg-fg/10 aria-[current=page]:font-semibold aria-[current=page]:underline underline-offset-8">Docs</a></li>
        <li><a href="/pricing" className="flex min-h-11 items-center rounded-ui px-3 hover:bg-fg/10">Pricing</a></li>
      </ul>
    </nav>
  );
}
```

## 8. Action panel (popover + anchor positioning)
Top layer, light dismiss and Esc are native. This is a **button group in a popover**, not an ARIA menu: do not add
`role="menu"`, `role="menuitem"` or `aria-haspopup` unless you implement the full arrow-key contract.
```tsx
<button type="button" popoverTarget="row-actions"
  className="min-h-11 rounded-ui ui-border border-line-strong bg-surface px-4 text-sm font-medium">Actions</button>
<div id="row-actions" popover="auto"
  className="inset-auto m-0 w-56 rounded-ui-lg ui-border border-line bg-raised p-2 text-fg shadow-ui [position-area:block-end_span-inline-end] [position-try-fallbacks:flip-block,flip-inline,flip-block_flip-inline]">
  <button type="button" className="flex min-h-11 w-full items-center rounded-ui px-3 text-start hover:bg-fg/10 focus-visible:outline-2 focus-visible:outline-accent">Rename</button>
  <button type="button" className="flex min-h-11 w-full items-center rounded-ui px-3 text-start text-danger hover:bg-danger/10 focus-visible:outline-2 focus-visible:outline-accent">Delete</button>
</div>
```
Browsers without anchor positioning show the panel centred, which is acceptable. Use logical `position-area` keywords only (never mix with physical ones).

## 9. Tooltip (supplementary text only)
Essential information must be visible without hovering (touch has no hover). A tooltip may repeat an icon button's name.
```tsx
<span className="group relative inline-flex">
  <button type="button" aria-label="Copy link" aria-describedby="tip-copy" className="inline-flex size-11 items-center justify-center rounded-ui hover:bg-fg/10">
    <svg className="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" aria-hidden="true"><rect x="9" y="9" width="11" height="11" rx="2" /><path d="M5 15V6a2 2 0 0 1 2-2h9" /></svg>
  </button>
  <span id="tip-copy" role="tooltip"
    className="pointer-events-none absolute bottom-full start-1/2 mb-2 -translate-x-1/2 whitespace-nowrap rounded-ui bg-fg px-2 py-1 text-sm text-canvas opacity-0 transition-opacity group-focus-within:opacity-100 group-hover:opacity-100 motion-reduce:transition-none">Copy link</span>
</span>
```

## 10. Toast
Use for low-stakes confirmations ("Saved"). Errors that need action belong inline (`Alert`). Keep visible >= 6 seconds
(pause while hovered), include a close button, never rely on toasts alone. Mirror the text into a persistent live region,
because content inside a hidden popover is announced unreliably.
```tsx
<div role="status" aria-live="polite" className="sr-only" id="toast-live" />
<div id="toast" popover="manual"
  className="inset-auto bottom-4 end-4 m-0 w-[min(22rem,calc(100%-2rem))] rounded-ui-lg ui-border border-line bg-raised p-4 text-fg shadow-ui">
  <p id="toast-text" />
</div>
```
```ts
export function toast(message: string) {
  const el = document.getElementById('toast') as HTMLElement | null;
  if (!el) return;
  document.getElementById('toast-text')!.textContent = message;
  document.getElementById('toast-live')!.textContent = message;
  el.showPopover();
  window.setTimeout(() => el.hidePopover(), 6000);
}
```

## 11. Tabs (WAI-ARIA tabs pattern: arrow keys move, Tab leaves)
```tsx
function Tabs({ tabs }: { tabs: { id: string; label: string; panel: React.ReactNode }[] }) {
  const [active, setActive] = useState(0);
  const refs = useRef<(HTMLButtonElement | null)[]>([]);
  const move = (i: number) => { const n = (i + tabs.length) % tabs.length; setActive(n); refs.current[n]?.focus(); };
  return (
    <div>
      <div role="tablist" aria-label="Project sections" className="flex gap-1 border-b border-line"
        onKeyDown={(e) => {
          if (e.key === 'ArrowRight') { e.preventDefault(); move(active + 1); }
          if (e.key === 'ArrowLeft') { e.preventDefault(); move(active - 1); }
          if (e.key === 'Home') { e.preventDefault(); move(0); }
          if (e.key === 'End') { e.preventDefault(); move(tabs.length - 1); }
        }}>
        {tabs.map((t, i) => (
          <button key={t.id} ref={(el) => { refs.current[i] = el; }} role="tab" type="button" id={`tab-${t.id}`}
            aria-selected={i === active} aria-controls={`panel-${t.id}`} tabIndex={i === active ? 0 : -1}
            onClick={() => setActive(i)}
            className="min-h-11 border-b-2 border-transparent px-4 text-sm font-medium text-muted transition-colors hover:text-fg aria-selected:border-accent aria-selected:text-fg focus-visible:outline-2 focus-visible:outline-offset-[-2px] focus-visible:outline-accent">
            {t.label}
          </button>
        ))}
      </div>
      {tabs.map((t, i) => (
        <div key={t.id} role="tabpanel" id={`panel-${t.id}`} aria-labelledby={`tab-${t.id}`} hidden={i !== active} tabIndex={0} className="py-6">{t.panel}</div>
      ))}
    </div>
  );
}
```

## 12. Data table
```tsx
<div className="overflow-x-auto rounded-ui-lg ui-border border-line">
  <table className="w-full min-w-[40rem] border-collapse text-sm">
    <caption className="sr-only">Recent deployments</caption>
    <thead className="bg-surface text-muted">
      <tr>
        <th scope="col" className="px-4 py-3 text-start font-medium">Project</th>
        <th scope="col" className="px-4 py-3 text-start font-medium">Status</th>
        <th scope="col" className="px-4 py-3 text-end font-medium">Duration</th>
      </tr>
    </thead>
    <tbody className="divide-y divide-line">
      <tr className="hover:bg-fg/5">
        <th scope="row" className="px-4 py-3 text-start font-medium">Billing API</th>
        <td className="px-4 py-3"><span className="text-success">✓ Deployed</span></td>
        <td className="px-4 py-3 text-end tabular-nums">1m 42s</td>
      </tr>
    </tbody>
  </table>
</div>
```
Numbers: `tabular-nums text-end`. Sort buttons inside `<th>` with `aria-sort`. Mobile: horizontal scroll inside the wrapper, or restructure to cards below `md`.

## 13. Breadcrumb and pagination
```tsx
<nav aria-label="Breadcrumb"><ol className="flex flex-wrap items-center gap-2 text-sm text-muted">
  <li><a href="/projects" className="underline-offset-4 hover:underline">Projects</a></li>
  <li aria-hidden="true">/</li>
  <li aria-current="page" className="text-fg">Billing API</li>
</ol></nav>

<nav aria-label="Pagination"><ul className="flex items-center gap-1">
  <li><a href="?page=1" className="flex size-11 items-center justify-center rounded-ui hover:bg-fg/10">1</a></li>
  <li><a href="?page=2" aria-current="page" className="flex size-11 items-center justify-center rounded-ui bg-accent text-accent-fg">2</a></li>
</ul></nav>
```

## 14. Interactive card (the whole card is one link)
One real link in the heading, stretched with a pseudo-element: keyboard and screen-reader users get one clear target.
```tsx
<article className="group relative ui-border rounded-ui-lg border-line bg-surface p-6 transition-shadow hover:shadow-ui focus-within:outline-2 focus-within:outline-offset-2 focus-within:outline-accent">
  <h3 className="text-lg font-semibold">
    <a href="/projects/billing-api" className="after:absolute after:inset-0 focus-visible:outline-hidden">Billing API</a>
  </h3>
  <p className="mt-2 text-muted">Last deployed 2 hours ago.</p>
</article>
```
Only cards that are actually clickable get hover lift. Static cards stay still.

## 15. KPI / stat card
```tsx
<Card as="article" className="flex flex-col gap-1">
  <p className="text-sm text-muted">Active users</p>
  <p className="text-4xl font-bold tabular-nums">12,480</p>
  <p className="text-sm text-success"><span aria-hidden="true">▲</span> 12% <span className="sr-only">increase</span> vs last week</p>
</Card>
```
Show the comparison period. A number with no context is decoration.

## 16. Pricing card
```tsx
<Card as="article" className="relative flex flex-col gap-5 border-accent">
  <Badge tone="accent">Most popular</Badge>
  <h3 className="text-xl font-semibold">Team</h3>
  <p><span className="text-4xl font-bold tabular-nums">₹1,499</span> <span className="text-muted">per month</span></p>
  <ul className="flex flex-col gap-2 text-sm">
    <li className="flex gap-2"><span aria-hidden="true" className="text-success">✓</span>Unlimited projects</li>
    <li className="flex gap-2"><span aria-hidden="true" className="text-success">✓</span>Priority support</li>
  </ul>
  <a href="/signup?plan=team" className={buttonClass({ size: 'lg' })}>Start free trial</a>
</Card>
```
Prices for India: `new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(1499)`.

## 17. Forms
- Real `<label>` for every control; placeholder is an example, never the label. Optional fields say "(optional)".
- `autocomplete` tokens (`name`, `email`, `tel-national`, `postal-code`, `current-password`, `new-password`, `one-time-code`),
  `inputMode` (`email`, `tel`, `numeric`), `type` set correctly. India: phone `inputMode="tel" autoComplete="tel-national"` with a visible `+91` prefix; PIN `inputMode="numeric" pattern="[0-9]{6}" autoComplete="postal-code"`.
- Validate on blur (after the first touch) and on submit; never while the person is still typing their first attempt.
- On submit with errors: move focus to an error summary (`role="alert"`, links to each field) or to the first invalid field.
- Errors say what to fix: "Enter a 6-digit PIN code", not "Invalid input".
- Password fields: show/hide toggle (`<button type="button" aria-pressed>`), allow paste, no composition rules that block password managers.
- Submit button keeps its label and shows loading (`Button loading`); disable double submit; confirm success with an inline `Alert tone="success"`.

---

## FILE: references/motion.md

# Motion

Motion explains change (where something came from, what just happened). It is not decoration. Default to
**one orchestrated moment** (page-load reveal or a hero interaction) plus small, fast feedback on controls.
A page where every section fades up on scroll, every card lifts on hover and three things loop forever is the generic AI look.

## 1. Tokens
| use | duration | easing |
|-----|----------|--------|
| press / toggle feedback | 80-120ms | `ease-out` |
| hover, focus, colour changes | 150ms | `ease-out` |
| menus, popovers, tooltips | 150-200ms | `cubic-bezier(0.2, 0.7, 0.2, 1)` |
| dialogs, drawers, sheets | 200-300ms | `cubic-bezier(0.2, 0.7, 0.2, 1)` in, `ease-in` out |
| page-load reveal (the one moment) | 500-700ms, stagger 60-80ms | `cubic-bezier(0.2, 0.7, 0.2, 1)` |
| anything > 700ms | only for storytelling surfaces (hero scenes), never for UI feedback | - |

Exits are faster than entrances (about 60-70%). Animate only `transform`, `opacity` (and `clip-path`/`filter` sparingly).
Never animate `width`, `height`, `top`, `left`, `margin` (layout thrash); never `transition-all`.
Tailwind: `transition-colors`, `transition-opacity`, `transition-transform`, `transition-shadow`, or
`transition-[color,background-color,border-color,opacity,transform]`, with `duration-150` / `ease-out`.

## 2. Reduced motion (per element, not a global kill-switch)
`prefers-reduced-motion: reduce` does not mean "no feedback"; it means no large movement, parallax, zoom or looping.
Do NOT use the one-liner `* { animation-duration: 0.01ms !important; }`: it makes some animations jump or flash and
can break scripts waiting for `animationend`. Decide per animation: swap movement for a fade, or remove it.
```css
.rise {
  animation: rise 0.6s cubic-bezier(0.2, 0.7, 0.2, 1) both;
  animation-delay: calc(var(--i, 0) * 70ms);
  @media (prefers-reduced-motion: reduce) { animation: none; }   /* content simply appears */
}
```
Tailwind: `motion-safe:animate-pulse`, `motion-reduce:animate-none`, `motion-reduce:transition-none`.
Auto-playing movement longer than 5 seconds needs a visible pause control (WCAG 2.2.2). No flashing more than 3 times a second.

## 3. Entrance of the page (the one moment)
```css
@keyframes rise { from { opacity: 0; translate: 0 14px; } to { opacity: 1; translate: 0 0; } }
```
Apply `.rise` with `style={{ '--i': n }}` to the 3-6 elements of the hero only. Do not repeat on every section.

## 4. Top-layer elements (dialog, popover): `@starting-style` + `allow-discrete`
The element changes `display` and enters the top layer, so animate with discrete transitions (see `assets/starter/src/index.css`):
```css
dialog { opacity: 0; transition: opacity .2s ease-out, display .2s allow-discrete, overlay .2s allow-discrete; }
dialog[open] { opacity: 1; @starting-style { opacity: 0; } }
```
Keep the transition on the base state (not only `[open]`), otherwise the exit snaps shut.

## 5. State changes and navigation
- Same-document UI changes (tab switch, list reorder, route change in an SPA): **View Transitions**
  (`document.startViewTransition(() => update())`), with `view-transition-name` on persistent elements. Provide a no-animation fallback by default (the call is optional).
- Scroll-linked effects (reading progress, subtle reveals): CSS scroll-driven animations
  (`animation-timeline: view()`), guarded with `@supports (animation-timeline: view())`; the content must be fully usable without them.
- Loading: `Skeleton` blocks (`animate-pulse motion-reduce:animate-none`) for layout-shaped content, a spinner only inside a button or for unknown short waits,
  `<progress>` when the amount is known. Never a full-screen spinner that blocks reading.

## 6. Micro-interactions that earn their place
| where | what |
|-------|------|
| button press | colour shift via `active:bg-accent-active`; optional `active:scale-[0.98]` |
| success | the check icon draws or the label swaps to "Saved" for ~2s |
| error | the field border and message appear; a 2-step 4px shake only if reduced motion is off |
| toggle | thumb translates, track recolours (`transition-colors`) |
| list item added/removed | fade + small translate; the list reflows with a View Transition |
| copy | tooltip text becomes "Copied" and returns |

## 7. Do not
- Fade-up on every section; parallax on everything; infinite bounce/float on icons; auto-rotating carousels.
- Hover transitions on non-interactive cards; marquee/ticker without a pause and without `motion-reduce` handling.
- Animation that delays the first meaningful paint or blocks input; entrance animations longer than the content takes to read.
- Hiding content until JS runs (opacity 0 in CSS with the animation added by script): if the script fails the page stays blank.

---

## FILE: references/accessibility.md

# Accessibility (WCAG 2.2 AA is the floor, not a bonus)

Why it matters beyond compliance: a large share of users in India browse on small, low-cost Android phones in
sunlight, with large system text, one-handed, often with TalkBack or switch/voice control. Accessible UI is robust UI.

## 1. Contrast and colour
- Body text 4.5:1, large text (>= 24px, or >= 18.66px bold) 3:1, UI boundaries/icons/focus indicators 3:1.
  Palette tokens in this skill are pre-verified (`fg` 7:1, `muted` 4.5:1, `accent` 4.5:1, `line-strong` 3:1, status 4.5:1,
  also on their own 12% tint, `accent-fg` 4.5:1 on `accent` and on its hover/active colours). Do not invent hex values.
- Text over images or gradients: put an opaque or scrim layer behind it and check the worst pixel region.
- Never use colour as the only signal (error, success, selected, chart series, link in body text): add icon, text, pattern or underline.
- Check: `python3 scripts/contrast_check.py "#fg" "#bg"` and `python3 scripts/contrast_check.py --css src/theme.css`.

## 2. Keyboard and focus
- Everything operable with a keyboard; order follows the visual order; no `tabindex` > 0.
- Visible focus on every interactive element (`focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent`), 3:1 against its surroundings.
- A sticky header must not hide the focused element: set `scroll-padding-top` on `html` (WCAG 2.4.11).
- Skip link as the first focusable element ("Skip to main content") that becomes visible on focus.
- No keyboard traps. Esc closes dialogs/popovers (native elements do this). Focus returns to the trigger (native).
- Custom widgets follow the WAI-ARIA Authoring Practices keyboard contract (tabs: arrows; menu: arrows; combobox: arrows + Esc); otherwise use native elements.

## 3. Semantics first
- Native elements before ARIA: `<button>`, `<a href>`, `<dialog>`, `<details>`, `<select>`, `<input type=...>`, `<progress>`, `<table>`.
  First rule of ARIA: if a native element exists, use it. Bad ARIA is worse than none.
- Landmarks: one `<header>`, `<nav aria-label>`, one `<main id="main">`, `<footer>`. Exactly one `<h1>`; headings descend without skipping levels (style with classes, not by choosing a smaller tag).
- Lists are lists (`<ul>`/`<ol>`), data is a table with `<th scope>` and a `<caption>`, quotes are `<blockquote>`.
- Page language: `<html lang="en">` (or `hi`, `mr`, `ta`...). Switch language inline with `lang` on the element (`<span lang="hi">`).
- Page `<title>` unique and descriptive. Link text makes sense alone ("Read the pricing guide", not "click here").
- Icon-only controls: `aria-label`; decorative icons/glyphs: `aria-hidden="true"`; informative images: meaningful `alt`; decorative images `alt=""`.

## 4. Forms
- Every control has a programmatic label (`<label htmlFor>`); placeholder is not a label; required/optional is stated in text.
- Errors: text, icon, `aria-invalid`, `aria-describedby`; summary with links on submit; move focus to it or the first invalid field.
- Use `autocomplete` tokens and the right `type`/`inputMode` (see `components.md`). Do not block paste. No re-asking for info already given (WCAG 3.3.7).
- Authentication must not rely on a cognitive test (3.3.8): allow password managers, OTP autofill (`autocomplete="one-time-code"`).

## 5. Dialogs, popovers, live regions
- Modal = native `<dialog>` opened with `showModal()` / `command="show-modal"`. Do not add `role="dialog"`, `aria-modal`, a focus trap or `overflow:hidden` on `body`.
  Label it (`aria-labelledby` the heading). Put the safest action first in DOM order (it gets initial focus).
- Popover (`popover` attribute): light dismiss and Esc are native; this is not an ARIA menu.
- Live regions: `role="status"` (polite) for results ("Saved", "3 results"); `role="alert"` only for errors that need immediate attention.
  The live region must exist in the DOM before its text changes.
- Loading containers: `role="status"` + a text label on the container; hide skeleton blocks with `aria-hidden`.

## 6. Size, spacing, reflow, zoom
- Touch targets >= 44x44px on touch layouts (never below 24x24, WCAG 2.5.8), with spacing between them.
- Reflow at 320px width without horizontal scroll (except data tables/code in their own scroller); text resizes to 200% without loss.
- Never disable zoom (`maximum-scale`, `user-scalable=no`). Use `rem`/`em` for text; do not fix container heights around text.
- Text spacing overrides (line-height 1.5, paragraph spacing 2x, letter 0.12em) must not clip content: avoid fixed heights on text blocks.
- Hindi/Indic scripts need more line-height (>= 1.7) and fonts with proper Devanagari glyphs (see `typography.md`).

## 7. Motion, themes, user preferences
- `prefers-reduced-motion`: handle per animation (see `motion.md`). Provide pause controls for auto-playing content > 5s.
- `prefers-color-scheme` + manual toggle; `<meta name="color-scheme" content="light dark">` and `color-scheme` on `:root`.
- `forced-colors: active` (Windows High Contrast): keep real borders on controls, use `outline-color: Highlight`, do not rely on background colour alone for state.
- `prefers-contrast: more`: optional; where cheap, strengthen `line` to `line-strong`.

## 8. Verify (do not claim "accessible" without evidence)
1. `python3 scripts/lint_ui.py src index.html` (structural mistakes) and `node scripts/check_classes.mjs src index.html`.
2. `python3 scripts/contrast_check.py --css src/theme.css`.
3. Keyboard pass: Tab through the whole page with the mouse unplugged. Every control reachable, focus always visible, Esc closes overlays, nothing trapped.
4. Zoom pass: 200% browser zoom and 320px viewport: no overlap, no horizontal scroll.
5. Automated: axe (`npx @axe-core/cli http://localhost:5173`) or Lighthouse. These find roughly a third of issues; they never replace steps 3-4.
6. Screen reader smoke test: VoiceOver (iOS/macOS), TalkBack (Android), or NVDA (Windows): headings list, landmarks list, one form, one dialog.
State in the delivery what you verified and what you did not.

---

## FILE: references/blueprints.md

# Blueprints (54 starting hypotheses)

A blueprint is a *hypothesis*, not a template. Use it to skip blank-page indecision, then do the anti-generic
review (`anti-generic.md`) and change at least one structural decision so your result is not a clone.
If the user has brand colours, keep the blueprint's structure and derive the theme from the brand:
`python3 scripts/tokens_to_tailwind.py --brand "#HEX" --mode dark|light`.

Columns: palette id (`palettes.md`), type pairing id (`typography.md`), surface style and layouts (`surfaces.md`),
and the ONE signature move that makes the page memorable. Everything else stays quiet so the signature can work.

| # | archetype | palette | type | style | layout | signature move |
|---|-----------|---------|------|-------|--------|----------------|
| 01 | Cyberpunk AI startup | `cyber-black-green` (01) | `space-grotesk-cyber` (05) | glass | L1 L2 | Live model output streams into a real, copyable terminal pane with a latency badge; crimson only for the live status and the primary CTA. |
| 02 | Developer terminal portfolio | `hacker-terminal` (04) | `jetbrains-mono-coder` (22) | terminal | L1 | Projects open as README panes; `/` opens a keyboard command palette; the whole site still reads with JavaScript off. |
| 03 | SaaS analytics dashboard | `midnight-slate` (21) | `inter-minimalist` (01) | soft | L4 L12 | KPI strip with sparklines and the comparison period; saved views as tabs; every chart has a 'view as table' toggle. |
| 04 | Cloud infrastructure startup | `electric-horizon` (08) | `geist-developer` (02) | soft | L1 L3 | Architecture diagram that redraws with a region/scale slider; status-page link lives in the header. |
| 05 | Open source tool portal | `hacker-terminal` (04) | `red-hat-mono` (30) | terminal | L7 | Install command with package-manager tabs and one-click copy; real repository stats; contributors strip. |
| 06 | Web3 and crypto protocol | `cyberpunk-void` (03) | `space-mono-hacker` (23) | glass | L2 | Live on-chain stats ticker that pauses on hover and focus; risk disclosure always visible, not buried. |
| 07 | AI LLM playground | `quantum-teal` (07) | `ibm-plex-tech` (24) | soft | L3 | Prompt/response split with token counter, streaming caret and a parameter drawer; stop and retry are always reachable. |
| 08 | Cyber security dashboard | `midnight-neon-red` (39) | `fira-code-terminal` (21) | terminal | L4 | Alert feed ordered by severity with icon + label; red reserved for critical only; incident timeline per alert. |
| 09 | Automation agency landing | `saas-indigo` (25) | `outfit-creative` (03) | soft | L2 | Before/after workflow diagram with real hours-saved numbers; the booking form has three fields. |
| 10 | Mobile app landing page | `electric-horizon` (08) | `manrope-sharp` (40) | soft | L1 | A phone frame built in CSS showing the real onboarding UI; store badges are real links; a QR code for desktop visitors. |
| 11 | Luxury jewellery brand | `royal-velvet` (11) | `cormorant-luxury` (12) | editorial | L11 | Slow product zoom on hover (tap on touch); gold used only as 1px rules and the single CTA. |
| 12 | High-end architecture studio | `classic-noir` (17) | `prata-elegant` (16) | editorial | L5 | Project index as a typographic list; hovering reveals the image; floor plans drawn as SVG. |
| 13 | Designer fashion magazine | `onyx-platinum` (15) | `bodoni-classic` (15) | editorial | L5 L10 | Oversized serif masthead, drop-cap article opener, asymmetric image grid with captions. |
| 14 | Fine dining restaurant | `midnight-bronze` (12) | `instrument-serif-noir` (14) | organic | L11 | Menu set as a typographic page with dietary marks as icon + text; reservation widget shows real time slots. |
| 15 | Art gallery and exhibition | `dark-truffle` (16) | `fraunces-modern-serif` (19) | editorial | L10 | Artwork viewer with title, medium and dimensions; calm 'gallery wall' backdrop; keyboard next/previous. |
| 16 | Boutique hotel landing | `espresso-copper` (13) | `playfair-editorial` (11) | organic | L11 | Room explorer with price per night and an availability calendar that works by keyboard. |
| 17 | Organic skincare brand | `terracotta-minimal` (41) | `quicksand-soft` (38) | organic | L8 | Ingredient glossary in popovers; plain-language product facts; no unverifiable before/after claims. |
| 18 | Aesthetic portfolio | `sleek-mahogany` (14) | `syne-futuristic` (07) | soft | L10 | Case studies show constraints, process and outcome; masonry gallery with real alt text. |
| 19 | Horology showcase | `titanium-gold` (18) | `cinzel-royal` (13) | editorial | L11 | Movement exploded view drawn in SVG; parts are labelled on hover and on tap. |
| 20 | Heritage coffee brand | `cozy-latte` (47) | `lora-warm-editorial` (17) | organic | L8 | Origin map and tasting-notes wheel as accessible SVG; subscription chooser with clear cadence and price. |
| 21 | Neobank mobile web app | `deep-fintech` (22) | `plus-jakarta-pro` (04) | soft | L6 L4 | Balance card with a privacy-hide toggle; transaction rows align amounts right with merchant and category. |
| 22 | Crypto trading platform | `crypto-obsidian` (24) | `inter-minimalist` (01) | soft | L4 | Order ticket with live price, fee preview and a confirm step; gain/loss shown with arrows plus signed numbers. |
| 23 | Investment fund portal | `enterprise-navy` (27) | `lato-professional` (34) | soft | L12 | Performance chart with period selector and standard disclosures; downloadable factsheet. |
| 24 | Global logistics enterprise | `midnight-slate` (21) | `open-sans-corporate` (32) | soft | L4 | Shipment timeline with ETA confidence; map as SVG with a table fallback. |
| 25 | Tax and legal advisory firm | `clean-slate-light` (49) | `roboto-standard` (31) | editorial | L5 | Plain-language explainers with a deadline calendar; consultation form asks only what is needed. |
| 26 | InsurTech landing page | `emerald-growth` (23) | `work-sans-modern` (36) | soft | L7 | Three-step quote estimator with a running premium; policy terms available as plain text. |
| 27 | Accounting SaaS | `analytics-teal` (28) | `general-sans-corporate` (10) | soft | L12 | Invoice editor with a live preview; keyboard-first table entry. |
| 28 | Enterprise HR portal | `cloud-violet` (26) | `montserrat-clean` (33) | soft | L4 | Leave balance and request flow; org chart as an accessible tree. |
| 29 | Real estate investment firm | `desert-dune` (45) | `dm-sans-clean` (39) | soft | L7 | Yield calculator with sliders AND numeric inputs; property cards with real facts. |
| 30 | Venture capital website | `saas-indigo` (25) | `manrope-sharp` (40) | editorial | L5 | Portfolio as an index list with sector filter; thesis essays set for reading. |
| 31 | Gen-Z creator portfolio | `obsidian-fuchsia` (31) | `outfit-creative` (03) | soft | L2 | Link-hub of stacked cards and embeds, with a 'now' status line. |
| 32 | Neo-brutalist agency | `cyber-lime` (35) | `space-grotesk-cyber` (05) | brutal | L2 | Oversized type, thick borders, hover shifts the hard shadow; still fully keyboard and screen-reader accessible. |
| 33 | Indie game studio portal | `retro-vaporwave` (34) | `chakra-petch-cyber` (48) | brutal | L7 | Game cards with platform icons + text; trailer behind a click-to-load facade (no autoplay). |
| 34 | Music producer or DJ | `electric-sunset` (32) | `syne-futuristic` (07) | glass | L1 | Waveform player with real audio, keyboard controls and a transcript for talk content. |
| 35 | Podcast and media hub | `neon-tangerine` (37) | `bebas-neue-headline` (41) | soft | L7 | Episode list with a sticky mini-player, chapters and transcripts. |
| 36 | Streetwear e-commerce | `obsidian-fuchsia` (31) | `clash-display-tech` (08) | brutal | L7 | Drop countdown from a real timestamp (announced politely to screen readers); size picker as a radio group. |
| 37 | Digital art collective | `creative-cyan-dark` (38) | `righteous-futuristic` (47) | glass | L10 | Artist pages with honest fee breakdowns on any mint or purchase flow. |
| 38 | Meme and viral portal | `saas-indigo` (25) | `anton-bold-banner` (43) | brutal | L10 | Fast list with a 'Load more' button instead of an infinite-scroll trap. |
| 39 | Futuristic event landing | `midnight-neon-red` (39) | `staatliches-poster` (46) | terminal | L1 | Schedule grid with a timezone switch (IST by default), speaker cards, add-to-calendar. |
| 40 | EdTech and learning hub | `neon-peach` (33) | `poppins-vibrant` (35) | soft | L7 | Course cards with duration, level and language badges; progress shown as ring + text. |
| 41 | Eco and green energy | `forest-sage` (44) | `work-sans-modern` (36) | organic | L3 | Impact counters with cited sources; savings calculator with visible assumptions. |
| 42 | Meditation app | `warm-sand` (42) | `quicksand-soft` (38) | organic | L6 | Breathing circle that swaps to text counts under reduced motion; session picker with durations. |
| 43 | Organic agriculture platform | `earthy-moss` (50) | `nunito-rounded` (37) | organic | L7 | Farm profiles with batch traceability; seasonal availability calendar. |
| 44 | Architecture and interior design | `terracotta-minimal` (41) | `satoshi-minimal` (09) | editorial | L5 | Before/after slider whose handle works by keyboard (arrow keys). |
| 45 | Craft coffee and bakery | `cozy-latte` (47) | `lora-warm-editorial` (17) | organic | L8 | Today's menu with sold-out states; click-and-collect time picker. |
| 46 | Minimalist blogging platform | `clean-slate-light` (49) | `lora-warm-editorial` (17) | editorial | L5 | Reading-first: 65ch measure, reading progress, footnotes as popovers. |
| 47 | Holistic health and yoga studio | `olive-organic` (43) | `dm-sans-clean` (39) | organic | L8 | Class schedule table with level badges; booking with a waitlist state. |
| 48 | Handmade crafts e-commerce | `autumn-rust` (48) | `quicksand-soft` (38) | organic | L7 | Maker stories on product pages; made-to-order lead time shown before add-to-cart. |
| 49 | Non-profit or social cause | `warm-minimalist-gray` (46) | `open-sans-corporate` (32) | soft | L8 | Impact numbers with sources; two-step donate form that supports UPI. |
| 50 | Personal developer brand hub | `dark-synthwave` (05) | `geist-developer` (02) | glass | L1 | Now / Writing / Projects index with RSS; light and dark both polished. |
| 51 | Hindi-first EdTech for Bharat learners | `warm-sand` (42) | `poppins-vibrant` (35) | soft | L7 | Persistent हिन्दी / English switch in the header; lessons light on data; Devanagari line-height >= 1.7. |
| 52 | UPI / fintech app for Bharat | `deep-fintech` (22) | `plus-jakarta-pro` (04) | soft | L6 | Rupee amounts with Indian grouping (Rs 1,23,456); UPI ID field with a verify state; 44px+ tap targets. |
| 53 | Local store ordering (WhatsApp-first) | `forest-sage` (44) | `nunito-rounded` (37) | organic | L7 | Catalogue with quantity steppers, a running cart bar and an 'Order on WhatsApp' deep link; small images for 2G/3G. |
| 54 | Government service portal | `clean-slate-light` (49) | `open-sans-corporate` (32) | editorial | L6 | Step-by-step application with save and resume; plain-language labels in two or more languages; WCAG AA; print-friendly. |

Rows 51-54 are India-first: Devanagari/Indic scripts, rupee formatting (`Intl.NumberFormat('en-IN')`), UPI, WhatsApp, low-bandwidth,
and 360x800 as the primary viewport. See `SKILL.md` -> India-first defaults.

---

## FILE: references/anti-generic.md

# Anti-generic review

Language models drift to the average of everything they have seen, so unprompted UI converges on the same look:
Inter, purple-blue gradient, centred hero, three equal cards, fade-up on everything. This file is how to notice
the drift and correct it. Run it on the design plan BEFORE writing code, and again on the result.

## 1. The review (3 minutes)
1. Write the plan (see `SKILL.md`). Underline every decision that you would also make for ANY product.
2. **Swap test**: replace the product name with a competitor's. If the page still "works", it is generic: change the signature move.
3. **Squint test**: blur your eyes at the layout. There must be ONE focal point and a clear second. If everything is equally loud, remove emphasis from three things.
4. **Accent test**: imagine the accent colour removed. Does hierarchy survive through size, weight and space? If not, the accent is doing structure's job.
5. **Domain test**: does one detail come from the product's world (tabular numbers and signed deltas for finance, monospace and keyboard hints for developer tools, ruled lines and captions for editorial, ingredient facts for skincare)?
6. Change at least one structural decision (layout, type pairing, surface style, or the hero's content) if the plan matches a tell below.

## 2. Tells and what to do instead
| area | tell | instead |
|------|------|---------|
| type | one neutral sans at one weight everywhere; every heading centred; tracked ALL-CAPS eyebrow above every heading; one gradient word in the headline | a pairing from `typography.md` with real contrast of scale (one very large, the rest small); left-aligned headings; eyebrow only where it carries information |
| colour | purple-to-blue gradient on white; cyan glow on near-black "because tech"; grey cards on grey canvas; accent used at 100% everywhere; pure `#000`/`#fff` | one palette id, accent <= 10% of the area, status colours with icons, off-black / off-white from the tokens |
| layout | centred hero, logo cloud, three equal feature cards, alternating zig-zag, testimonial grid, centred CTA band, in that order | follow the blueprint's layout, break the symmetry (a bento, a sticky split, an index list), lead with the product itself |
| shape | everything in a rounded card; card inside card inside card; the same radius on every element | cards only for things that are discrete objects; sections separated by space and rules; nested radius = outer - padding |
| depth | `shadow-lg` + glow on everything; glass on every surface | one elevation system (see `surfaces.md`); blur on at most two surfaces |
| components | gradient buttons with glow; emoji as icons; "Learn more →" on every card; tabs used instead of headings | solid accessible buttons with the full state contract; one icon family; links named by destination |
| content | invented metrics ("10x faster"), fake logos, lorem ipsum, stock avatars, generic testimonials | real or clearly labelled sample content; specific numbers with a source and period; omit what you cannot support |
| copy | "Unlock the power of", "Seamless", "Revolutionize", "Supercharge", "Elevate"; triplet rhythm in every list; em-dash overuse | say what it does in plain words; concrete nouns and verbs; vary sentence length |
| motion | fade-up on each section; floating/bouncing icons; parallax everywhere; looping glows | one orchestrated page-load moment; fast feedback on controls (`motion.md`) |
| imagery | floating gradient blobs; tilted device mockups showing nothing; a stock photo under a dark overlay | the real UI, an SVG diagram, a real photograph, or typography as the image |
| code | `div` soup with `onClick`, `any`, magic pixels, `!important`, no states, one 600-line component | semantic elements, typed props, tokens, small components, five states |
| process | "polish" added at the end | the signature move and the states are designed first |

## 3. Positive moves (how to have a point of view)
- Commit to a direction in one sentence ("quiet editorial index", "loud neo-brutalist poster", "calm instrument panel") and let every choice serve it.
- Spend boldness in ONE place (scale, colour, motion or composition), keep the rest restrained. Restraint is also a direction when executed precisely.
- Use asymmetry and scale contrast deliberately; let one element break the grid.
- Build a memorable, domain-specific detail (the "signature move" column in `blueprints.md`) and make it work, not just look.
- Texture and atmosphere come from real techniques: a CSS gradient mesh with purpose, a hairline grid, a noise layer at 3% opacity, a carefully set type specimen: not from decoration for its own sake.
- Vary between projects: do not reuse the same palette/type/layout combination you used last time. Selection by the brief, not by habit.

## 4. UX writing rules
- Buttons name action + object: "Save changes", "Send message", "Delete project" (never "Submit", "OK", "Click here").
- Sentence case for UI text; no exclamation marks in errors; no blame ("You entered...").
- Errors: what happened, why if known, how to fix. "Enter a 6-digit PIN code."
- Empty states invite: what will appear here, plus the action to create it.
- Confirmations restate the consequence: "Delete this project? This removes its 14 builds."
- Units and context on numbers ("12,480 active users, last 7 days"); dates unambiguous (`12 Mar 2026`); currency formatted for the locale.
- Consistent vocabulary: pick "project" or "workspace" and use it everywhere. Never build sentences by concatenating strings (breaks translation).
- Write real content for the demo; if it is placeholder, label it as sample data.

---

## FILE: references/examples.md

# Worked examples (brief -> plan -> key code -> checks)

Each example shows the thinking order the skill expects: plan first, tokens second, components third, verification last.
The company names are fictional.

---

## Example 1: Hindi-first coding school landing page (blueprint 51)

**Brief:** "Landing page for Aarambh, a Hindi-first coding school for Class 9-12 students. Most visitors are on phones with
limited data. The goal is a WhatsApp enquiry."

**Design plan**
```
Subject / audience / job : coding school; students and parents on 360px Android; job = start a WhatsApp enquiry
Direction                : warm, friendly, trustworthy; Hindi headline, English technical terms kept in Latin
Palette                  : 42 warm-sand (light native, system default)    Type: 35 poppins-vibrant + Devanagari
Surface style            : soft          Layouts: L1 (copy + live demo), L7 (courses), L6 (enquiry)
Signature move           : "Write your first line of code": a tiny live editor, no sign-up, works offline
Risk check               : not the terracotta+cream cliche? accent is ochre on sand: swap test passes because of the live editor
Delivery constraints     : 360x800 first, images <= 60KB, no autoplay video, lang="hi" on Hindi blocks
```

**Setup**
```bash
python3 scripts/tokens_to_tailwind.py --palette warm-sand --default system --out src/theme.css
python3 scripts/font_links.py 35 --hindi      # paste the <link> tags into index.html, the @theme vars into index.css
```

**Key code**
```tsx
import { buttonClass } from './components/Button';

export function Hero() {
  const wa = 'https://wa.me/91XXXXXXXXXX?text=' + encodeURIComponent('नमस्ते, मुझे कोडिंग क्लास की जानकारी चाहिए');
  return (
    <section className="mx-auto grid w-full max-w-6xl items-center gap-10 px-4 py-12 sm:px-6 lg:grid-cols-[minmax(0,6fr)_minmax(0,5fr)] lg:py-24">
      <div className="flex flex-col gap-5">
        <h1 lang="hi" className="text-[clamp(2rem,1.1rem+4vw,3.75rem)] font-bold leading-[1.25]">
          कोडिंग सीखें, शुरुआत से
        </h1>
        <p lang="hi" className="max-w-prose text-lg leading-[1.8] text-muted">
          कक्षा 9 से 12 के लिए हिन्दी में सिखाया जाने वाला HTML, Python और web development का पहला कोर्स।
        </p>
        <div className="flex flex-wrap gap-3">
          <a href={wa} rel="noopener noreferrer" className={buttonClass({ size: 'lg' })}>WhatsApp पर पूछें</a>
          <a href="#courses" className={buttonClass({ variant: 'secondary', size: 'lg' })}>कोर्स देखें</a>
        </div>
      </div>
      <LiveEditor />
    </section>
  );
}
```
`LiveEditor` is a `<textarea>` with a visible `<label>` ("अपना पहला कोड लिखें") whose value renders into a sandboxed
`<iframe srcDoc>` (`sandbox=""`), with a "Run" `Button` and `role="status"` output text. It needs no network.

**Checks that matter here:** Devanagari line-height >= 1.7 (done), headline wraps at 320px without clipping,
`lang="hi"` on Hindi text, `+91` formats and 44px targets, page weight small (fonts: 2 families, <= 4 weights).

---

## Example 2: Ops dashboard for a delivery start-up (blueprint 03 variant)

**Brief:** "Dashboard for dispatchers to watch live deliveries, spot late orders and reassign riders."

**Design plan**
```
Subject / audience / job : dispatch dashboard; dispatchers on large monitors, all day; job = spot late orders fast
Direction                : calm instrument panel; information-dense but quiet; red only for late
Palette                  : 21 midnight-slate (dark native)    Type: 01 inter-minimalist (tabular numbers)
Surface style            : soft          Layouts: L4 (shell), L12 (table)
Signature move           : an ETA-confidence timeline per order (on time / at risk / late) with the rider's last ping age
Risk check               : not a grid of equal gradient KPI cards: ONE hero metric ("Late now: 7") + a quiet strip
Keyboard                 : j/k move between orders, Enter opens details, r reassigns (shown in a visible shortcut list)
```

**Shell and KPI strip**
```tsx
<div className="grid min-h-dvh grid-cols-1 lg:grid-cols-[16rem_minmax(0,1fr)]">
  <aside aria-label="Sidebar" className="hidden border-e border-line bg-surface p-4 lg:block">{/* nav */}</aside>
  <main id="main" className="flex min-w-0 flex-col gap-6 p-4 sm:p-6">
    <section aria-label="Key numbers" className="grid gap-4 sm:grid-cols-[2fr_1fr_1fr]">
      <Card as="article" className="flex flex-col gap-1 border-danger">
        <p className="text-sm text-muted">Late now</p>
        <p className="text-5xl font-bold tabular-nums text-danger">7</p>
        <p className="text-sm text-fg"><span aria-hidden="true">▲</span> 3 more than 10 minutes ago</p>
      </Card>
      <Card as="article"><p className="text-sm text-muted">In transit</p><p className="text-3xl font-semibold tabular-nums">182</p></Card>
      <Card as="article"><p className="text-sm text-muted">Avg. delivery time</p><p className="text-3xl font-semibold tabular-nums">28 min</p></Card>
    </section>
    {/* L12 data page: filters + <table> with sticky header, five states per async view */}
  </main>
</div>
```
Status chips: `Badge` with glyph + text ("▲ At risk", "✕ Late", "✓ On time"). The late card is the only red surface on the page.

**Checks:** table has `caption`, `th scope`, `tabular-nums`, `text-end` numbers; every async view has loading/empty/error;
screen-reader live region announces "3 more late orders" politely; contrast verified with `contrast_check.py --css`.

---

## Example 3: Neo-brutalist portfolio for a motion designer (blueprint 32)

**Brief:** "Loud, raw portfolio. I make title sequences. Light theme, no gradients, big type."

**Design plan**
```
Direction      : loud poster, thick lines, flat colour; accessible despite the noise
Palette        : 35 cyber-lime, LIGHT twin (data-theme="light")    Type: 05 space-grotesk-cyber
Surface style  : brutal (3px borders, hard shadow in fg)             Layouts: L2 (bento of projects)
Signature move : project titles set at 12vw-ish scale that become the hover target; the hard shadow shifts 4px
Risk check     : not a gradient/glass page; colour only from the palette's accent, borders in fg
```

**Setup:** `python3 scripts/tokens_to_tailwind.py --palette cyber-lime --out src/theme.css` then
`<html data-theme="light" data-style="brutal">`.

**Key code**
```tsx
<a href="/work/title-sequence-a"
  className="group block ui-border border-fg bg-surface p-6 shadow-ui transition-[transform,box-shadow] duration-150 hover:-translate-x-1 hover:-translate-y-1 hover:shadow-[10px_10px_0_0_var(--fg)] focus-visible:outline-4 focus-visible:outline-offset-4 focus-visible:outline-accent motion-reduce:transition-none motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0">
  <h2 className="text-[clamp(2.5rem,1rem+9vw,8rem)] font-bold uppercase leading-[0.9] tracking-tight">Title sequence A</h2>
  <p className="mt-3 font-medium">Main titles, 2025. Client: indie feature film.</p>
</a>
```
Video previews are click-to-load (no autoplay), poster images have `alt`, and the loudness never lowers text contrast (`fg` on `surface` is >= 7:1).

---

## Generic output vs skill-level output

| area | generic | skill-level |
|------|---------|-------------|
| first screen | centred headline over a purple gradient, two buttons | one focal point tied to the product (live demo, real UI, strong type), asymmetric composition |
| colour | ad-hoc Tailwind colours and hex values | one palette id, token utilities, accent <= 10%, contrast verified |
| type | Inter at default sizes | pairing from the library, fluid `clamp()` scale, 65ch measure, Hindi-ready stack |
| buttons | gradient + glow, hover only | state contract: focus ring, active, disabled, loading, 44px target |
| forms | placeholder as label, red border as the only error cue | label, hint, error text + icon, `aria-invalid`, summary on submit |
| states | happy path only | loading, empty, error, partial, success all designed |
| motion | fade-up on every section | one orchestrated entrance, per-element reduced-motion handling |
| responsive | desktop mock-up that breaks at 360px | mobile-first, checked at 320/360/768/1280, `dvh` units |
| theming | hard-coded `bg-white`, no dark mode | tokens, `color-scheme`, no-flash toggle |
| delivery | long essay before the code | 3-5 line rationale, complete code, 3 next steps, what was verified |

---

## FILE: assets/starter (source to copy)

### assets/starter/src/index.css

```css
@import "tailwindcss";
@import "./theme.css"; /* generated: python3 ../../scripts/tokens_to_tailwind.py --palette <id> --out src/theme.css */

/* ------------------------------------------------------------------ fonts */
@theme {
  /* Latin face first, then Devanagari, then system fonts (Hindi renders correctly without extra downloads). */
  --font-display: "DM Sans", "Noto Sans Devanagari", system-ui, sans-serif;
  --font-body: "DM Sans", "Noto Sans Devanagari", system-ui, sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
}

/* ------------------------------------------- surface style (one per product)
   <html data-style="soft|glass|brutal|terminal|editorial|organic">. Components read these variables,
   so switching style never needs component edits. */
:root {
  --ui-radius: 0.75rem;
  --ui-radius-lg: 1.25rem;
  --ui-border: 1px;
  --ui-shadow: 0 1px 2px rgb(0 0 0 / 0.06), 0 14px 32px -18px rgb(0 0 0 / 0.28);

  /* interaction colours derived from the verified tokens (they move AWAY from accent-fg, so contrast only improves) */
  --accent-hover: color-mix(in oklab, var(--accent) 86%, var(--fg));
  --accent-active: color-mix(in oklab, var(--accent) 76%, var(--fg));
  --danger-hover: color-mix(in oklab, var(--danger) 88%, var(--fg));
}
[data-style="glass"] {
  --ui-radius: 1rem;
  --ui-radius-lg: 1.75rem;
  --ui-shadow: 0 10px 40px -12px rgb(0 0 0 / 0.45);
}
[data-style="brutal"] {
  --ui-radius: 0px;
  --ui-radius-lg: 0px;
  --ui-border: 3px;
  --ui-shadow: 6px 6px 0 0 var(--fg);
}
[data-style="terminal"] {
  --ui-radius: 2px;
  --ui-radius-lg: 4px;
  --ui-border: 1px;
  --ui-shadow: none;
}
[data-style="editorial"] {
  --ui-radius: 0px;
  --ui-radius-lg: 0px;
  --ui-border: 1px;
  --ui-shadow: none;
}
[data-style="organic"] {
  --ui-radius: 1.25rem;
  --ui-radius-lg: 2rem;
  --ui-border: 1px;
  --ui-shadow: 0 1px 0 rgb(255 255 255 / 0.08) inset, 0 20px 40px -24px rgb(0 0 0 / 0.35);
}

@theme inline {
  --radius-ui: var(--ui-radius);
  --radius-ui-lg: var(--ui-radius-lg);
  --shadow-ui: var(--ui-shadow);
  --color-accent-hover: var(--accent-hover);
  --color-accent-active: var(--accent-active);
  --color-danger-hover: var(--danger-hover);
}

@utility ui-border {
  border-width: var(--ui-border);
  border-style: solid;
}

/* -------------------------------------------------------------------- base */
@layer base {
  html {
    accent-color: var(--accent); /* native checkboxes, radios, sliders */
    -webkit-text-size-adjust: 100%;
    scroll-padding-top: 4rem;
  }
  body {
    background-color: var(--canvas);
    color: var(--fg);
    font-family: var(--font-body);
    line-height: 1.6;
    min-height: 100dvh;
  }
  h1, h2, h3 {
    font-family: var(--font-display);
    line-height: 1.15;
    text-wrap: balance;
  }
  p { text-wrap: pretty; }
  ::selection { background: color-mix(in oklab, var(--accent) 30%, transparent); }

  /* Keyboard focus: visible, 2px, offset, uses the verified accent colour. */
  :focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
  }
  @media (forced-colors: active) {
    :focus-visible { outline-color: Highlight; }
  }
}

/* One orchestrated entrance (not a scattered fade-up on every section). */
@keyframes rise {
  from { opacity: 0; translate: 0 14px; }
  to { opacity: 1; translate: 0 0; }
}
.rise {
  animation: rise 0.6s cubic-bezier(0.2, 0.7, 0.2, 1) both;
  animation-delay: calc(var(--i, 0) * 70ms);
  @media (prefers-reduced-motion: reduce) {
    animation: none;
  }
}

/* ------------------------------------------------- native <dialog> (modal)
   The browser provides focus containment, inert page, Esc/back dismissal, focus return.
   Do NOT add role="dialog", aria-modal, a focus trap, or overflow:hidden on body. */
dialog {
  margin: auto; /* Tailwind preflight resets margin to 0, which removes the UA centring of modal dialogs */
  color: var(--fg);
  background: var(--raised);
  border: var(--ui-border) solid var(--line-strong);
  border-radius: var(--ui-radius-lg);
  box-shadow: var(--ui-shadow);
  padding: 0;
  width: min(32rem, calc(100% - 2rem));
  max-height: calc(100dvh - 2rem);

  /* entry/exit animation (top-layer friendly) */
  opacity: 0;
  transform: scale(0.96);
  transition-property: opacity, transform, display, overlay;
  transition-duration: 0.2s;
  transition-timing-function: ease-out;
  transition-behavior: allow-discrete;
}
dialog[open] {
  opacity: 1;
  transform: scale(1);
  @starting-style {
    opacity: 0;
    transform: scale(0.96);
  }
}
dialog:modal {
  overscroll-behavior: contain; /* stop scroll chaining to the page behind */
}
dialog::backdrop {
  overflow: hidden; /* makes ::backdrop a scroll container so overscroll-behavior applies */
  overscroll-behavior: contain;
  background-color: rgb(0 0 0 / 0);
  transition-property: background-color, display, overlay;
  transition-duration: 0.2s;
  transition-timing-function: ease-out;
  transition-behavior: allow-discrete;
}
dialog[open]::backdrop {
  background-color: rgb(0 0 0 / 0.55);
  @starting-style {
    background-color: rgb(0 0 0 / 0);
  }
}
@media (prefers-reduced-motion: reduce) {
  dialog { transform: none; transition-duration: 0.1s; }
  dialog[open] { @starting-style { transform: none; } }
}
```

### assets/starter/src/theme.css

```css
/* theme.css - generated by scripts/tokens_to_tailwind.py (palette 30 clean-minimalist-saas).
   Regenerate instead of editing values by hand: every pair is contrast-verified. */

:root {
  color-scheme: light dark;
  --canvas: #F4F4F5;
  --surface: #FFFFFF;
  --raised: #FFFFFF;
  --line: #DFDFDF;
  --line-strong: #8A8A8A;
  --fg: #171717;
  --muted: #6B6B6B;
  --accent: #225BD8;
  --accent-fg: #FAFAFA;
  --success: #137337;
  --warning: #A24B08;
  --danger: #B91C1C;
  --info: #1D4ED8;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --canvas: #101113;
    --surface: #191A1D;
    --raised: #202124;
    --line: #37383B;
    --line-strong: #6D6E70;
    --fg: #EEEFF1;
    --muted: #919294;
    --accent: #6B95F1;
    --accent-fg: #0E0F11;
    --success: #34D399;
    --warning: #FBBF24;
    --danger: #F87171;
    --info: #60A5FA;
  }
}
:root[data-theme="light"] {
  color-scheme: light;
  --canvas: #F4F4F5;
  --surface: #FFFFFF;
  --raised: #FFFFFF;
  --line: #DFDFDF;
  --line-strong: #8A8A8A;
  --fg: #171717;
  --muted: #6B6B6B;
  --accent: #225BD8;
  --accent-fg: #FAFAFA;
  --success: #137337;
  --warning: #A24B08;
  --danger: #B91C1C;
  --info: #1D4ED8;
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --canvas: #101113;
  --surface: #191A1D;
  --raised: #202124;
  --line: #37383B;
  --line-strong: #6D6E70;
  --fg: #EEEFF1;
  --muted: #919294;
  --accent: #6B95F1;
  --accent-fg: #0E0F11;
  --success: #34D399;
  --warning: #FBBF24;
  --danger: #F87171;
  --info: #60A5FA;
}

/* Tailwind v4: tokens become utilities, e.g. bg-canvas text-fg border-line bg-accent text-accent-fg */
@theme inline {
  --color-canvas: var(--canvas);
  --color-surface: var(--surface);
  --color-raised: var(--raised);
  --color-line: var(--line);
  --color-line-strong: var(--line-strong);
  --color-fg: var(--fg);
  --color-muted: var(--muted);
  --color-accent: var(--accent);
  --color-accent-fg: var(--accent-fg);
  --color-success: var(--success);
  --color-warning: var(--warning);
  --color-danger: var(--danger);
  --color-info: var(--info);
}
```

### assets/starter/src/lib/cn.ts

```ts
/** Join class names, dropping falsy values. Tiny stand-in for clsx. */
export function cn(...parts: Array<string | false | null | undefined>): string {
  return parts.filter(Boolean).join(' ');
}
```

### assets/starter/src/components/Button.tsx

```tsx
import type { ButtonHTMLAttributes, ReactNode } from 'react';
import { cn } from '../lib/cn';

type Variant = 'primary' | 'secondary' | 'ghost' | 'danger';
type Size = 'sm' | 'md' | 'lg';

const base =
  'inline-flex items-center justify-center gap-2 rounded-ui ui-border border-transparent font-medium ' +
  'select-none transition-colors duration-150 ' +
  'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent ' +
  'disabled:opacity-50 disabled:cursor-not-allowed aria-busy:cursor-progress';

// Hover/active colours keep text contrast >= 4.5:1 (see --accent-hover in index.css).
const variants: Record<Variant, string> = {
  primary: 'bg-accent text-accent-fg hover:bg-accent-hover active:bg-accent-active',
  secondary: 'bg-surface text-fg border-line-strong hover:bg-raised active:bg-canvas',
  ghost: 'text-fg hover:bg-fg/10 active:bg-fg/15',
  danger: 'bg-danger text-canvas hover:bg-danger-hover',
};

// md and lg meet the 44px touch-target minimum; sm is for dense desktop toolbars only.
const sizes: Record<Size, string> = {
  sm: 'min-h-9 px-3 text-sm',
  md: 'min-h-11 px-5 text-base',
  lg: 'min-h-12 px-7 text-lg',
};

/** Class string for anything that must LOOK like a button, e.g. <a href="/pricing" className={buttonClass()}>. */
export function buttonClass({ variant = 'primary', size = 'md', className }: { variant?: Variant; size?: Size; className?: string } = {}): string {
  return cn(base, variants[variant], sizes[size], className);
}

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant;
  size?: Size;
  loading?: boolean;
  children: ReactNode;
}

export function Button({
  variant = 'primary',
  size = 'md',
  loading = false,
  disabled,
  type = 'button', // never rely on the implicit "submit"
  className,
  children,
  ...rest
}: ButtonProps) {
  return (
    <button
      type={type}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
      className={buttonClass({ variant, size, className })}
      {...rest}
    >
      {loading && (
        <svg className="size-4 animate-spin motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <circle cx="12" cy="12" r="9" stroke="currentColor" strokeWidth="3" opacity="0.25" />
          <path d="M21 12a9 9 0 0 0-9-9" stroke="currentColor" strokeWidth="3" strokeLinecap="round" />
        </svg>
      )}
      {children}
    </button>
  );
}
```

### assets/starter/src/components/Field.tsx

```tsx
import { useId } from 'react';
import type { InputHTMLAttributes, ReactNode, TextareaHTMLAttributes } from 'react';
import { cn } from '../lib/cn';

interface ShellProps {
  label: string;
  hint?: string;
  error?: string;
  optional?: boolean;
  children: (a11y: { id: string; describedBy: string | undefined; invalid: boolean }) => ReactNode;
}

/** Label + control + hint + error, wired with htmlFor / aria-describedby / aria-invalid. */
function FieldShell({ label, hint, error, optional, children }: ShellProps) {
  const id = useId();
  const hintId = `${id}-hint`;
  const errId = `${id}-err`;
  const describedBy = [hint && hintId, error && errId].filter(Boolean).join(' ') || undefined;
  return (
    <div className="flex flex-col gap-1.5">
      <label htmlFor={id} className="text-sm font-medium text-fg">
        {label}
        {optional && <span className="ms-1 font-normal text-muted">(optional)</span>}
      </label>
      {children({ id, describedBy, invalid: Boolean(error) })}
      {hint && !error && (
        <p id={hintId} className="text-sm text-muted">
          {hint}
        </p>
      )}
      {error && (
        <p id={errId} className="flex items-start gap-1.5 text-sm text-danger">
          <svg className="mt-0.5 size-4 shrink-0" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path d="M10 2 1 18h18L10 2Zm1 12H9v-2h2v2Zm0-4H9V7h2v3Z" />
          </svg>
          <span>{error}</span>
        </p>
      )}
    </div>
  );
}

const control =
  'w-full min-h-11 rounded-ui ui-border border-line-strong bg-surface px-3 py-2 text-fg ' +
  'placeholder:text-muted transition-colors ' +
  'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent ' +
  'aria-invalid:border-danger disabled:opacity-60 disabled:cursor-not-allowed';

type FieldMeta = Pick<ShellProps, 'label' | 'hint' | 'error' | 'optional'>;

export function TextField({ label, hint, error, optional, className, ...rest }: FieldMeta & Omit<InputHTMLAttributes<HTMLInputElement>, 'id'>) {
  return (
    <FieldShell label={label} hint={hint} error={error} optional={optional}>
      {({ id, describedBy, invalid }) => (
        <input id={id} aria-describedby={describedBy} aria-invalid={invalid || undefined} className={cn(control, className)} {...rest} />
      )}
    </FieldShell>
  );
}

export function TextAreaField({ label, hint, error, optional, className, ...rest }: FieldMeta & Omit<TextareaHTMLAttributes<HTMLTextAreaElement>, 'id'>) {
  return (
    <FieldShell label={label} hint={hint} error={error} optional={optional}>
      {({ id, describedBy, invalid }) => (
        <textarea id={id} aria-describedby={describedBy} aria-invalid={invalid || undefined} className={cn(control, 'field-sizing-content min-h-24', className)} {...rest} />
      )}
    </FieldShell>
  );
}
```

### assets/starter/src/components/Card.tsx

```tsx
import { createElement } from 'react';
import type { HTMLAttributes } from 'react';
import { cn } from '../lib/cn';

interface CardProps extends HTMLAttributes<HTMLElement> {
  as?: 'div' | 'section' | 'article' | 'li';
}

/** Surface container. Radius, border width and shadow come from the active data-style. */
export function Card({ as = 'div', className, ...rest }: CardProps) {
  return createElement(as, {
    className: cn(
      'ui-border rounded-ui-lg border-line bg-surface p-6 shadow-ui',
      'in-data-[style=glass]:bg-surface/60 in-data-[style=glass]:backdrop-blur-xl',
      className,
    ),
    ...rest,
  });
}
```

### assets/starter/src/components/Badge.tsx

```tsx
import type { ReactNode } from 'react';
import { cn } from '../lib/cn';

type Tone = 'neutral' | 'accent' | 'success' | 'warning' | 'danger' | 'info';

// Colour is never the only signal: every tone carries a glyph and a text label.
const tones: Record<Tone, { cls: string; glyph: string }> = {
  neutral: { cls: 'bg-fg/10 text-fg', glyph: '•' },
  accent: { cls: 'bg-accent/10 text-accent', glyph: '★' },
  success: { cls: 'bg-success/10 text-success', glyph: '✓' },
  warning: { cls: 'bg-warning/10 text-warning', glyph: '▲' },
  danger: { cls: 'bg-danger/10 text-danger', glyph: '✕' },
  info: { cls: 'bg-info/10 text-info', glyph: 'i' },
};

export function Badge({ tone = 'neutral', children }: { tone?: Tone; children: ReactNode }) {
  const t = tones[tone];
  return (
    <span className={cn('inline-flex items-center gap-1.5 rounded-full px-2.5 py-0.5 text-sm font-medium', t.cls)}>
      <span aria-hidden="true">{t.glyph}</span>
      {children}
    </span>
  );
}
```

### assets/starter/src/components/Alert.tsx

```tsx
import type { ReactNode } from 'react';
import { cn } from '../lib/cn';

type Tone = 'info' | 'success' | 'warning' | 'danger';

const tones: Record<Tone, { stripe: string; text: string; glyph: string }> = {
  info: { stripe: 'border-s-info', text: 'text-info', glyph: 'i' },
  success: { stripe: 'border-s-success', text: 'text-success', glyph: '✓' },
  warning: { stripe: 'border-s-warning', text: 'text-warning', glyph: '▲' },
  danger: { stripe: 'border-s-danger', text: 'text-danger', glyph: '✕' },
};

/** Danger alerts interrupt screen readers (role="alert"); others are polite (role="status"). */
export function Alert({ tone = 'info', title, children }: { tone?: Tone; title: string; children?: ReactNode }) {
  const t = tones[tone];
  return (
    <div
      role={tone === 'danger' ? 'alert' : 'status'}
      className={cn('flex gap-3 rounded-ui ui-border border-s-4 border-line bg-surface p-4', t.stripe)}
    >
      <span aria-hidden="true" className={cn('mt-0.5 font-bold', t.text)}>
        {t.glyph}
      </span>
      <div className="flex flex-col gap-1">
        <p className={cn('font-semibold', t.text)}>{title}</p>
        {children && <div className="text-sm text-fg">{children}</div>}
      </div>
    </div>
  );
}
```

### assets/starter/src/components/Dialog.tsx

```tsx
import { useId } from 'react';
import type { ReactNode } from 'react';
import { Button } from './Button';
import type { ButtonProps } from './Button';

const nativeInvokers = typeof HTMLButtonElement !== 'undefined' && 'commandForElement' in HTMLButtonElement.prototype;

/**
 * Opens the <dialog> with the given id as a modal.
 * Declarative (command/commandfor, Baseline Dec 2025); falls back to showModal() where unsupported.
 */
export function DialogTrigger({ dialogId, ...props }: Omit<ButtonProps, 'command' | 'commandfor'> & { dialogId: string }) {
  return (
    <Button
      command="show-modal"
      commandfor={dialogId}
      onClick={
        nativeInvokers
          ? undefined
          : () => (document.getElementById(dialogId) as HTMLDialogElement | null)?.showModal()
      }
      {...props}
    />
  );
}

interface DialogProps {
  id: string;
  title: string;
  children: ReactNode;
  /** Buttons rendered in the footer. Put the SAFE action first: it receives initial focus. */
  actions: ReactNode;
  /** Called with the value of the button used ('' for Esc / back gesture). */
  onClose?: (returnValue: string) => void;
}

/**
 * Native modal dialog. The browser already provides: inert page, focus containment,
 * top layer, ::backdrop, Esc / back-gesture dismissal and focus return to the trigger.
 * So: no role="dialog", no aria-modal, no focus-trap code.
 */
export function Dialog({ id, title, children, actions, onClose }: DialogProps) {
  const titleId = useId();
  return (
    <dialog
      id={id}
      aria-labelledby={titleId}
      closedby="any"
      onClose={(e) => {
        const dlg = e.currentTarget;
        onClose?.(dlg.returnValue);
        dlg.returnValue = ''; // reset so a stale value never leaks into the next close
      }}
    >
      <form method="dialog" className="flex flex-col gap-4 p-6">
        <h2 id={titleId} className="text-xl font-semibold">
          {title}
        </h2>
        <div className="text-muted">{children}</div>
        <div className="flex flex-wrap justify-end gap-3 pt-2">{actions}</div>
      </form>
    </dialog>
  );
}
```

### assets/starter/src/components/ThemeToggle.tsx

```tsx
import { useState } from 'react';

type Theme = 'light' | 'dark';

function currentTheme(): Theme {
  const set = document.documentElement.dataset.theme;
  if (set === 'light' || set === 'dark') return set;
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

export function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>(currentTheme);

  function toggle() {
    const next: Theme = theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try {
      localStorage.setItem('theme', next);
    } catch {
      /* storage can be blocked (private mode, sandboxed iframes): the toggle still works for this visit */
    }
    setTheme(next);
  }

  return (
    <button
      type="button"
      onClick={toggle}
      aria-pressed={theme === 'dark'}
      className="inline-flex min-h-11 items-center gap-2 rounded-ui ui-border border-line-strong bg-surface px-4 text-sm font-medium text-fg transition-colors hover:bg-raised"
    >
      <span aria-hidden="true">{theme === 'dark' ? '☾' : '☀'}</span>
      Dark mode
    </button>
  );
}
```

### assets/starter/src/components/Skeleton.tsx

```tsx
import { cn } from '../lib/cn';

/** Placeholder block while data loads. Hidden from screen readers; announce loading on the container instead. */
export function Skeleton({ className }: { className?: string }) {
  return <div aria-hidden="true" className={cn('animate-pulse rounded-ui bg-fg/10 motion-reduce:animate-none', className)} />;
}
```

### assets/starter/src/components/EmptyState.tsx

```tsx
import type { ReactNode } from 'react';

/** An empty screen is an invitation to act: say what is missing and offer the next step. */
export function EmptyState({ title, children, action }: { title: string; children: ReactNode; action?: ReactNode }) {
  return (
    <div className="flex flex-col items-start gap-3 rounded-ui-lg ui-border border-dashed border-line-strong p-8">
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="max-w-prose text-muted">{children}</p>
      {action}
    </div>
  );
}
```

### assets/starter/src/react-augment.d.ts

```ts
// Invoker Commands (command / commandfor) are Baseline since Dec 2025 but not yet in @types/react.
import 'react';

declare module 'react' {
  interface ButtonHTMLAttributes<T> {
    command?: 'show-modal' | 'close' | 'request-close' | 'show-popover' | 'hide-popover' | 'toggle-popover' | `--${string}`;
    commandfor?: string;
  }
}

declare module 'react' {
  // <dialog closedby="any|closerequest|none"> - light-dismiss control (Chromium/Firefox; Safari ignores it gracefully).
  interface DialogHTMLAttributes<T> {
    closedby?: 'any' | 'closerequest' | 'none';
  }
}
```

### assets/starter/index.html

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <!-- Never add maximum-scale or user-scalable=no: it blocks pinch-zoom (WCAG 1.4.4). -->
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!-- Tells the browser both themes exist, so scrollbars/form controls/first paint match. -->
    <meta name="color-scheme" content="light dark" />
    <meta name="description" content="Starter project for Let-s-Code-India-UI-Builder: React, TypeScript and Tailwind CSS v4 with verified design tokens." />
    <title>Let-s-Code-India UI Starter</title>

    <!-- Fonts: replace with the pair you chose (python3 scripts/font_links.py <id>). -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet" />

    <!-- No-flash theme: runs before first paint. localStorage can throw (private mode, sandboxes). -->
    <script>
      try {
        var saved = localStorage.getItem('theme');
        if (saved === 'light' || saved === 'dark') document.documentElement.dataset.theme = saved;
      } catch (e) {}
    </script>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

