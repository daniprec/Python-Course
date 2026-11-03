# %% [markdown]
# Session 3: Loops
[Slides](https://docs.google.com/presentation/d/1fqrnB94OHVW3pIVe59A_3SMny-to2GCF/edit?usp=sharing&ouid=112793419067458804625&rtpof=true&sd=true)

## Where are my keys?

You lost your keys. They are in one of the drawers of your desk. You open the drawers one by one, and you stop as soon as you find them.

**How do we tell Python to repeat "open the next drawer" until the keys appear?**

# %%
drawers = ["notebooks", "cables", "keys", "old photos"]

# %% [markdown]
- With what we know: print `Opening drawer 1`, `Opening drawer 2`, `Opening drawer 3`.

# %%

# %% [markdown]
**And with 100 drawers?**

# %% [markdown]
## 1. Your first `for` loop

```python
for <element> in <sequence>:
    <code>
```

- Open drawers 1 to 3 with `for drawer_number in range(1, 4)`. Then 1 to 100.
- What do the colon and the indentation do? Remove them and run.
- Predict the output, then run it.

```python
for level in range(1, 4):
    print("Starting level", level)
    print("Ready!")

print("Game finished")
```

# %%

# %%

# %%

# %% [markdown]
### `range()`

- Print `range(1, 6)`, `range(5)` and `range(1, 11, 3)` with a loop. Which numbers are included?
- Count backwards from 5 to 1.
- What does `range(10, 0)` give? Why?

# %%

# %%

# %%

# %% [markdown]
### Exercise: Rocket launch

A countdown from 10 to 1, then `Lift-off!` once.

# %%

# %% [markdown]
### Exercise: Character levels

Level `level` requires `level ** 2 * 100` XP. Print `Level 1 requires 100 XP`, and so on up to level 10.

# %%

# %% [markdown]
## 2. Looping through sequences

- Loop over the string `"Python"`: print `Give me a P!`, `Give me a y!`...
- A list: `planets = ["Mercury", "Venus", "Earth", "Mars"]`. Print `Visiting` and each planet.
- Loop over our `drawers`. Print `Checking` and the contents.
- `for num in [1, 2, 3, 4, 5]: print("I do not care about the number")`. How many lines?

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Roll call

A list with four names. Print `Welcome, Ada!` for each one.

# %%

# %% [markdown]
## 3. Updating variables in a loop

- Build one sentence from `["Hello", "my", "name", "is", "Daniel"]`. Start from `sentence = ""`. Print `sentence` inside the loop: what do you see?
- Add the spaces.
- Add the numbers from 1 to 5. Print the running total at every step.

# %%

# %%

# %%

# %% [markdown]
### Exercise: Boss battle

The boss has `100` health points. You attack five times, `18` damage each. After every attack, print the attack number and the boss's health.

# %%

# %% [markdown]
### Exercise: Gauss and the factorial

1. Add all the numbers from 1 to 100. Check with $\frac{n(n+1)}{2}$.
2. $5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1$. Compute the factorial of any `num`. Where do you start: at `0` or at `1`?
3. What is $20!$? How many digits?

# %%

# %%

# %%

# %% [markdown]
## 4. Decisions inside loops

- For each number in `[-2, -1, 0, 1, 2]`, print whether it is negative, or zero or positive.
- **Alien detector**: scan rooms 1 to 20. Print `Scanning room N`, but if `N` is divisible by 7, print `Warning: alien detected in room N` instead.
- **Factors**: all the factors of `52`. And of `360`? How many are there?

# %%

# %%

# %%

# %% [markdown]
## 5. Nested loops

- Search each piece of furniture in `["desk", "wardrobe", "bedside table"]`, and open drawers 1 to 3 in each. How many drawers in total?
- Predict, then run:

```python
for number in range(3):
    for letter in ["a", "b", "c"]:
        print(number, letter)
```

# %%

# %%

# %% [markdown]
### Exercise: Treasure map

Four rows, five columns. Print `Searching position ROW COL` for every position. At row 3, column 4, also print `Treasure found!`.

# %%

# %% [markdown]
### Exercise: Cinema seats

Three rows, four seats each. Print `Row 2, seat 3` and so on. Which loop is the rows? How many labels before you run?

# %%

# %% [markdown]
### Exercise: Multiplication tables

Print the multiplication tables of 1 to 9: `3 x 4 = 12`.

# %%

# %% [markdown]
## 6. `break` and `continue`

- Back to the hook: open our `drawers` until you find the keys. Is `old photos` checked?
- Print the numbers in `range(10)`, but print `Stop!` and stop when the number is above 5.
- In a nested loop, does `break` stop both loops? Try it with the numbers and letters above.

# %%

# %%

# %%

# %% [markdown]
### Exercise: Reaching a threshold

Add the numbers of `[1, 3, 4, 5, 7, 9]` until the sum reaches `10` or more. Print the sum and the number where you stopped.

# %%

# %% [markdown]
### Predict, run, fix

```python
# Multiply odd numbers until the result is higher than n
n = 1000
result = 0

for i in range(n):
    if i % 2 == 1:
        result = result * i
    if result > n:
        break

print(result)
```

# %%

# %% [markdown]
### `continue`

- Print `num x 2 = ...` for the numbers 0 to 4, skipping 2.
- Predict which numbers are printed:

```python
for n in range(1, 10):
    sqn = n ** (1 / 2)
    if sqn % 1 == 0:
        continue
    print(n)
```

# %%

# %%

# %% [markdown]
## 7. `while` loops

```python
while <condition>:
    <code>
```

- Count from 1 to 5 with `while`. What happens if you forget `num = num + 1`? (Stop the cell with the stop button.)
- The threshold exercise again, with `while`.

# %%

# %%

# %% [markdown]
### For or while?

1. The sum of the first 50 even numbers.
2. The first 20 terms of the Fibonacci sequence.
3. The first Fibonacci number higher than 999.
4. The multiples of 5 between 1 and 100.
5. The first 10 prime numbers.
6. Divide a number by 2 until the result is less than 1.
7. Sum the digits of a number until the result has one digit.
8. The first 15 square numbers.

Code numbers 3 and 6.

# %%

# %%

# %% [markdown]
### Why do these loops never end?

```python
i = 1
while i != 0:
    i += 1
```

```python
n = 2
while n % 2 == 0:
    n = n * 2
```

```python
i = 1
while i > 0:
    i = i // 2
    i += 1
```

# %% [markdown]
## 8. Challenge

1. **Staircase**: for `height = 5`, print `#`, `##`, ..., `#####`. Hint: `"#" * 3`.
2. **FizzBuzz**: the numbers 1 to 30, but `Fizz` for multiples of 3, `Buzz` for multiples of 5, `FizzBuzz` for both. Does the order of your conditions matter?
3. **Doubling, revisited**: 10,000 euros at 5% per year. With a `while` loop, after how many years do you have at least 20,000? And at 3%?

# %%

# %%

# %%

# %% [markdown]
## Next session

You wrote the factorial loop for `5`. Now you need it for `10`, `20` and `100`, in different parts of your program. **Do we copy and paste the loop every time?**
