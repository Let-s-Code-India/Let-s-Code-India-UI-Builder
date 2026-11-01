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
