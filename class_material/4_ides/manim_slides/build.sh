#!/usr/bin/env bash
# Build the Module 4 slides. The finished decks are written next to this folder
# (class_material/4_ides/), named like the other sessions.
#
#   ./build.sh            720p (default, good for a projector)
#   ./build.sh -ql        480p, fast, for checking layouts
#   ./build.sh -qh        1080p
#
# For each deck you get an animated HTML file (open in a browser) and a static PDF.
set -euo pipefail
cd "$(dirname "$0")"
Q="${1:--qm}"
OUT=".."

declare -A SCENES=(
  [session25]="S25Workshop S25VSCode S25Copilot S25Environments S25Recap"
  [session26]="S26Libraries S26Scripts S26Recap"
  [session27]="S27Files S27Data S27Library S27Recap"
)
declare -A NAMES=(
  [session25]="session_25_workshop_vscode_environments"
  [session26]="session_26_libraries_scripts"
  [session27]="session_27_files_library"
)

for s in session25 session26 session27; do
  for scene in ${SCENES[$s]}; do
    echo ">> rendering $scene"
    manim render "$Q" "$s.py" "$scene"
  done
  echo ">> exporting ${NAMES[$s]}"
  manim-slides convert --one-file ${SCENES[$s]} "$OUT/${NAMES[$s]}.html"
  python make_pdf.py "$OUT/${NAMES[$s]}.pdf" ${SCENES[$s]}
done
echo "Done. Open the .html files in a browser (arrow keys or click to advance)."
