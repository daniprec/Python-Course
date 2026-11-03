"""Build the text files of the masking-with-images lesson (data/masking/).

The images are reduced (one pixel of every few, so values stay exact) and saved
with np.savetxt, so students load them with np.loadtxt as in Session 17.
Colour images are saved as 2D arrays of shape (rows, columns * 3): students
reshape them back to (rows, columns, 3).

Run from the repository root:  python scripts/masking_images/make_data.py
"""
import pathlib

import cv2
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
IMG = ROOT / "img"
OUT = ROOT / "data" / "masking"
OUT.mkdir(parents=True, exist_ok=True)


def read_rgb(name: str) -> np.ndarray:
    """Read an image from img/ as an RGB array (alpha channel kept if present)."""
    img = cv2.imread(str(IMG / name), cv2.IMREAD_UNCHANGED)
    if img.shape[2] == 4:
        return cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def gray(rgb: np.ndarray) -> np.ndarray:
    """Convert RGB to grayscale integers."""
    return cv2.cvtColor(np.ascontiguousarray(rgb[:, :, :3]), cv2.COLOR_RGB2GRAY).astype(int)


def save(name: str, arr: np.ndarray):
    """Save a 2D array, or a colour image as (rows, columns * 3), as integers."""
    if arr.ndim == 3:
        arr = arr.reshape(arr.shape[0], -1)
    np.savetxt(OUT / name, arr, fmt="%d")
    print(name, arr.shape, f"{(OUT / name).stat().st_size / 1e6:.2f} MB")


# Dog without background: transparent pixels become black (0), dog pixels are at least 1
dog = read_rgb("dog-nobg.png")[::4, ::4]
inside = dog[:, :, 3] >= 128
dog_gray = np.where(inside, np.clip(gray(dog), 1, 255), 0)
dog_rgb = np.where(inside[:, :, None], np.clip(dog[:, :, :3], 1, 255), 0)
save("dog.txt", dog_gray)
save("dog_rgb.txt", dog_rgb)

# Beach
beach = read_rgb("beach.jpg")[::4, ::4]
save("beach.txt", gray(beach))
save("beach_rgb.txt", beach)

# Second dog: black frame (0), white rectangle (255), dog strictly in between
dog_2 = read_rgb("dog-2.png")[::4, ::4]
g = gray(dog_2)
inside = dog_2[:, :, 3] >= 128
background = np.where(g >= 128, 255, 0)
save("dog_2.txt", np.where(inside, np.clip(g, 1, 254), background))

# Cat with a green background
save("cat_green_rgb.txt", read_rgb("cat-green.jpg")[::2, ::2])

# Schrodinger: skeleton and live cat side by side
save("cat_skeleton.txt", gray(read_rgb("cat-skeleton.jpg")[::11, ::11]))
