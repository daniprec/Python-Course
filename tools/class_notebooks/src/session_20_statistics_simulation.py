# %% [markdown]
# Session 20: Statistics and Simulation
## The random walk

A walker moves forward, but at each step tumbles one step to the left (`-1`) or to the right (`+1`), at random. Like tossing a coin 100 times.

<img src="https://qph.cf2.quoracdn.net/main-qimg-85602ae0258abac4a739172309395a55-pjlq" width="400">

**After 100 steps, where is the walker most likely to end up? How far can they get?**

# %% [markdown]
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slides 2 and 3.</div>

# %% [markdown]
A related question, before we start:

# %% [markdown]
<div style="background-color:#e3f2fd; color:#0d2b45; border-left:6px solid #1976d2; padding:10px 14px; border-radius:4px;"><b>Poll 1.</b> A coin gives 62 heads in 100 flips. Is it fair?<br>A. Yes, it is fair<br>B. Probably not<br>C. Can't tell</div>

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
## 1. Describing data

Before simulating data, let's describe some.

- Mean and standard deviation of `measurements`.

# %%
measurements = np.array([12.1, 11.8, 12.5, 12.0, 11.6, 12.4])

# %%


# %% [markdown]
<div style="background-color:#fff8e1; color:#3d2e00; border-left:6px solid #f9a825; padding:10px 14px; border-radius:4px;"><b>More in the notes:</b> median, minimum and maximum work the same way. In the exam, they are on the cheat sheet. See <a href="https://danielprecioso.com/Python-Course/modules/numpy/statistics.html#descriptive-statistics">Descriptive statistics</a>.</div>

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

# %% [markdown]
<div style="background-color:#e3f2fd; color:#0d2b45; border-left:6px solid #1976d2; padding:10px 14px; border-radius:4px;"><b>Poll 2.</b> Before running anything: what is the shape of <code>np.mean(part_points, axis=0)</code>?<br>A. (10,)<br>B. (3,)<br>C. (10, 3)<br>D. A single number</div>

# %%


# %% [markdown]
## 2. Do the parts agree?

- Correlation between the open problems and the multiple-choice part of `part_points`. Hint: `np.corrcoef()`. Between which values can it be? Can we generalise?

# %% [markdown]
<div style="background-color:#e3f2fd; color:#0d2b45; border-left:6px solid #1976d2; padding:10px 14px; border-radius:4px;"><b>Poll 3.</b> Guess the correlation between the open problems and the multiple-choice part.<br>A. About 0<br>B. About 0.3<br>C. About 0.6<br>D. About 0.9</div>

# %%


# %% [markdown]
<div style="background-color:#fff8e1; color:#3d2e00; border-left:6px solid #f9a825; padding:10px 14px; border-radius:4px;"><b>More in the notes:</b> covariance, with <code>np.cov()</code>. See <a href="https://danielprecioso.com/Python-Course/modules/numpy/statistics.html#correlation-and-covariance">Correlation and covariance</a>.</div>

# %% [markdown]
## 3. Is this coin fair?

A coin gives 62 heads in 100 flips. Back to poll 1: let's test it.

- Fix a seed, so that everyone gets the same results.
- Simulate 10,000 experiments of 100 flips of a fair coin, at once. Hint: `np.random.binomial()`.
- In which proportion of them is the number of heads at least as far from 50 as 62?

# %%


# %%


# %%


# %% [markdown]
<div style="background-color:#e3f2fd; color:#0d2b45; border-left:6px solid #1976d2; padding:10px 14px; border-radius:4px;"><b>Poll 4.</b> This proportion is a (simulated) p-value. What does it mean?<br>A. The probability that the coin is fair<br>B. If the coin were fair, how often a result this extreme would happen<br>C. The probability that the coin is biased</div>

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

An array `ser` of 10 random steps, each `-1` or `1`. Hint: `np.random.choice()`.

# %%


# %% [markdown]
<div style="background-color:#fff8e1; color:#3d2e00; border-left:6px solid #f9a825; padding:10px 14px; border-radius:4px;"><b>More in the notes:</b> the same with <code>np.random.randint()</code> and masking. See <a href="https://danielprecioso.com/Python-Course/modules/numpy/statistics.html#random-walk-simulation">Random walk simulation</a>.</div>

