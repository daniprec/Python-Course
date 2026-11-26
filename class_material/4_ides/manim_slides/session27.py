"""Session 27: organise and build (files, directories, text and JSON, your own library)."""

from ie_theme import *  # noqa: F401,F403

TREE = [
    (0, "Home", "dir"),
    (1, "Documents", "dir"),
    (1, "IE", "dir"),
    (2, "ComputerProgramming", "dir"),
    (3, "hello.py", "file"),
    (3, "data.csv", "file"),
    (3, "data", "dir"),
    (4, "weather.json", "file"),
    (1, "Downloads", "dir"),
]


def you_are_here(row):
    """A pin placed to the right of a tree row."""
    p = pill("you are here", fill=TANGERINE, color=INK, size=18)
    p.next_to(row, RIGHT, buff=0.4)
    return p


class S27Files(Deck):
    section = "Session 27"

    def construct(self):
        self.begin()
        self.heading("Files and directories", "The floor plan of your workshop")

        # --- the tree ------------------------------------------------------------
        tree = tree_rows(TREE, size=22).to_edge(LEFT, buff=0.8).shift(DOWN * 0.6)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in tree], lag_ratio=0.25), run_time=2.4)
        self.click(hard=True)
        note = VGroup(
            T("A directory is a drawer", 28, OCEAN, BOLD),
            T("it holds files and other directories", 22, INK),
            T("The top one is the root of the hierarchy", 22, INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 3.2 + UP * 0.3)
        self.play(FadeIn(note, shift=LEFT * 0.3))
        self.play(Indicate(tree[0], color=MARINE))
        self.click(hard=True)

        # --- operating systems -----------------------------------------------------
        self.heading("Paths on each system", "Python needs to know WHERE a file is")
        cards = equalize(VGroup(
            card("Windows", "drive letters: C:\\\nseparator: backslash\nC:\\Users\\maria\\Documents", w=4.0, tsize=26, bsize=18),
            card("macOS", "one root: /\nseparator: slash\n/Users/maria/Documents", w=4.0, tsize=26, bsize=18),
            card("Linux", "one root: /\nseparator: slash\n/home/maria/Documents", w=4.0, tsize=26, bsize=18),
        )).arrange(RIGHT, buff=0.4).shift(UP * 0.2)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.5)
            self.click(hard=True)
        self.play(FadeIn(callout("In Python, a forward slash works everywhere, even on Windows: \"C:/Users/maria\".", "tip", w=12, size=20)
                         .to_edge(DOWN, buff=0.9)))
        self.click(hard=True)

        # --- the working directory -------------------------------------------------
        self.heading("The working directory", "Where Python looks first")
        tree = tree_rows(TREE, size=22).to_edge(LEFT, buff=0.8).shift(DOWN * 0.6)
        self.play(FadeIn(tree))
        self.click(hard=True)
        cwd_row = tree[3]
        pin = you_are_here(cwd_row)
        self.play(FadeIn(pin, shift=LEFT * 0.3), Indicate(cwd_row, color=TANGERINE))
        self.click(hard=True)
        code, ln = window(["import os", "print(os.getcwd())"], w=4.6, size=20, title="Python")
        code.move_to(RIGHT * 4.6 + UP * 1.5)
        self.play(FadeIn(code))
        self.click(hard=True)
        kinds = [
            ("data.csv", "relative: a file in the working directory", 5),
            ("data/weather.json", "relative: a file in the subfolder data", 7),
            ("C:/Users/maria/data.csv", "absolute: the full path from the root", None),
        ]
        info = VGroup()
        for path, what, _ in kinds:
            info.add(VGroup(M(path, 18, MARINE), T(what, 16, INK)).arrange(DOWN, aligned_edge=LEFT, buff=0.08))
        info.arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(RIGHT * 4.6 + DOWN * 0.7)
        for (path, what, idx), item in zip(kinds, info):
            self.play(FadeIn(item, shift=LEFT * 0.2))
            self.click(hard=True)
            if idx is not None:
                self.play(Indicate(tree[idx], color=GREEN, scale_factor=1.05), run_time=0.6)
                self.click(hard=True)
        # the error
        self.play(FadeOut(info), FadeOut(code))
        self.click(hard=True)
        self.play(pin.animate.next_to(tree[1], RIGHT, buff=0.4))
        self.click(hard=True)
        term, tl = window(['open("data.csv")', "FileNotFoundError:", "No such file: 'data.csv'"], w=5.8, size=20,
                          title="Python", colors=[WHITE, "#FF8A9A", "#FF8A9A"])
        term.move_to(RIGHT * 4.4 + UP * 0.9).to_edge(RIGHT, buff=0.4)
        self.play(FadeIn(term[:3]))
        self.click(hard=True)
        self.play(Write(tl[0]), run_time=0.7)
        self.click(hard=True)
        self.play(FadeIn(tl[1]), FadeIn(tl[2]))
        self.click(hard=True)
        self.play(Indicate(tl[1], color=RED))
        self.click(hard=True)
        fix = callout("The file is not where Python\nis looking. Check the working\ndirectory and the spelling.", "important",
                      w=5.0, size=18).move_to(DOWN * 1.5).align_to(term, RIGHT)
        self.play(FadeIn(fix, shift=UP * 0.2))
        self.click(hard=True)

        # --- moving around in the terminal ----------------------------------------
        self.heading("Moving around in the terminal", "The same floor plan, with commands")
        tree = tree_rows(TREE, size=20, gap=0.1).to_edge(LEFT, buff=0.8).shift(UP * 0.0)
        self.play(FadeIn(tree))
        pin = you_are_here(tree[0])
        self.play(FadeIn(pin))
        term, tl = window(["$ pwd", "$ ls", "$ cd IE", "$ cd ComputerProgramming", "$ cd ..", "$ cd ComputerProgramming"],
                          w=4.7, size=18, title="Terminal", gap=0.25)
        term.move_to(RIGHT * 4.6 + UP * 0.1)
        self.play(FadeIn(term[:3]))
        moves = [(0, 0, "pwd: show where you are"), (1, 0, "ls: list what is here"),
                 (2, 2, "cd IE: go into a folder"), (3, 3, "cd name: go deeper"),
                 (4, 2, "cd ..: go to the parent folder"), (5, 3, None)]
        cap = None
        for i, row, text in moves:
            self.play(Write(tl[i]), run_time=0.6)
            self.play(pin.animate.next_to(tree[row], RIGHT, buff=0.4), run_time=0.5)
            if cap:
                self.play(FadeOut(cap), run_time=0.2)
            cap = T(text, 22, MARINE, BOLD).to_edge(DOWN, buff=0.85) if text else None
            if cap:
                self.play(FadeIn(cap), run_time=0.3)
            self.click(hard=True)
        if cap:
            self.play(FadeOut(cap))
        self.play(FadeIn(callout("VS Code opens its terminal in the folder you opened (File > Open Folder).", "tip", w=11.5, size=18)
                         .to_edge(DOWN, buff=0.65)))
        self.click(hard=True)


