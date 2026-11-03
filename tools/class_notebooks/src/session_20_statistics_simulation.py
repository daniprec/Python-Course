# %% [markdown]
# Session 20: Statistics and Simulation
## The random walk

A walker moves forward, but at each step tumbles one step to the left (`-1`) or to the right (`+1`), at random. Like tossing a coin 100 times.

<img src="https://qph.cf2.quoracdn.net/main-qimg-85602ae0258abac4a739172309395a55-pjlq" width="400">

**After 100 steps, where is the walker most likely to end up? How far can they get?**

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
- Your intuition first. And after 1,000 steps? 10,000?

# %% [markdown]
## 1. Describing data

Before simulating data, let's describe some.

- Mean, median, standard deviation, minimum and maximum of `measurements`.

# %%
measurements = np.array([12.1, 11.8, 12.5, 12.0, 11.6, 12.4])

# %%

# %% [markdown]
The midterm, one more time: points of the 10 students (Madrid and Segovia) in each part: open problems (out of 40), debugging (out of 30), multiple choice (out of 30).

- Mean of each part. Mean of each student.

# %%
part_points = np.array([
    [35, 20, 25],
    [15, 15, 20],
    [40, 25, 25],
    [15, 15, 15],
    [40, 25, 25],
    [20, 15, 15],
    [30, 25, 25],
    [40, 25, 25],
    [5, 10, 10],
    [25, 25, 20],
])

# %%

# %% [markdown]
### Exercise: Shapes of the means

Without running the code, predict the shapes of both mean arrays. Then compute the standard deviation of each part. In which part are the students most different from each other? Is that a fair comparison?

# %%

# %%

# %% [markdown]
## 2. Correlation and covariance

- Covariance matrix of `study_hours` and `exam_scores`. Hint: `np.cov()`. Shape? Which entry matters?
- Correlation matrix. Hint: `np.corrcoef()`. Between which values can it be?

# %%
study_hours = np.array([1, 2, 3, 4, 5, 6])
exam_scores = np.array([52, 55, 65, 71, 78, 85])

# %%

# %%

# %% [markdown]
### Exercise: Do the parts agree?

Correlation between the open problems and the multiple-choice part of `part_points`. Do students who do well in one part also do well in the other? Can we generalise?

# %%

# %% [markdown]
## 3. Is this coin fair?

A coin gives 62 heads in 100 flips.

- Fix a seed, so that everyone gets the same results.
- Simulate 100 flips of a fair coin, with `np.random.randint()`. How many heads?
- Simulate 10,000 experiments of 100 flips at once. Hint: `np.random.binomial()`.
- In which proportion of them is the number of heads at least as far from 50 as 62? What does this number mean, and what does it not mean?

# %%

# %%

# %%

# %%

# %% [markdown]
## 4. A random walk

Run the helper below.

# %%
import matplotlib.cm as cm


def plot_series(ls_ser, xlabel=None, ylabel=None, title=None):
    """Plot a list of series in shades of green (a 2D array: one line per column)."""
    if isinstance(ls_ser, np.ndarray):
        ls_ser = [ls_ser]
    colors = cm.Greens(np.linspace(1, 0.3, len(ls_ser)))
    plt.figure(figsize=(12, 6))
    for i, ser in enumerate(ls_ser):
        plt.plot(ser, color=colors[i])
    plt.xlabel(xlabel if xlabel else "Index")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

# %% [markdown]
### Exercise: Random steps

An array `ser` of 10 random steps, each `-1` or `1`. First with `np.random.randint()`, then with `np.random.choice()`.

# %%

# %%

# %% [markdown]
### Exercise: Cumulative steps

Add the steps of `ser` cumulatively: `[1, -1, -1, -1, 1]` gives `[1, 0, -1, -2, -1]`.

# %%

# %% [markdown]
### Exercise: Start at zero

Same, but the walk starts at `0`: `[1, -1, -1, -1, 1]` gives `[0, 1, 0, -1, -2, -1]`. Integers, please.

# %%

# %% [markdown]
- Write `random_walk(steps)`, which returns the positions of one walk.
- Simulate 5 walks of 100 steps, store them in a list and plot them with `plot_series`.

# %%

# %%

# %% [markdown]
## 5. Many walkers

### Exercise: Many walks at once

Improve `random_walk` into `random_walks(steps, num)`, which simulates `num` walks at once, with no loop. Store 100 walks of 100 steps in `arr_sim` and plot them (`plot_series` wants one walk per column). Hint: `size=(num, steps)` and `axis`.

# %%

# %%

# %% [markdown]
### Exercise: The fifth walker

Where did the 5th walker end up after 17 steps?

# %%

# %% [markdown]
### Exercise: Move the origin

The walks begin at `0`. Make them start at `-30` and plot them.

# %%

# %% [markdown]
### Exercise: Walking together

Two people choose a direction independently at each step, but only move when both agree:

- Both `+1`: move `+1`. Both `-1`: move `-1`.
- They disagree: stay in place.

Simulate 100 steps of this joint walk, starting at `0`, and plot it. Hint: a mask.

# %%

# %% [markdown]
## 6. Where do the walkers end up?

Run the helper below.

# %%
def plot_distribution(ser, name="Our Points", bins=30, xlabel=None, plot_normal=False):
    """Plot the histogram of a series, optionally with the normal curve of the same mean and std."""
    plt.figure(figsize=(12, 6))
    plt.hist(ser, bins=bins, density=True, alpha=0.6, color="g", label=name)
    if plot_normal:
        x = np.linspace(np.min(ser), np.max(ser), 100)
        mean, std = np.mean(ser), np.std(ser)
        pdf = np.exp(-((x - mean) ** 2) / (2 * std**2)) / (std * np.sqrt(2 * np.pi))
        plt.plot(x, pdf, linewidth=2, color="r", label="Normal Distribution")
    plt.xlabel(xlabel)
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.show()

# %% [markdown]
1,000 walkers, 100 steps each, in `arr_walks`.

- Without running any code: shape of `arr_walks`?
- The final position of each walker. Plot its distribution.
- Average final position: with a loop, then with NumPy. Is it what you expected?
- Standard deviation of the final positions. How far can a walker get?

# %%

# %%

# %%

# %%

# %% [markdown]
### The normal distribution

- Does the histogram look familiar?
- 1,000 points from a normal distribution with the same mean and standard deviation. Hint: `np.random.normal()`. Plot them.
- Overlay the normal curve on the walkers: `plot_normal=True`.
- Repeat with 1,000 and 10,000 steps. How does the standard deviation grow with the number of steps?

# %%

# %%

# %%

# %% [markdown]
## 7. Challenge: approximating π with Monte Carlo

Random points in the square $[-1, 1]^2$. The proportion inside the unit circle $x^2 + y^2 \leq 1$ is close to $\pi / 4$.

1. Write `monte_carlo_pi(num_points)`. Hint: `np.random.uniform()`.
2. Estimate $\pi$ with 100, 10,000 and 1,000,000 points. Run each several times: how stable is it?
3. Compare with the grid of points from the masking session. Which one is better for the same number of points?

# %%

# %%

# %% [markdown]
## Next session

A grayscale photo is a matrix of numbers, one per pixel. **Can we keep only a small fraction of those numbers and still recognise the photo?**
