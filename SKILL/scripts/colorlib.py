#!/usr/bin/env python3
"""colorlib.py - shared colour maths for Let-s-Code-India-UI-Builder.

Standard library only. Provides WCAG contrast, HSL/mix helpers and
`derive_tokens()`, which turns three seed colours (canvas, surface, accent)
into a complete, contrast-verified token set.

Token names (used everywhere in this skill):
  canvas, surface, raised, line, line-strong, fg, muted,
  accent, accent-fg, success, warning, danger, info
"""
from __future__ import annotations

import colorsys
import re

TOKEN_ORDER = [
    "canvas", "surface", "raised", "line", "line-strong", "fg", "muted",
    "accent", "accent-fg", "success", "warning", "danger", "info",
]

_HEX = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


# ---------------------------------------------------------------- basics
def norm(h: str) -> str:
    """Normalise '#abc' / 'ABCDEF' to '#RRGGBB' (upper-case)."""
    m = _HEX.match(h.strip())
    if not m:
        raise ValueError(f"not a hex colour: {h!r}")
    v = m.group(1)
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    return "#" + v.upper()


def to_rgb(h: str) -> tuple[int, int, int]:
    h = norm(h)[1:]
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def to_hex(rgb) -> str:
    r, g, b = (max(0, min(255, int(round(c)))) for c in rgb)
    return f"#{r:02X}{g:02X}{b:02X}"


def lum(h: str) -> float:
    """WCAG 2.x relative luminance."""
    def chan(c: int) -> float:
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = to_rgb(h)
    return 0.2126 * chan(r) + 0.7152 * chan(g) + 0.0722 * chan(b)


