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
