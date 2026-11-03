# %% [markdown]
# Session 1: Introduction to Python
## Saving money

You put 10,000 euros in a bank account that pays 5% interest per year. At the end of every year, the interest is added to the account.

**How much money will you have after 10 years? After how many years will you have doubled it?**

By the end of this session, Python will answer both questions for you.

# %% [markdown]
## 1. Hello, world!

- Click the cell below and type `print("Hello, world!")`. Run it with `Shift` + `Enter` (or the play button on the left).

# %%

# %% [markdown]
- Change the message so that Python says hello to you, not to the world.
- Print your favourite food.
- Print two messages, one per line. How many cells do you need?

# %%

# %%

# %%

# %% [markdown]
## 2. Comments

- Run a cell that contains only `# Hello`. What happens?
- Write `print("Hello, world!")  # My first line of code`. Is the comment printed?
- And `print("Hello # world")`? Why is this `#` different?

# %%

# %%

# %%

# %% [markdown]
## 3. Debugging

Making mistakes is normal. Read the error message: it tells you what went wrong and where.

Each line has a bug. Type it, run it, read the error, fix it.

```python
print("Hello, world!)
```

```python
print("Hello, world!"
```

```python
Print("Hello, world!")
```

# %%

# %%

# %%

# %% [markdown]
## 4. Python as a calculator

- Compute `5 + 8 + 3`. Does `5+8+3` also work? Which one is easier to read?
- Try every operator with `5` and `2`:

| Operation | Symbol |
|---|---|
| Sum | `+` |
| Subtraction | `-` |
| Multiplication | `*` |
| Division | `/` |
| Exponentiation | `**` |
| Quotient | `//` |
| Remainder | `%` |

# %%

# %%

# %%

# %% [markdown]
- What is the difference between `5 / 2` and `5 // 2`?
- Use `%` to decide whether `2026` is even. And `2027`?
- Is `2 + 3 * 4` equal to `20` or to `14`? How do you get the other one?

# %%

# %%

# %%

# %% [markdown]
### Exercise: Compound interest

Back to the bank. After one year you have $10000 \cdot 1.05$; after two years, $10000 \cdot 1.05 \cdot 1.05$.

1. How much do you have after 1, 2 and 3 years?
2. After 10 years? Hint: `**`.
3. After how many years do you double your money? Try a few values.

# %%

# %%

# %%

# %% [markdown]
### Exercise: Celsius to Fahrenheit

$C = (F - 32) \cdot 5 / 9$. It is 32 degrees Celsius in Madrid. How many degrees Fahrenheit is that?

# %%

# %% [markdown]
### Exercise: Square root

This line should compute $\sqrt{4}$. It runs, but the answer is wrong. Why? Fix it.

```python
print(4 ** 1/2)
```

# %%

# %% [markdown]
## 5. Variables

- Store `4` in `x` and `9` in `y`. Print them.
- Predict the output of `print("x")`: `x`, `4`, or an error?
- Print `x = 4` using the variable: `print("x =", x)`.

# %%

# %%

# %%

# %% [markdown]
- $f(x) = a \cdot x + b$ with $a = 2$ and $b = 3$. Compute $f(4)$ with variables `a`, `b`, `x` and `y`.
- Now $f(10)$. Which line do you change?
- Store `10` in `x` again. What does `print(x)` show now?

# %%

# %%

# %%

# %% [markdown]
- Variables can store text too: `message = "I love pizza"`. Print it.
- Which names work? Predict, then try.

```python
message_2 = "I love salad too"
2nd_message = "bla bla bla"
my message = "hello"
```

- What happens if you print a variable that does not exist?

```python
q = 8
p = q * t
```

# %%

# %%

# %%

# %% [markdown]
### Exercise: Compound interest with variables

1. Store the initial money, the interest rate and the number of years in three variables.
2. Compute the final amount using only the variables.
3. Change the rate to 3%. How much do you have after 10 years? How many years to double it now?

# %%

# %%

# %% [markdown]
### Exercise: A messy formula

With $x = 1/2$, compute

$$y = \sqrt{\frac{3x - 1}{x^3}}$$

Hint: brackets, and the square root from section 4.

# %%

# %% [markdown]
## Next session

Your name is a variable too: `name = "Daniel"`. **How do we write "Hello, Daniel!" for any name, take its first letter, and let Python decide what to say?**
