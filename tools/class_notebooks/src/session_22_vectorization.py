# %% [markdown]
# Session 22: Vectorization
## A loop in disguise

A weather station stores one million temperatures in Celsius. We need them in Fahrenheit: $F = 1.8\,C + 32$.

Below is the loop that does it. It works.

**Can the loop disappear? And how do we recognize a loop that can?**

# %%
import numpy as np

rng = np.random.default_rng(0)
celsius = rng.uniform(-10, 40, size=1_000_000)

# %% [markdown]
- Convert with a loop. How long does it take? Hint: `%%time` at the top of the cell.
- Convert without a loop. Same result? Hint: `np.allclose()`. How long now?
- What did the loop do with each element? Did one iteration need any other?

# %%

# %%

# %% [markdown]
Today: a loop is a pattern. Learn to recognize it, and the replacement is almost always one line.

| The loop... | The replacement |
|---|---|
| works on each element on its own | arithmetic on the array |
| has an `if` inside | a mask, or `np.where()` (section 4) |
| accumulates (sum, count, running total) | `.sum()`, `.mean()`, `.cumsum()` with an `axis` |
| is a `while` that searches | `np.argmax()` on a Boolean array |
| calls a function that fails on arrays | a mask, or `np.vectorize()` |
| is nested (every row with every column) | broadcasting |

## 1. Element by element: just arithmetic

- A function with only arithmetic inside: does it need any change to accept an array?

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
## 2. A loop that accumulates: reductions and `axis`

- A shopping cart: `total += price * quantity` in a loop. Then without it. Hint: element-wise product and `.sum()`.
- How many `scores` are at least 50? Loop with a counter, then a Boolean array and `.sum()`.
- What fraction of them? Hint: `.mean()` of a Boolean array.
- Average of every student (rows) and of every exam (columns) in `grades`. Hint: `axis`.
- The running total of `steps`: a loop with `total += s`, then `np.cumsum()`.
- One Boolean from many: does **everyone** pass? Did **anyone** get 100? Hint: `.all()`, `.any()`.

# %%
prices = np.array([2.5, 4.0, 1.2, 10.0])
quantities = np.array([4, 1, 10, 2])
scores = np.array([38, 47, 62, 95, 99, 71, 44])
grades = np.array([[60, 70, 80], [40, 90, 50], [100, 30, 70], [55, 65, 75]])
steps = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: The Best Day

`sales` has the sales of 4 weeks (rows) over 7 days (columns, Monday to Sunday).

- Total of every week.
- Total of every weekday over the 4 weeks.
- Which weekday sells the most? Hint: `np.argmax()`.

# %%
sales = np.array([[5, 3, 4, 6, 9, 12, 2],
                  [4, 2, 5, 7, 8, 11, 3],
                  [6, 3, 3, 5, 10, 13, 1],
                  [5, 4, 4, 6, 9, 10, 2]])

# %%

# %% [markdown]
## 3. A `while` that searches: `np.argmax()`

Starting at index `0`, add the `steps` one by one **until the total reaches 20**. How many steps does it take?

- Write it with a `while` loop.
- `np.cumsum(steps) >= 20` is a Boolean array. Where is the first `True`? Hint: `np.argmax()`.
- What does `np.argmax()` return when there is no `True` at all? Try the threshold 100. How do we protect against it? Hint: `.any()`.
- First day of `temps` above 35.
- Does every `while` become a one-liner? Think of a loop where step $i$ needs the result of step $i-1$.

# %%
temps = np.array([31, 33, 34, 36, 38, 30])

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: The First Negative Balance

`changes` holds the monthly changes of a bank account that starts at `0`. In which month does the balance first go below `0`? If it never does, print a message.

# %%
changes = np.array([200, -150, 100, -250, 300])

# %%

# %% [markdown]
## 4. A loop with an `if`: masks (review)

Predict, run, fix.

```python
arr = np.array([1, 2, 3, 4, 5])
if arr > 0:
    print("positive")
```

- Why can `if` not use an array of Booleans? What do we use instead?
- The element-wise "not": `not mask` fails. What works?
- Values of `arr` greater than 2: with a loop, then with a mask.
- In `grid`, replace every `0` with `2`.
- Add 1 to every odd number of `numbers`, so it becomes the closest even.
- Every price above 100 gets a 10% discount. With a mask, then with `np.where(condition, if_true, if_false)`. Which one do we prefer?

# %%
arr = np.array([1, 2, 3, 4, 5])
grid = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
numbers = np.array([1, 2, 3, 4, 5, 6, 7])
prices = np.array([50, 120, 80, 200, 99.0])

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Curve the Grades

Rewrite without a loop.

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

Hint: two masks, or `np.where()`, or `np.clip()`.

# %%

# %%

# %% [markdown]
## 5. Functions that do not broadcast

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
## 6. Challenge: A nested loop

Every point with every other point: `distances[i, j]` is the absolute difference between `points[i]` and `points[j]`.

```python
distances = np.zeros((len(points), len(points)))
for i in range(len(points)):
    for j in range(len(points)):
        distances[i, j] = abs(points[i] - points[j])
```

Rewrite without loops. Hint: shapes `(4, 1)` and `(1, 4)`.

Then, a multiplication table of the numbers 1 to 9, in one line.

# %%
points = np.array([1, 4, 9, 16])

# %%

# %% [markdown]
## Next session

Review and homework: a random student, a random exercise from the NumPy problem set. **Could you solve and explain any of them at the board?**

In the course notes, as extension: the Monty Hall simulation at full speed, and more masking practice (Masking: Avoiding Loops).
