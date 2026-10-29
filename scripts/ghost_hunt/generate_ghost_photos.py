"""
Generate the broken ghost-camera photos for the Halloween session.

Run from anywhere:  python scripts/ghost_hunt/generate_ghost_photos.py   (needs numpy and Pillow)

Input : ghost_1.png ... ghost_5.png, in the same folder as this script (square images)
Output: data/ghost_photos/photo_1 ... photo_5 (text files that students read with
        np.loadtxt() straight from their GitHub URLs, see modules/numpy/load.qmd), and
        answers.json with the keys next to this script. answers.json is in .gitignore:
        never commit it.

Every grayscale photo is 300x300 with values in [0, 1], a white frame (4 px) and a
black line just inside it (2 px), so it always contains pure white and pure black.

- photo_1 (.txt)  9 fragments with shuffled letter names; fragment[0, 0] holds the
                  fragment number (1-9, row by row).
- photo_2 (.txt)  9 fragments named by position, flattened to one value per line.
                  The photo was transposed, inverted, and squeezed into a narrow range.
- photo_3 (.csv)  9 fragments named by position, separated by semicolons; every row
                  was multiplied by a gain.
- photo_4 (.csv)  9 fragments named by position; rows mixed by a lens matrix
                  (stored = L @ photo). Three lenses, only one invertible.
- photo_5 (.txt)  colour photo, squared (darker). Its 3 channels are saved in
                  shuffled files channel_1..4, one of them a decoy.

Each photo hides one digit of the case number: the first decimal of the mean of its
top-right quarter (rows 0-149, columns 150-299); for the colour photo, the red channel.
"""
import json
import os
import shutil

import numpy as np
from PIL import Image, ImageOps

SIZE = 300
TILE = SIZE // 3
SEED = 31
LOW_CONTRAST = (2, 4)       # source images that get a contrast stretch

rng = np.random.default_rng(SEED)
here = os.path.dirname(os.path.abspath(__file__))
src = here                                     # ghost_1.png ... ghost_5.png live next to this script
out = os.path.join(here, "..", "..", "data", "ghost_photos")   # repo data/ghost_photos
shutil.rmtree(out, ignore_errors=True)
for k in range(1, 6):
    os.makedirs(os.path.join(out, f"photo_{k}"))


def rgb_of(k: int) -> np.ndarray:
    img = Image.open(os.path.join(src, f"ghost_{k}.png")).convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)
    if k in LOW_CONTRAST:
        img = ImageOps.autocontrast(img, cutoff=1)
    return np.asarray(img, dtype=float) / 255


def add_frame(img: np.ndarray) -> np.ndarray:
    """White frame (4 px) with a black line inside (2 px). Works for 2D and 3D arrays."""
    img = img.copy()
    inner = img[6:-6, 6:-6].copy()
    img[:] = 1
    img[4:-4, 4:-4] = 0
    img[6:-6, 6:-6] = inner
    return img


def fragments_of(photo: np.ndarray) -> dict:
    return {(r, c): photo[r * TILE:(r + 1) * TILE, c * TILE:(c + 1) * TILE].copy()
            for r in range(3) for c in range(3)}


def quarter_value(photo: np.ndarray) -> float:
    quarter = photo[:150, 150:] if photo.ndim == 2 else photo[:150, 150:, 0]
    return float(np.mean(quarter) * 10)


def digit_of(photo: np.ndarray) -> int:
    return int(quarter_value(photo))


answers = {}
gray = np.array([0.299, 0.587, 0.114])
photos = {k: np.round(add_frame(rgb_of(k) @ gray), 4) for k in (1, 2, 3, 4)}
photos[5] = np.round(add_frame(rgb_of(5)), 4)

# --- Photo 1: shuffled fragments in .txt -----------------------------------------
rng.shuffle(list("ABCDEFGHI"))                 # keeps the random stream (lens, channels) unchanged
# Fragment position stored in fragment_A ... fragment_I. Chosen so that the fragments
# joined in file order give a different digit than the recovered photo.
FILE_POSITION = [4, 7, 0, 5, 8, 2, 1, 6, 3]
letters = [None] * 9
for k, pos in enumerate(FILE_POSITION):
    letters[pos] = "ABCDEFGHI"[k]
order = []
for pos, (_, frag) in enumerate(fragments_of(photos[1]).items()):
    frag[0, 0] = pos + 1
    np.savetxt(os.path.join(out, "photo_1", f"fragment_{letters[pos]}.txt"), frag, fmt="%.4f")
    order.append(letters[pos])
