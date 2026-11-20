"""Session 25: set up the workshop (IDE, VS Code, Copilot, environments)."""

from ie_theme import *  # noqa: F401,F403


class S25Workshop(Deck):
    section = "Session 25"

    def construct(self):
        self.begin()

        # --- title card -------------------------------------------------------
        kicker = T("Module 4", 30, MARINE, BOLD)
        main = T("IDEs & Tools", 72, OCEAN, BOLD)
        sub = T("From the sketchbook\nto the workshop", 32, GREY, line_spacing=0.9)
        txt = VGroup(kicker, main, sub).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        txt.to_edge(LEFT, buff=1.0).shift(UP * 0.3)
        tb = toolbox(3.6).shift(RIGHT * 3.6 + DOWN * 0.2)
        h = hammer(1.3).next_to(tb, UL, buff=-0.4).shift(UP * 0.1)
        w = wrench(1.3).next_to(tb, UR, buff=-0.4).shift(UP * 0.1)
        self.play(FadeIn(txt, shift=RIGHT * 0.4), run_time=0.8)
        self.play(DrawBorderThenFill(tb), run_time=1.0)
        self.play(FadeIn(h, shift=UP * 0.4), FadeIn(w, shift=UP * 0.4), run_time=0.6)
        self.click()

        # --- the sketchbook ---------------------------------------------------
        self.heading("So far: the sketchbook", "Notebooks are perfect to explore ideas")
        nb = VGroup(*[RoundedRectangle(corner_radius=0.1, width=3.4, height=0.7,
                                       fill_color=WHITE, stroke_color=MARINE, stroke_width=3)
                      for _ in range(3)]).arrange(DOWN, buff=0.2)
        for i, cell in enumerate(nb):
            cell.add(T(["print('hello')", "x = 2 ** 10", "np.mean(data)"][i], 20, GREY, font=MONO)
                     .move_to(cell))
        nb_lab = T("A notebook: run cell by cell", 22, INK)
        nbg = VGroup(nb, nb_lab).arrange(DOWN, buff=0.3).shift(LEFT * 4.2 + DOWN * 0.8)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in nb], lag_ratio=0.3),
                  FadeIn(nb_lab), run_time=1.2)
        self.click()

        need_t = T("Real projects need more:", 28, OCEAN, BOLD)
        needs = VGroup(*[card(a, b, w=6.6, tsize=22, bsize=18) for a, b in [
            ("Code you can reuse", "functions in one file, used by many"),
            ("Files you read and write", "data, results, settings"),
            ("Libraries you install", "other people's tools"),
            ("Projects that stay separate", "each one with its own tools"),
        ]]).arrange(DOWN, buff=0.15)
        right = VGroup(need_t, needs).arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(RIGHT * 3.0 + DOWN * 0.95)
        self.play(FadeIn(need_t))
        for c in needs:
            self.play(FadeIn(c, shift=LEFT * 0.4), run_time=0.5)
            self.click()

        # --- the workshop -----------------------------------------------------
        self.heading("The workshop: an IDE", "Integrated Development Environment")
        tbox = toolbox(3.6).shift(LEFT * 4.6 + DOWN * 0.5)
        lab = T("VS Code", 28, OCEAN, BOLD).next_to(tbox, DOWN, buff=0.3)
        self.play(DrawBorderThenFill(tbox), FadeIn(lab), run_time=0.9)
        drawers = [
            ("Editor", "where you write your code", hammer(0.8)),
            ("Terminal", "where you give commands: python, pip, conda", wrench(0.8)),
            ("Files panel", "the shelves: your folders and scripts", folder(0.9)),
            ("Extensions", "attachments: Python, Jupyter, Copilot", package(0.7)),
        ]
        cards = VGroup()
        for name, desc, icon in drawers:
            c = card(name, desc, w=7.2, tsize=24, bsize=20)
            row = VGroup(icon, c).arrange(RIGHT, buff=0.35)
            cards.add(row)
        cards.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(RIGHT * 2.9 + DOWN * 0.45)
        for row in cards:
            self.play(FadeIn(row, shift=LEFT * 0.8),
                      Indicate(tbox, scale_factor=1.04, color=MARINE), run_time=0.7)
            self.click()
        new_lab = T("VS Code: everything in one place", 28, OCEAN, BOLD).next_to(tbox, DOWN, buff=0.3)
        self.play(Transform(lab, new_lab), Indicate(tbox, scale_factor=1.08, color=MARINE))
        self.click()

        # --- map of the module ------------------------------------------------
        self.heading("Our plan for Module 4", "Three sessions, each one builds on the previous")
        stations = [
            ("Session 25", "Set up the workshop", ["VS Code", "Copilot", "Environments"]),
            ("Session 26", "Stock the tools", ["Libraries", "Scripts"]),
            ("Session 27", "Organise and build", ["Files", "Your own library"]),
        ]
        cols = VGroup()
        for s, name, items in stations:
            head = VGroup(T(s, 22, MARINE, BOLD), T(name, 22, OCEAN, BOLD)).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            pills = VGroup(*[pill(i, fill=OCEAN, size=20) for i in items]).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            body = VGroup(head, pills).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            frame = RoundedRectangle(corner_radius=0.2, width=4.2, height=4.0, fill_color=ICE,
                                     stroke_color=MARINE, stroke_width=3)
            body.move_to(frame).align_to(frame, LEFT).shift(RIGHT * 0.3)
            cols.add(VGroup(frame, body))
        cols.arrange(RIGHT, buff=0.7).shift(DOWN * 0.5)
        for i, c in enumerate(cols):
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.6)
            if i:
                arr = Arrow(cols[i - 1].get_right(), c.get_left(), buff=0.08, color=MARINE, stroke_width=6)
                self.play(GrowArrow(arr), run_time=0.3)
            self.click()

        # --- how to work ------------------------------------------------------
        self.heading("How to work in this module")
        rules = VGroup(
            card("Practise in VS Code", "do your exercises there, not in Colab", w=11.5, tsize=26, bsize=22),
            card("One environment per project", "start from a fresh one every time", w=11.5, tsize=26, bsize=22),
            card("Stuck? Ask.", "email dprecioso@faculty.ie.edu\nwith the error message and your operating system", w=11.5, tsize=26, bsize=22),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 0.4)
        for r in rules:
            self.play(FadeIn(r, shift=UP * 0.3), run_time=0.5)
            self.click()


