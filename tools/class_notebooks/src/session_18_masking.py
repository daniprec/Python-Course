# %% [markdown]
# Session 18: Masking
## Who passed?

Back to the midterm. We have the final grade of every student. The pass mark is `5`.

**Who passed? How many? Who failed?**

# %%
import numpy as np

students = np.array(["Alice", "Bruno", "Chloe", "Diego", "Emma", "Farid"])
final_grades = np.array([8, 5, 9, 4.5, 9, 5])

# %% [markdown]
- With what we know: a loop.

# %%

# %% [markdown]
**Can we do better?**

# %% [markdown]
## 1. A mask is a set

- What does `final_grades >= 5` return? Type? Shape?
- Use it to select the grades that passed. And the names?
- Who failed?
- How many passed? Which proportion of the class?

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Predict the mask

Without running it: what does this print? Then select the values greater than or equal to `5`.

```python
values = np.array([2, 5, 8, 1, 9])
mask = values % 2 == 1
print(values[mask])
```

# %%

# %% [markdown]
### Masks in mathematics

The universe $U = \{1, \dots, 20\}$ and the set $A = \{x \in U : x \text{ is even}\}$.

- Build the mask of $A$. Then the set $A$.
- `True` is `1`, `False` is `0`. Which function from your maths courses is the mask?
- Mask vs. selection: which one has the length of $U$?

# %%
numbers = np.arange(1, 21)

# %%

# %%

# %% [markdown]
## 2. Set operations are logical operations

$B = \{x \in U : 3 \mid x\}$.

| Mathematics | NumPy |
|---|---|
| $A \cap B$ | `&` |
| $A \cup B$ | <code>&#124;</code> |
| $A^c$ | `~` |
| $\lvert A \rvert$ | `np.sum` |
| $\lvert A \rvert / \lvert U \rvert$ | `np.mean` |
| $\exists$, $\forall$ | `np.any`, `np.all` |

- $A \cap B$, $A \cup B$, $A^c$, $A \setminus B$.
- $|A \cap B|$? Probability that a random $x \in U$ is in $A \cup B$?
- Is there an even number above 15? Is every element of $A \cap B$ a multiple of 6?

# %%

# %%

# %%

# %% [markdown]
### Exercise: De Morgan's laws

Check with masks that $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$. Hint: `np.array_equal()`.

Which numbers of $U$ are neither even nor multiples of 3?

# %%

# %% [markdown]
## 3. Changing values with a mask

- Everyone gets 1.5 bonus points, but no grade can go above 10.
- A column with `"Pass"` or `"Fail"` for each student. Hint: `np.where()`.
- Alice's cumulative points after each exercise are below. After which exercise did she reach 50 points? Hint: `np.argmax()` on a mask.

# %%
alice_cumulative = np.array([15, 35, 40, 50, 55, 60, 65, 65, 70, 75, 80])

# %%

# %%

# %%

# %% [markdown]
## 4. Predict, run, fix

Each line has a bug. Predict the error, type it, run it, fix it.

```python
numbers[numbers % 3 == 0 | numbers % 5 == 0]
(numbers % 3 == 0) and (numbers % 5 == 0)
```

```python
arr = np.array([2, 8, 1, 9, 3, 7])
high = arr[arr > 6]
arr[high] = -1
```

# %%

# %%

# %% [markdown]
## 5. Practice

### Exercise: Multiples of 3 or 5

