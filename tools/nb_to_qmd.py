#!/usr/bin/env python3
"""
Simple notebook (.ipynb) -> Quarto .qmd converter.
- Reads all .ipynb files from a source directory and writes .qmd files to a target directory.
- Preserves markdown and code cells.
- Adds a small YAML front-matter with title and format.
- Optionally wraps markdown cells that start with 'Solution' or 'Exercise' into callouts.

Usage:
    python tools/nb_to_qmd.py <src_dir> <dst_dir>

This script avoids external dependencies and uses the Python stdlib.
"""

import json
import sys
from pathlib import Path


def prettify_title(filename: str) -> str:
    name = Path(filename).stem
    # replace underscores and dashes with spaces, capitalize words
    parts = [p.capitalize() for p in name.replace("-", " ").replace("_", " ").split()]
    return " ".join(parts)


def convert_nb(nb_path: Path, out_path: Path):
    with nb_path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])

    title = prettify_title(nb_path.name)

    lines = []
    lines.append("---")
    lines.append(f'title: "{title}"')
    lines.append("format: html")
    lines.append("---")
    lines.append("")

    for cell in cells:
        ctype = cell.get("cell_type", "")
        source = "".join(cell.get("source", []))

        if ctype == "markdown":
            # simple detection: if source lines start with 'Solution' or 'Exercise', wrap in callout
            stripped = source.lstrip()
            lower = stripped.lower()
            if lower.startswith("solution") or lower.startswith("exercise"):
                lines.append('::: {.callout-tip collapse="true"}')
                lines.append(source)
                lines.append(":::")
            else:
                lines.append(source)
            lines.append("")
        elif ctype == "code":
            # preserve language if metadata has it, else use python
            lang = "python"
            # Some notebooks store code as arrays of lines; ensure fences are correct
            lines.append(f"```{{{lang}}}")
            lines.append(source)
            lines.append("```")
            lines.append("")
        else:
            # skip other cell types but include a comment
            lines.append(f"<!-- skipped cell type: {ctype} -->")
            lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tools/nb_to_qmd.py <src_dir> <dst_dir>")
        sys.exit(1)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    if not src.exists():
        print("Source folder does not exist:", src)
        sys.exit(1)

    n = 0
    for ip in src.glob("*.ipynb"):
        out_file = dst / (ip.stem + ".qmd")
        print("Converting", ip, "->", out_file)
        convert_nb(ip, out_file)
        n += 1
    print("Converted", n, "notebooks")
