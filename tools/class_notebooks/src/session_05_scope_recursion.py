# %% [markdown]
# Session 5: Scope, Recursion and Docstrings
[Slides](https://docs.google.com/presentation/d/13jwQaj-3BOn6TYnKjrvq2L2Hpx6TsmHa/edit?usp=sharing&ouid=112793419067458804625&rtpof=true&sd=true)

## The end of the world

In a temple there are three towers, **A**, **B** and **C**. Tower A holds 64 golden disks, from the largest at the bottom to the smallest at the top. Monks move the disks to tower C, one disk per second, and never put a larger disk on top of a smaller one. When they finish, the world ends.

**How long do we have left?**

# %%
n_disks = 64
seconds_per_year = 60 * 60 * 24 * 365

# %% [markdown]
- With 1 disk, how many moves? With 2? With 3? Draw it.

# %% [markdown]
## 1. Variables inside functions

- `double(num)` creates `x = 2` and returns `x * num`. Call it with `8`. Then `print(num)` and `print(x)`. What happens?
- `greet(name)` stores the message in `msg` and prints it. Can you print `msg` outside the function?
- `g = 9.81` outside any function. Can `weight(mass)` use `g` inside?

# %%

# %%

# %%

# %% [markdown]
### Local, enclosing, global, built-in

| Scope | Where |
|---|---|
| **L**ocal | inside the current function |
| **E**nclosing | inside a surrounding function |
| **G**lobal | at the top level of the notebook |
| **B**uilt-in | `print`, `len`, `range` |

- Predict the result and the final value of `x`:

```python
x = 5

def modify_variable(y):
    x = 10
    return y + x

result = modify_variable(7)
print(result)
print(x)
```

# %%

# %% [markdown]
### Names that clash

Predict, run, fix.

```python
def square_root(x):
    return x ** (1 / 2)

square_root = square_root(16)
print(square_root(9))
```

```python
print = "Hello!"
print(print)
```

To repair the second one, restart the session.

# %%

# %%

# %% [markdown]
## 2. `return` inside `if` and `for`

- `check_even(number)`: `return True` inside an `if`, and `return False` after it. Do we need the `else`?
- `find_element(sequence, target)`: `True` if `target` is in `sequence`. Try `5` and `8` in `[1, 2, 3, 4, 5, 6]`. When does the loop stop?

# %%

# %%

# %% [markdown]
### Exercise: Prime numbers

1. `is_prime(number)`: `False` as soon as you find a divisor, `True` if the loop ends.
2. Test `3`, `11`, `4`. And `1`, `0`, `-7`? Fix it.
3. Is `2027` prime? Which year is the next prime?

# %%

# %%

# %%

# %% [markdown]
## 3. Functions inside functions

- `closest_lower_prime(number)`: the largest prime strictly below `number`. Use `is_prime`. Try `12`, `22` and `100`.
- `closest_lower_prime_list(numbers)`: prints the closest lower prime of every number in `[5, 136, 782]`.

# %%

# %%

# %% [markdown]
## 4. Recursion

A function that calls itself needs a **base case** (stop) and a **recursive case** (a smaller problem).

- $n! = n \cdot (n - 1)!$. Predict, run, fix:

```python
def factorial(num):
    return num * factorial(num - 1)

print(factorial(5))
```

- Trace `factorial(4)` by hand: which calls happen, and in which order do they return?

# %%

# %%

# %% [markdown]
### Exercise: Fibonacci

$F(0) = 0$, $F(1) = 1$, $F(n) = F(n-1) + F(n-2)$.

1. Recursive `fibonacci(n)`. Check `fibonacci(6)` is `8`.
2. How long does `fibonacci(30)` take? And `35`? Why?

# %%

# %%

# %% [markdown]
### Exercise: Tower of Hanoi

To move $n$ disks from A to C: move $n - 1$ disks from A to B, move the largest disk to C, move the $n - 1$ disks from B to C.

1. `hanoi(n, source, target, auxiliary)` prints every move. Try `hanoi(3, "A", "C", "B")`.
2. Count the moves for $n = 1, \dots, 6$. Guess the formula.
3. Back to the hook: with 64 disks, how many years do we have left?

# %%

# %%

# %%

# %% [markdown]
## 5. Generators

`yield` gives back a value and **pauses** the function.

- `generate_even_numbers(limit)` yields `0, 2, 4, ...` below `limit`. Print what you get when you call it. Type? Can you add `3` to it?
- Get the values with a `for` loop. Then with `next()`, one at a time.
- Replace `yield` with `return`. What changes?

# %%

# %%

# %%

# %% [markdown]
### Exercise: Fibonacci generator

A generator that yields the Fibonacci numbers one by one. Print the first 20. Then find the first one above 999.

# %%

# %% [markdown]
## 6. Docstrings and type hints

```python
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b
```

- Add a docstring to `greet(name)`. Hover over `greet` in Colab: what do you see?
- Add type hints to `add`. Does `add("3", "4")` fail? Does Python check the hints?
- `check_pass(name: str, grade: float) -> str`, with a docstring with `Parameters` and `Returns`.

# %%

# %%

# %%

# %% [markdown]
### Exercise: Document your work

Add docstrings and type hints to `is_prime`, `closest_lower_prime` and `hanoi`. From now on, every function you write has them.

# %%

# %% [markdown]
## Next session

Review session: you present your homework at the board. **Can you explain every line of your code?**