*Project Euler, [Problem 1](https://projecteuler.net/problem=1).*

<img src="https://raw.githubusercontent.com/daniprec/Python-Course/main/img/masking-multiples.png" width="600" alt="The numbers 1 to 29. Multiples of 3 in blue, of 5 in orange, of both in green.">

1. Sum of the natural numbers below `1000` that are multiples of 3 or 5, with a mask.
2. Check the inclusion–exclusion principle: $|A \cup B| = |A| + |B| - |A \cap B|$. What is $A \cap B$?
3. The multiples of $d$ below $n$ add up to $d \cdot \frac{m(m+1)}{2}$, with $m = \lfloor (n-1)/d \rfloor$. Get the same answer with no array at all.

# %%

# %%

# %%

# %% [markdown]
### Exercise: Estimating π by counting points

The quarter disc $x^2 + y^2 < 1$ inside $[0, 1]^2$ has area $\pi / 4$.

<img src="https://raw.githubusercontent.com/daniprec/Python-Course/main/img/masking-pi-grid.png" width="300" alt="A 20 by 20 grid of points: 316 inside the quarter circle in blue, 84 outside in grey.">

1. A grid of $N \times N$ points: `x = (np.arange(N) + 0.5) / N`.
2. Mask of the points inside the disc. Hint: broadcasting.
3. Estimate $\pi$ for $N = 10, 100, 1000$. How fast does the error shrink?
4. Show the mask with `plt.imshow(inside, cmap="gray", origin="lower")`.

# %%

# %%

# %% [markdown]
### Exercise: Pascal's triangle modulo 2

$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.

1. A $64 \times 64$ array with Pascal's triangle **modulo 2**. One loop over the rows; each row in one line, with slicing.
2. Mask of the odd entries. Show it with `plt.imshow(odd, cmap="gray_r")`. Which shape is it?
3. How many odd entries in the first 64 rows? And in the first $2^k$?

<img src="https://raw.githubusercontent.com/daniprec/Python-Course/main/img/masking-sierpinski.png" width="300" alt="The odd entries of the first 64 rows of Pascal's triangle in black: a triangle made of smaller triangles.">

Bonus: Lucas's theorem says $\binom{n}{k}$ is odd exactly when `(n & k) == k`. Build the same mask with no loop.

# %%
import matplotlib.pyplot as plt

# %%

# %%

# %% [markdown]
## 6. Masking with images

An image is an array, a mask is a set of pixels. Run the helpers below.

# %%
import cv2
import requests


def load_image(url: str, color: bool = False) -> np.ndarray:
    """Download an image as a NumPy array (grayscale by default, RGB if color=True)."""
    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype="uint8")
    if color:
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)


def show_image(img: np.ndarray):
    """Display an image or a mask."""
    if img.ndim == 3 and img.max() > 1:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap="gray", vmin=0, vmax=max(1, img.max()))
    plt.axis("off")
    plt.show()


url_img = "https://raw.githubusercontent.com/daniprec/Python-Course/main/img/"
url_dog = url_img + "dog-nobg.png"
url_beach = url_img + "beach.jpg"

# %% [markdown]
### A dog on the beach

- Load the dog and the beach. Shape? Type?
- Which pixels belong to the dog? Show the mask.
- An empty mask for the beach (all `False`). Put the dog mask in the bottom-right corner.
- Paste the dog on the beach.

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercises

1. **Bottom-left corner.**
2. **Flip it**: the puppy would rather look at the sea.
3. **A bigger dog** (`dog-cheems.png`): remove its white border and make it smaller.
4. **Colour**: repeat with `color=True`. What changes in the shape of the mask?
5. **Green dog**: paint the dog green.
6. **Green screen** (`cat-green.jpg`): cut the cat out of its green background.
7. **Negative**: invert the colours of the beach.

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
### Challenge: Schrödinger's cat

`cat-skeleton.jpg` holds a live cat and a skeleton side by side. Superimpose them by alternating pixels like a chessboard: `a` from the live cat, `d` from the skeleton.

```
a d a
d a d
a d a
```

1. Split the picture in two halves. Flip one so both look the same way.
2. A chessboard mask with two slicing assignments.
3. Combine the halves with the mask.

<img src="https://raw.githubusercontent.com/daniprec/Python-Course/main/img/cat-schrodinger.jpg" width="300" alt="A cat and its skeleton superimposed.">

# %%

# %%

# %%

# %% [markdown]
## 7. Challenge: the Mandelbrot set

$c \in M$ if the sequence $z_0 = 0$, $z_{k+1} = z_k^2 + c$ stays bounded. Once $|z_k| > 2$, it escapes.

1. A grid of complex numbers on $[-2, 0.5] \times [-1.25, 1.25]$: `x[np.newaxis, :] + 1j * y[:, np.newaxis]`.
2. A mask `inside`, all `True`. Loop 50 times: update `z` only where `inside`, then remove the points with `np.abs(z) > 2`.
3. Show `inside`.

<img src="https://raw.githubusercontent.com/daniprec/Python-Course/main/img/masking-mandelbrot.png" width="300" alt="The Mandelbrot set in white on black.">

Bonus: store the iteration at which each point escapes and show that array instead.

# %%

# %% [markdown]
## Next session

You are on a game show. Three doors: a car behind one, goats behind the others. You pick a door, the host opens another one with a goat. **Should you switch?**
