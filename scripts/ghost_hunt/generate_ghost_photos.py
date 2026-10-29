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

Every photo is stored in ONE file, cut into pieces that were put back in the wrong order.
Students always (1) split the file and join the pieces in the right order, then
(2) undo the specific transformation of that photo.

- photo_1/shattered.txt  300x300. 3x3 grid of fragments, shuffled, no numbers: students
                         order them by eye. SECRET, not on the page: the bottom-right
                         fragment is mirrored along the anti-diagonal (it looks like a second
                         top-left corner); students must spot it and fix it, e.g. with
                         fragment[::-1, ::-1].T.
- photo_2/frozen.txt     90,000 values, one per line (reshape to 300x300). Its two
                         vertical halves are swapped. The photo was transposed, inverted,
                         and squeezed into a narrow range.
- photo_3/banded.csv     300x300, separated by semicolons. 4 vertical strips, shuffled
                         (order found by eye). Every row was multiplied by a gain.
- photo_4/cursed.csv     300x300, separated by commas. 5 horizontal strips, shuffled; the
                         top-left pixel of each strip holds its number (1-5). Rows mixed by
                         a lens matrix (stored = L @ photo). lens_1..3.csv: only one is
                         invertible.
- photo_5/colour.txt     300x1200: four 300x300 channels side by side (red, green, blue in
                         shuffled places, plus a decoy). The colour photo inside was
                         shuffled in a 3x3 grid, numbered like photo 1, and squared.

Each photo hides one digit of the case number: the SECOND decimal of the mean of
photo[150:, 150:250]; for the colour photo, the red channel.
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


def grid_tiles(photo: np.ndarray) -> list:
    """The 9 fragments of a 3x3 grid, row by row (works for 2D and 3D arrays)."""
    return [photo[r * TILE:(r + 1) * TILE, c * TILE:(c + 1) * TILE].copy()
            for r in range(3) for c in range(3)]


def join_grid(tiles: list) -> np.ndarray:
    return np.concatenate([np.concatenate(tiles[r * 3:(r + 1) * 3], axis=1) for r in range(3)], axis=0)


def number_tiles(tiles: list) -> None:
    """Write the fragment number (1-9) in the top-left pixel of each fragment."""
    for pos, tile in enumerate(tiles):
        tile[0, 0] = pos + 1


def anti_transpose(tile: np.ndarray) -> np.ndarray:
    """Mirror along the anti-diagonal (bottom-left to top-right). It is its own inverse."""
    return tile[::-1, ::-1].T


def quarter_value(photo: np.ndarray) -> float:
    # The region cuts through the bottom-right fragment of photo 1, so its secret mirror
    # changes the digit (a region that holds a whole fragment would not notice it).
    # Region and second decimal were chosen by search: every half-fixed photo below gives
    # a wrong digit, and every correct value is at least 0.002 away from a digit change.
    region = photo[150:, 150:250] if photo.ndim == 2 else photo[150:, 150:250, 0]
    return float(np.mean(region) * 100)


def digit_of(photo: np.ndarray):
    value = quarter_value(photo)
    if not np.isfinite(value):                 # e.g. dividing by a black column: nan
        return None
    return int(value) % 10                     # second decimal of the mean


def save(name: str, arr: np.ndarray, **kwargs) -> None:
    np.savetxt(os.path.join(out, name), arr, fmt="%.4f", **kwargs)


answers = {}
gray = np.array([0.299, 0.587, 0.114])
photos = {k: np.round(add_frame(rgb_of(k) @ gray), 4) for k in (1, 2, 3, 4)}
photos[5] = np.round(add_frame(rgb_of(5)), 4)

# --- Photo 1: 3x3 grid, shuffled, no numbers (ordered by eye) ------------------------
rng.shuffle(list("ABCDEFGHI"))                 # keeps the random stream (lens, channels) unchanged
# The 9 places of the stored photo are named A ... I, row by row. SLOT_1[k] is the
# fragment (0-8) placed in place k. Chosen so that the stored photo, not unshuffled,
# gives a different digit than the recovered photo.
SLOT_1 = [4, 7, 0, 5, 8, 2, 1, 6, 3]
tiles_1 = grid_tiles(photos[1])
tiles_1[8] = anti_transpose(tiles_1[8])        # SECRET: bottom-right fragment mirrored (not on the page)
shattered = join_grid([tiles_1[pos] for pos in SLOT_1])
unmirrored_1 = join_grid(tiles_1)              # ordered and joined, corner not fixed yet
tiles_1[8] = anti_transpose(tiles_1[8])        # fixed
save("photo_1/shattered.txt", shattered)
letters = [None] * 9
for k, pos in enumerate(SLOT_1):
    letters[pos] = "ABCDEFGHI"[k]
answers["photo_1"] = "".join(letters)          # place letters in the order of the original photo
recovered_1 = join_grid(tiles_1)               # identical to the original photo

# --- Photo 2: two halves swapped; frozen negative, transposed, flattened -------------
CONTRAST, LOW = 20, 0.31
stored_2 = np.round((1 - photos[2].T) / CONTRAST + LOW, 4)
left, right = np.hsplit(stored_2, 2)
frozen = np.hstack((right, left))
save("photo_2/frozen.txt", frozen.flatten())
answers["photo_2"] = CONTRAST
stretched_2 = (stored_2 - stored_2.min()) / (stored_2.max() - stored_2.min())
recovered_2 = (1 - stretched_2).T

