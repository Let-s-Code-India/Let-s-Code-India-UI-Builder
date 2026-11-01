#!/usr/bin/env python3
"""build_blueprints.py - writes references/blueprints.md from the table below.

Each blueprint is a concrete starting hypothesis: palette id + type pairing id + surface style +
layout recipe + ONE signature move. Ids are validated against build_palettes.SEEDS,
font_links.PAIRS, the style list and the layout ids in references/surfaces.md.

Usage: python3 scripts/build_blueprints.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_palettes import SEEDS  # noqa: E402
from font_links import PAIRS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STYLES = {"soft", "glass", "brutal", "terminal", "editorial", "organic"}
LAYOUTS = {f"L{i}" for i in range(1, 13)}
PID = {s[0]: s[1] for s in SEEDS}
TID = {p[0]: p[1] for p in PAIRS}

# (name, palette#, type#, style, layouts, signature move)
B = [
    ("Cyberpunk AI startup", 1, 5, "glass", "L1 L2", "Live model output streams into a real, copyable terminal pane with a latency badge; crimson only for the live status and the primary CTA."),
    ("Developer terminal portfolio", 4, 22, "terminal", "L1", "Projects open as README panes; `/` opens a keyboard command palette; the whole site still reads with JavaScript off."),
    ("SaaS analytics dashboard", 21, 1, "soft", "L4 L12", "KPI strip with sparklines and the comparison period; saved views as tabs; every chart has a 'view as table' toggle."),
    ("Cloud infrastructure startup", 8, 2, "soft", "L1 L3", "Architecture diagram that redraws with a region/scale slider; status-page link lives in the header."),
    ("Open source tool portal", 4, 30, "terminal", "L7", "Install command with package-manager tabs and one-click copy; real repository stats; contributors strip."),
    ("Web3 and crypto protocol", 3, 23, "glass", "L2", "Live on-chain stats ticker that pauses on hover and focus; risk disclosure always visible, not buried."),
    ("AI LLM playground", 7, 24, "soft", "L3", "Prompt/response split with token counter, streaming caret and a parameter drawer; stop and retry are always reachable."),
    ("Cyber security dashboard", 39, 21, "terminal", "L4", "Alert feed ordered by severity with icon + label; red reserved for critical only; incident timeline per alert."),
    ("Automation agency landing", 25, 3, "soft", "L2", "Before/after workflow diagram with real hours-saved numbers; the booking form has three fields."),
    ("Mobile app landing page", 8, 40, "soft", "L1", "A phone frame built in CSS showing the real onboarding UI; store badges are real links; a QR code for desktop visitors."),
    ("Luxury jewellery brand", 11, 12, "editorial", "L11", "Slow product zoom on hover (tap on touch); gold used only as 1px rules and the single CTA."),
    ("High-end architecture studio", 17, 16, "editorial", "L5", "Project index as a typographic list; hovering reveals the image; floor plans drawn as SVG."),
    ("Designer fashion magazine", 15, 15, "editorial", "L5 L10", "Oversized serif masthead, drop-cap article opener, asymmetric image grid with captions."),
    ("Fine dining restaurant", 12, 14, "organic", "L11", "Menu set as a typographic page with dietary marks as icon + text; reservation widget shows real time slots."),
    ("Art gallery and exhibition", 16, 19, "editorial", "L10", "Artwork viewer with title, medium and dimensions; calm 'gallery wall' backdrop; keyboard next/previous."),
    ("Boutique hotel landing", 13, 11, "organic", "L11", "Room explorer with price per night and an availability calendar that works by keyboard."),
    ("Organic skincare brand", 41, 38, "organic", "L8", "Ingredient glossary in popovers; plain-language product facts; no unverifiable before/after claims."),
    ("Aesthetic portfolio", 14, 7, "soft", "L10", "Case studies show constraints, process and outcome; masonry gallery with real alt text."),
    ("Horology showcase", 18, 13, "editorial", "L11", "Movement exploded view drawn in SVG; parts are labelled on hover and on tap."),
    ("Heritage coffee brand", 47, 17, "organic", "L8", "Origin map and tasting-notes wheel as accessible SVG; subscription chooser with clear cadence and price."),
    ("Neobank mobile web app", 22, 4, "soft", "L6 L4", "Balance card with a privacy-hide toggle; transaction rows align amounts right with merchant and category."),
    ("Crypto trading platform", 24, 1, "soft", "L4", "Order ticket with live price, fee preview and a confirm step; gain/loss shown with arrows plus signed numbers."),
    ("Investment fund portal", 27, 34, "soft", "L12", "Performance chart with period selector and standard disclosures; downloadable factsheet."),
    ("Global logistics enterprise", 21, 32, "soft", "L4", "Shipment timeline with ETA confidence; map as SVG with a table fallback."),
    ("Tax and legal advisory firm", 49, 31, "editorial", "L5", "Plain-language explainers with a deadline calendar; consultation form asks only what is needed."),
    ("InsurTech landing page", 23, 36, "soft", "L7", "Three-step quote estimator with a running premium; policy terms available as plain text."),
    ("Accounting SaaS", 28, 10, "soft", "L12", "Invoice editor with a live preview; keyboard-first table entry."),
    ("Enterprise HR portal", 26, 33, "soft", "L4", "Leave balance and request flow; org chart as an accessible tree."),
    ("Real estate investment firm", 45, 39, "soft", "L7", "Yield calculator with sliders AND numeric inputs; property cards with real facts."),
    ("Venture capital website", 25, 40, "editorial", "L5", "Portfolio as an index list with sector filter; thesis essays set for reading."),
    ("Gen-Z creator portfolio", 31, 3, "soft", "L2", "Link-hub of stacked cards and embeds, with a 'now' status line."),
    ("Neo-brutalist agency", 35, 5, "brutal", "L2", "Oversized type, thick borders, hover shifts the hard shadow; still fully keyboard and screen-reader accessible."),
    ("Indie game studio portal", 34, 48, "brutal", "L7", "Game cards with platform icons + text; trailer behind a click-to-load facade (no autoplay)."),
    ("Music producer or DJ", 32, 7, "glass", "L1", "Waveform player with real audio, keyboard controls and a transcript for talk content."),
    ("Podcast and media hub", 37, 41, "soft", "L7", "Episode list with a sticky mini-player, chapters and transcripts."),
    ("Streetwear e-commerce", 31, 8, "brutal", "L7", "Drop countdown from a real timestamp (announced politely to screen readers); size picker as a radio group."),
    ("Digital art collective", 38, 47, "glass", "L10", "Artist pages with honest fee breakdowns on any mint or purchase flow."),
    ("Meme and viral portal", 25, 43, "brutal", "L10", "Fast list with a 'Load more' button instead of an infinite-scroll trap."),
    ("Futuristic event landing", 39, 46, "terminal", "L1", "Schedule grid with a timezone switch (IST by default), speaker cards, add-to-calendar."),
    ("EdTech and learning hub", 33, 35, "soft", "L7", "Course cards with duration, level and language badges; progress shown as ring + text."),
    ("Eco and green energy", 44, 36, "organic", "L3", "Impact counters with cited sources; savings calculator with visible assumptions."),
    ("Meditation app", 42, 38, "organic", "L6", "Breathing circle that swaps to text counts under reduced motion; session picker with durations."),
    ("Organic agriculture platform", 50, 37, "organic", "L7", "Farm profiles with batch traceability; seasonal availability calendar."),
    ("Architecture and interior design", 41, 9, "editorial", "L5", "Before/after slider whose handle works by keyboard (arrow keys)."),
    ("Craft coffee and bakery", 47, 17, "organic", "L8", "Today's menu with sold-out states; click-and-collect time picker."),
    ("Minimalist blogging platform", 49, 17, "editorial", "L5", "Reading-first: 65ch measure, reading progress, footnotes as popovers."),
    ("Holistic health and yoga studio", 43, 39, "organic", "L8", "Class schedule table with level badges; booking with a waitlist state."),
    ("Handmade crafts e-commerce", 48, 38, "organic", "L7", "Maker stories on product pages; made-to-order lead time shown before add-to-cart."),
    ("Non-profit or social cause", 46, 32, "soft", "L8", "Impact numbers with sources; two-step donate form that supports UPI."),
    ("Personal developer brand hub", 5, 2, "glass", "L1", "Now / Writing / Projects index with RSS; light and dark both polished."),
    # India-first extras
    ("Hindi-first EdTech for Bharat learners", 42, 35, "soft", "L7", "Persistent हिन्दी / English switch in the header; lessons light on data; Devanagari line-height >= 1.7."),
    ("UPI / fintech app for Bharat", 22, 4, "soft", "L6", "Rupee amounts with Indian grouping (Rs 1,23,456); UPI ID field with a verify state; 44px+ tap targets."),
    ("Local store ordering (WhatsApp-first)", 44, 37, "organic", "L7", "Catalogue with quantity steppers, a running cart bar and an 'Order on WhatsApp' deep link; small images for 2G/3G."),
    ("Government service portal", 49, 32, "editorial", "L6", "Step-by-step application with save and resume; plain-language labels in two or more languages; WCAG AA; print-friendly."),
]


def main() -> int:
    rows = []
    for i, (name, p, t, style, layouts, sig) in enumerate(B, start=1):
        assert p in PID and t in TID, (i, p, t)
        assert style in STYLES, (i, style)
        assert all(x in LAYOUTS for x in layouts.split()), (i, layouts)
        rows.append(f"| {i:02d} | {name} | `{PID[p]}` ({p:02d}) | `{TID[t]}` ({t:02d}) | {style} | {layouts} | {sig} |")
    md = ["# Blueprints (54 starting hypotheses)",
          "",
          "A blueprint is a *hypothesis*, not a template. Use it to skip blank-page indecision, then do the anti-generic",
          "review (`anti-generic.md`) and change at least one structural decision so your result is not a clone.",
          "If the user has brand colours, keep the blueprint's structure and derive the theme from the brand:",
          "`python3 scripts/tokens_to_tailwind.py --brand \"#HEX\" --mode dark|light`.",
          "",
          "Columns: palette id (`palettes.md`), type pairing id (`typography.md`), surface style and layouts (`surfaces.md`),",
          "and the ONE signature move that makes the page memorable. Everything else stays quiet so the signature can work.",
          "",
          "| # | archetype | palette | type | style | layout | signature move |",
          "|---|-----------|---------|------|-------|--------|----------------|",
          *rows,
          "",
          "Rows 51-54 are India-first: Devanagari/Indic scripts, rupee formatting (`Intl.NumberFormat('en-IN')`), UPI, WhatsApp, low-bandwidth,",
          "and 360x800 as the primary viewport. See `SKILL.md` -> India-first defaults.",
          ""]
    (ROOT / "references/blueprints.md").write_text("\n".join(md), encoding="utf-8")
    print(f"wrote references/blueprints.md ({len(B)} blueprints)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
