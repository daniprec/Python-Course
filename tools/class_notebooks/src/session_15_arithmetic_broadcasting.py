# %% [markdown]
# Session 15: Array Arithmetic and Broadcasting
## Today's goal: the final grades in one line

Closing Session 14. This is how we compute the final grade of every student:

```python
np.sum(marks * weights, axis=1) / 10
```

By the end of the class you will understand every piece: `*`, why `marks` and `weights` can be multiplied, and `axis`.

**How does one line compute the grade of every student?**

# %% [markdown]
### Setup

Helpers and data: the midterm from Session 14 (after the revisions), a house in the plane, and the face and chessboard images.

# %%
import matplotlib.pyplot as plt
import numpy as np


def show(image):
    """Display a 2D array as a grayscale image (0 = black, 1 = white)."""
    plt.imshow(image, cmap="gray", vmin=0, vmax=1)
    plt.axis("off")
    plt.show()


def draw(*shapes):
    """Draw one or more polygons given as arrays of points with shape (n, 2)."""
    for shape in shapes:
        closed = np.vstack([shape, shape[:1]])  # repeat the first point to close the polygon
        plt.plot(closed[:, 0], closed[:, 1], marker="o")
    plt.axhline(0, color="gray", linewidth=0.5)
    plt.axvline(0, color="gray", linewidth=0.5)
    plt.axis("equal")
    plt.grid(True)
    plt.show()


students = ["Alice", "Bruno", "Chloe", "Diego", "Emma", "Farid"]

# Points of each exercise: 2 open problems, 3 debugging, 6 multiple choice
weights = np.array([20, 20, 10, 10, 10, 5, 5, 5, 5, 5, 5])

marks = np.array([
    [0.75, 1, 0.5, 1, 0.5, 1, 1, 0, 1, 1, 1],      # Alice
    [0.5, 0.25, 1, 0.5, 0, 1, 0, 1, 1, 0, 1],      # Bruno
    [1, 1, 1, 1, 0.5, 1, 1, 1, 0, 1, 1],           # Chloe
    [0.25, 0.5, 0.5, 0.5, 0.5, 0, 1, 0, 1, 0, 1],  # Diego
    [1, 1, 0.5, 1, 1, 1, 0, 1, 1, 1, 1],           # Emma
    [0.5, 0.5, 0.5, 0, 1, 1, 1, 0, 0, 1, 0],       # Farid
])

# The corners of a house, one point (x, y) per row
house = np.array([
    [0, 0],  # bottom-left
    [4, 0],  # bottom-right
    [4, 3],  # top-right
    [2, 5],  # roof
    [0, 3],  # top-left
])
corners = ["bottom-left", "bottom-right", "top-right", "roof", "top-left"]

# The face and the chessboard from Session 14
face = np.zeros((8, 8))
face[2, 2] = 1
face[2, 5] = 1
face[5, 2:6] = 1
face[4, 1] = 1
face[4, 6] = 1

board = np.zeros((8, 8))
board[::2, 1::2] = 1
board[1::2, ::2] = 1

# %% [markdown]
- Run the line.

# %%

# %% [markdown]
### With what we knew: loops

The points of a student in one exercise are her mark times the value of the exercise. The final score is the sum over all exercises; divided by 10, the grade.

- The nested-loop version. Compare its length with the line above.

# %%

# %% [markdown]
## 1. Element-wise operations

Same shape: the operator acts element by element.

- One student: `marks[0] * weights`.
- Vectors, as in linear algebra: `u + v`, `u - v`, `3 * u`, `u / 2`, `u ** 2`.
- Warning: `u * v` is **not** the dot product.

# %%
u = np.array([1, 2, 3])
v = np.array([4, 0, -1])

# %%

# %%

# %%

# %% [markdown]
### Exercise: A linear combination

With `w = np.array([0, 1, 1])`, compute $2u - v + 3w$ without a loop. Then the midpoint $\frac{u + v}{2}$.

# %%

# %% [markdown]
## 2. Images are arrays too

- The negative of the face: `1 - face`.
- A darker face. Hint: multiply.
- `face + board`. What happens above 1?

# %%

# %%

# %%

# %% [markdown]
### Exercise: Blending two images

Show $0.7 \cdot \text{face} + 0.3 \cdot \text{board}$. Try other weights that add up to 1. What happens when the weight of `face` goes from 1 to 0?

# %%

# %% [markdown]
## 3. Broadcasting

`marks` is `(6, 11)`, `weights` is `(11,)`, and `marks * weights` works. Why?

- Compare shapes from the **right**.
- Compatible if equal, or one of them is 1.
- The smaller array is stretched.

```text
marks     (6, 11)
weights       (11,)  -> (1, 11) -> (6, 11)
```

# %%

# %% [markdown]
### Broadcasting with the house

`house` has shape `(5, 2)`: one point per row.

- Draw the house.
- Move the house to the right.
- Make the house twice as big. Then twice as big **and** 3 right, 1 up.
- Stretch it horizontally only.

