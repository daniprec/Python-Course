# Module 4 slides (IDEs & Tools)

This folder holds the **source** of the slides. The finished decks are one level up, in `class_material/4_ides/`.

Animated, clickable slides for Module 4, built with [Manim](https://www.manim.community/) and
[manim-slides](https://manim-slides.eertmans.be/). Every concept is explained with one idea:
**Python development is a workshop**. The IDE is the toolbox, a library is a tool, `pip` and
`conda` are deliveries, an environment is one bench per project, a notebook is a sketchbook
and a script is a blueprint.

| Deck | Scenes |
|---|---|
| Session 25 | The workshop (IDE) · Installing VS Code · GitHub Copilot · Environments · Recap |
| Session 26 | Libraries, pip and conda · Scripts · Recap |
| Session 27 | Files and directories · Reading and writing files, JSON · Build your own library · Recap |

## Use the slides without installing anything

Open the pre-built files in `class_material/4_ides/` (one level up):

| Deck | Animated (browser) | Static (PDF) |
|---|---|---|
| Session 25 | `session_25_workshop_vscode_environments.html` | `session_25_workshop_vscode_environments.pdf` |
| Session 26 | `session_26_libraries_scripts.html` | `session_26_libraries_scripts.pdf` |
| Session 27 | `session_27_files_library.html` | `session_27_files_library.pdf` |

In the HTML deck press the right arrow (or click) to play the next step, the left arrow to go back and `F` for full screen.
The PDF has one page per slide, showing its final version (all the build-up steps are done), to share or print. The `.html` files are self-contained: download one and open it.

## Rebuild them

You need Python 3.9 or newer, [FFmpeg](https://ffmpeg.org/) and the system libraries Manim needs
(Pango and Cairo; see the [Manim installation guide](https://docs.manim.community/en/stable/installation.html)).

```bash
cd class_material/4_ides/manim_slides
pip install -r requirements.txt     # manim 0.19.0 and manim-slides 5.7.0 (these versions work together)
./build.sh                          # renders everything and writes the decks to class_material/4_ides/ (about 40 minutes at 720p)
```

To check a layout quickly, render one scene at low quality and present it:

```bash
manim render -ql session25.py S25Environments
manim-slides present S25Environments     # opens a window; arrow keys to advance
```

`./build.sh -ql` renders everything at 480p in a few minutes.

## Files

| File | What it is |
|---|---|
| `ie_theme.py` | IE University colours, the helpers (cards, terminal windows, icons, callouts) and the `Deck` base class every scene extends |
| `session25.py`, `session26.py`, `session27.py` | The scenes. Each `self.click()` is one step of the presentation |
| `logos/` | Logos used on the slides: the IE School of Science & Technology logo (`sstech.png`, shown on every slide) and the VS Code, Anaconda, GitHub Copilot and Python logos (copies of the files in `img/`; `python.png` is rendered from `img/python.svg`) |
| `make_pdf.py` | Builds the static PDF with one page per slide (final version) |
| `build.sh` | Renders every scene and exports the HTML and PDF decks to `class_material/4_ides/` |

## Editing

- One slide step = one `self.click()`. Put the animations before it (`self.play(...)`), and the next click reveals the next ones.
- Use the helpers instead of raw shapes: `card`, `window` (terminal / code), `callout`, `pill`, `tree_rows`, `keys`, `toolbox`, `folder`, `file_icon`.
- Colours are the IE palette. Sea Blue (`SEA`) is decoration only, never text.
- The font is Montserrat. If it is not installed, Manim falls back to a default font and the text can be a little wider, so install it for the intended look.
- Going back one step jumps instead of playing in reverse (`skip_reversing = True` in `Deck`). It avoids a rendering step that can hang on some machines.
- The PDF has one page per slide: `make_pdf.py` keeps the last frame of the step before each new heading (or `wipe()`), and the last step of each scene. A slide that builds in four steps is one page.
- Every slide shows the Scitech logo (top right) and a slide number (bottom right). The number only changes when a new slide starts (a new `heading()` or `wipe()`), never between the steps of one slide, and it continues across the scenes of a deck, so render the scenes in order (`build.sh` does).
