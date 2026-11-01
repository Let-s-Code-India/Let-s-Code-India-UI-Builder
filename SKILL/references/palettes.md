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
