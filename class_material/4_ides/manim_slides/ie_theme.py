"""Shared look and helpers for the Module 4 slides (IE University palette).

Metaphor used everywhere: Python development is a WORKSHOP.
  IDE = toolbox / workbench, library = tool, pip/conda = delivery,
  environment = one bench per project, script = blueprint, notebook = sketchbook.
"""

from manim import *  # noqa: F401,F403
from manim_slides import Slide

# --- IE University palette (see the ie-brand skill) -------------------------
OCEAN = "#000066"      # primary: headings
MARINE = "#0032A0"     # accent: strokes, diagrams
SEA = "#47BFFF"        # decoration only, never text
LIGHT = "#BDE8FF"      # surfaces
ICE = "#E6F7FF"        # soft surfaces
INK = "#0F0F0F"        # body text
GREY = "#434445"       # secondary text
SOFT = "#F4F4F4"       # soft background
GREEN = "#6DC201"      # decoration / success (pair with text + icon)
TANGERINE = "#FF7B31"  # highlight
RED = "#F31233"        # decoration / error (pair with text + icon)
WINE = "#7E1103"       # error text on light backgrounds
YELLOW = "#FBCA1E"     # warning decoration
NIGHT = "#1B1A43"      # terminal background
MIDDLE = "#BFC1C3"     # terminal secondary text

FONT = "Montserrat"
MONO = "monospace"

config.background_color = WHITE


def T(text, size=30, color=INK, weight=NORMAL, font=FONT, **kw):
    return Text(text, font=font, font_size=size, color=color, weight=weight, **kw)


def M(text, size=24, color=WHITE, **kw):
    return Text(text, font=MONO, font_size=size, color=color, **kw)


# --- icons (drawn with basic shapes, so no files or emoji fonts needed) ------
def toolbox(w=3.0, color=MARINE):
    body = RoundedRectangle(corner_radius=0.12, width=w, height=w * 0.62,
                            fill_color=color, fill_opacity=1, stroke_width=0)
    lid = Line(body.get_left() + UP * w * 0.08, body.get_right() + UP * w * 0.08,
               color=WHITE, stroke_width=4)
    handle = Arc(start_angle=0, angle=PI, radius=w * 0.2, color=color, stroke_width=10)
    handle.next_to(body, UP, buff=-0.02)
    latch = RoundedRectangle(corner_radius=0.05, width=w * 0.16, height=w * 0.14,
                             fill_color=SEA, fill_opacity=1, stroke_width=0)
    latch.move_to(body.get_center() + UP * w * 0.08)
    return VGroup(handle, body, lid, latch)


def hammer(s=1.0, color=GREY):
    head = RoundedRectangle(corner_radius=0.05, width=0.75 * s, height=0.28 * s,
                            fill_color=color, fill_opacity=1, stroke_width=0)
    handle = RoundedRectangle(corner_radius=0.04, width=0.14 * s, height=1.0 * s,
                              fill_color=TANGERINE, fill_opacity=1, stroke_width=0)
    handle.next_to(head, DOWN, buff=-0.05)
    return VGroup(handle, head).rotate(PI / 6)


def wrench(s=1.0, color=MARINE):
    shaft = RoundedRectangle(corner_radius=0.07, width=0.16 * s, height=1.1 * s,
                             fill_color=color, fill_opacity=1, stroke_width=0)
    ring = Annulus(inner_radius=0.1 * s, outer_radius=0.26 * s, color=color,
                   fill_opacity=1, stroke_width=0)
    ring.next_to(shaft, UP, buff=-0.1)
    return VGroup(shaft, ring).rotate(-PI / 6)


def bench(w=3.2, color=MARINE):
    top = RoundedRectangle(corner_radius=0.05, width=w, height=0.22,
                           fill_color=color, fill_opacity=1, stroke_width=0)
    l1 = Rectangle(width=0.18, height=0.9, fill_color=color, fill_opacity=1, stroke_width=0)
    l2 = l1.copy()
    l1.next_to(top, DOWN, buff=0).shift(RIGHT * (-w / 2 + 0.3))
    l2.next_to(top, DOWN, buff=0).shift(RIGHT * (w / 2 - 0.3))
    return VGroup(l1, l2, top)


def folder(w=1.4, fill=LIGHT, stroke=MARINE):
    body = Rectangle(width=w, height=w * 0.7, fill_color=fill, fill_opacity=1,
                     stroke_color=stroke, stroke_width=3)
    tab = Rectangle(width=w * 0.4, height=w * 0.16, fill_color=fill, fill_opacity=1,
                    stroke_color=stroke, stroke_width=3)
    tab.next_to(body, UP, buff=0, aligned_edge=LEFT)
    return VGroup(tab, body)


