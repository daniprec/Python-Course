"""Build the static PDF: one page per slide, showing its final state.

Usage: python make_pdf.py OUT.pdf SceneA SceneB ...
A page ends where the next heading (or wipe) clears the screen, so build-up
steps are skipped and only the finished slide is kept.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import img2pdf

out, scenes = sys.argv[1], sys.argv[2:]
pages = []
with tempfile.TemporaryDirectory() as tmp:
    for scene in scenes:
        cfg = json.load(open(f"slides/{scene}.json"))["slides"]
        fin = json.load(open(f"slides/{scene}.finals.json"))
        keep = sorted(set(fin["finals"]) | {len(cfg) - 1})
        for k in keep:
            png = Path(tmp) / f"{len(pages):03d}.png"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-sseof", "-0.04",
                            "-i", cfg[k]["file"], "-frames:v", "1", str(png)], check=True)
            pages.append(str(png))
    with open(out, "wb") as f:
        f.write(img2pdf.convert(pages))
print(f"{out}: {len(pages)} pages")
