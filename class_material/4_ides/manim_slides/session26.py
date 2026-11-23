"""Session 26: stock the tools (libraries, pip and conda, scripts)."""

from ie_theme import *  # noqa: F401,F403


class S26Libraries(Deck):
    section = "Session 26"

    def construct(self):
        self.begin()
        self.heading("Libraries", "Ready-made tools for your workshop")

        # --- what is a library -------------------------------------------------
        tb = toolbox(3.4).shift(LEFT * 4.0 + DOWN * 0.4)
        lab = T("numpy", 30, OCEAN, BOLD, font=MONO).next_to(tb, DOWN, buff=0.3)
        self.play(DrawBorderThenFill(tb), FadeIn(lab), run_time=0.9)
        tools = VGroup(*[pill(t, fill=MARINE, size=22) for t in
                         ["np.array", "np.mean", "np.linalg.solve", "np.random.normal"]]) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 2.0 + DOWN * 0.2)
        arrows = VGroup(*[Arrow(tb.get_right(), t.get_left(), buff=0.2, color=GREY, stroke_width=3,
                                max_tip_length_to_length_ratio=0.12) for t in tools])
        self.play(LaggedStart(*[AnimationGroup(GrowArrow(a), FadeIn(t, shift=LEFT * 0.3))
                                for a, t in zip(arrows, tools)], lag_ratio=0.35))
        say = T("A library is a toolbox of ready-made functions.\nYou do not write (or test) them yourself.", 24, INK,
                line_spacing=0.9).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(say, shift=UP * 0.2))
        self.click()

        # --- two kinds ---------------------------------------------------------
        self.heading("Two kinds of libraries", "Where does the tool come from?")
        left = VGroup(
            T("Standard library", 28, OCEAN, BOLD),
            T("comes with Python", 22, GREY),
            VGroup(VGroup(*[pill(t, fill=MARINE, size=20) for t in ["math", "json"]]).arrange(RIGHT, buff=0.2),
                   VGroup(*[pill(t, fill=MARINE, size=20) for t in ["os", "collections"]]).arrange(RIGHT, buff=0.2))
            .arrange(DOWN, buff=0.2),
        ).arrange(DOWN, buff=0.3)
        lf = RoundedRectangle(corner_radius=0.2, width=6.4, height=3.3, fill_color=ICE,
                              stroke_color=MARINE, stroke_width=3)
        left.move_to(lf)
        lg = VGroup(lf, left).shift(LEFT * 3.5 + DOWN * 0.2)
        right = VGroup(
            T("Third-party library", 28, OCEAN, BOLD),
            T("downloaded and installed by you", 22, GREY),
            VGroup(VGroup(*[pill(t, fill=OCEAN, size=20) for t in ["numpy", "pandas"]]).arrange(RIGHT, buff=0.2),
                   VGroup(*[pill(t, fill=OCEAN, size=20) for t in ["matplotlib", "typer"]]).arrange(RIGHT, buff=0.2))
            .arrange(DOWN, buff=0.2),
        ).arrange(DOWN, buff=0.3)
        rf = RoundedRectangle(corner_radius=0.2, width=6.4, height=3.3, fill_color=SOFT,
                              stroke_color=MARINE, stroke_width=3)
        right.move_to(rf)
        rg = VGroup(rf, right).shift(RIGHT * 3.5 + DOWN * 0.2)
        self.play(FadeIn(lg, shift=UP * 0.3))
        say2 = T("Already in the workshop", 22, MARINE, BOLD).next_to(lg, DOWN, buff=0.3)
        self.play(FadeIn(say2))
        self.click()
        self.play(FadeIn(rg, shift=UP * 0.3))
        say3 = T("Delivered when you order it", 22, MARINE, BOLD).next_to(rg, DOWN, buff=0.3)
        self.play(FadeIn(say3), run_time=0.8)
        self.click()

        # --- importing ---------------------------------------------------------
        self.heading("Taking a tool out of the box", "Three ways to import")
        rows = [
            ("import math", "math.sqrt(9)", "use the library name"),
            ("from math import sqrt", "sqrt(9)", "take one tool out"),
            ("import numpy as np", "np.array([1, 2])", "give it a short alias"),
        ]
        grp = VGroup()
        for imp, use, note in rows:
            a, _ = window([imp], w=5.2, title="", size=20, pad=0.55)
            arrow = Arrow(LEFT * 0.4, RIGHT * 0.4, color=MARINE, stroke_width=5)
            b, _ = window([use], w=4.4, title="", size=20, pad=0.55)
            n = T(note, 20, GREY)
            row = VGroup(a, arrow, b).arrange(RIGHT, buff=0.3)
            grp.add(VGroup(row, n).arrange(DOWN, aligned_edge=LEFT, buff=0.1))
        grp.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(DOWN * 0.05)
        for g in grp:
            self.play(FadeIn(g, shift=UP * 0.2), run_time=0.6)
            self.click()
        self.play(FadeIn(callout("Put all your imports at the top of the file.", "tip", w=8, size=20)
                         .to_edge(DOWN, buff=0.65)))
        self.click()

        # --- the empty drawer --------------------------------------------------
        self.heading("The empty drawer", "A library that is not installed")
        term, ln = window(["import typer",
                           "ModuleNotFoundError: No module named 'typer'"], w=11.5, size=22,
                          title="Python", colors=[WHITE, "#FF8A9A"])
        term.shift(UP * 0.3)
        self.play(FadeIn(term[:3]))
        self.play(Write(ln[0]), run_time=0.7)
        self.play(FadeIn(ln[1]))
        self.play(Indicate(ln[1], color=RED))
        self.click()
        self.play(term.animate.scale(0.8).move_to(UP * 1.2))
        fix = callout("Install it first, in the environment you are working in.", "important", w=11.5).move_to(DOWN * 0.5)
        self.play(FadeIn(fix, shift=UP * 0.2))
        act = callout("The environment name must appear in your terminal prompt: (cp_env) $", "warning", w=11.5, size=20)
        act.next_to(fix, DOWN, buff=0.25)
        self.play(FadeIn(act, shift=UP * 0.2))
        self.click()

        # --- pip and conda -----------------------------------------------------
        self.heading("Ordering a tool: pip and conda", "Two delivery services")
        pip_c = card("pip", "from PyPI\npure Python libraries", w=4.6, tsize=30, bsize=22)
        con_c = card("conda", "from Anaconda channels\ndata science libraries", w=4.6, tsize=30, bsize=22)
        pc = VGroup(pip_c, con_c).arrange(RIGHT, buff=1.0).shift(UP * 0.5)
        self.play(FadeIn(pc, shift=UP * 0.3))
        cmds = VGroup(M("pip install numpy", 22, INK), M("conda install numpy", 22, INK))
        cmds[0].next_to(pip_c, DOWN, buff=0.35)
        cmds[1].next_to(con_c, DOWN, buff=0.35)
        self.play(Write(cmds[0]), Write(cmds[1]), run_time=1.0)
        self.click()
        self.wipe()
        # flow chart: try conda first
        s1 = pill("conda install name", fill=OCEAN, size=24)
        q = Polygon(UP * 0.7, RIGHT * 1.7, DOWN * 0.7, LEFT * 1.7, fill_color=LIGHT, fill_opacity=1,
                    stroke_color=MARINE, stroke_width=3)
        qt = T("found?", 24, INK, BOLD).move_to(q)
        s2 = pill("pip install name", fill=MARINE, size=24)
        s3 = pill("done", fill=GREEN, color=INK, size=24)
        flow = VGroup(s1, VGroup(q, qt), s2).arrange(RIGHT, buff=1.0).shift(UP * 0.8)
        s3.next_to(flow[1], DOWN, buff=1.0)
        a1 = Arrow(s1.get_right(), q.get_left(), buff=0.1, color=GREY)
        a_yes = Arrow(q.get_bottom(), s3.get_top(), buff=0.1, color=GREY)
        a_no = Arrow(q.get_right(), s2.get_left(), buff=0.1, color=GREY)
        yes = T("yes", 22, INK, BOLD).next_to(a_yes, RIGHT, buff=0.1)
        no = T("no", 22, INK, BOLD).next_to(a_no, UP, buff=0.05)
        a3 = Arrow(s2.get_bottom(), s3.get_right(), buff=0.1, color=GREY)
        self.play(FadeIn(s1))
        self.play(GrowArrow(a1), FadeIn(flow[1]))
        self.click()
        self.play(GrowArrow(a_yes), FadeIn(yes), FadeIn(s3))
        self.click()
        self.play(GrowArrow(a_no), FadeIn(no), FadeIn(s2))
        self.play(GrowArrow(a3))
        self.play(FadeIn(callout("Rule for this course: try conda first. If not found, use pip INSIDE the same environment.",
                                 "important", w=12, size=20).to_edge(DOWN, buff=0.7)))
        self.click()

        # --- extras ------------------------------------------------------------
        self.heading("Two things you will meet")
        c1 = callout("error: externally-managed-environment\nYou are installing into the operating system's Python.\nDo not force it: activate a conda environment.",
                     "warning", w=12.2, size=20).shift(UP * 0.6)
        c2 = callout("In a notebook you can write  %pip install numpy  in a cell.\nIn VS Code we prefer the terminal, with the right environment active.",
                     "note", w=12.2, size=20).next_to(c1, DOWN, buff=0.4)
        self.play(FadeIn(c1, shift=UP * 0.2))
        self.click()
        self.play(FadeIn(c2, shift=UP * 0.2))
        self.click()

        # --- your turn ---------------------------------------------------------
        self.heading("Your turn", "Install matplotlib in cp_env")
        term, ln = window(["$ conda activate cp_env", "(cp_env) $ conda install matplotlib",
                           "(cp_env) $ conda list numpy"], w=11, size=22, title="Terminal")
        term.shift(UP * 0.2)
        self.play(FadeIn(term[:3]))
        for l in ln:
            self.play(Write(l), run_time=0.9)
            self.click()
        self.play(FadeIn(callout("Then, in a notebook: import matplotlib.pyplot as plt. No error means it worked.",
                                 "tip", w=12, size=20).to_edge(DOWN, buff=0.8)))
        self.click()


