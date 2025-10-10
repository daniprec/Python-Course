#!/usr/bin/env python3
"""
Scan expected output directories for .ipynb files and print per-cell metadata and brief outputs.
This is intended for temporary CI debugging to verify whether Quarto propagated chunk metadata
(for example `error=true`) into the executed notebook cells.
"""

import glob
import json
import os

SEARCH_GLOB = "**/*.ipynb"


def dump_notebook(fn):
    print("---- Notebook:", fn, "----")
    try:
        with open(fn, "r", encoding="utf-8") as fh:
            nb = json.load(fh)
    except Exception as e:
        print(f"Failed to load {fn}: {e}")
        return
    cells = nb.get("cells", [])
    print(f"Cells: {len(cells)}")
    for i, c in enumerate(cells):
        meta = c.get("metadata", {})
        print("--- cell", i, "metadata ---")
        print(json.dumps(meta, indent=2, ensure_ascii=False))
        if "execution" in c:
            print("execution:", c["execution"])
        src = "".join(c.get("source") or [])
        preview = src.strip().splitlines()[:2]
        print("source-preview:", preview)
        outs = c.get("outputs", [])
        if outs:
            print("outputs:", len(outs))
            for o in outs[:3]:
                t = o.get("output_type")
                print(" output_type:", t)


def main():
    found = False
    # search recursively from current working directory for any .ipynb files
    for fn in glob.glob(SEARCH_GLOB, recursive=True):
        if os.path.isfile(fn):
            found = True
            dump_notebook(fn)
    if not found:
        print(
            "No .ipynb files found in expected locations. Listing tree for debugging:"
        )
        for root, dirs, files in os.walk("."):
            for name in files:
                print(os.path.join(root, name))


if __name__ == "__main__":
    main()
