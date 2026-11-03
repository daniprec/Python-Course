"""Rebuild every clean class notebook from tools/class_notebooks/src/.

Run from the repository root:  python tools/class_notebooks/build_all.py
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "tools" / "class_notebooks" / "src"
BUILDER = ROOT / "tools" / "class_notebooks" / "py2nb.py"


def folder(session: int) -> str:
    """Return the class_material subfolder for a session number."""
    if session <= 6:
        return "1_fundamentals"
    if session <= 12:
        return "2_structures"
    return "3_numpy"


ok = True
for src in sorted(SRC.glob("session_*.py")):
    out = ROOT / "class_material" / folder(int(src.stem[8:10])) / f"{src.stem}.ipynb"
    result = subprocess.run([sys.executable, str(BUILDER), str(src), str(out), "--check"])
    ok = ok and result.returncode == 0
sys.exit(0 if ok else 1)