answers["photo_1"] = "".join(order)
recovered_1 = photos[1].copy()                 # the recovered photo keeps the fragment numbers
for pos in range(9):
    recovered_1[(pos // 3) * TILE, (pos % 3) * TILE] = pos + 1

# --- Photo 2: frozen negative, transposed, flattened fragments -----------------------
CONTRAST, LOW = 20, 0.31
stored_2 = np.round((1 - photos[2].T) / CONTRAST + LOW, 4)
for (r, c), frag in fragments_of(stored_2).items():
    np.savetxt(os.path.join(out, "photo_2", f"fragment_{r}_{c}.txt"), frag.flatten(), fmt="%.4f")
answers["photo_2"] = CONTRAST
stretched_2 = (stored_2 - stored_2.min()) / (stored_2.max() - stored_2.min())
recovered_2 = (1 - stretched_2).T

# --- Photo 3: row gains in .npy ----------------------------------------------------
band_gains = np.array([0.95, 0.6, 0.85, 0.45, 0.75, 0.2, 0.9, 0.5, 0.7, 0.35])
gain = np.repeat(band_gains, SIZE // len(band_gains))
stored_3 = np.round(photos[3] * gain.reshape(-1, 1), 4)
for (r, c), frag in fragments_of(stored_3).items():
    np.savetxt(os.path.join(out, "photo_3", f"fragment_{r}_{c}.csv"), frag, fmt="%.4f", delimiter=";")
answers["photo_3"] = int(np.argmin(gain))
recovered_3 = stored_3 / stored_3[:, 0].reshape(-1, 1)

# --- Photo 4: lens matrix in .csv --------------------------------------------------
perm = rng.permutation(SIZE)
lens_ok = np.eye(SIZE, dtype=int)[perm]
lens_dup = lens_ok.copy()
i, j = rng.choice(SIZE, 2, replace=False)
lens_dup[i] = lens_dup[j]                      # two equal rows: determinant 0
lens_zero = lens_ok.copy()
lens_zero[rng.integers(SIZE)] = 0              # one empty row: determinant 0
lenses = {1: lens_dup, 2: lens_ok, 3: lens_zero}
stored_4 = lens_ok @ photos[4]
for (r, c), frag in fragments_of(stored_4).items():
    np.savetxt(os.path.join(out, "photo_4", f"fragment_{r}_{c}.csv"), frag, fmt="%.4f", delimiter=",")
for k, L in lenses.items():
    np.savetxt(os.path.join(out, "photo_4", f"lens_{k}.csv"), L, fmt="%d", delimiter=",")
answers["photo_4"] = 2
recovered_4 = np.linalg.inv(lens_ok) @ stored_4

# --- Photo 5: colour, squared, channels in shuffled files ---------------------------
dark = np.round(photos[5] ** 2, 4)
files = rng.permutation([1, 2, 3, 4])          # red, green, blue, decoy
for channel in range(3):
    np.savetxt(os.path.join(out, "photo_5", f"channel_{files[channel]}.txt"), dark[:, :, channel], fmt="%.4f")
np.savetxt(os.path.join(out, "photo_5", f"channel_{files[3]}.txt"), dark.mean(axis=2)[rng.permutation(SIZE)], fmt="%.4f")
answers["photo_5"] = "".join(str(f) for f in files[:3])
recovered_5 = np.sqrt(dark)

# --- Case number: one digit per photo -----------------------------------------------
recovered = {1: recovered_1, 2: recovered_2, 3: recovered_3, 4: recovered_4, 5: recovered_5}
answers["digits"] = {k: digit_of(p) for k, p in recovered.items()}
answers["values"] = {k: round(quarter_value(p), 4) for k, p in recovered.items()}
answers["case"] = "".join(str(answers["digits"][k]) for k in range(1, 6))

# Half-fixed photos should give a different digit
frags_1 = [np.loadtxt(os.path.join(out, "photo_1", f"fragment_{x}.txt")) for x in "ABCDEFGHI"]
half_fixed = {
    "1: fragments in file order": np.vstack([np.hstack(frags_1[r * 3:(r + 1) * 3]) for r in range(3)]),
    "2: only stretched": stretched_2,
    "2: not transposed": 1 - stretched_2,
    "2: not inverted": stretched_2.T,
    "3: not divided": stored_3,
    "3: divided by columns": stored_3 / stored_3[:, 0],
    "4: not undone": stored_4,
    "5: not brightened": dark,
    "5: channels reversed": recovered_5[:, :, ::-1],
    "5: blue, red, green": recovered_5[:, :, [2, 0, 1]],
}
answers["half_fixed_digits"] = {k: digit_of(v) for k, v in half_fixed.items()}

with open(os.path.join(here, "answers.json"), "w") as f:
    json.dump(answers, f, indent=2)

print(json.dumps(answers, indent=1))
