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
