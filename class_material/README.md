# Class Material

This folder contains the slides and notebooks used in class, one per session, named `session_NN_topic`. There is no notebook for session 13.

The notebooks are clean: a guide for the class (prompts and exercises), the starter data, and empty cells to be filled during class. No outputs and no solutions. To start a new year, copy them to Google Drive and open them in Colab.

| Module | Sessions |
|---|---|
| `1_fundamentals` | 1–6 |
| `2_structures` | 7–12 |
| `3_numpy` | 14–23 (`side_project_mnist.pptx` is not a session) |

## Editing or restoring a notebook

The notebooks are generated from text sources in `tools/class_notebooks/src/`. If a notebook in this folder gets written on, rebuild the clean versions from the repository root:

```bash
python tools/class_notebooks/build_all.py
```

To change a notebook, edit its source and rebuild. `tools/class_notebooks/STYLE.md` describes the format and the style of the guides.
