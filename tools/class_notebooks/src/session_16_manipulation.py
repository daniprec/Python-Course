# %% [markdown]
# Session 16: Array Manipulation
## Our FPL midfielders

We play **Fantasy Premier League** in a mini-league with friends. These are the season statistics of the five midfielders in our squad. We want **one row per player**:

| Player | Goals | Assists | Clean Sheets | Defensive Contributions | Yellow Cards | Red Cards | Own Goals | Penalties Missed |
|--------|-------|---------|--------------|-------------------------|--------------|-----------|-----------|------------------|
| Midfielder 1 | 15 | 10 | 12 | 2  | 3 | 0 | 0 | 1 |
| Midfielder 2 | 6  | 7  | 10 | 14 | 6 | 0 | 0 | 0 |
| Midfielder 3 | 2  | 3  | 11 | 22 | 9 | 1 | 1 | 0 |
| Midfielder 4 | 9  | 11 | 8  | 1  | 2 | 0 | 0 | 0 |
| Midfielder 5 | 4  | 12 | 9  | 5  | 4 | 0 | 0 | 1 |

But the website exports them **stat by stat** (all the goals, then all the assists...):

| Statistic | Midfielder 1 | Midfielder 2 | Midfielder 3 | Midfielder 4 | Midfielder 5 |
|-----------|--------------|--------------|--------------|--------------|--------------|
| Goals | 15 | 6 | 2 | 9 | 4 |
| Assists | 10 | 7 | 3 | 11 | 12 |
| Clean Sheets | 12 | 10 | 11 | 8 | 9 |
| Defensive Contributions | 2 | 14 | 22 | 1 | 5 |
| Yellow Cards | 3 | 6 | 9 | 2 | 4 |
| Red Cards | 0 | 0 | 1 | 0 | 0 |
| Own Goals | 0 | 0 | 1 | 0 | 0 |
| Penalties Missed | 1 | 0 | 0 | 0 | 1 |

**How do we turn the second table into the first?**

Today's questions:

- The second table into the first: **reshape** and **transpose**.
- We sign a player in January: **add a row**.
- We compare with a friend's midfielders: **join** two arrays.
- Attack (goals, assists), defence (clean sheets, defensive contributions), discipline (cards, own goals, penalties missed): **split** the array.

# %%
import numpy as np

# Second table, as the website exports it: one long array, stat by stat
site_export = np.array([
    15, 6, 2, 9, 4,    # goals
    10, 7, 3, 11, 12,  # assists
    12, 10, 11, 8, 9,  # clean sheets
    2, 14, 22, 1, 5,   # defensive contributions
    3, 6, 9, 2, 4,     # yellow cards
    0, 0, 1, 0, 0,     # red cards
    0, 0, 1, 0, 0,     # own goals
    1, 0, 0, 0, 1,     # penalties missed
])

# %% [markdown]
## 1. Reshape arrays

`reshape()` returns a **new** array with the same values and a different shape.

- `np.arange(6).reshape(2, 3)`. Did the original change?
- `-1` lets NumPy compute one dimension. Which shapes are possible for `site_export`? Which ones fail?

# %%

# %%

# %%

# %% [markdown]
### Exercise: Contact sheet

A photographer prints photos numbered 1 to 6 in 3 rows of 2. Build the matrix without `np.array`.

### Exercise: Fill by columns

The printer fills the sheet **column by column**: $\begin{pmatrix} 1 & 4\\ 2 & 5\\ 3 & 6 \end{pmatrix}$. Build that one too.

# %%

# %%

# %% [markdown]
### Exercise: The Sudoku box

Number the 81 cells of a Sudoku from 0 to 80, row by row, in a 9×9 grid. Extract the central 3×3 box.

# %%

# %% [markdown]
## 2. Reshape is not transpose

1. `site_export.reshape(8, 5)`: one row per statistic. Correct, but not what we want.
2. `site_export.reshape(5, 8)`: right shape, **wrong values**. Why?
3. `site_export.reshape(8, 5).T`: one row per player. Compare with the first table. Call it `stats`.

