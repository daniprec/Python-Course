# %% [markdown]
# Session 17: Loading and Saving Data
## The ghost camera

Last night we went ghost hunting with a **ghost camera**: it beeps when a ghost is nearby, and every time it beeped, we snapped a picture. By the end of the night the camera got completely spooked... and broke. Every photo is broken, each one in a different way. The camera log:

```text
22:13  BEEP! Ghost nearby ............. photo_1 saved
       ERROR: memory shattered. 9 fragments shuffled inside the photo.
23:02  BEEP! Ghost nearby ............. photo_2 saved
       ERROR: sensor frozen. Flattened, halves swapped, contrast lost.
00:31  BEEP! Ghost nearby ............. photo_3 saved
       ERROR: interference on the sensor rows. Photo cut into 4 strips.
01:45  BEEP! Ghost nearby ............. photo_4 saved
       ERROR: lens cursed. Rows scrambled. Photo cut into 5 strips.
       NOTE: 3 lenses found in the camera bag.
03:33  BEEP! BEEP! BEEP! STRONG GHOST . photo_5 saved (colour)
       NOTE: ghost surrounded by small ORANGE flames.
       ERROR: colour channels separated and shuffled. Very low light.
03:34  CAMERA FAILURE. Too many ghosts.
```

**Who did we catch?** Load the broken files, recover all five photos, and find the **case number**.

Groups of three. Suggestion: A takes photos 1 and 2, B photos 3 and 4, C photo 5 and the case number. The first group to find the case number closes the investigation.

# %% [markdown]
Run the toolkit: `BASE` is the folder of the photos online, `show(image)` displays a 2D (grayscale) or 3D (colour) array, and `check(photo, key)` checks a key, e.g. `check(1, "ABCDEFGHI")` or `check("case", "12345")`.

# %%
import hashlib

import matplotlib.pyplot as plt
import numpy as np

# The photos are stored in the course repository
BASE = "https://raw.githubusercontent.com/daniprec/Python-Course/main/data/ghost_photos"


def show(image):
    """Display an image: a 2D array (grayscale, 0 = black, 1 = white) or a 3D array (colour)."""
    if image.ndim == 2:
        plt.imshow(image, cmap="gray", vmin=0, vmax=1)
    else:
        plt.imshow(np.clip(image, 0, 1))
    plt.axis("off")
    plt.show()


_KEYS = {1: "acba8dd74b724348", 2: "f5ca38f748a1d6ea", 3: "9ae2bdd7beedc2e7", 4: "d4735e3a265e16ee", 5: "865736a1c30a82dc", "case": "2eb2158e4711ef9f"}


def check(photo, key):
    """Check the key of a photo (1 to 5) or of the case ("case")."""
    digest = hashlib.sha256(str(key).strip().upper().encode()).hexdigest()[:16]
    if digest != _KEYS[photo]:
        print(f"Wrong key for photo {photo}. Keep investigating...")
    elif photo == "case":
        print("Correct case number! The ghost hunt is solved.")
    else:
        print(f"Correct key! Photo {photo} is recovered.")

# %% [markdown]
## 1. Where are the photos?

| Photo | Files |
|-------|-------|
| 1 | `photo_1/shattered.txt` |
| 2 | `photo_2/frozen.txt` |
| 3 | `photo_3/banded.csv` (separated by `;`) |
| 4 | `photo_4/cursed.csv` (separated by `,`), and the lenses `photo_4/lens_1.csv`, `lens_2.csv`, `lens_3.csv` |
| 5 | `photo_5/colour.txt` |

- The URL of a file: `f"{BASE}/photo_1/shattered.txt"`.
- Load it with `np.loadtxt()`. Shape? Smallest and largest value? Show it.
- A `.csv` file: what does `delimiter` do?

Every photo is $300 \times 300$, values in $[0, 1]$, with a **white frame** (4 pixels of `1`) and, just inside it, a thin **black line** (`0`).

