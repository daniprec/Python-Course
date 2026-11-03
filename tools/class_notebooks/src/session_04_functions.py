# %% [markdown]
# Session 4: Functions
[Slides](https://docs.google.com/presentation/d/1-61OlUNDBjW_2vNQ1_-jdvyWb4Oh03ke/edit?usp=sharing&ouid=112793419067458804625&rtpof=true&sd=true)

## Did Leia pass?

The grades arrive from an online form. The form sends everything as text. The pass mark is `5`.

**Did Leia pass? And how do we write that check once, and reuse it for Luke, Yoda and every other student?**

# %%
name = "Leia"
grade_text = "6.5"

# %% [markdown]
- With what we know: `if grade_text >= 5`.

# %%

# %% [markdown]
## 1. Built-in functions: `type()`

$z = f(x, y) = x + y$: a function takes inputs and gives an output. `print()` is one.

- What is the type of `10`, `2.72`, `"Hello world"`, `False`? And of `print`?
- What is the type of `grade_text`? Is that why the hook failed?
- Predict, then run:

```python
x = "10"
y = 10
print(type(x))
print(type(y))
```

# %%

# %%

# %%

# %% [markdown]
## 2. Changing the type: `int()`, `float()`, `round()`, `abs()`

- `x = "12"`. What is `x * 2`? Convert it with `int()` and try again.
- `x = 5.9999`. Compare `int(x)`, `f"{x:.0f}"` and `round(x, 0)`. And `int(-5.9)`?
- `int("Hello")`? `int("3.14")`? `int(3.14)`?

# %%

# %%

# %%

# %% [markdown]
- Which lines work? Predict, then try.

```python
float("4.5")
float("4")
float("four")
float("4,5")
float("5 / 2")
```

- Round `price = 19.987` to 2, 1 and 0 decimals.
- It was `3` degrees in the morning and `-4` at night. How big was the change?
- Back to the hook: did Leia pass?

# %%

# %%

# %%

# %%

# %% [markdown]
## 3. `str()`, `len()` and combining functions

- `age = 25`. Build `"I am 25 years old"` with `+`. Why do you need `str()`? And with an f-string?
- `len("a b")`? Do spaces count?
- How many digits does `90000012345` have? Hint: two functions, one inside the other.
- Predict, then run:

```python
x = "100"
print(type(x))
print(type(int(x)))
print(int(x) + 50)
```

# %%

# %%

# %%

# %%

# %% [markdown]
## 4. Asking the user: `input()`

- Ask the user for their name and greet them.
- Ask for a number. What type is it? Print whether it is even or odd.
- What prints if the user types `5`? `x = int(input("Give me a number: "))`, then `print(x * 8)`.

# %%

# %%

# %%

# %% [markdown]
### Exercises

1. **Calculator**: ask for two numbers. Print their sum, difference, product and division.
2. **Restaurant bill**: ask for the price of a meal and the tip percentage. Print the tip and the total.
3. **Three password attempts**: the password is `python`. Print `Access granted` and stop, or `Incorrect password`.

# %%

# %%

# %%

# %% [markdown]
## 5. Defining our own functions

```python
def <function_name>(<argument>):
    <code>
```

- Define `greet(name)`, which prints `Hello, NAME!`. Does defining it print anything?
- Call it with `"Jorge"`, `"Ana"`, `"Luis"`.
- Write `say_goodbye(name)`.

# %%

# %%

# %%

# %% [markdown]
### Exercises

1. `multiplication_table(x)`: prints `x x 1 = ...` up to `x x 10`. Try 3 and 8.
2. `countdown(number)`: prints from `number` down to `1`.

# %%

# %%

# %% [markdown]
## 6. Several arguments

- Write `check_pass(name, grade)`: prints `NAME has passed!` or `NAME has failed`. Try Luke (8), Yoda (2), Leia (6).
- What happens with `check_pass(6, "Leia")`?
- Predict:

```python
def describe_pet(name, animal):
    print(f"{name} is a {animal}")

describe_pet("Nina", "cat")
describe_pet("dog", "Rex")
```

- Make `check_pass` print a warning and stop when `name` is not a string or `grade` is not a number. Hint: `type()` and `return`.

# %%

# %%

# %%

# %%

# %% [markdown]
## 7. `print` or `return`?

- `add_print(a, b)` prints `a + b`. `add_return(a, b)` returns it. Store the result of each one in `result`. What is in `result`?
- Double the result of each one.
- `square_root(x)` with `return`. Compute $\sqrt{16}$ and $\sqrt{\sqrt{81}}$.

# %%

# %%

# %%

# %% [markdown]
### Exercises

1. `make_email(username, domain)`: returns `ana@university.edu`.
2. `is_even(number)`: returns `True` or `False`. Use it inside an `if`.
3. `distance_2d(x1, y1, x2, y2)`: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$. Is `distance_2d(1, 1, 2, 2)` equal to `distance_2d(2, 2, 1, 1)`?
4. `first_half(text)`: `first_half("python")` returns `"pyt"`.
5. `sum_of_squares(n)`: $1^2 + 2^2 + \dots + n^2$. Check $n = 4$ gives $30$.
6. Back to the last session: `factorial(n)`. Compute $10!$, $20!$, $100!$.

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
### Predict, run, fix

```python
def greet(name)
    print(f"Hello, {name}")
```

```python
def double(x):
    result = x * 2

print(result)
```

```python
def double(x):
    print(x * 2)

answer = double(5)
print(answer + 10)
```

# %%

# %%

# %%

# %% [markdown]
## 8. Keyword arguments and default values

- `greet(name, greeting="Hello")`. Call it with and without `greeting`.
- `root(x, n=2)`: $\sqrt[n]{x}$. Square root of 4, fourth root of 16.
- Does `root(n=4, 16)` work?
- Which keyword argument does `round()` have? Try `round(6.78)`.

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Discount

`apply_discount(price, discount=10)` returns the price after the discount. `apply_discount(100)` is `90`; `apply_discount(100, discount=25)` is `75`.

# %%

# %% [markdown]
### Exercise: Calculator

`calculator(num1, num2, operation="addition")`, with `"subtraction"`, `"multiplication"` and `"division"`. Then handle division by zero, unknown operations, and add `"power"`.

# %%

# %%

# %% [markdown]
### Exercise: Radioactive decay

$$N(t) = N_0 \cdot (1/2)^{t / T_h}$$

$N_0$ atoms at the start, half-life $T_h$.

1. `radioactive_decay(n0, half_life=5730, t=500)`.
2. **Carbon-14** (half-life 5730 years): 1000 atoms, how many after 2000 years?
3. **Uranium-238** (half-life 4.468 billion years): 100 atoms, how many after 1 billion years?
4. 5000 atoms, half-life 100 years: after 0, 50, 100 and 200 years.

# %%

# %%

# %%

# %% [markdown]
## Next session

```python
x = 3

def change_x():
    x = 4

change_x()
print(x)
```

**Is `x` 3 or 4? Why?**
