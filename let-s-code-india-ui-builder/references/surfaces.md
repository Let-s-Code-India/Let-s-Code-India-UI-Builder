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
