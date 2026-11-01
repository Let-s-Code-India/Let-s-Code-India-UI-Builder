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
