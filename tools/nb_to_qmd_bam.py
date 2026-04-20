#!/usr/bin/env python3
"""
Enhanced notebook (.ipynb) -> Quarto .qmd converter following BAM course style.
- Reads all .ipynb files from a source directory and writes .qmd files to a target directory.
- Preserves markdown and code cells with proper Quarto formatting.
- Adds YAML front-matter with title, subtitle, and format.
- Wraps Exercise and Solution cells in callouts.
- Handles cells that should not execute (broken code for exercises).
- Detects empty code cells and marks them as non-executable.

Usage:
    python tools/nb_to_qmd_bam.py <src_dir> <dst_dir>
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List


def prettify_title(filename: str) -> str:
    """Convert filename to a readable title."""
    name = Path(filename).stem
    # Remove common prefixes like "1_1_", "2_3_", etc.
    name = re.sub(r"^\d+_\d+_", "", name)
    name = re.sub(r"^\d+_", "", name)
    # Remove _class suffix
    name = name.replace("_class", "")
    # Replace underscores and dashes with spaces, capitalize words
    parts = [p.capitalize() for p in name.replace("-", " ").replace("_", " ").split()]
    return " ".join(parts)


def extract_subtitle(cells: List[Dict]) -> str:
    """Extract a subtitle from the first few markdown cells."""
    for cell in cells[:5]:
        if cell.get("cell_type") == "markdown":
            source = "".join(cell.get("source", []))
            # Look for sentences that could be subtitles
            lines = [
                line.strip()
                for line in source.split("\n")
                if line.strip() and not line.strip().startswith("#")
            ]
            if lines:
                # Get first non-empty, non-heading line
                subtitle = lines[0][:80]  # Limit length
                return subtitle
    return "Python Programming Course"


def is_likely_broken_code(source: str) -> bool:
    """
    Detect if code is likely intentionally broken for exercise purposes.
    """
    if not source or source.strip() == "":
        return True

    # Common patterns in broken code
    broken_patterns = [
        r'print\(["\'][^"\']*\n',  # Unclosed string in print
        r"print\([^)]*$",  # Unclosed print statement
        r"^\s*#\s*[Ff]ix",  # Comment asking to fix
        r"^\s*#\s*[Yy]our\s+code",  # Your code here comment
        r"^\s*\.\.\.",  # Ellipsis placeholder
        r"pass\s*$",  # Just pass statement
    ]

    for pattern in broken_patterns:
        if re.search(pattern, source, re.MULTILINE):
            return True

    # Check for syntax that's clearly incomplete
    open_parens = source.count("(") - source.count(")")
    open_brackets = source.count("[") - source.count("]")
    open_braces = source.count("{") - source.count("}")

    if open_parens != 0 or open_brackets != 0 or open_braces != 0:
        return True

    return False


def is_exercise_or_solution(source: str) -> tuple:
    """
    Check if a markdown cell is an exercise or solution.
    Returns (is_special, type, rest_of_content)
    """
    stripped = source.strip()
    lower = stripped.lower()

    if lower.startswith("**exercise"):
        # Extract exercise text
        return (True, "exercise", stripped)
    elif lower.startswith("exercise"):
        return (True, "exercise", stripped)
    elif lower.startswith("**solution"):
        return (True, "solution", stripped)
    elif lower.startswith("solution"):
        return (True, "solution", stripped)

    return (False, None, source)


def convert_nb(nb_path: Path, out_path: Path, module_name: str = ""):
    """Convert a notebook to QMD format."""
    with nb_path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    title = prettify_title(nb_path.name)
    subtitle = extract_subtitle(cells)

    lines = []
    lines.append("---")
    lines.append(f'title: "{title}"')
    if module_name:
        lines.append(f'subtitle: "{module_name}"')
    else:
        lines.append(f'subtitle: "{subtitle}"')
    lines.append("format: html")
    lines.append("---")
    lines.append("")

    in_exercise_callout = False
    in_solution_callout = False

    for i, cell in enumerate(cells):
        ctype = cell.get("cell_type", "")
        source = "".join(cell.get("source", []))

        if ctype == "markdown":
            # Check if this is an exercise or solution
            is_special, special_type, content = is_exercise_or_solution(source)

            # Close previous callout if needed
            if in_exercise_callout or in_solution_callout:
                lines.append(":::")
                lines.append("")
                in_exercise_callout = False
                in_solution_callout = False

            if is_special:
                if special_type == "exercise":
                    lines.append("::: {.callout-note}")
                    lines.append("## Exercise")
                    lines.append("")
                    # Remove the "Exercise." or "**Exercise.**" prefix
                    content = re.sub(r"^\*\*[Ee]xercise\.?\*\*\s*", "", content)
                    content = re.sub(r"^[Ee]xercise\.?\s*", "", content)
                    lines.append(content)
                    in_exercise_callout = True
                elif special_type == "solution":
                    lines.append('::: {.callout-tip collapse="true"}')
                    lines.append("## Solution")
                    lines.append("")
                    # Remove the "Solution." or "**Solution.**" prefix
                    content = re.sub(r"^\*\*[Ss]olution\.?\*\*\s*", "", content)
                    content = re.sub(r"^[Ss]olution\.?\s*", "", content)
                    lines.append(content)
                    in_solution_callout = True
            else:
                lines.append(source)
            lines.append("")

        elif ctype == "code":
            # Close any open callout before a code cell unless we're in an exercise
            if in_solution_callout:
                # Keep solution callout open to include code
                pass
            elif in_exercise_callout:
                # Keep exercise callout open to include code
                pass

            # Detect if this code should not be executed
            is_broken = is_likely_broken_code(source)

            # Look ahead to see if next cell is also code (might be part of exercise)
            next_is_code = False
            if i + 1 < len(cells) and cells[i + 1].get("cell_type") == "code":
                next_is_code = True

            lines.append("```{python}")
            if is_broken:
                lines.append("#| eval: false")
            lines.append(source.rstrip())
            lines.append("```")
            lines.append("")

            # Close callout if this was the last code cell in exercise/solution
            if (in_exercise_callout or in_solution_callout) and not next_is_code:
                # Check if next cell is markdown - if so, don't close yet
                if i + 1 < len(cells) and cells[i + 1].get("cell_type") == "markdown":
                    next_source = "".join(cells[i + 1].get("source", []))
                    is_special, _, _ = is_exercise_or_solution(next_source)
                    if is_special:
                        # Next cell starts a new exercise/solution, close this one
                        lines.append(":::")
                        lines.append("")
                        in_exercise_callout = False
                        in_solution_callout = False
                # else let it stay open

        else:
            # Other cell types (raw, etc.)
            lines.append(f"<!-- skipped cell type: {ctype} -->")
            lines.append("")

    # Close any remaining callout
    if in_exercise_callout or in_solution_callout:
        lines.append(":::")
        lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    if len(sys.argv) < 3:
        print("Usage: python tools/nb_to_qmd_bam.py <src_dir> <dst_dir> [module_name]")
        sys.exit(1)

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    module_name = sys.argv[3] if len(sys.argv) > 3 else ""

    if not src.exists():
        print("Source folder does not exist:", src)
        sys.exit(1)

    # Find all notebooks, excluding _class versions for now (we'll handle them separately)
    notebooks = sorted(src.glob("*.ipynb"))

    # Filter out checkpoint files
    notebooks = [nb for nb in notebooks if ".ipynb_checkpoints" not in str(nb)]

    n = 0
    for nb_path in notebooks:
        out_file = dst / (nb_path.stem + ".qmd")
        print(f"Converting {nb_path.name} -> {out_file.name}")
        convert_nb(nb_path, out_file, module_name)
        n += 1

    print(f"\nConverted {n} notebooks to {dst}")


if __name__ == "__main__":
    main()
