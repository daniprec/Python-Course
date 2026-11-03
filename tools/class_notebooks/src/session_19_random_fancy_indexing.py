# %% [markdown]
# Session 19: Random Numbers and Fancy Indexing
## The Monty Hall problem

You are on a game show. Three doors: a car behind one, goats behind the others. You pick a door, say No. 1. The host, who knows what is behind the doors, opens another one, say No. 3, which has a goat. Then he asks: "Do you want to pick door No. 2?"

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Monty_open_door.svg/640px-Monty_open_door.svg.png" width="400">

In 1990 Marilyn vos Savant answered "switch" in her *Parade* column. Thousands of readers, many with a PhD, wrote back to say she was wrong. Paul Erdős was only convinced by a computer simulation.

**Should you switch? Let's simulate thousands of games and find out.**

# %%
import numpy as np

# %% [markdown]
- Your intuition first: probability of winning if you keep? If you switch?

# %% [markdown]
## 1. The game matrix

One row per game, one column per door. `0` is a goat, `1` is the car.

- Build `x`, a matrix of zeros for 10 games.

# %%

# %% [markdown]
### Exercise: Inspect the game matrix

Without running any code: shape of `x`? Type of `x`? Type of its elements? Then check. Can we ask for integers?

# %%

# %%

# %% [markdown]
### Exercise: Rows, columns, elements

Print the first row (doors of the first game), the first column (first door of each game) and the first element.

# %%

# %%

# %% [markdown]
- Put a car behind the first door of the first game.
- Put a car behind the first door of **every** game. Is this a fair game?

# %%

# %%

# %% [markdown]
## 2. Fancy indexing

To place each car at a random door we need one column index per row.

`x[[a0, b0, c0], [a1, b1, c1]]` selects `x[a0, a1]`, `x[b0, b1]`, `x[c0, c1]`.

- Select the diagonal of `y`.
- Select `2`, `6` and `7` in one line.
- Set the diagonal of `y` to `0`.

# %%
y = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

# %%

# %%

# %% [markdown]
### Predict, run, fix

Each snippet has a bug. Predict the error, type it, run it, fix it.

**Mismatched index lists**

```python
idx = [0, 1]
idy = [0, 1, 2]
print(y[idx, idy])
```

**Coordinates in the wrong order**: the programmer wants the diagonal.

```python
print(y[(0, 0), (1, 1), (2, 2)])
```

**Negative index lists**: the programmer wants `[7 5 3]`.

```python
idx = [0, 1, 2]
idy = [0, 1, 2]
print(y[-idx, -idy])
```

# %%

# %%

# %%

# %% [markdown]
## 3. Random integers

- A random integer with `np.random.randint(0, 3)`. Which values can it take?
- Ten of them at once. Hint: `size=`.
- Run the cell again. Same numbers? Now fix a seed with `np.random.seed()` and run twice.

# %%

# %%

# %%

# %% [markdown]
## 4. Random cars

- 10 games: one random car per game, in one line, with fancy indexing. Hint: `np.arange()` for the rows.
- Wrap it in a function `monty_hall_init(n_games)` that returns the game matrix. Create 1000 games.

# %%

# %%

# %% [markdown]
### Exercise: Check the generated games

Check that `x`:

1. Has minimum `0` and maximum `1`.
2. Has as many cars as games.
3. Has a car in about 33% of all doors.
4. Has the same proportion of cars behind each door.
5. Has exactly one car per game.

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
## 5. First strategy: keep the first pick

The host does not matter here: we never change our mind.

- 10,000 games. Loop over them: pick a random door, count the cars won.
- Win probability?
- Same thing without a loop. Hint: one random pick per game, then fancy indexing.

# %%

# %%

# %%

# %% [markdown]
## 6. Second strategy: switch doors

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Monty-RightCarSwitch.svg/1920px-Monty-RightCarSwitch.svg.png" width="300">

The doors are $\{0, 1, 2\}$. The car is behind door $A$, the guest picks $B$. The host opens $C \in \{0, 1, 2\} \setminus \{A, B\}$. The guest switches to the only door in $\{0, 1, 2\} \setminus \{B, C\}$.

One game first: `monty_hall_init(1)`.

- The guest picks a random door. Where is the car? Hint: `np.argmax()`.
- Which doors can the host open? First with Python sets, then with `np.setdiff1d()`.
- The host opens one of them at random. Hint: `np.random.choice()`.
- The guest switches. Did we win?

# %%

# %%

# %%

# %%

# %% [markdown]
Now 10,000 games:

- Put the steps above inside a loop. Win probability when switching?
- Repeat with 10 games, 100, 10,000, 100,000. What changes? Why are 10 games not enough?

# %%

# %%

# %% [markdown]
### Exercise: The host without sets

If the guest picked wrong, the host must open door `(3 - id_guest - id_car) % 3`.

1. Check it by hand for every pair of different `id_guest` and `id_car`.
2. What does it give when `id_guest == id_car`? Fix that case by adding `1` or `2` at random, modulo 3.
3. Which door does the guest switch to? Simulate 10,000 games with this rule.

# %%

# %%

# %% [markdown]
## 7. Challenge: Monty Hall with four doors

One car, three goats. The guest picks a door, the host opens **one** goat door not picked by the guest, the guest switches to one of the two remaining closed doors at random.

1. `monty_hall_init_4(n_games)`: an `(n_games, 4)` matrix with one random car per row.
2. Simulate 10,000 games keeping the first pick, and 10,000 switching.
3. Is switching still a good idea? Can you get the exact probabilities by hand?

# %%

# %%

# %% [markdown]
## Next session

A walker tumbles one step left or right at random, 100 times. **Where is the walker most likely to end up, and how far can they get?**