# %%

# %%

# %%

# %% [markdown]
### Exercise: Spot the difference

Without running code: what is the first row of `site_export.reshape(5, 8)`? And of `site_export.reshape(8, 5).T`? Which one is Midfielder 1?

# %%

# %% [markdown]
## 3. Flatten arrays

- `flatten()` returns a one-dimensional copy. `stats.flatten()`: is it the same as `site_export`?
- How do you get `site_export` back from `stats`?

# %%

# %%

# %% [markdown]
## 4. Joining arrays

- `np.concatenate((a, b), axis=0)`: one on top of the other.
- `np.concatenate((a, b), axis=1)`: side by side.
- All dimensions except the joining one must match. What if they do not?

Compare with `np.sum(a, axis=0)`: concatenate **adds** along the axis, sum **squeezes** it.

# %%

# %%

# %%

# %% [markdown]
### Stacking

- `np.hstack()`, `np.vstack()`, `np.column_stack()` with two 1D arrays. Shapes?
- And with two 2D arrays?
- Watch 1D arrays: `vstack` turns `(N,)` into a row `(1, N)`.

# %%

# %%

# %% [markdown]
### Exercise: Rouché–Frobenius

A system $Ax = b$ with $n$ unknowns has a solution if and only if $\text{rank}(A) = \text{rank}([A|b])$; it is unique if the rank equals $n$.

Write `rouche_frobenius_theorem(A, b)` that builds $[A|b]$ with a stacking function and returns whether the system is inconsistent, has a unique solution, or infinitely many. Use `np.linalg.matrix_rank()`.

# %%
A = np.array([[2, 1, -1], [1, 3, 2], [1, -1, 2]])
b = np.array([8, 13, 3])

# %%

# %% [markdown]
### Exercise: The January transfer

We sign `new_player` in January. Add him to `stats` as a new row. What is the new shape?

# %%
new_player = np.array([5, 4, 6, 3, 2, 0, 0, 0])

# %%

# %% [markdown]
## 5. Splitting arrays

- `np.split(arr, 3)`: equal parts (error if not possible).
- `np.array_split(arr, 4)`: unequal parts allowed.
- `np.hsplit()` / `np.vsplit()`: by columns / by rows.
- A **list of positions** cuts where you want: `np.hsplit(stats, [2, 4])` gives attack, defence, discipline. Shapes?

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Split the points

FPL points for a midfielder: goal 5, assist 3, clean sheet 1, defensive contribution 2, yellow −1, red −3, own goal −2, penalty missed −2.

Split `points` into attack (first two), defence (next two), and discipline (last four). Check with the sums: 8, 3, and −8.

# %%
# FPL points of a midfielder, in the same order as the columns of stats
points = np.array([5, 3, 1, 2, -1, -3, -2, -2])

# %%

# %% [markdown]
## 6. Challenge: One array for the whole mini-league

Deactivate AI assistant tools.

A friend sent you `rival_export`: their 5 midfielders, stat by stat. Without loops:

1. Turn it into one row per player, one column per statistic.
2. Join it with `stats` into `league` (our players first). Shape?
3. Split `league` into the three groups and compute each player's points per group.
4. Total FPL points of every player (hint: `@`).
5. Report with two columns: player number (1 to 10) and total points.

# %%
# A friend's 5 midfielders, stat by stat
rival_export = np.array([
    11, 3, 7, 1, 5,    # goals
    6, 5, 9, 2, 8,     # assists
    10, 12, 7, 13, 9,  # clean sheets
    3, 16, 2, 25, 6,   # defensive contributions
    2, 5, 1, 8, 3,     # yellow cards
    0, 0, 0, 1, 0,     # red cards
    0, 1, 0, 0, 0,     # own goals
    1, 0, 0, 0, 1,     # penalties missed
])

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
## Next session

Happy Halloween. Our ghost camera broke last night, and every photo it saved is a scrambled file online. **Can we load the files and recover the photos?**