class S26Scripts(Deck):
    section = "Session 26"

    def construct(self):
        self.begin()
        self.heading("Scripts", "From the sketchbook to the blueprint")

        # --- notebook vs script -----------------------------------------------
        nb = card("Notebook  (.ipynb)", None, w=4.6, tsize=26).shift(RIGHT * -0.5 + UP * 1.0)
        sc = card("Script  (.py)", None, w=4.6, tsize=26, fill=OCEAN, stroke=OCEAN).shift(RIGHT * 4.4 + UP * 1.0)
        sc[1][0].set_color(WHITE)
        self.play(FadeIn(nb, shift=RIGHT * 0.3), FadeIn(sc, shift=LEFT * 0.3))
        self.click()
        table = [
            ("Structure", "cells, one by one", "one program, top to bottom"),
            ("Output", "below each cell", "in the terminal"),
            ("Best for", "exploring, learning", "projects and reuse"),
            ("Reusable with import", "difficult", "yes"),
        ]
        for i, (what, a, b) in enumerate(table):
            y = -0.05 - 0.8 * i
            tw = T(what, 20, MARINE, BOLD).move_to([-5.6, y, 0], aligned_edge=LEFT)
            ta = T(a, 22, INK).move_to([nb.get_center()[0], y, 0])
            tb = T(b, 22, INK).move_to([sc.get_center()[0], y, 0])
            rule = Line([-6.6, y - 0.4, 0], [6.8, y - 0.4, 0], color=LIGHT, stroke_width=2)
            self.play(FadeIn(tw), FadeIn(ta, shift=UP * 0.1), FadeIn(tb, shift=UP * 0.1), Create(rule), run_time=0.5)
            self.click()

        # --- anatomy of a script ----------------------------------------------
        self.heading("Anatomy of a script", "Three parts, always in this order")
        code, ln = window(["import numpy as np", "", "", "def greet(name):", '    return f"Hello, {name}!"',
                           "", "", 'name = "BAM"', "print(greet(name))"], w=6.4, size=24, title="hello.py", gap=0.1)
        code.shift(LEFT * 3.4 + DOWN * 0.3)
        self.play(FadeIn(code[:3]))
        labels = [("1  imports", MARINE, ln[0:1]), ("2  functions", OCEAN, ln[3:5]), ("3  main code", GREY, ln[7:9])]
        for name, col, lines in labels:
            self.play(*[Write(l) for l in lines], run_time=0.8)
            br = SurroundingRectangle(VGroup(*lines), color=SEA, buff=0.1, corner_radius=0.08)
            lab = pill(name, fill=col, size=22).next_to(code, RIGHT, buff=0.6).align_to(br, UP)
            self.play(Create(br), FadeIn(lab, shift=LEFT * 0.2), run_time=0.6)
            self.click()
        run, rl = window(["$ python hello.py", "Hello, BAM!"], w=4.4, size=22, title="Terminal", colors=[WHITE, MIDDLE])
        run.scale(0.8).move_to(RIGHT * 5.15 + DOWN * 2.6)
        self.play(FadeIn(run[:3]))
        self.play(Write(rl[0]), run_time=0.8)
        self.play(FadeIn(rl[1]))
        self.click()

        # --- execution order ---------------------------------------------------
        self.heading("Execution order", "Python reads from the first line to the last")
        code, ln = window(['print("1. start")', "", "def say_hello():", '    print("3. inside the function")',
                           "", 'print("2. after the definition")', "say_hello()", 'print("4. end")'],
                          w=8.2, size=22, title="order.py", gap=0.12)
        code.shift(LEFT * 3.0 + UP * 0.15)
        self.play(FadeIn(code))
        out, ol = window(["1. start", "2. after the definition", "3. inside the function", "4. end"], w=5.0, size=20,
                         title="Output", colors=[MIDDLE] * 4)
        out.shift(RIGHT * 4.4 + UP * 0.5)
        self.play(FadeIn(out[:3]))
        ptr = Triangle(fill_color=TANGERINE, fill_opacity=1, stroke_width=0).scale(0.16).rotate(-PI / 2)
        note = T("only defined, not run", 18, TANGERINE, BOLD)
        order = [(0, 0), (2, None), (5, 1), (6, None), (3, 2), (7, 3)]
        for k, (line_idx, out_idx) in enumerate(order):
            tgt = ln[line_idx]
            pos = np.array([code.get_left()[0] - 0.25, tgt.get_y(), 0])
            if k == 0:
                ptr.move_to(pos)
                self.play(FadeIn(ptr), run_time=0.3)
            else:
                self.play(ptr.animate.move_to(pos), run_time=0.4)
            self.play(Indicate(tgt, color=SEA, scale_factor=1.03), run_time=0.4)
            if line_idx == 2:
                note.next_to(tgt, RIGHT, buff=0.5)
                self.play(FadeIn(note), run_time=0.3)
            if line_idx == 6:
                self.play(FadeOut(note), run_time=0.2)
            if out_idx is not None:
                self.play(FadeIn(ol[out_idx].set_color(WHITE)), run_time=0.3)
            self.click()
        self.play(FadeOut(ptr))
        self.play(FadeIn(callout("A function only runs when you call it.", "important", w=8, size=20)
                         .to_edge(DOWN, buff=0.8)))
        self.click()

        # --- main guard --------------------------------------------------------
        self.heading("The main function", "if __name__ == \"__main__\"")
        code, ln = window(["def compute_square(x):", "    return x ** 2", "", "def main():",
                           "    print(compute_square(7))", "", 'if __name__ == "__main__":', "    main()"],
                          w=5.8, size=19, title="script_square.py", gap=0.1)
        code.shift(LEFT * 3.7 + DOWN * 0.2)
        self.play(FadeIn(code))
        self.click()
        run_card = card("Run it", "python script_square.py", w=5.6, tsize=24, bsize=20)
        imp_card = card("Import it", "from script_square import compute_square", w=5.6, tsize=24, bsize=17)
        cards = VGroup(run_card, imp_card).arrange(DOWN, buff=1.25).shift(RIGHT * 3.6 + UP * 0.45)
        name_run = T('__name__ is "__main__"', 22, INK)
        name_imp = T('__name__ is "script_square"', 22, INK)
        res_run = VGroup(tick(0.25), T("main() runs: prints 49", 22, INK, BOLD)).arrange(RIGHT, buff=0.2)
        res_imp = VGroup(cross(0.25, color=GREY), T("main() is skipped", 22, INK, BOLD)).arrange(RIGHT, buff=0.2)
        guard = SurroundingRectangle(VGroup(ln[6], ln[7]), color=SEA, buff=0.1, corner_radius=0.08)
        self.play(Create(guard))
        self.play(FadeIn(run_card, shift=LEFT * 0.3))
        name_run.next_to(run_card, DOWN, buff=0.15)
        res_run.next_to(name_run, DOWN, buff=0.15)
        self.play(FadeIn(name_run), FadeIn(res_run))
        self.click()
        self.play(FadeIn(imp_card, shift=LEFT * 0.3))
        name_imp.next_to(imp_card, DOWN, buff=0.15)
        res_imp.next_to(name_imp, DOWN, buff=0.15)
        self.play(FadeIn(name_imp), FadeIn(res_imp))
        self.click()
        self.play(FadeIn(callout("The same file works as a program AND as a collection of functions.", "tip", w=11.5, size=18)
                         .to_edge(DOWN, buff=0.65)))
        self.click()

        # --- importing from another script ------------------------------------
        self.heading("Reusing your own tools", "Import functions from another script")
        a, al = window(["# script_sum.py", "def sum_fun(a, b):", "    return a + b"], w=5.4, size=21, title="script_sum.py")
        b, bl = window(["# script_calc.py", "from script_sum import sum_fun", "", "def diff_fun(a, b):",
                        "    return a - b", "", "print(sum_fun(10, 4))", "print(diff_fun(10, 4))"],
                       w=6.4, size=18, title="script_calc.py", gap=0.1)
        a.shift(LEFT * 4.3 + UP * 0.2)
        b.shift(RIGHT * 3.0 + DOWN * 0.1)
        self.play(FadeIn(a))
        self.click()
        self.play(FadeIn(b))
        arc = CurvedArrow(a.get_right() + UP * 0.2, bl[1].get_left(), color=TANGERINE, angle=-0.6)
        self.play(Create(arc))
        sf = bl[1][0:4]
        self.play(Flash(bl[1], color=SEA), run_time=0.6)
        self.click()
        notes = VGroup(
            T("Both files in the same folder", 22, INK),
            T("No .py in the import:  from script_sum import ...", 22, INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(notes, shift=UP * 0.2))
        self.click()

        # --- input -------------------------------------------------------------
        self.heading("Asking the user", "input() always returns a string")
        code, ln = window(['text = input("Enter some numbers: ")',
                           "numbers = [float(x) for x in text.split()]", "print(numbers)"],
                          w=10.5, size=22, title="numbers.py")
        code.shift(UP * 0.5)
        self.play(FadeIn(code))
        self.click()
        run, rl = window(["Enter some numbers: 2 4 4 4", "[2.0, 4.0, 4.0, 4.0]"], w=7, size=22, title="Terminal",
                         colors=[WHITE, MIDDLE])
        run.shift(DOWN * 2.2).scale(0.9)
        self.play(FadeIn(run[:3]))
        self.play(Write(rl[0]), run_time=1.0)
        self.play(FadeIn(rl[1]))
        self.click()


class S26Recap(Deck):
    section = "Session 26"

    def construct(self):
        self.begin()
        self.heading("Tools in the box", "Before the next session")
        items = [
            "A library is a toolbox; the standard library comes with Python",
            "pip and conda install the rest, always into the active environment",
            "A script runs top to bottom; main() + the main guard make it reusable",
            "You can import your own functions from another script",
        ]
        rows = VGroup(*[VGroup(tick(0.28), T(i, 24, INK)).arrange(RIGHT, buff=0.3) for i in items])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(UP * 0.15 + LEFT * 0.3)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.5)
            self.click()
        nxt = callout("Next session: organise files and folders, and build your own library.", "note", w=12)
        nxt.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(nxt, shift=UP * 0.2))
        self.click()