class S27Data(Deck):
    section = "Session 27"

    def construct(self):
        self.begin()
        self.heading("Reading and writing files", "open() and its modes")

        # --- modes --------------------------------------------------------------
        modes = equalize(VGroup(
            card('"r"  read', "the file must exist", w=3.9, tsize=28, bsize=22),
            card('"w"  write', "creates it, or ERASES it", w=3.9, tsize=26, bsize=20, fill="#FFF1E8", stroke=TANGERINE),
            card('"a"  append', "adds at the end", w=3.9, tsize=26, bsize=20),
        )).arrange(RIGHT, buff=0.4).shift(UP * 0.4)
        for m in modes:
            self.play(FadeIn(m, shift=UP * 0.3), run_time=0.5)
            self.click(hard=True)
        self.play(Indicate(modes[1], color=TANGERINE))
        self.play(FadeIn(callout("Always open files inside a with block: it closes the file for you.", "tip", w=11, size=20)
                         .to_edge(DOWN, buff=0.9)))
        self.click(hard=True)

        # --- write and read ---------------------------------------------------
        self.heading("Write, then read", "notes.txt")
        code, ln = window(['with open("notes.txt", "w") as file:', '    file.write("First line\\n")',
                           '    file.write("Second line\\n")'], w=7.0, size=20, title="write.py", gap=0.15)
        code.move_to(LEFT * 3.2 + UP * 0.8)
        f = file_icon(1.9, lines=0).move_to(RIGHT * 4.3 + UP * 0.9)
        fl = M("notes.txt", 20, INK).next_to(f, DOWN, buff=0.15)
        self.play(FadeIn(code))
        self.play(FadeIn(f), FadeIn(fl))
        self.click(hard=True)
        rows = VGroup()
        for k, txt in enumerate(["First line", "Second line"]):
            row = M(txt, 17, INK).move_to(f.get_center() + UP * (0.3 - 0.4 * k))
            rows.add(row)
        for k in range(2):
            self.play(Indicate(ln[1 + k], color=SEA), FadeIn(rows[k], shift=DOWN * 0.15), run_time=0.7)
            self.click(hard=True)
        code2, ln2 = window(['with open("notes.txt", "r") as file:', "    for line in file:", "        print(line.strip())"],
                            w=7.0, size=20, title="read.py", gap=0.15)
        code2.move_to(LEFT * 3.2 + DOWN * 1.8).scale(0.9)
        self.play(FadeIn(code2))
        out, ol = window(["First line", "Second line"], w=3.6, size=18, title="Output", colors=[MIDDLE, MIDDLE])
        out.move_to(RIGHT * 4.3 + DOWN * 1.8)
        self.play(FadeIn(out[:3]))
        self.play(Indicate(f, color=SEA))
        self.play(FadeIn(ol[0].set_color(WHITE)))
        self.play(FadeIn(ol[1].set_color(WHITE)))
        self.click(hard=True)

        # --- careful with w ------------------------------------------------------
        self.heading("Careful with \"w\"", "It deletes the previous content")
        f = file_icon(1.8, lines=0).move_to(LEFT * 3.5 + DOWN * 0.3)
        rows = VGroup(*[M(t, 20, INK) for t in ["Alice", "Bob", "Carla"]]).arrange(DOWN, buff=0.15).move_to(f)
        fl = M("employees.json", 20, INK).next_to(f, DOWN, buff=0.2)
        self.play(FadeIn(f), FadeIn(fl), LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.3))
        self.click(hard=True)
        op = M('open("employees.json", "w")', 22, WHITE)
        opw, _ = window(['open("employees.json", "w")'], w=6.4, size=22, title="Python")
        opw.move_to(RIGHT * 3.2 + DOWN * 0.2)
        self.play(FadeIn(opw[:3]))
        self.play(Write(_[0]), run_time=1.0)
        self.play(FadeOut(rows, shift=DOWN * 0.3), f[0].animate.set_stroke(RED), run_time=0.8)
        gone = VGroup(cross(0.3), T("Old content: gone", 24, WINE, BOLD)).arrange(RIGHT, buff=0.2).next_to(f, UP, buff=0.4)
        self.play(FadeIn(gone))
        self.click(hard=True)
        self.play(FadeIn(callout("Write the result to a NEW file name, as in the next exercise.", "tip", w=10, size=20)
                         .to_edge(DOWN, buff=0.9)))
        self.click(hard=True)

        # --- json ----------------------------------------------------------------
        self.heading("JSON", "A text format that looks like Python dictionaries")
        d = card("In memory", None, w=4.4, tsize=24)
        d_code = VGroup(M('{"name": "Alice",', 22, INK), M(' "age": 30}', 22, INK)).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        d = VGroup(RoundedRectangle(corner_radius=0.15, width=5.4, height=2.6, fill_color=ICE, stroke_color=MARINE, stroke_width=3),
                   VGroup(T("A Python dict", 24, OCEAN, BOLD), d_code).arrange(DOWN, buff=0.2))
        d[1].move_to(d[0])
        d.move_to(LEFT * 4.0 + UP * 0.9)
        fj = file_icon(1.3, lines=3).move_to(RIGHT * 4.6 + UP * 0.9)
        fjl = M("file.json", 20, INK).next_to(fj, DOWN, buff=0.15)
        self.play(FadeIn(d), FadeIn(fj), FadeIn(fjl))
        dump_arrow = Arrow(d.get_right() + UP * 0.35, fj.get_left() + UP * 0.35, buff=0.2, color=MARINE, stroke_width=6)
        dump_lab = M("json.dump(data, file)", 20, OCEAN).next_to(dump_arrow, UP, buff=0.1)
        self.click(hard=True)
        self.play(GrowArrow(dump_arrow), FadeIn(dump_lab))
        load_arrow = Arrow(fj.get_left() + DOWN * 0.35, d.get_right() + DOWN * 0.35, buff=0.2, color=TANGERINE, stroke_width=6)
        load_lab = M("data = json.load(file)", 20, INK).next_to(load_arrow, DOWN, buff=0.1)
        self.click(hard=True)
        self.play(GrowArrow(load_arrow), FadeIn(load_lab))
        self.click(hard=True)
        table = [("dict", "object { }"), ("list, tuple", "array [ ]"), ("str", "string"),
                 ("int, float", "number"), ("True, False, None", "true, false, null")]
        tbl = VGroup(*[VGroup(M(a, 20, INK), T("→", 20, GREY), M(b, 20, MARINE)).arrange(RIGHT, buff=0.3) for a, b in table])
        tbl.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(DOWN * 1.8)
        self.play(FadeOut(dump_lab), FadeOut(load_lab), FadeOut(dump_arrow), FadeOut(load_arrow))
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in tbl], lag_ratio=0.2))
        self.click(hard=True)

        # --- exercise flow ----------------------------------------------------
        self.heading("Exercise: JSON data manager", "A small pipeline")
        steps = [("employees.json", "file"), ("load", "step"), ("add Carla", "step"), ("dump", "step"),
                 ("employees_updated.json", "file")]
        mobs = VGroup()
        for name, kind in steps:
            if kind == "file":
                mobs.add(VGroup(file_icon(1.0, lines=3), M(name, 17, INK)).arrange(DOWN, buff=0.15))
            else:
                mobs.add(pill(name, fill=MARINE, size=26))
        mobs.arrange(RIGHT, buff=0.55).shift(UP * 0.3)
        arrows = VGroup(*[Arrow(mobs[i].get_right(), mobs[i + 1].get_left(), buff=0.1, color=GREY, stroke_width=4) for i in range(4)])
        self.play(FadeIn(mobs[0]))
        for i in range(4):
            self.play(GrowArrow(arrows[i]), FadeIn(mobs[i + 1], shift=RIGHT * 0.2), run_time=0.6)
            self.click(hard=True)
        self.play(FadeIn(callout("Run it, then open the new file to check that Carla is there.", "tip", w=10, size=20)
                         .to_edge(DOWN, buff=0.9)))
        self.click(hard=True)


