#!/usr/bin/env python3
"""lint_ui.py - fast static checks for the mistakes AI-generated UI code makes most often.

Usage
  python3 scripts/lint_ui.py src index.html            # files and/or folders
  python3 scripts/lint_ui.py src --strict              # warnings also fail the run
  python3 scripts/lint_ui.py src --ignore transition-all,hardcoded-color

Exit code: 0 = no errors, 1 = errors found (or warnings with --strict).
This is a heuristic linter (no AST). It is deliberately conservative: an ERROR is almost
always a real bug; a WARN is a smell worth a look. Class-name validity is a separate,
exact check: scripts/check_classes.mjs (uses the real Tailwind compiler).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EXTS = {".tsx", ".jsx", ".ts", ".js", ".html", ".htm", ".vue", ".svelte", ".css", ".astro"}
SKIP_DIRS = {"node_modules", "dist", "build", ".git", ".next", ".vite", "coverage"}
SKIP_FILES = {"theme.css", "palettes.css"}  # generated token files may contain raw hex

TW_COLORS = ("slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|"
             "cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose")
VALID_SHADES = {"50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"}

RE_BAD_SHADE = re.compile(rf"\b(?:bg|text|border|ring|from|to|via|fill|stroke|divide|outline|shadow|accent|caret|decoration)-(?:{TW_COLORS})-(\d{{2,3}})\b")
RE_ZHUGE = re.compile(r"(?<![\w-])z-(?:\[\d{3,}\]|\d{3,}\b)|z-index\s*:\s*\d{3,}")
TAG = r"(?:=>|[^>])*"  # JSX attributes may contain arrow functions
RE_IMG = re.compile(rf"<img\b(?!{TAG}\balt\s*=){TAG}>", re.S)
RE_BTN = re.compile(rf"<button\b(?!{TAG}\btype\s*=){TAG}>", re.S)
RE_INPUT = re.compile(rf"<input\b({TAG})>", re.S)
RE_CLICK_DIV = re.compile(rf"<(?:div|span|li|p|section)\b(?!{TAG}\brole\s*=){TAG}\bonClick\s*=", re.S)
RE_TABINDEX = re.compile(r"tab[iI]ndex\s*=\s*[\"{]\s*([1-9]\d*)")
RE_VIEWPORT = re.compile(r"(user-scalable\s*=\s*(?:no|0)|maximum-scale\s*=\s*1(?:\.0)?\b)")
RE_HTML_NO_LANG = re.compile(r"<html\b(?![^>]*\blang\s*=)[^>]*>", re.I)
RE_VH = re.compile(r"(?<![\w-])(?:min-|max-)?h-screen\b|\b100vh\b")
RE_HEX_ARB = re.compile(r"\b(?:bg|text|border|ring|fill|stroke|from|to|via|outline|shadow|decoration)-\[#[0-9a-fA-F]{3,8}\]")
RE_ABS = re.compile(r"(?<![\w-])(?:bg|border)-(?:white|black)\b|(?<![\w:-])text-(?:white|black)\b")
RE_PXFONT = re.compile(r"\btext-\[\d+(?:\.\d+)?px\]")
RE_BLUR = re.compile(r"\bbackdrop-blur")
RE_DEADLINK = re.compile(r"<a\b[^>]*\bhref\s*=\s*[\"']#[\"']", re.S)
RE_BLANK = re.compile(r"<a\b(?=[^>]*target\s*=\s*[\"']_blank[\"'])(?![^>]*\brel\s*=)[^>]*>", re.S)
RE_REDUCED_HACK = re.compile(r"(?:animation|transition)-duration\s*:\s*0?\.01ms")
RE_DIALOG_ARIA = re.compile(r"<dialog\b[^>]*(?:role\s*=\s*[\"']dialog|aria-modal)", re.S)
RE_OUTLINE_OFF = re.compile(r"\b(?:focus(?:-visible)?:)?outline-(?:none|hidden|0)\b|outline\s*:\s*(?:none|0)\b")
RE_FOCUS_STYLE = re.compile(r"focus(?:-visible|-within)?:(?:ring|outline|border|shadow|bg|underline)|:focus-visible|:focus\b")
RE_LOREM = re.compile(r"lorem ipsum", re.I)
RE_HEX_CSS = re.compile(r"#(?:000|fff|000000|ffffff)\b", re.I)


def blank_comments(text: str) -> str:
    """Replace HTML and /* */ comments with spaces (newlines kept) so rules never fire on prose."""
    def blank(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    return re.sub(r"/\*.*?\*/", blank, text, flags=re.S)


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def lint_text(path: Path, text: str, ignore: set[str]):
    out: list[tuple[int, str, str, str]] = []  # (line, level, rule, msg)

    def add(pos_or_line, level, rule, msg, is_pos=True):
        if rule in ignore:
            return
        ln = line_of(text, pos_or_line) if is_pos else pos_or_line
        out.append((ln, level, rule, msg))

    text = blank_comments(text)
    ext = path.suffix.lower()
    is_markup = ext in {".tsx", ".jsx", ".html", ".htm", ".vue", ".svelte", ".astro"}
    is_css = ext == ".css"

    for m in RE_BAD_SHADE.finditer(text):
        if m.group(1) not in VALID_SHADES:
            add(m.start(), "ERROR", "bad-shade", f"'{m.group(0)}' does not exist in the Tailwind palette (shades: 50-950).")
    for m in RE_ZHUGE.finditer(text):
        add(m.start(), "ERROR", "z-index-war", "z-index >= 100: use the top layer (<dialog>/popover) or the small scale (z-10/z-40/z-50).")
    for m in RE_REDUCED_HACK.finditer(text):
        add(m.start(), "ERROR", "reduced-motion-hack", "global 0.01ms duration makes some animations MORE jarring; handle reduced motion per element.")
    for m in RE_VIEWPORT.finditer(text):
        add(m.start(), "ERROR", "zoom-blocked", "viewport blocks pinch-zoom (WCAG 1.4.4). Remove user-scalable/maximum-scale.")
    for m in RE_TABINDEX.finditer(text):
        add(m.start(), "ERROR", "positive-tabindex", "tabindex > 0 breaks natural focus order; use 0 or -1.")

    if is_markup:
        for m in RE_IMG.finditer(text):
            add(m.start(), "ERROR", "img-alt", "<img> without alt (use alt=\"\" for decorative images).")
        for m in RE_CLICK_DIV.finditer(text):
            add(m.start(), "ERROR", "div-onclick", "onClick on a non-interactive element: use <button> or <a>.")
        for m in RE_BTN.finditer(text):
            add(m.start(), "WARN", "button-type", "<button> without type (defaults to submit inside forms).")
        for m in RE_INPUT.finditer(text):
            attrs = m.group(1)
            if re.search(r"type\s*=\s*[\"'{]\s*(hidden|submit|button|reset|image)", attrs):
                continue
            if text.rfind("<label", 0, m.start()) > text.rfind("</label>", 0, m.start()):
                continue  # nested in <label>: implicit association
            if not re.search(r"\b(id|aria-label|aria-labelledby)\s*=", attrs) and "{...props}" not in attrs and "{...rest}" not in attrs:
                add(m.start(), "WARN", "input-label", "<input> has no id / aria-label to associate a <label>.")
        for m in RE_DEADLINK.finditer(text):
            add(m.start(), "WARN", "dead-link", "href=\"#\" goes nowhere; link a real target or use <button>.")
        for m in RE_BLANK.finditer(text):
            add(m.start(), "WARN", "blank-rel", "target=\"_blank\" without rel=\"noopener noreferrer\".")
        for m in RE_DIALOG_ARIA.finditer(text):
            add(m.start(), "WARN", "dialog-aria", "native <dialog> opened with showModal() already exposes dialog semantics; drop role/aria-modal.")
        for m in RE_LOREM.finditer(text):
            add(m.start(), "WARN", "lorem", "placeholder text: write real, specific copy.")
        if ext in {".html", ".htm"}:
            for m in RE_HTML_NO_LANG.finditer(text):
                add(m.start(), "WARN", "html-lang", "<html> without lang (use lang=\"en\" or \"hi\").")
            n_h1 = len(re.findall(r"<h1\b", text, re.I))
            spa_shell = re.search(r"id\s*=\s*[\"'](root|app)[\"']", text) and re.search(r"type\s*=\s*[\"']module", text)
            if n_h1 != 1 and re.search(r"<body\b", text, re.I) and not spa_shell:
                add(1, "WARN", "h1-count", f"page has {n_h1} <h1>; expected exactly 1.", is_pos=False)
        for m in RE_HEX_ARB.finditer(text):
            add(m.start(), "WARN", "hardcoded-color", f"'{m.group(0)}' bypasses tokens; use bg-canvas/surface/accent, text-fg/muted, border-line.")
        for m in RE_ABS.finditer(text):
            add(m.start(), "WARN", "absolute-color", f"'{m.group(0).strip()}' ignores the active theme; use a token (surface, fg, accent-fg ...).")
        for m in RE_PXFONT.finditer(text):
            add(m.start(), "WARN", "px-font", f"'{m.group(0)}': use the type scale (text-sm/base/lg...) or clamp() for fluid headings.")
        if len(RE_BLUR.findall(text)) > 4:
            add(1, "WARN", "blur-budget", "more than 4 backdrop-blur uses: expensive on low-end Android; keep it to 1-2 hero surfaces.", is_pos=False)

    for m in RE_VH.finditer(text):
        add(m.start(), "WARN", "vh-units", "100vh/h-screen jumps with mobile browser bars; use dvh (min-h-dvh / 100dvh).")
    if "transition-all" in text:
        add(text.index("transition-all"), "WARN", "transition-all",
            "transition-all animates layout properties; list properties (transition-colors, transition-transform, transition-opacity).")

    # focus indicator removed without replacement (line-level heuristic)
    for i, line in enumerate(text.splitlines(), start=1):
        if RE_OUTLINE_OFF.search(line) and not RE_FOCUS_STYLE.search(line):
            if is_css:
                if ":focus-visible" in text:
                    continue
            if "outline-hidden" in line and "focus-visible" in line:
                continue
            add(i, "ERROR", "focus-removed", "focus outline removed without a replacement indicator (use :focus-visible ring/outline).", is_pos=False)

    if is_css and path.name not in SKIP_FILES:
        for m in RE_HEX_CSS.finditer(text):
            add(m.start(), "WARN", "pure-black-white", "pure #000/#fff: prefer token colours (canvas/fg) to avoid harsh contrast.")
        if text.count("!important") > 3:
            add(1, "WARN", "important", "more than 3 uses of !important: fix specificity instead.", is_pos=False)
    return out


def collect(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for p in map(Path, paths):
        if p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.is_file() and f.suffix.lower() in EXTS and not (set(f.parts) & SKIP_DIRS) and f.name not in SKIP_FILES:
                    files.append(f)
        elif p.is_file():
            files.append(p)
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--strict", action="store_true", help="fail on warnings too")
    ap.add_argument("--ignore", default="", help="comma-separated rule ids to skip")
    a = ap.parse_args()
    ignore = {x.strip() for x in a.ignore.split(",") if x.strip()}
    files = collect(a.paths)
    if not files:
        print("no files to lint")
        return 2
    errors = warns = 0
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for ln, level, rule, msg in sorted(lint_text(f, text, ignore)):
            print(f"{f}:{ln}: [{level}] {rule} - {msg}")
            errors += level == "ERROR"
            warns += level == "WARN"
    print(f"\n{len(files)} files checked: {errors} error(s), {warns} warning(s)")
    return 1 if errors or (a.strict and warns) else 0


if __name__ == "__main__":
    sys.exit(main())
