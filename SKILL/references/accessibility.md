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
