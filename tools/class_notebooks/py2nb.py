"""Convert a percent-format source file into a clean class notebook.

Source format (one file per session):
    "# %% [markdown]" starts a markdown cell; the following lines are plain
    Markdown (no comment prefix), so "# Title" is a heading.
    "# %%" starts a code cell; the following lines are Python. A "# %%" line
    followed by nothing (or blank lines) is an empty cell to fill in class.

Usage:
    python3 py2nb.py SOURCE.py OUTPUT.ipynb          # build
    python3 py2nb.py SOURCE.py OUTPUT.ipynb --check  # build and run every non-empty code cell
"""
import contextlib, hashlib, io, json, sys, traceback

def parse(text):
    cells, kind, buf = [], None, []
    def flush():
        if kind is not None:
            src = "\n".join(buf).strip("\n")
            cells.append((kind, src))
    for line in text.split("\n"):
        s = line.strip()
        if s == "# %% [markdown]":
            flush(); kind, buf = "markdown", []
        elif s == "# %%":
            flush(); kind, buf = "code", []
        else:
            buf.append(line)
    flush()
    return cells

def lines(s):
    if not s:
        return []
    parts = s.split("\n")
    return [p + "\n" for p in parts[:-1]] + [parts[-1]]

def build(src_path, out_path):
    cells = parse(open(src_path, encoding="utf-8").read())
    nb_cells = []
    for i, (kind, src) in enumerate(cells):
        cid = hashlib.md5(f"{out_path}-{i}".encode()).hexdigest()[:8]
        c = {"cell_type": kind, "id": cid, "metadata": {}, "source": lines(src)}
        if kind == "code":
            c["execution_count"] = None
            c["outputs"] = []
        nb_cells.append(c)
    nb = {
        "cells": nb_cells,
        "metadata": {
            "colab": {"provenance": []},
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return cells

def check(cells):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.show = lambda *a, **k: plt.close("all")
    g, ok = {}, True
    for i, (kind, src) in enumerate(cells):
        if kind != "code" or not src.strip():
            continue
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(src, f"cell{i}", "exec"), g)
        except Exception:
            ok = False
            print(f"cell {i} FAILED:\n{src[:300]}")
            traceback.print_exc(limit=1)
    n_code = sum(1 for k, _ in cells if k == "code")
    n_empty = sum(1 for k, s in cells if k == "code" and not s.strip())
    print(f"{'OK' if ok else 'ERRORS'}: {len(cells)} cells, {n_code} code ({n_empty} empty for class)")
    return ok

if __name__ == "__main__":
    cells = build(sys.argv[1], sys.argv[2])
    if "--check" in sys.argv:
        sys.exit(0 if check(cells) else 1)
