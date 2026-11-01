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