# --- Photo 3: four vertical strips, shuffled; row gains ------------------------------
band_gains = np.array([0.95, 0.6, 0.85, 0.45, 0.75, 0.2, 0.9, 0.5, 0.7, 0.35])
gain = np.repeat(band_gains, SIZE // len(band_gains))
stored_3 = np.round(photos[3] * gain.reshape(-1, 1), 4)
SLOT_3 = [2, 0, 3, 1]                          # strip placed in each place, left to right
strips_3 = np.hsplit(stored_3, 4)
banded = np.hstack([strips_3[s] for s in SLOT_3])
save("photo_3/banded.csv", banded, delimiter=";")
answers["photo_3"] = int(np.argmin(gain))
recovered_3 = stored_3 / stored_3[:, 0].reshape(-1, 1)

# --- Photo 4: lens matrix; five horizontal strips, shuffled, numbered ----------------
perm = rng.permutation(SIZE)
lens_ok = np.eye(SIZE, dtype=int)[perm]
lens_dup = lens_ok.copy()
i, j = rng.choice(SIZE, 2, replace=False)
lens_dup[i] = lens_dup[j]                      # two equal rows: determinant 0
lens_zero = lens_ok.copy()
lens_zero[rng.integers(SIZE)] = 0              # one empty row: determinant 0
lenses = {1: lens_dup, 2: lens_ok, 3: lens_zero}
stored_4 = (lens_ok @ photos[4]).astype(float)
for s in range(5):
    stored_4[s * 60, 0] = s + 1                # strip number in its top-left pixel (frame column)
SLOT_4 = [3, 0, 4, 2, 1]                       # strip placed in each place, top to bottom
strips_4 = np.vsplit(stored_4, 5)
cursed = np.vstack([strips_4[s] for s in SLOT_4])
save("photo_4/cursed.csv", cursed, delimiter=",")
for k, L in lenses.items():
    np.savetxt(os.path.join(out, "photo_4", f"lens_{k}.csv"), L, fmt="%d", delimiter=",")
answers["photo_4"] = 2
recovered_4 = np.linalg.inv(lens_ok) @ stored_4   # the numbers end up in the white frame column

# --- Photo 5: colour, 3x3 shuffled and numbered, squared, channels side by side ------
SLOT_5 = [7, 3, 8, 1, 6, 0, 5, 2, 4]
dark = np.round(photos[5] ** 2, 4)
tiles_5 = grid_tiles(dark)
number_tiles(tiles_5)                          # same number in the 3 channels
dark_numbered = join_grid(tiles_5)
dark_shuffled = join_grid([tiles_5[pos] for pos in SLOT_5])
files = rng.permutation([1, 2, 3, 4])          # places of red, green, blue, decoy (1-4)
blocks = [None] * 4
for channel in range(3):
    blocks[files[channel] - 1] = dark_shuffled[:, :, channel]
blocks[files[3] - 1] = dark.mean(axis=2)[rng.permutation(SIZE)]   # decoy: static
save("photo_5/colour.txt", np.hstack(blocks))
answers["photo_5"] = "".join(str(f) for f in files[:3])
recovered_5 = np.sqrt(dark_numbered)

# --- Case number: one digit per photo -----------------------------------------------
recovered = {1: recovered_1, 2: recovered_2, 3: recovered_3, 4: recovered_4, 5: recovered_5}
answers["digits"] = {k: digit_of(p) for k, p in recovered.items()}
answers["values"] = {k: round(quarter_value(p), 4) for k, p in recovered.items()}
answers["case"] = "".join(str(answers["digits"][k]) for k in range(1, 6))

# Half-fixed photos should give a different digit
frozen_2d = np.loadtxt(os.path.join(out, "photo_2", "frozen.txt")).reshape(SIZE, SIZE)
stretched_frozen = (frozen_2d - frozen_2d.min()) / (frozen_2d.max() - frozen_2d.min())
banded_l = np.loadtxt(os.path.join(out, "photo_3", "banded.csv"), delimiter=";")
cursed_l = np.loadtxt(os.path.join(out, "photo_4", "cursed.csv"), delimiter=",")
half_fixed = {
    "1: not unshuffled": np.loadtxt(os.path.join(out, "photo_1", "shattered.txt")),
    "1: corner not mirrored back": unmirrored_1,
    "1: corner fixed with .T": join_grid(tiles_1[:8] + [tiles_1[8][::-1, ::-1]]),
    "2: halves not swapped": (1 - stretched_frozen).T,
    "2: only stretched": stretched_2,
    "2: not transposed": 1 - stretched_2,
    "2: not inverted": stretched_2.T,
    "3: strips not unshuffled": banded_l / banded_l[:, 0].reshape(-1, 1),
    "3: middle strips swapped": np.hstack([strips_3[k] for k in (0, 2, 1, 3)]) / gain.reshape(-1, 1),
    "3: not divided": stored_3,
    "3: divided by columns": stored_3 / stored_3[:, 0],
    "4: strips not unshuffled": np.linalg.inv(lens_ok) @ cursed_l,
    "4: not undone": stored_4,
    "5: not unshuffled": np.sqrt(dark_shuffled),
    "5: not brightened": dark_numbered,
    "5: channels reversed": recovered_5[:, :, ::-1],
    "5: blue, red, green": recovered_5[:, :, [2, 0, 1]],
}
answers["half_fixed_digits"] = {k: digit_of(v) for k, v in half_fixed.items()}

with open(os.path.join(here, "answers.json"), "w") as f:
    json.dump(answers, f, indent=2)

print(json.dumps(answers, indent=1))
