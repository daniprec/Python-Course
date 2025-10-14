#!/usr/bin/env python3
"""Fix href paths in _quarto.yml by searching for matching files in the repo.

This script loads `_quarto.yml`, finds all `href:` values, and if a target file
doesn't exist, searches the workspace for a filename with the same basename
ignoring underscores/hyphens and case. It updates the href to the found path.

Run as a dry-run first with --apply to write changes.
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except Exception:
    print(
        "ERROR: Missing Python package 'PyYAML'. Install with: python -m pip install --user pyyaml",
        file=sys.stderr,
    )
    sys.exit(2)


def normalize(s: str) -> str:
    return re.sub(r"[-_\s]+", "", s).lower()


def find_candidate(root: Path, href: str):
    target = Path(href)
    if target.exists():
        return None
    basename = target.name
    norm = normalize(basename)
    for p in root.rglob("*"):
        if p.is_file():
            if normalize(p.name) == norm:
                return str(p.as_posix())
    return None


def walk_and_fix(node, root: Path, changes: dict):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "href" and isinstance(v, str):
                cand = find_candidate(root, v)
                if cand:
                    changes[v] = cand
                    node[k] = cand
            else:
                walk_and_fix(v, root, changes)
    elif isinstance(node, list):
        for item in node:
            walk_and_fix(item, root, changes)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true", help="Write changes to _quarto.yml")
    args = p.parse_args()

    repo = Path(".").resolve()
    cfg = repo / "_quarto.yml"
    if not cfg.exists():
        print("_quarto.yml not found", file=sys.stderr)
        sys.exit(2)

    data = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    changes = {}
    walk_and_fix(data.get("website", {}), repo, changes)

    if not changes:
        print("No hrefs needed fixing.")
        return

    print("Proposed href fixes:")
    for old, new in changes.items():
        print(f"  {old} -> {new}")

    if args.apply:
        cfg.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
        print("Applied changes to _quarto.yml")


if __name__ == "__main__":
    main()
