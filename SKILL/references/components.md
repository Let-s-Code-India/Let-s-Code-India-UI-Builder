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