def file_icon(w=1.0, lines=3, fill=WHITE, stroke=MARINE):
    h = w * 1.3
    body = Rectangle(width=w, height=h, fill_color=fill, fill_opacity=1,
                     stroke_color=stroke, stroke_width=3)
    rows = VGroup(*[Line(LEFT * w * 0.32, RIGHT * w * 0.32, color=stroke, stroke_width=3)
                    for _ in range(lines)]).arrange(DOWN, buff=h * 0.16)
    rows.move_to(body.get_center() + DOWN * 0.05)
    return VGroup(body, rows)


def package(w=1.2, color=TANGERINE):
    box = Square(w, fill_color=color, fill_opacity=1, stroke_color=INK, stroke_width=2)
    ribbon_v = Rectangle(width=w * 0.18, height=w, fill_color=WHITE, fill_opacity=0.9, stroke_width=0)
    ribbon_h = Rectangle(width=w, height=w * 0.18, fill_color=WHITE, fill_opacity=0.9, stroke_width=0)
    return VGroup(box, ribbon_v, ribbon_h)


def bolt(s=1.0, color=YELLOW):
    pts = [(0.15, 0.6), (-0.25, -0.05), (0.0, -0.05), (-0.15, -0.6), (0.3, 0.1), (0.05, 0.1)]
    return Polygon(*[np.array([x * s, y * s, 0]) for x, y in pts], fill_color=color,
                   fill_opacity=1, stroke_color=INK, stroke_width=2)


def tick(s=0.35, color=GREEN):
    c = Circle(radius=s, fill_color=color, fill_opacity=1, stroke_width=0)
    mark = VMobject(color=WHITE, stroke_width=6).set_points_as_corners(
        [LEFT * s * 0.45 + UP * 0.0, LEFT * s * 0.1 + DOWN * s * 0.35, RIGHT * s * 0.5 + UP * s * 0.4])
    return VGroup(c, mark)


def cross(s=0.35, color=RED):
    c = Circle(radius=s, fill_color=color, fill_opacity=1, stroke_width=0)
    a = Line(UL * s * 0.45, DR * s * 0.45, color=WHITE, stroke_width=6)
    b = Line(UR * s * 0.45, DL * s * 0.45, color=WHITE, stroke_width=6)
    return VGroup(c, a, b)


def keycap(label, size=24):
    t = T(label, size, INK, BOLD)
    r = RoundedRectangle(corner_radius=0.12, width=max(t.width + 0.5, 0.8), height=0.7,
                         fill_color=SOFT, stroke_color=GREY, stroke_width=3)
    t.move_to(r)
    return VGroup(r, t)


def keys(*labels, size=24):
    g = VGroup()
    for i, lab in enumerate(labels):
        if i:
            g.add(T("+", size, GREY))
        g.add(keycap(lab, size))
    return g.arrange(RIGHT, buff=0.2)


# --- cards, windows, callouts -----------------------------------------------
def card(title, body=None, w=3.6, h=None, fill=LIGHT, stroke=MARINE, tsize=26, bsize=20):
    t = T(title, tsize, OCEAN, BOLD)
    parts = [t]
    if body:
        parts.append(T(body, bsize, INK, line_spacing=0.9))
    inner = VGroup(*parts).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
    height = h if h else inner.height + 0.5
    w = max(w, inner.width + 0.8)
    rect = RoundedRectangle(corner_radius=0.15, width=w, height=height, fill_color=fill,
                            fill_opacity=1, stroke_color=stroke, stroke_width=3)
    inner.move_to(rect).align_to(rect, LEFT).shift(RIGHT * 0.3)
    return VGroup(rect, inner)


def pill(text, fill=MARINE, color=WHITE, size=22, pad=0.35):
    t = T(text, size, color, BOLD)
    r = RoundedRectangle(corner_radius=0.3, width=t.width + pad * 2, height=t.height + 0.3,
                         fill_color=fill, fill_opacity=1, stroke_width=0)
    t.move_to(r)
    return VGroup(r, t)