# %%

# %%

# %% [markdown]
## 2. Photo 1: The shattered photo

Nine $100 \times 100$ fragments, put back in a random order. We name the places row by row:

```text
A B C
D E F
G H I
```

- Cut the photo into its nine fragments (`np.vsplit()`, then `np.hsplit()`), in a list, in the order A, ..., I. Show each one.
- Find the right order. The white frame gives the corners and the edges; the picture does the rest.
- Join them again: each row side by side, then the three rows one on top of the other.

**Key:** the letters, in the order of the original photo, e.g. `check(1, "ABCDEFGHI")`.

# %%

# %%

# %%

# %% [markdown]
## 3. Photo 2: The frozen photo

One value per line. Flattened, left and right halves swapped, contrast squeezed into a tiny range, and **mirrored along the diagonal**.

- Give it back its square shape. Cut it into halves and swap them.
- Stretch the values back to $[0, 1]$: $\text{stretched} = \frac{\text{stored} - \min}{\max - \min}$. Why does this work?
- Undo the mirror.

**Key:** how many times did the ghost reduce the contrast? The original range was 1.

# %%

# %%

# %%

# %% [markdown]
## 4. Photo 3: The banded photo

Each row $i$ was multiplied by its own **gain** between 0 and 1: $\text{stored}[i, j] = \text{photo}[i, j] \times \text{gain}[i]$. Then the photo was cut into **four vertical strips** and shuffled.

- Cut it into four strips and put them in order. Which strip has the black line on its left edge? On its right edge? Try both orders for the middle ones.
- The first column of the original is the white frame. So what is the first column of the rebuilt photo?
- Divide every row by its gain. Careful with broadcasting: shape `(300,)` or `(300, 1)`?

**Key:** the index of the first row with the smallest gain.

# %%

# %%

# %%

# %% [markdown]
## 5. Photo 4: The cursed lens

The rows were scrambled by a lens matrix: $\text{stored} = L \cdot \text{photo}$. Only one of the three lenses was used. Then the photo was cut into **five horizontal strips** and shuffled; the **top-left pixel** of each strip stores its number, 1 to 5, from top to bottom.

- Cut it into five strips, sort them by their number (`np.argsort()`), join them.
- Load the three lenses. Which one has an inverse? Hint: the determinant.
- Undo the lens: $\text{photo} = L^{-1} \cdot \text{stored}$.

**Key:** the number of the lens.

# %%

# %%

# %%

# %% [markdown]
## 6. Photo 5: The colour photo

$300 \times 900$: three $300 \times 300$ images side by side, numbered 1 to 3 from left to right. They are the red, green and blue channels, in a shuffled order. Every value was squared.

- Cut it into three images. Join them along a **new** axis: shape `(300, 300, 3)`. Hint: `np.stack()`.
- Undo the square.
- Which image is red, green, blue? Try the orders. Clue: small **orange** flames. Blue or green flames belong to other spirits.

**Key:** the numbers of the red, green and blue images, in that order, e.g. `check(5, "123")`.

# %%

# %%

# %%

# %% [markdown]
## 7. The case number

Each recovered photo hides one digit: the **second decimal of the mean brightness of `photo[100:250, 100:]`**. A mean of `0.4371` gives `3`. For the colour photo, only the red channel.

- One digit per photo, from photo 1 to photo 5.
- A photo that is only half fixed gives a wrong digit.

**Key:** the five digits, e.g. `check("case", "12345")`.

# %%

# %%

# %% [markdown]
## 8. Saving the evidence

- Save a recovered photo with `np.save()`. Load it back with `np.load()`. Same array?
- Save it with `np.savetxt()`. Open the file: what is inside?
- `np.savetxt()` with photo 5: predict, then run.

# %%

# %%

# %%

# %% [markdown]
## Next session

Back to the midterm. We have the final grade of every student, and the pass mark is `5`. **Who passed?**
