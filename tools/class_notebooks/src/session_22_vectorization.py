# %% [markdown]
# Session 22: Vectorization
## One million games

Back to Monty Hall. Below is our simulation from that session: a loop that plays the games one by one, always switching doors.

**Can we play one million games at once, without a loop?**

# %%
import numpy as np


def monty_hall_init(n_games: int) -> np.ndarray:
    """One row per game, one column per door: 1 for the car, 0 for a goat."""
    x = np.zeros((n_games, 3), dtype=int)
    ls_id_car = np.random.randint(0, 3, size=n_games)
    x[np.arange(n_games), ls_id_car] = 1
    return x


def play_with_loop(game: np.ndarray) -> float:
    """Play every game with a loop, always switching; return the win probability."""
    n_games = game.shape[0]
    sum_car = 0
    for id_game in range(n_games):
        id_guest = np.random.randint(0, 3)
        id_car = np.argmax(game[id_game])
        id_host = (3 - id_guest - id_car) % 3
        if id_host == id_car:
            id_host = (id_host + np.random.randint(1, 3)) % 3
        id_swap = (3 - id_guest - id_host) % 3
        sum_car += game[id_game, id_swap]
    return sum_car / n_games

# %% [markdown]
- Play 10,000 games. And 1,000,000? How long does it take? Hint: `%%time` at the top of the cell.

# %%

# %%

# %% [markdown]
## 1. Vectorization (review)

- Add `a` and `b` element-wise with a loop. Then without it.
- Repeat with two arrays of one million random numbers. Time both. Hint: `%timeit`.

# %%
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# %%

# %%

# %% [markdown]
### Exercise: Vectorize a Polynomial

Rewrite without the loop. Does `f` need any change?

```python
def f(x):
    return x**2 + 2*x + 1

result = np.zeros(arr.shape)
for i in range(len(arr)):
    result[i] = f(arr[i])
```

# %%
arr = np.array([1, 2, 3, 4, 5])

# %%

# %% [markdown]
## 2. When `if` meets an array

Predict, run, fix.

```python
if arr > 0:
    print("its higher")
```

```python
mask = arr > 1
print(not mask)
```

- What does `mask` contain? Why can `if` not use it?
- The element-wise "not".
- One Boolean from many: `.all()`, `.any()`. Write "not all" and "none".

# %%

# %%

# %%

# %% [markdown]
## 3. Functions that do not broadcast

Divide `numerators` by `denominators`. When the denominator is `0`, return $10^{10}$.

- Write `safe_division(numerator, denominator)` with an `if`. Does it work on the arrays?
- `np.vectorize()`. Is it faster than a loop?

# %%
numerators = np.array([1, 2, 3])
denominators = np.array([0, 1, 2])

# %%

# %%

# %% [markdown]
### Exercise: Safe Division with Masks

Same task, without `np.vectorize()`. Hint: a mask and its `~`.

# %%

# %% [markdown]
## 4. Masking (review)

- Values greater than 2: with a loop, then with a mask.
- In `grid`, replace every `0` with `2`.
- Raise every odd number of `numbers` to its closest even.
- Broadcasting vs. element-wise replacement: which shapes must match?

# %%
arr = np.array([1, 2, 3, 4, 5])
grid = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
numbers = np.array([1, 2, 3, 4, 5, 6, 7])

# %%

# %%

# %%

# %% [markdown]
### Exercise: Fix the Program

Replace every negative $x$ with $x^2$. Without running it: which error, and why? Then fix the last line.

```python
arr = np.array([-3, -2, -1, 0, 1, 2, 3])
mask_neg = arr < 0
replacement_values = np.array([10, 20])
arr[mask_neg] = replacement_values
```

# %%

# %% [markdown]
### Exercise: Random Replacements

Replace all negative values with random integers between 1 and 10.

# %%
arr = np.array([1, -1, 2, -2, 3, -3])

# %%

# %% [markdown]
## 5. Monty Hall at full speed

- **Keep** the first pick: the guest's choice for every game at once, and the win probability. Hint: fancy indexing.
- Where is the car in every game? Hint: `axis`.
- The host's door: `(3 - id_guest - id_car) % 3`. Fix the games where the guest picked the car, with a mask.
- **Switch**: the remaining door, and the win probability.
- One million games: time it and compare with the loop.

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
## 6. Challenge: Curve the Grades

Rewrite without a loop. Then, with one Boolean each: does **everyone** pass (at least 50)? Did **anyone** get 100?

```python
curved = np.zeros(scores.shape)
for i in range(len(scores)):
    new_score = scores[i] + 5
    if new_score > 100:
        new_score = 100
    if new_score < 50:
        new_score = 50
    curved[i] = new_score
```

# %%
scores = np.array([38, 47, 62, 95, 99, 71, 44])

# %%

# %% [markdown]
## Next session

Review and homework: a random student, a random exercise from the NumPy problem set. **Could you solve and explain any of them at the board?**
