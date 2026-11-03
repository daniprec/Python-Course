# Class notebook style guide

The teacher (Daniel, IE University, Computer Programming I for Maths students) projects these notebooks in class and writes code into them live. Each year he copies a **clean** notebook into Google Drive and opens it in Colab. A clean notebook contains only the guide for the class and the exercises: no code written in class, no outputs, no solutions.

References: `src/session_18_masking.py` (source format) and `class_material/3_numpy/session_14_numpy_intro.ipynb` (the reference session).

## Structure

1. First markdown cell: `# Session NN: Title`, then `## <hook>`: a short concrete problem or story, ending with a **bold question** that the session answers.
2. A starter code cell with the data needed for the hook (and imports, except in a session where writing the import is the point).
3. Numbered sections `## 1. ...`, `## 2. ...`, about 5–8 in total, for a 90-minute class. Under each heading: 2–5 terse bullet prompts (questions or tasks, not explanations), each followed by an empty code cell (roughly one empty cell per bullet).
4. Exercises: `### Exercise: Name`, a short statement (hints in one line), then empty cells. Never include solutions.
5. Optionally `## N. Challenge`, then always `## Next session`: one or two lines that pose the next session's question.

## Content rules

- Follow the course notes for that session (`Python-Course/modules/<module>/<topic>.qmd`): same order, same running examples, same exercise names where possible, so the notebook matches the website. Prompts only; the notes hold the explanations.
- Reuse good material from the old written-on notebook (datasets, running examples, questions the teacher asked) but **never** keep code that was written live in class, outputs, or students' names typed in class.
- Given code is limited to: data, imports, and helper functions students are not meant to write (plotting, loaders), each with a one-line docstring.
- Code that is meant to fail (predict the error, debugging) goes in a markdown ```python block, not in a code cell.
- Data must load in Colab: use URLs like `https://raw.githubusercontent.com/daniprec/Python-Course/main/data/...`, never local paths. Check the file exists in the repo.
- English, terse, no emojis. Inside a Markdown table cell, write a pipe as `<code>&#124;</code>`.

## Build

Write the source to `tools/class_notebooks/src/session_NN_topic.py` (percent format, see `py2nb.py`), then:

    python3 tools/class_notebooks/py2nb.py SRC OUT.ipynb --check

It must print `OK`. Every non-empty code cell must run top to bottom.

## Don'ts

- Do not run git commands (the repo index lock causes trouble).
- Do not delete or rename old files; do not edit the .qmd notes or anything outside your assigned output files.
