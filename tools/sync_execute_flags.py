#!/usr/bin/env python3
"""
Sync execute=false flags from .qmd code fences into corresponding .quarto_ipynb/.ipynb code cell metadata.

Usage (dry-run):
  python tools/sync_execute_flags.py --dir modules

To apply changes:
  python tools/sync_execute_flags.py --dir modules --apply
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import nbformat
except Exception:
    print(
        "ERROR: Missing Python package 'nbformat'. Install with: python -m pip install --user nbformat",
        file=sys.stderr,
    )
    sys.exit(2)

FENCE_RE = re.compile(r"```(?:\{([^}]*)\})?\s*\n(.*?)\n```", re.DOTALL)


def parse_qmd_execute_flags(path: Path):
    text = path.read_text(encoding="utf-8")
    flags = []
    for m in FENCE_RE.finditer(text):
        header = (m.group(1) or "").strip()
        if not header:
            continue
        parts = header.split()
        lang = parts[0].strip()
        if not lang:
            continue
        execute_false = any(
            p.lower().replace(" ", "") in ("execute=false", "execute:false")
            for p in parts[1:]
        )
        flags.append(bool(execute_false))
    return flags


def sync_file(qmd_path: Path, apply: bool):
    base = qmd_path.with_suffix("")
    nb_paths = [
        base.with_suffix(ext)
        for ext in (".quarto_ipynb", ".ipynb")
        if base.with_suffix(ext).exists()
    ]
    if not nb_paths:
        print(f"[SKIP] No notebook counterpart for {qmd_path.name}")
        return

    flags = parse_qmd_execute_flags(qmd_path)
    if not flags:
        print(f"[OK] No execute=false flags found in {qmd_path}")
        return

    for nb_path in nb_paths:
        nb = nbformat.read(str(nb_path), as_version=nbformat.NO_CONVERT)
        code_cells = [c for c in nb.cells if c.cell_type == "code"]
        if not code_cells:
            print(f"[WARN] No code cells in {nb_path.name}")
            continue

        changed = False
        for i, cell in enumerate(code_cells):
            desired = flags[i] if i < len(flags) else False
            md = cell.get("metadata", {})
            quarto_md = md.get("quarto", {})
            prev = quarto_md.get("execute", None)
            if desired:
                if prev is not False:
                    quarto_md["execute"] = False
                    md["quarto"] = quarto_md
                    cell["metadata"] = md
                    changed = True
            else:
                if "quarto" in md and md["quarto"].get("execute", None) is False:
                    del md["quarto"]["execute"]
                    if not md["quarto"]:
                        md.pop("quarto", None)
                    cell["metadata"] = md
                    changed = True

        if changed:
            if apply:
                nbformat.write(nb, str(nb_path))
                rel = os.path.relpath(str(nb_path), str(Path.cwd()))
                print(f"[APPLY] Updated notebook {rel}")
            else:
                rel = os.path.relpath(str(nb_path), str(Path.cwd()))
                print(f"[DRY] Would update notebook {rel}")
        else:
            print(f"[OK] {nb_path.name} already matches .qmd flags")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dir", default="modules", help="root directory to scan")
    p.add_argument(
        "--apply", action="store_true", help="write changes (default: dry-run)"
    )
    args = p.parse_args()

    root = Path(args.dir)
    if not root.exists():
        print(f"Directory not found: {root}", file=sys.stderr)
        sys.exit(2)

    qmds = sorted(root.rglob("*.qmd"))
    if not qmds:
        print("No .qmd files found.")
        return

    for q in qmds:
        sync_file(q, apply=args.apply)


if __name__ == "__main__":
    main()