# %% [markdown]
### Exercise: From steps to positions

Add the steps of `ser` cumulatively, starting at `0`: `[1, -1, -1, -1, 1]` gives `[0, 1, 0, -1, -2, -1]`. Integers, please. Hint: `np.cumsum()`.

# %%


# %% [markdown]
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slides 4 and 5.</div>

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
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slide 6.</div>

# %% [markdown]
### Exercise: The fifth walker

Where did the 5th walker end up after 17 steps?

# %% [markdown]
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slide 7.</div>

# %%


# %% [markdown]
<div style="background-color:#fff8e1; color:#3d2e00; border-left:6px solid #f9a825; padding:10px 14px; border-radius:4px;"><b>More in the notes:</b> two more exercises, "Move the origin" and "Walking together". Good practice for broadcasting and masking. See <a href="https://danielprecioso.com/Python-Course/modules/numpy/statistics.html#random-walk-simulation">Random walk simulation</a>.</div>

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
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slides 9 and 10.</div>

# %% [markdown]
1,000 walkers, 100 steps each, in `arr_walks`.

- Without running any code: shape of `arr_walks`?
- The final position of each walker. Plot its distribution.
- Average final position. Is it what you expected?
- Standard deviation of the final positions. How far can a walker get?

# %% [markdown]
<div style="background-color:#e3f2fd; color:#0d2b45; border-left:6px solid #1976d2; padding:10px 14px; border-radius:4px;"><b>Poll 5.</b> 1,000 walks of 100 steps, including the start. What is the shape of <code>arr_walks</code>?<br>A. (1000, 100)<br>B. (1000, 101)<br>C. (101, 1000)<br>D. (100, 1000)</div>

# %%


# %%


# %% [markdown]
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slide 11.</div>

# %% [markdown]
<div style="background-color:#e3f2fd; color:#0d2b45; border-left:6px solid #1976d2; padding:10px 14px; border-radius:4px;"><b>Poll 6.</b> What is the average final position of the 1,000 walkers?<br>A. About 0<br>B. About 10<br>C. About 50<br>D. About 100</div>

# %%


# %% [markdown]
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slide 12.</div>

# %% [markdown]
<div style="background-color:#e3f2fd; color:#0d2b45; border-left:6px solid #1976d2; padding:10px 14px; border-radius:4px;"><b>Poll 7.</b> And how far from 0 does a typical walker end up?<br>A. About 1<br>B. About 10<br>C. About 50<br>D. About 100</div>

# %%


# %% [markdown]
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slide 13.</div>

# %% [markdown]
### The normal distribution

- Does the histogram look familiar? Overlay the normal curve: `plot_normal=True`.
- Repeat with 10,000 steps. How does the standard deviation grow with the number of steps?

# %% [markdown]
<div style="background-color:#e8f5e9; color:#123d16; border-left:6px solid #2e7d32; padding:10px 14px; border-radius:4px;"><b>Slides:</b> go to slide 14.</div>

# %%


# %%


# %% [markdown]
<div style="background-color:#fff8e1; color:#3d2e00; border-left:6px solid #f9a825; padding:10px 14px; border-radius:4px;"><b>More in the notes:</b> sampling from a normal distribution with <code>np.random.normal()</code> (slide 15). See <a href="https://danielprecioso.com/Python-Course/modules/numpy/statistics.html#analysis-of-random-walk-distribution">Analysis of random walk distribution</a>.</div>

# %% [markdown]
## 7. Challenge: approximating π with Monte Carlo

Random points in the square $[-1, 1]^2$. The proportion inside the unit circle $x^2 + y^2 \leq 1$ is close to $\pi / 4$.

- Write `monte_carlo_pi(num_points)`. Hint: `np.random.uniform()`.
- Estimate $\pi$ with your own number of points and post it in the chat. Who gets closest?

# %%


# %% [markdown]
## Next session

A grayscale photo is a matrix of numbers, one per pixel. **Can we keep only a small fraction of those numbers and still recognise the photo?**