def window(lines, w=8.0, title="Terminal", size=24, colors=None, gap=0.2, pad=1.0):
    """Dark terminal / code window. Returns (group, [line mobjects])."""
    mobs, leads = [], []
    cw = M("a" * 20, size).width / 20  # width of one monospace character
    for i, ln in enumerate(lines):
        col = (colors[i] if colors and colors[i] else WHITE)
        leads.append(len(ln) - len(ln.lstrip(' ')))
        if ln:
            mobs.append(M(ln.lstrip(' '), size, col))
        else:  # blank line: an invisible spacer (empty Text collapses and breaks arrange)
            mobs.append(Rectangle(width=0.05, height=size * 0.016, stroke_width=0, fill_opacity=0))
    stack = VGroup(*mobs).arrange(DOWN, aligned_edge=LEFT, buff=gap)
    for m, lead in zip(mobs, leads):  # Text drops leading spaces, so indent by hand
        m.shift(RIGHT * lead * cw)
    h = stack.height + pad
    frame = RoundedRectangle(corner_radius=0.18, width=max(w, stack.width + 0.9), height=h,
                             fill_color=NIGHT, fill_opacity=1, stroke_width=0)
    bar = VGroup(*[Dot(radius=0.07, color=c) for c in (RED, YELLOW, GREEN)]).arrange(RIGHT, buff=0.12)
    bar.move_to(frame.get_top() + DOWN * 0.3 + LEFT * (frame.width / 2 - 0.5))
    ttl = T(title, 16, MIDDLE).move_to(frame.get_top() + DOWN * 0.3)
    stack.move_to(frame.get_center() + DOWN * 0.2).align_to(frame, LEFT).shift(RIGHT * 0.45)
    return VGroup(frame, bar, ttl, stack), mobs


def callout(text, kind="note", w=11.5, size=22):
    spec = {"note": (SEA, "i", ICE), "warning": (TANGERINE, "!", "#FFF1E8"),
            "tip": (GREEN, "✓", "#F0FAE3"), "important": (MARINE, "!", LIGHT)}[kind]
    bar_col, sym, fill = spec
    body = T(text, size, INK, line_spacing=0.9)
    badge = VGroup(Circle(radius=0.26, fill_color=bar_col, fill_opacity=1, stroke_width=0),
                   T(sym, 24, WHITE if kind != "note" else OCEAN, BOLD))
    badge[1].move_to(badge[0])
    inner = VGroup(badge, body).arrange(RIGHT, buff=0.3)
    rect = RoundedRectangle(corner_radius=0.15, width=max(w, inner.width + 0.8),
                            height=inner.height + 0.5, fill_color=fill, fill_opacity=1,
                            stroke_color=bar_col, stroke_width=3)
    inner.move_to(rect)
    return VGroup(rect, inner)


def labelled(mob, text, size=20, color=INK, direction=DOWN, buff=0.2):
    return VGroup(mob, T(text, size, color)).arrange(direction, buff=buff)


# --- base class for every deck ----------------------------------------------
class Deck(Slide):
    """Every `self.next_slide()` is one click of the presentation."""

    section = "Module 4"
    skip_reversing = True  # going back jumps instead of playing in reverse

    def begin(self):
        self.foot = T(f"Computer Programming I  ·  Module 4  ·  {self.section}", 18, GREY)
        self.foot.to_corner(DL, buff=0.3)
        self.add(self.foot)
        self.current_title = None

    def heading(self, text, sub=None):
        """Replace everything on screen (except the footer) with a new title."""
        olds = [m for m in self.mobjects if m is not self.foot]
        t = T(text, 44, OCEAN, BOLD)
        bar = Rectangle(width=0.12, height=t.height + 0.1, fill_color=SEA, fill_opacity=1,
                        stroke_width=0)
        parts = [VGroup(bar, t).arrange(RIGHT, buff=0.25)]
        if sub:
            parts.append(T(sub, 24, GREY))
        g = VGroup(*parts).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        g.to_corner(UL, buff=0.5)
        anims = [FadeOut(*olds)] if olds else []
        self.play(*anims, FadeIn(g, shift=RIGHT * 0.3), run_time=0.7)
        self.current_title = g
        return g

    def wipe(self):
        """Clear the content area, keep the title and footer."""
        keep = (self.foot, self.current_title)
        olds = [m for m in self.mobjects if m not in keep]
        if olds:
            self.play(FadeOut(*olds), run_time=0.4)

    def click(self):
        self.next_slide()

    def type_lines(self, mobs, run_time=0.5, pause_between=False):
        for m in mobs:
            self.play(Write(m), run_time=run_time)
            if pause_between:
                self.click()


def tree_rows(rows, size=22, step=0.55, gap=0.13):
    """rows: list of (indent, name, kind) with kind 'dir' or 'file'.
    Returns a VGroup of rows; each row is VGroup(icon, label)."""
    out = VGroup()
    for indent, name, kind in rows:
        icon = folder(0.42) if kind == "dir" else file_icon(0.26, lines=2)
        label = T(name, size, INK if kind == "file" else OCEAN, NORMAL if kind == "file" else BOLD,
                  font=MONO if kind == "file" else FONT)
        out.add(VGroup(icon, label).arrange(RIGHT, buff=0.2))
    out.arrange(DOWN, aligned_edge=LEFT, buff=gap)
    for row, (indent, _, _) in zip(out, rows):
        row.shift(RIGHT * indent * step)
    return out