class S27Library(Deck):
    section = "Session 27"

    def construct(self):
        self.begin()
        self.heading("Build your own library", "From loose tools to a labelled toolbox")

        # --- running example ---------------------------------------------------
        xs = [1, 2, 3, 4]
        ys = [2.1, 3.9, 6.2, 7.8]
        b1, b0 = np.polyfit(xs, ys, 1)
        ax = Axes(x_range=[0, 5, 1], y_range=[0, 9, 1], x_length=5.6, y_length=3.7, tips=False,
                  axis_config={"color": GREY, "include_numbers": False}).shift(LEFT * 3.4 + DOWN * 0.5)
        dots = VGroup(*[Dot(ax.c2p(x, y), color=MARINE, radius=0.1) for x, y in zip(xs, ys)])
        self.play(Create(ax), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.3))
        line = ax.plot(lambda x: b0 + b1 * x, x_range=[0.3, 4.6], color=TANGERINE, stroke_width=6)
        self.play(Create(line), run_time=1.0)
        eq = T("y = b0 + b1 · x", 28, OCEAN, BOLD).shift(RIGHT * 3.2 + UP * 0.8)
        fn = M("linear_regression(x, y)", 24, INK).next_to(eq, DOWN, buff=0.4)
        self.play(FadeIn(eq, shift=LEFT * 0.2))
        self.play(FadeIn(fn, shift=LEFT * 0.2))
        goal = T("Goal: install this function like numpy,\nand use it from any folder.", 24, INK, line_spacing=0.9).next_to(fn, DOWN, buff=0.5)
        self.click(hard=True)
        self.play(FadeIn(goal))
        self.click(hard=True)

        # --- step 1 & 2: module then package ---------------------------------
        self.heading("Step 1 and 2: a module, then a package", "Two folders with the same name")
        proj = tree_rows([(0, "my_first_library/", "dir"), (1, "my_first_library/", "dir"), (2, "__init__.py", "file"),
                          (2, "regression.py", "file"), (1, "setup.py", "file"), (1, "requirements.txt", "file")],
                         size=22, gap=0.15).move_to(LEFT * 4.2 + UP * 0.2)
        self.play(FadeIn(proj[0]))
        self.play(FadeIn(proj[3], shift=RIGHT * 0.2))
        self.click(hard=True)
        self.play(FadeIn(proj[1]), FadeIn(proj[2], shift=RIGHT * 0.2))
        self.click(hard=True)
        outer = pill("the project", fill=OCEAN, size=20).next_to(proj[0], RIGHT, buff=0.5)
        inner = pill("the package", fill=MARINE, size=20).next_to(proj[1], RIGHT, buff=0.5)
        self.play(FadeIn(outer, shift=LEFT * 0.2))
        self.play(FadeIn(inner, shift=LEFT * 0.2))
        init = callout("__init__.py (can be empty)\ntells Python: this folder\nis a package.", "note", w=5.0, size=20).move_to(RIGHT * 4.3 + UP * 0.4)
        self.play(FadeIn(init, shift=LEFT * 0.2))
        self.click(hard=True)
        imp, _ = window(["from my_first_library.regression import linear_regression"], w=9.4, size=17, title="Python")
        imp.move_to(RIGHT * 0.5 + DOWN * 2.2)
        self.play(FadeIn(imp[:3]))
        self.play(Write(_[0]), run_time=1.4)
        self.click(hard=True)

        # --- step 3: setup.py -----------------------------------------------------
        self.heading("Step 3: the setup file", "The label on the toolbox")
        code, ln = window(["from setuptools import find_packages, setup", "", "setup(", '    name="my_first_library",',
                           '    version="0.1",', "    packages=find_packages(),", '    install_requires=["numpy", "typer"],', ")"],
                          w=9.4, size=20, title="setup.py", gap=0.1)
        code.shift(LEFT * 1.8 + DOWN * 0.1)
        self.play(FadeIn(code[:3]))
        for l in ln:
            self.play(Write(l), run_time=0.25)
        self.click(hard=True)
        labels = [(3, "its name"), (4, "its version"), (5, "which folders to install"), (6, "libraries it needs")]
        for i, text in labels:
            br = SurroundingRectangle(ln[i], color=SEA, buff=0.06, corner_radius=0.05)
            lab = T(text, 20, MARINE, BOLD).next_to(code, RIGHT, buff=0.4).set_y(ln[i].get_y())
            self.play(Create(br), FadeIn(lab, shift=LEFT * 0.2), run_time=0.5)
            self.click(hard=True)
            self.play(FadeOut(br), FadeOut(lab), run_time=0.2)
        self.play(FadeIn(callout("Newer projects use pyproject.toml. The ideas are the same.", "note", w=9, size=20)
                         .to_edge(DOWN, buff=0.9)))
        self.click(hard=True)

        # --- step 4: install ------------------------------------------------------
        self.heading("Step 4: install it", "Put the new tool in your environment")
        pkg = package(1.1).shift(LEFT * 5.0 + UP * 0.3)
        pkl = T("my_first_library", 18, INK).next_to(pkg, DOWN, buff=0.15)
        env = RoundedRectangle(corner_radius=0.2, width=4.4, height=3.0, fill_color=ICE, stroke_color=OCEAN, stroke_width=4).shift(RIGHT * 4.0 + UP * 0.3)
        envl = T("cp_env", 24, OCEAN, BOLD).move_to(env.get_top() + DOWN * 0.4)
        others = VGroup(pill("numpy", fill=MARINE, size=18), pill("typer", fill=MARINE, size=18)).arrange(RIGHT, buff=0.2).move_to(env).shift(DOWN * 0.4)
        self.play(FadeIn(pkg), FadeIn(pkl), FadeIn(env), FadeIn(envl), FadeIn(others))
        term, tl = window(["(cp_env) $ pip install ."], w=7.0, size=22, title="Terminal in the project folder")
        term.move_to(LEFT * 0.4 + DOWN * 2.3)
        self.play(FadeIn(term[:3]))
        self.play(Write(tl[0]), run_time=1.0)
        self.click(hard=True)
        self.play(pkg.animate.move_to(env.get_center() + UP * 0.3 + LEFT * 0.0).scale(0.7), FadeOut(pkl), run_time=1.2)
        newpill = pill("my_first_library", fill=TANGERINE, color=INK, size=18).next_to(others, UP, buff=0.2)
        self.play(ReplacementTransform(pkg, newpill))
        self.play(Flash(newpill, color=GREEN))
        self.click(hard=True)
        self.play(FadeOut(term), FadeOut(env), FadeOut(envl), FadeOut(others), FadeOut(newpill))
        # use from anywhere
        lib = VGroup(toolbox(1.6), T("installed", 20, OCEAN, BOLD)).arrange(DOWN, buff=0.15).move_to(UP * 0.7)
        places = VGroup(*[card(t, None, w=3.2, tsize=22) for t in ["a notebook", "another folder", "any script"]]).arrange(RIGHT, buff=0.5).move_to(DOWN * 1.1)
        self.play(FadeIn(lib))
        arrows = VGroup(*[Arrow(lib.get_bottom(), p.get_top(), buff=0.15, color=MARINE) for p in places])
        self.play(LaggedStart(*[AnimationGroup(FadeIn(p, shift=UP * 0.2), GrowArrow(a)) for p, a in zip(places, arrows)], lag_ratio=0.3))
        self.play(FadeIn(callout("Changed your code? Reinstall with pip install .  or use pip install -e .", "tip", w=11, size=20)
                         .to_edge(DOWN, buff=0.8)))
        self.click(hard=True)

        # --- step 5 & 6: typer and a new module -------------------------------------
        self.heading("Step 5 and 6: options and more modules", "typer turns arguments into command-line options")
        code, ln = window(["import typer", "", 'def main(name: str = "Daniel"):', '    print(f"Name is {name}")', "",
                           'if __name__ == "__main__":', "    typer.run(main)"], w=6.0, size=19, title="demo.py", gap=0.08)
        code.move_to(LEFT * 3.8 + DOWN * 0.2)
        run, rl = window(["$ python demo.py", "Name is Daniel", "$ python demo.py --name Bella", "Name is Bella"], w=6.4, size=19,
                         title="Terminal", colors=[WHITE, MIDDLE, WHITE, MIDDLE], gap=0.18)
        run.shift(RIGHT * 3.6 + UP * 0.3)
        self.play(FadeIn(code))
        self.click(hard=True)
        self.play(FadeIn(run[:3]))
        for i, l in enumerate(rl):
            self.play(Write(l) if i % 2 == 0 else FadeIn(l), run_time=0.7)
            if i == 1:
                self.click(hard=True)
        self.play(Circumscribe(rl[2][-12:], color=SEA))
        self.click(hard=True)
        self.play(FadeOut(code), FadeOut(run))
        tree2 = tree_rows([(0, "my_first_library/", "dir"), (1, "my_first_library/", "dir"), (2, "__init__.py", "file"),
                           (2, "regression.py", "file"), (2, "error.py", "file"), (1, "setup.py", "file")],
                          size=22, gap=0.15).shift(LEFT * 3.6 + DOWN * 0.2)
        self.play(FadeIn(VGroup(*[tree2[i] for i in (0, 1, 2, 3, 5)])))
        self.play(FadeIn(tree2[4], shift=RIGHT * 0.3))
        self.play(Indicate(tree2[4], color=TANGERINE))
        side = VGroup(T("A library usually has several modules", 24, INK),
                      T("error.py: measures how good the fit is", 24, INK)).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 3.4 + UP * 0.3)
        self.play(FadeIn(side, shift=LEFT * 0.2))
        self.play(FadeIn(callout("After adding a module, reinstall: pip install .", "warning", w=8, size=20).to_edge(DOWN, buff=0.9)))
        self.click(hard=True)


class S27Recap(Deck):
    section = "Session 27"

    def construct(self):
        self.begin()
        self.heading("The workshop is yours", "Module 4 in one slide")
        items = [
            ("Session 25", "VS Code, Anaconda, Copilot, one environment per project"),
            ("Session 26", "Libraries with pip and conda, scripts with main()"),
            ("Session 27", "Files, JSON, and your own installable library"),
        ]
        rows = VGroup()
        for s, text in items:
            rows.add(VGroup(pill(s, fill=OCEAN, size=22), T(text, 22, INK)).arrange(RIGHT, buff=0.4))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.45).shift(UP * 0.2 + LEFT * 0.3)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.5)
            self.click(hard=True)
        tb = toolbox(1.4).to_corner(UR, buff=0.6).shift(DOWN * 0.95)
        self.play(DrawBorderThenFill(tb))
        end = callout("Use these tools in every project from now on.\nStuck? Email the error message and your operating system.",
                      "note", w=11, size=20).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(end, shift=UP * 0.2))
        self.click(hard=True)