def contrast(a: str, b: str) -> float:
    la, lb = lum(a), lum(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


def to_hsl(h: str) -> tuple[float, float, float]:
    r, g, b = (c / 255 for c in to_rgb(h))
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    return hh, ss, ll


def from_hsl(h: float, s: float, l: float) -> str:
    r, g, b = colorsys.hls_to_rgb(h % 1.0, max(0, min(1, l)), max(0, min(1, s)))
    return to_hex((r * 255, g * 255, b * 255))


def mix(a: str, b: str, t: float) -> str:
    """Linear sRGB mix; t = amount of b (0..1)."""
    ra, rb = to_rgb(a), to_rgb(b)
    return to_hex(tuple(x + (y - x) * t for x, y in zip(ra, rb)))


def min_contrast(c: str, against: list[str]) -> float:
    return min(contrast(c, x) for x in against)


def is_dark(h: str) -> bool:
    return lum(h) < 0.18


# ------------------------------------------------------------ derivation
def _against(against, color: str) -> list[str]:
    return against(color) if callable(against) else against


def _tints(color: str, base: list[str], amount: float = 0.12) -> list[str]:
    """Backgrounds a status/accent colour can sit on: plain surfaces plus its own 12% tint
    (the `bg-accent/10 text-accent` pattern)."""
    return base + [mix(b, color, amount) for b in base]


def _nudge(color: str, against, target: float, toward: str,
           limit: float = 0.85) -> tuple[str, bool]:
    """Mix `color` toward `toward` in small steps until min contrast >= target.
    `against` is a list of backgrounds or a function colour -> list of backgrounds."""
    if min_contrast(color, _against(against, color)) >= target:
        return color, False
    t = 0.0
    while t < limit:
        t += 0.02
        cand = mix(color, toward, t)
        if min_contrast(cand, _against(against, cand)) >= target:
            return cand, True
    return mix(color, toward, limit), True


def derive_tokens(canvas: str, surface: str, accent: str, mode: str):
    """Return (tokens, notes) for one mode ('dark' or 'light').

    Guarantees (checked again by contrast_check.py):
      fg >= 7:1, muted >= 4.5:1, accent >= 4.5:1, accent-fg on accent (also its hover/active mixes) >= 4.5:1,
      line-strong >= 3:1, status colours >= 4.5:1 - each against
      canvas, surface, raised AND their own 12% tint (bg-accent/10 text-accent).
    """
    dark = mode == "dark"
    notes: list[str] = []
    canvas, surface, accent = norm(canvas), norm(surface), norm(accent)
    h, s, _ = to_hsl(canvas)

    # ---- surface sanity -------------------------------------------------
    ratio = contrast(canvas, surface)
    if dark:
        too_bright = lum(surface) > lum(canvas) and ratio > 2.2
        if lum(surface) <= lum(canvas) or ratio < 1.08 or too_bright:
            old = surface
            surface = canvas
            t = 0.0
            while contrast(canvas, surface) < 1.13 and t < 0.3:
                t += 0.01
                surface = mix(canvas, "#FFFFFF", t)
            notes.append(f"surface derived (seed {old} unusable as card colour)")
    else:
        if ratio < 1.08:
            if lum(surface) < lum(canvas):
                notes.append(f"canvas {canvas} -> {surface}, surface -> #FFFFFF (layering)")
                canvas, surface = surface, "#FFFFFF"
            else:
                notes.append("surface derived (too close to canvas)")
                surface = mix(canvas, "#000000", 0.05)
        elif ratio > 2.2:
            notes.append(f"surface derived (seed {surface} too strong)")
            surface = mix(canvas, "#000000", 0.05)

    # ---- raised ---------------------------------------------------------
    if dark:
        raised = surface
        t = 0.0
        while contrast(surface, raised) < 1.08 and t < 0.25:
            t += 0.01
            raised = mix(surface, "#FFFFFF", t)
    else:
        raised = "#FFFFFF"

    base = [canvas, surface, raised]

    # ---- fg (>= 7:1) -----------------------------------------------------
    tint_s = min(s, 0.22)
    if dark:
        fg = from_hsl(h, tint_s, 0.94)
        toward = "#FFFFFF"
    else:
        fg = from_hsl(h, tint_s, 0.09)
        toward = "#000000"
    fg, _ = _nudge(fg, base, 7.0, toward, 1.0)

    # ---- muted (>= 4.5:1, as quiet as allowed) -------------------------
    muted = fg
    for t in (0.46, 0.42, 0.38, 0.34, 0.30, 0.26, 0.22, 0.18, 0.14, 0.10, 0.06):
        cand = mix(fg, canvas, t)
        if min_contrast(cand, base) >= 4.6:
            muted = cand
            break

    # ---- borders --------------------------------------------------------
    line = mix(surface, fg, 0.14)
    line_strong = fg
    for t in [x / 100 for x in range(20, 100, 2)]:
        cand = mix(canvas, fg, t)
        if min_contrast(cand, base) >= 3.0:
            line_strong = cand
            break

    # ---- accent (usable as text/link colour) ----------------------------
    accent_toward = "#FFFFFF" if dark else "#000000"
    new_accent, changed = _nudge(accent, lambda c: _tints(c, base), 4.5, accent_toward)
    if changed:
        notes.append(f"accent {accent} -> {new_accent} (4.5:1 on canvas/surface)")
    accent = new_accent

    # ---- accent-fg (>= 4.5:1 on accent) ---------------------------------
    dark_ink = from_hsl(h, min(s, 0.2), 0.06)
    light_ink = from_hsl(h, min(s, 0.1), 0.98)
    for _ in range(60):
        ink = dark_ink if contrast(accent, dark_ink) >= contrast(accent, light_ink) else light_ink
        hover, active = mix(accent, fg, 0.14), mix(accent, fg, 0.24)  # button states mix accent toward fg
        if min(contrast(accent, ink), contrast(hover, ink), contrast(active, ink)) >= 4.7:
            break
        accent = mix(accent, "#FFFFFF" if dark else "#000000", 0.03)
    accent_fg = dark_ink if contrast(accent, dark_ink) >= contrast(accent, light_ink) else light_ink

    # ---- status colours ---------------------------------------------------
    status_base = (
        {"success": "#34D399", "warning": "#FBBF24", "danger": "#F87171", "info": "#60A5FA"}
        if dark else
        {"success": "#15803D", "warning": "#B45309", "danger": "#B91C1C", "info": "#1D4ED8"}
    )
    status = {}
    for k, v in status_base.items():
        status[k], _ = _nudge(v, lambda c: _tints(c, base), 4.5, accent_toward)

    tokens = {
        "canvas": canvas, "surface": surface, "raised": raised,
        "line": line, "line-strong": line_strong,
        "fg": fg, "muted": muted,
        "accent": accent, "accent-fg": accent_fg,
        **status,
    }
    return tokens, notes


def verify_tokens(t: dict) -> list[str]:
    """Return a list of human-readable failures (empty list = all good)."""
    base = [t["canvas"], t["surface"], t["raised"]]
    fails: list[str] = []

    def need(name: str, ratio: float, target: float) -> None:
        if ratio + 1e-9 < target:
            fails.append(f"{name} {ratio:.2f} < {target}")

    need("fg", min_contrast(t["fg"], base), 7.0)
    need("muted", min_contrast(t["muted"], base), 4.5)
    need("accent", min_contrast(t["accent"], _tints(t["accent"], base)), 4.5)
    need("accent-fg/accent", contrast(t["accent-fg"], t["accent"]), 4.5)
    need("accent-fg/accent-hover", contrast(t["accent-fg"], mix(t["accent"], t["fg"], 0.14)), 4.5)
    need("accent-fg/accent-active", contrast(t["accent-fg"], mix(t["accent"], t["fg"], 0.24)), 4.5)
    need("line-strong", min_contrast(t["line-strong"], base), 3.0)
    for k in ("success", "warning", "danger", "info"):
        need(k, min_contrast(t[k], _tints(t[k], base)), 4.5)
    need("surface/canvas", contrast(t["surface"], t["canvas"]), 1.04)
    return fails


def twin_seeds(native_canvas: str, native_mode: str, accent: str):
    """Seed colours for the opposite theme (light twin of a dark palette, etc.)."""
    h, s, _ = to_hsl(native_canvas)
    neutral = s < 0.03          # greys have no hue: borrow the accent's hue for a quiet, harmonious tint
    if neutral:
        h = to_hsl(accent)[0]
        s = 0.12 if native_mode == "dark" else 0.10   # becomes ~0.04-0.08 after the scaling below
    if native_mode == "dark":
        s2 = min(max(s * 0.45, 0.04), 0.22)
        return from_hsl(h, s2, 0.955), "#FFFFFF", accent, "light"
    s2 = min(max(s * 0.7, 0.08), 0.35)
    return from_hsl(h, s2, 0.07), from_hsl(h, s2, 0.105), accent, "dark"


if __name__ == "__main__":  # tiny self-test
    t, n = derive_tokens("#0B0B0B", "#141414", "#EF4444", "dark")
    assert t["fg"] and contrast(t["fg"], t["canvas"]) >= 7
    print("colorlib ok", t, n)