# %%

# %%

# %%

# %%

# %% [markdown]
- Pull the roof: `pull = np.array([1, 1, 1, 1.5, 1])`, one factor per point. Does `house * pull` work? Why not? Fix it with a reshape.

# %%

# %%

# %% [markdown]
### One value per row, or one per column?

- Exercise 4 was badly worded: extra points **per exercise**. Add `correction` to `marks`.
- An attendance bonus **per student**. Does `marks + bonus` work? Fix it.
- Same rule for `-`, `*`, `/`, `**`, `>`?
- What if `marks` were square, `(6, 6)`?

# %%
correction = np.array([0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0])  # one value per exercise
bonus = np.array([0, 0.5, 0, 0, 0.25, 0])  # one value per student

# %%

# %%

# %%

# %% [markdown]
- Linear algebra: multiplying a matrix by a row scales its columns; by a column, its rows. Which products with a diagonal matrix are these?
- A column times a row: the multiplication table from `np.arange(1, 4)` and `np.arange(1, 6)`. Which product of linear algebra is it? And with `+`?

# %%

# %%

# %% [markdown]
### Exercise: Which shapes broadcast?

Without running code: which can be added to `house`, shape `(5, 2)`? Shape of the result?

1. `0.5`
2. `(2,)`
3. `(5,)`
4. `(1, 2)`
5. `(5, 1)`
6. `(3, 2)`

# %%

# %% [markdown]
### Exercise: Painting with broadcasting

No loops, no slicing. Start from `ramp = np.linspace(0, 1, 8)`.

1. A gradient from black (left) to white (right).
2. From black (top) to white (bottom).
3. A diagonal gradient: black top-left, white bottom-right.
4. Light the face from the right.

Which shapes are involved in each one?

# %%

# %%

# %%

# %%

# %% [markdown]
### Practice

Deactivate AI assistant tools.

### Exercise: Scale and broadcast

Compute the element-wise product $5 \cdot A \cdot v$, with $A$ the $3 \times 4$ matrix of the integers 1 to 12, and $v = [-2, -1, 0, 1]$.

# %%

# %% [markdown]
---

# Part 2: Array functions

`*` and broadcasting are done. One piece of our line is left: `axis`.

# %% [markdown]
## 4. Aggregation: the `axis` argument

- `points = marks * weights`. Then `np.sum(points)`: the whole class. Useful?
- `axis=1`: one value per student. The final grades.
- `axis=0`: one value per exercise.
- The house: `np.sum(house, axis=0)` and `axis=1`. Which shape disappears?
- The bounding box of the house: `np.min`, `np.max`. Its width and height?
- `np.prod` and `np.cumsum` on `[1, 2, 3, 4]`.

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Centering the house

Compute the center of the house (mean of its corners, one value for $x$, one for $y$), and move the house so its center is at the origin. Check the new center. Draw both.

# %%

# %% [markdown]
## 5. Sorting, searching, statistics

`np.argmax`, `np.argmin`, `np.argsort` return **positions**: use them to look up names.

- Who got the best grade?
- Ranking from best to worst.
- The highest corner of the house.
- Mean, median, standard deviation of the final grades. Average mark of each exercise?

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: The farthest corner

The norm of $(x, y)$ is $\sqrt{x^2 + y^2}$. Find the corner of the house farthest from the origin, without a loop. Then all the corners, from the closest to the farthest.

# %%

# %%

# %% [markdown]
## 6. Matrices

- `*` is element-wise; `@` is matrix multiplication.
- Dot product: `u @ v`, the same as `np.sum(u * v)`.
- **The grades, again:** `marks @ weights / 10`, one dot product per student.

# %%

# %%

# %% [markdown]
### Linear transformations

A matrix $M$ transforms point $p$ into $Mp$. Our points are rows, so all at once: `house @ M.T`.

- Shear the house with `H`. Draw both.
- `np.linalg.det(H)`: how do areas change?
- `np.linalg.inv(H)`: undo the shear. Check with `np.allclose()`.

# %%
H = np.array([[1, 1], [0, 1]])  # shear

# %%

# %%

# %%

# %% [markdown]
### Rotation: trigonometry meets matrices

NumPy works in radians: `np.radians(90)`.

$$R(\theta)=\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$$

- Build $R(90^\circ)$. Why `6.1e-17` instead of `0`?
- Rotate the house. Determinant of $R$?

# %%

# %%

# %% [markdown]
## 7. Challenge

Deactivate AI assistant tools.

Rotate the house 90° and then stretch it horizontally by 2, with `S = np.array([[2, 0], [0, 1]])`.

1. Build $M = S R$ and draw the transformed house.
2. Is $SR$ the same as $RS$?
3. By how much did the area change?
4. Recover the original house.
5. A stretch can be done with broadcasting (`house * [2, 1]`), but a rotation cannot. Why?

# %%

# %%

# %%

# %%

# %% [markdown]
## Next session

A fantasy football website exports the statistics of our players stat by stat. **How do we turn them into one row per player?**