class S25VSCode(Deck):
    section = "Session 25"

    def construct(self):
        self.begin()
        self.heading("Installing VS Code", "Setting up the workbench")

        # --- 1. editor without python -----------------------------------------
        b = bench(4.0).shift(LEFT * 3.5 + DOWN * 0.8)
        editor = card("VS Code", "the editor", w=3.2, tsize=26).next_to(b, UP, buff=0.1)
        self.play(FadeIn(b), FadeIn(editor, shift=DOWN * 0.3), run_time=0.8)
        miss = VGroup(cross(0.3), T("Python is NOT included", 26, WINE, BOLD)).arrange(RIGHT, buff=0.25)
        miss.shift(RIGHT * 3.4 + UP * 0.2)
        self.play(FadeIn(miss, shift=LEFT * 0.3))
        why = T("VS Code needs a Python interpreter\nto run your code", 24, INK, line_spacing=0.9)
        why.next_to(miss, DOWN, buff=0.4)
        self.play(FadeIn(why))
        self.click()

        # --- 2. three steps ---------------------------------------------------
        self.wipe()
        b = bench(4.2).shift(RIGHT * 3.5 + DOWN * 1.5)
        steps = VGroup(
            card("1  VS Code", "the workbench", w=6.0, tsize=26),
            card("2  Anaconda", "the power supply: Python + conda", w=6.0, tsize=26),
            card("3  Extensions", "the attachments: Python, Jupyter", w=6.0, tsize=26),
        ).arrange(DOWN, buff=0.35).to_edge(LEFT, buff=0.7).shift(DOWN * 0.5)
        self.play(FadeIn(steps[0], shift=RIGHT * 0.3), FadeIn(b))
        self.click()
        power = VGroup(RoundedRectangle(corner_radius=0.1, width=1.9, height=1.2, fill_color=OCEAN,
                                        fill_opacity=1, stroke_width=0),
                       T("Anaconda", 20, WHITE, BOLD)).shift(RIGHT * 5.6 + UP * 0.9)
        power[1].move_to(power[0])
        bl = bolt(0.8).next_to(power, UP, buff=0.1)
        cable = CubicBezier(power.get_bottom(), power.get_bottom() + DOWN * 1.0,
                            b.get_top() + UP * 1.0 + RIGHT * 1.5, b.get_top() + RIGHT * 1.5,
                            color=GREY, stroke_width=6)
        self.play(FadeIn(steps[1], shift=RIGHT * 0.3), FadeIn(power), FadeIn(bl))
        self.play(Create(cable), run_time=0.9)
        self.play(Flash(b.get_top() + RIGHT * 1.5, color=YELLOW, flash_radius=0.4))
        self.click()
        att = VGroup(pill("Python", fill=MARINE, size=18), pill("Jupyter", fill=MARINE, size=18)) \
            .arrange(RIGHT, buff=0.2).next_to(b, UP, buff=0.05).shift(LEFT * 0.5)
        self.play(FadeIn(steps[2], shift=RIGHT * 0.3))
        self.play(LaggedStart(*[FadeIn(a, shift=DOWN * 0.4) for a in att], lag_ratio=0.4))
        self.click()

        # --- 3. check the installation ----------------------------------------
        self.heading("Is the power on?", "Check the installation from a terminal")
        term_g, ln = window(["(base) $ conda --version", "conda x.y.z"], w=8,
                            title="Anaconda Prompt / Terminal", colors=[WHITE, MIDDLE])
        term_g.move_to(UP * 0.3)
        self.play(FadeIn(term_g[:3]))
        self.play(Write(ln[0]), run_time=1.0)
        self.play(FadeIn(ln[1]))
        self.play(Circumscribe(ln[0][:6], color=SEA))
        self.click()
        notes = VGroup(
            callout("Windows: open the Anaconda Prompt. It starts with (base).", "tip", w=11.5, size=20),
            callout("Leave “Add Anaconda3 to my PATH” unticked; tick “Register as default Python”.", "warning", w=11.5, size=20),
            callout("macOS / Linux: if conda is not found, close and reopen the terminal.", "note", w=11.5, size=20),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.7)
        self.play(term_g.animate.scale(0.75).move_to(UP * 1.0))
        for n in notes:
            self.play(FadeIn(n, shift=UP * 0.2), run_time=0.5)
        self.click()

        # --- 4. pick the interpreter ------------------------------------------
        self.heading("Tell VS Code which Python to use", "The command palette")
        k = keys("Ctrl", "Shift", "P").shift(UP * 0.8 + LEFT * 3.5)
        mac = T("(Cmd + Shift + P on macOS)", 20, GREY).next_to(k, DOWN, buff=0.2)
        self.play(FadeIn(k, shift=DOWN * 0.2), FadeIn(mac))
        pal = RoundedRectangle(corner_radius=0.12, width=7.2, height=3.3, fill_color=NIGHT,
                               fill_opacity=1, stroke_width=0).shift(RIGHT * 3.0 + UP * 0.1)
        search = M("> Python: Select Interpreter", 22, WHITE).move_to(pal.get_top() + DOWN * 0.5).align_to(pal, LEFT).shift(RIGHT * 0.4)
        self.play(FadeIn(pal))
        self.play(Write(search), run_time=1.0)
        opts = VGroup(
            M("Python 3.12  (base)  conda", 20, WHITE),
            M("Python 3.12  (demo_env)  conda", 20, WHITE),
            M("/usr/bin/python3  system", 20, MIDDLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(search, DOWN, buff=0.45).align_to(search, LEFT)
        self.play(FadeIn(opts, shift=UP * 0.2))
        sel = SurroundingRectangle(opts[0], color=SEA, buff=0.12, corner_radius=0.08)
        self.play(Create(sel))
        self.click()
        info = VGroup(
            T("Pick the one with  base  or  conda  in its name", 24, INK),
            T("For notebooks: top right  →  Select Kernel", 24, INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(info, shift=UP * 0.2))
        self.click()

        # --- 5. troubleshooting -----------------------------------------------
        self.heading("When something goes wrong")
        rows = VGroup(
            VGroup(T("conda or python not recognised", 24, WINE, BOLD), T("→  Windows: Anaconda Prompt.  macOS/Linux: reopen the terminal", 22, INK)),
            VGroup(T("VS Code asks for an interpreter", 24, WINE, BOLD), T("→  Ctrl+Shift+P  →  Python: Select Interpreter", 22, INK)),
            VGroup(T("Cells will not run", 24, WINE, BOLD), T("→  Trust the folder (Restricted Mode)", 22, INK)),
        )
        cards = VGroup()
        for r in rows:
            r.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            fr = RoundedRectangle(corner_radius=0.15, width=11.5, height=r.height + 0.5, fill_color=SOFT,
                                  stroke_color=MIDDLE, stroke_width=2)
            r.move_to(fr).align_to(fr, LEFT).shift(RIGHT * 0.4)
            cards.add(VGroup(fr, r))
        cards.arrange(DOWN, buff=0.3).shift(DOWN * 0.4)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.5)
            self.click()


class S25Copilot(Deck):
    section = "Session 25"

    def construct(self):
        self.begin()
        self.heading("GitHub Copilot", "An apprentice in your workshop")

        # --- learn, don't skip -------------------------------------------------
        left_t = VGroup(tick(0.3), T("Use it to learn", 28, OCEAN, BOLD)).arrange(RIGHT, buff=0.25)
        right_t = VGroup(cross(0.3), T("Do not use it to skip", 28, WINE, BOLD)).arrange(RIGHT, buff=0.25)
        good = VGroup(*[T(s, 22, INK) for s in [
            "Explain this error message", "Give me a hint, after I tried", "Check my idea"]]) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        bad = VGroup(*[T(s, 22, INK) for s in [
            "Write the whole solution", "Code I cannot explain", "Answers I never run"]]) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        gcol = VGroup(left_t, good).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(LEFT * 3.4 + DOWN * 0.3)
        bcol = VGroup(right_t, bad).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(RIGHT * 3.4 + DOWN * 0.3)
        self.play(FadeIn(left_t), LaggedStart(*[FadeIn(x, shift=RIGHT * 0.3) for x in good], lag_ratio=0.3))
        self.click()
        self.play(FadeIn(right_t), LaggedStart(*[FadeIn(x, shift=RIGHT * 0.3) for x in bad], lag_ratio=0.3))
        self.click()
        self.play(FadeIn(callout("What matters is that YOU can explain and modify your code.", "important", w=11)
                         .to_edge(DOWN, buff=1.0)))
        self.click()

        # --- which route -------------------------------------------------------
        self.heading("Which route gives me Copilot?", "Two names that are easy to confuse")
        edu = card("GitHub Education", "student benefits", w=5.6, tsize=26)
        cls = card("GitHub Classroom", "a tool for teachers", w=5.6, tsize=26)
        grp = VGroup(edu, cls).arrange(RIGHT, buff=0.8).shift(UP * 0.1)
        yes = VGroup(tick(0.3), T("Yes: activates Copilot Student", 22, INK)).arrange(RIGHT, buff=0.2).next_to(edu, DOWN, buff=0.4)
        no = VGroup(cross(0.3), T("No: even if a teacher shares a link", 22, INK)).arrange(RIGHT, buff=0.2).next_to(cls, DOWN, buff=0.4)
        self.play(FadeIn(edu, shift=UP * 0.2), FadeIn(cls, shift=UP * 0.2))
        self.click()
        self.play(FadeIn(yes, shift=UP * 0.2))
        self.play(FadeIn(no, shift=UP * 0.2))
        self.click()

        # --- five steps --------------------------------------------------------
        self.heading("Five steps", "About 15 minutes, plus the wait for GitHub")
        names = ["Create a\nGitHub account", "Verify your\nuniversity email", "Apply to\nGitHub Education",
                 "Wait for the\ndecision", "Activate\nCopilot Student"]
        dots, labels = VGroup(), VGroup()
        for i, n in enumerate(names):
            d = VGroup(Circle(radius=0.38, fill_color=WHITE, stroke_color=MARINE, stroke_width=4),
                       T(str(i + 1), 26, OCEAN, BOLD))
            d[1].move_to(d[0])
            dots.add(d)
            labels.add(T(n, 19, INK, line_spacing=0.9))
        dots.arrange(RIGHT, buff=1.85).shift(UP * 0.9)
        for d, l in zip(dots, labels):
            l.next_to(d, DOWN, buff=0.35)
        line = Line(dots[0].get_center(), dots[-1].get_center(), color=LIGHT, stroke_width=6).set_z_index(-1)
        self.add(line)
        self.play(FadeIn(dots), FadeIn(labels))
        runner = Dot(radius=0.12, color=TANGERINE).move_to(dots[0])
        self.add(runner)
        for i, d in enumerate(dots):
            self.play(runner.animate.move_to(d), d[0].animate.set_fill(LIGHT), run_time=0.5)
            self.click()
        notes = VGroup(
            callout("Approval: minutes for many, several days for some. Do not reapply while one is pending.", "note", w=12, size=18),
            callout("Only upload what GitHub asks for. Never share passwords or codes. Never buy a paid plan.", "warning", w=12, size=18),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(notes, shift=UP * 0.2))
        self.click()

        # --- use it in VS Code -------------------------------------------------
        self.heading("Using it in VS Code", "Open the chat, ask for hints, stay in control")
        k = keys("Ctrl", "Alt", "I").shift(LEFT * 4.0 + UP * 1.1)
        self.play(FadeIn(k, shift=DOWN * 0.2))
        mac = T("Ctrl + Cmd + I on macOS", 20, GREY).next_to(k, DOWN, buff=0.2)
        self.play(FadeIn(mac))
        chat, ln = window(["You:", "Explain this error and give me a hint,", "not the full solution."],
                          w=7, title="Copilot Chat", size=22, colors=[SEA, WHITE, WHITE])
        chat.shift(RIGHT * 2.7 + UP * 0.9)
        self.play(FadeIn(chat[:3]))
        self.type_lines(ln, run_time=0.7)
        self.click()
        habits = VGroup(*[T(s, 22, INK) for s in [
            "1  Try it yourself first, then ask for a hint",
            "2  Ask it to explain code, not only to write it",
            "3  Read and run what it proposes: you are responsible",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(LEFT * 0.8 + DOWN * 1.2)
        self.play(LaggedStart(*[FadeIn(h, shift=RIGHT * 0.3) for h in habits], lag_ratio=0.4))
        self.click()
        off = callout("In class we may switch it off: click Copilot in the status bar (bottom right).", "warning", w=12, size=20)
        off.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(off, shift=UP * 0.2))
        self.click()


class S25Environments(Deck):
    section = "Session 25"

    def construct(self):
        self.begin()
        self.heading("Environments", "One bench for each project")

        # --- the problem: one shared toolbox -----------------------------------
        shared = VGroup(toolbox(2.6), T("NumPy 1.26", 22, OCEAN, BOLD)).arrange(DOWN, buff=0.25)
        shared.shift(DOWN * 0.3)
        pa = card("Project A", "needs NumPy 1.26", w=3.6, tsize=24).shift(LEFT * 4.6 + DOWN * 0.3)
        pb = card("Project B", "needs NumPy 2.x", w=3.6, tsize=24).shift(RIGHT * 4.6 + DOWN * 0.3)
        a1 = Arrow(pa.get_right(), shared.get_left(), buff=0.15, color=MARINE)
        b1 = Arrow(pb.get_left(), shared.get_right(), buff=0.15, color=MARINE)
        self.play(FadeIn(shared), FadeIn(pa), FadeIn(pb), GrowArrow(a1), GrowArrow(b1))
        ok = tick(0.3).next_to(pa, DOWN, buff=0.3)
        self.play(FadeIn(ok))
        self.click()
        new_lab = T("NumPy 2.x", 22, OCEAN, BOLD).move_to(shared[1])
        self.play(Transform(shared[1], new_lab), Indicate(shared[0], color=TANGERINE))
        bad = VGroup(cross(0.3), T("Project A breaks", 22, WINE, BOLD)).arrange(RIGHT, buff=0.2).next_to(pa, DOWN, buff=0.3)
        self.play(ReplacementTransform(ok, bad[0]), FadeIn(bad[1]), pa[0].animate.set_fill("#FDE7EA"))
        self.click()

        # --- the solution: separate environments -------------------------------
        self.wipe()
        envs = VGroup()
        for name, lib, col in [("base", "default", GREY), ("demo_env", "NumPy 1.26", MARINE), ("cp_env", "NumPy 2", OCEAN)]:
            fr = RoundedRectangle(corner_radius=0.2, width=3.7, height=3.2, fill_color=ICE,
                                  stroke_color=col, stroke_width=4)
            nm = T(name, 26, col, BOLD)
            items = VGroup(pill("Python", fill=col, size=18), pill(lib, fill=col, size=18)).arrange(DOWN, buff=0.15)
            content = VGroup(nm, items).arrange(DOWN, buff=0.35).move_to(fr)
            envs.add(VGroup(fr, content))
        envs.arrange(RIGHT, buff=0.5).shift(DOWN * 0.1)
        lab = T("Each environment has its own Python and its own libraries", 24, INK).to_edge(DOWN, buff=1.0)
        for e in envs:
            self.play(FadeIn(e, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(lab))
        self.click()
        self.play(FadeOut(lab))
        why = VGroup(
            card("Isolate", "no conflicts", w=3.8, tsize=24, bsize=19),
            card("Reproduce", "same results for all", w=3.8, tsize=24, bsize=19),
            card("Dispose", "broken? start again", w=3.8, tsize=24, bsize=19),
        ).arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.8)
        self.play(envs.animate.scale(0.75).shift(UP * 0.6))
        self.play(LaggedStart(*[FadeIn(w, shift=UP * 0.3) for w in why], lag_ratio=0.3))
        self.click()

        # --- create ------------------------------------------------------------
        self.heading("Create", "conda create -n  gives it a name")
        term, ln = window(["(base) $ conda create -n demo_env python=3.12", "...",
                           "Proceed ([y]/n)? y", "done"], w=11, title="Anaconda Prompt / Terminal",
                          colors=[WHITE, MIDDLE, WHITE, MIDDLE])
        term.shift(DOWN * 0.2)
        self.play(FadeIn(term[:3]))
        self.play(Write(ln[0]), run_time=1.4)
        self.play(FadeIn(ln[1]))
        self.click()
        self.play(Write(ln[2]), run_time=0.6)
        self.play(FadeIn(ln[3]))
        self.play(Circumscribe(ln[0][21:29], color=SEA))
        self.click()
        self.play(FadeIn(callout("First time? conda may ask you to accept the Terms of Service: type a.", "note", w=11.5, size=20)
                         .to_edge(DOWN, buff=0.8)))
        self.click()

        # --- activate ----------------------------------------------------------
        self.heading("Activate", "Walk over to the bench")
        term, ln = window(["(base) $ conda activate demo_env", "(demo_env) $ conda deactivate", "(base) $"], w=11,
                          title="Anaconda Prompt / Terminal", colors=[WHITE, WHITE, WHITE])
        term.shift(DOWN * 0.1)
        self.play(FadeIn(term[:3]))
        self.play(Write(ln[0]), run_time=1.2)
        self.play(FadeIn(ln[1][:11]))
        box = SurroundingRectangle(ln[1][:10], color=SEA, buff=0.07, corner_radius=0.06)
        self.play(Create(box))
        self.click()
        self.play(FadeOut(box), Write(ln[1][11:]), run_time=1.0)
        self.play(FadeIn(ln[2]))
        self.click()
        self.play(FadeIn(callout("The name in brackets tells you which environment is active.", "important", w=11)
                         .to_edge(DOWN, buff=0.8)))
        self.click()

        # --- install -----------------------------------------------------------
        self.heading("Install inside it", "Only the active environment receives the library")
        term, ln = window(["(demo_env) $ conda install numpy ipykernel",
                           "(demo_env) $ pip install typer   # only if conda cannot find it",
                           "(demo_env) $ conda list"], w=12, size=22, title="Anaconda Prompt / Terminal")
        term.shift(UP * 0.2)
        self.play(FadeIn(term[:3]))
        for l in ln:
            self.play(Write(l), run_time=1.0)
            self.click()
        self.play(FadeIn(callout("ModuleNotFoundError for a library you installed? Check the active environment.", "warning", w=12, size=20)
                         .to_edge(DOWN, buff=0.8)))
        self.click()

        # --- use in VS Code ----------------------------------------------------
        self.heading("Use it in VS Code", "Choose the bench in the bottom-right corner")
        vs = RoundedRectangle(corner_radius=0.15, width=10.5, height=3.3, fill_color=NIGHT,
                              fill_opacity=1, stroke_width=0).shift(UP * 0.55)
        code = VGroup(M("import numpy as np", 22, WHITE), M("print(np.__version__)", 22, WHITE)) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(vs).shift(UP * 0.3 + LEFT * 2.5)
        status = Rectangle(width=10.5, height=0.55, fill_color=MARINE, fill_opacity=1, stroke_width=0)
        status.move_to(vs.get_bottom() + UP * 0.275)
        interp = T("Python 3.12 (base)", 18, WHITE, BOLD).move_to(status).align_to(status, RIGHT).shift(LEFT * 0.4)
        self.play(FadeIn(vs), FadeIn(code), FadeIn(status), FadeIn(interp))
        self.play(Circumscribe(interp, color=TANGERINE))
        self.click()
        new = T("Python 3.12 (demo_env)", 18, WHITE, BOLD).move_to(status).align_to(status, RIGHT).shift(LEFT * 0.4)
        self.play(FadeOut(interp), FadeIn(new))
        self.play(Flash(new, color=GREEN))
        self.click()
        steps = VGroup(
            T("Script: click the interpreter and choose your environment", 22, INK),
            T("Notebook: Select Kernel  →  Python Environments  →  your environment", 22, INK),
            T("Notebooks need ipykernel in that environment", 22, INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(steps, shift=UP * 0.2))
        self.click()

        # --- share -------------------------------------------------------------
        self.heading("Share your bench", "requirements.txt lists the tools")
        me = VGroup(RoundedRectangle(corner_radius=0.15, width=3.8, height=2.6, fill_color=ICE,
                                     stroke_color=MARINE, stroke_width=3), T("Your computer", 22, OCEAN, BOLD)).shift(LEFT * 4.2)
        me[1].move_to(me[0].get_top() + DOWN * 0.4)
        fr = VGroup(RoundedRectangle(corner_radius=0.15, width=3.8, height=2.6, fill_color=ICE,
                                     stroke_color=MARINE, stroke_width=3), T("A classmate", 22, OCEAN, BOLD)).shift(RIGHT * 4.2)
        fr[1].move_to(fr[0].get_top() + DOWN * 0.4)
        for g in (me, fr):
            g.shift(UP * 0.2)
        self.play(FadeIn(me), FadeIn(fr))
        c1 = M("pip freeze > requirements.txt", 20, INK).next_to(me, DOWN, buff=0.4)
        self.play(Write(c1), run_time=1.0)
        f = file_icon(0.7).move_to(me[0]).shift(DOWN * 0.3)
        lab = M("requirements.txt", 16, INK).next_to(f, DOWN, buff=0.1)
        self.play(FadeIn(f), FadeIn(lab))
        self.click()
        self.play(f.animate.move_to(fr[0].get_center() + DOWN * 0.3), lab.animate.next_to(fr[0].get_center() + DOWN * 0.3 + DOWN * 0.6, ORIGIN),
                  run_time=1.2)
        c2 = M("pip install -r requirements.txt", 20, INK).next_to(fr, DOWN, buff=0.4).shift(LEFT * 0.7)
        self.play(Write(c2), run_time=1.0)
        self.click()


class S25Recap(Deck):
    section = "Session 25"

    def construct(self):
        self.begin()
        self.heading("Your workshop is ready", "Before the next session")
        items = [
            "VS Code installed, with the Python and Jupyter extensions",
            "Anaconda installed: conda --version works",
            "Copilot requested (optional, and follow each activity's AI rules)",
            "A fresh environment, cp_env, selected in VS Code",
        ]
        rows = VGroup()
        for i in items:
            rows.add(VGroup(tick(0.28), T(i, 24, INK)).arrange(RIGHT, buff=0.3))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(UP * 0.15 + LEFT * 0.3)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.5)
            self.click()
        nxt = callout("Next session: stock the toolbox with libraries, and write your first scripts.", "note", w=12)
        nxt.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(nxt, shift=UP * 0.2))
        self.click()
