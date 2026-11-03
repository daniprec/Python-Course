# %% [markdown]
# Session 2: Strings and Control Flow
## A maths party trick

1. Pick a number between 20 and 99.
2. Add its digits together.
3. Subtract that total from your original number.
4. Add the digits of the new number together.

Your answer is 9. Always.

**Can Python perform the trick, explain each step in a sentence, and check that the answer really is 9?**

# %%
my_number = 42

# %% [markdown]
## 1. Strings

- Store and print these four strings: `"This string is only text"`, `"This -string- has $pecial characters..."`, `"2.99"`, `'single quotes'`.
- Is `"2.99"` a number? What do `"3" + "2"` and `3 + 2` give?
- A string over two lines needs triple quotes `"""`. Are the spaces at the start of the second line kept?

# %%

# %%

# %%

# %% [markdown]
- Fix this code.

```python
long_string = "Why is this
      not working?!"
print(long_string)
```

# %%

# %% [markdown]
### Operations with strings

- `"Hello" + "World"`: how do you get the space in between?
- Predict: `2 + "3"`.
- `4 * "Hello"`. Now with a space between the words.

# %%

# %%

# %%

# %% [markdown]
## 2. f-strings

- Store your favourite number in `fav_num` and print `My favorite number is ...` with an f-string.
- `f"Louis is {23} years old."`: what can go inside the braces? Try `{23 / 7}` dog years.
- Remove the decimals with `{23 / 7:.0f}`. What does `.2f` do?

# %%

# %%

# %%

# %% [markdown]
### Exercise: Dog years

Print `NAME is X dog years old.`, where `X` is the age divided by 7, with no decimals. Then change `name` to `"Tina"` and run again.

# %%
name = "Michael"
age = 54

# %%

# %% [markdown]
### Exercise: Fill the braces

1. The cube root of 23, with three decimals.
2. Fix: `print(f"There are {365/7 weeks in a year")`
3. Complete: `print(f"The area of a square with side 5 cm is {} cm squared.")`

# %%

# %%

# %%

# %% [markdown]
### Exercise: The party trick

Use `my_number`. Print one sentence per step of the trick, with the value of that step. Hint: the tens digit is `my_number // 10`, the units digit is `my_number % 10`.

# %%

# %% [markdown]
## 3. String methods

- `s = "Hello world"`. Try `.upper()`, `.lower()`, `.capitalize()`, `.swapcase()`, `.title()`.
- After `s.upper()`, what is stored in `s`?
- Replace `"world"` with `"amigo"`. Replace only the first two `"foo"` in `"foo bar foo baz foo qux"`.
- How many times does `"pizza"` appear in `"pizza pizza pizza"`?

# %%

# %%

# %%

# %%

# %% [markdown]
- Does `"football"` start with `"foot"`? End with `"ball"`?
- `s = "I am Daniel and I am your teacher"`. Where is the first `"am"`? The last one? And `"Waldo"`?
- Clean `"  hey you  "` and `"eeeeeeh Macarena"`. Split `"How are you doing today?"` into words.
- Predict the difference between `s.upper().replace("false", "true")` and `s.replace("false", "true").upper()` for `s = "This statement is false."`.

# %%

# %%

# %%

# %%

# %% [markdown]
## 4. Indexing and slicing

Indices start at `0`.

- The first, the eighth and the last characters of `text`. The second to last?
- What happens with `text[5.0]`? And `text[20]`?

# %%
text = "Hello, World!"

# %%

# %%

# %% [markdown]
- Extract `"Hello"` and `"World"` with `text[start:end]`. Is `end` included?
- `"World"` again, with negative indices.
- Every second character. The whole string reversed.
- Predict before running: `text[7:][2]` and `text[2][7:]`.

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Digits

`digits = "123456789"`. With one slice each: the odd digits, the even digits, the digits backwards, the last three digits.

# %%

# %% [markdown]
## 5. Comparisons

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `<`, `>` | less, greater than |
| `<=`, `>=` | less, greater than or equal to |

- `x = 3`, `y = 2`. Are they equal? Different? Is `x > y`? What type is the answer?
- `3 == 3.0`? `3 == "3"`? `3 > "2"`?
- `"hi" == "HI"`? Is `"hello" > "hola"`? Why?
- Store whether `temperature = 38` is a fever (38 or more) in a variable `fever`.

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Security check

The secret code is `"Python"`. Compare it with the attempts `"Python"`, `"python"` and `"Python "`. Why does only one match?

# %%

# %% [markdown]
## 6. Making decisions: `if`, `else`, `elif`

```python
if <condition>:
    <runs only if the condition is True>
<always runs>
```

- `time_on_phone = 20`. Print a warning if it is more than 15. Then try `10`.
- Change any number below 5 into 5.
- Print `I am X years old` only if `years` is positive.

# %%

# %%

# %%

# %% [markdown]
- **Battery warning**: if `battery` is 20 or less, print `Low battery: return to base`. Always print `Status check complete` afterwards. Try `15` and `80`.
- **Even or odd**: one message or the other, with `else`.
- **Locked door**: `has_key` is `True` or `False`. Print `The door opens` or `The door is locked`.

# %%

# %%

# %%

# %% [markdown]
### Predict, run, fix

```python
x = 4
if x >= 0:
print(f"The square root of {x} is {x ** 0.5}")
```

```python
x = 4
if x % 2 = 0
    x = x ** 2
```

```python
name = "Alberto"
if "a" in name:
    print("The name contains the letter a")
else:
    print("The name does not contain the letter a")
```

# %%

# %%

# %% [markdown]
### More than two options: `elif`

- Positive, negative or zero?
- Which branch can never run? Fix the order.

```python
if x > 10:
    print("greater than 10")
elif x > 0:
    print("positive")
elif x < 0:
    print("negative")
elif x < -5:
    print("lower than -5")
else:
    print("zero")
```

# %%

# %%

# %% [markdown]
### Exercise: Theme-park ticket

Free under 4, €8 from 4 to 12, €15 from 13 to 64, €10 from 65. Store the price in `price`. Test one age per category.

# %%

# %% [markdown]
### Exercise: A piecewise function

$$
f(x) =
\begin{cases}
x^2, & x < 0, \\
2x + 1, & 0 \leq x < 3, \\
7, & x \geq 3.
\end{cases}
$$

Test $x = -2$, $x = 1$, $x = 5$. What happens at $x = 3$?

# %%

# %% [markdown]
### Exercise: Check the trick

Back to the hook. Print `The trick works` if the final answer is 9, and `The trick fails` otherwise. Try `my_number = 20`, `57`, `99`. And `100`? And `15`?

# %%

# %% [markdown]
## 7. `and`, `or`, `not`

- A student passes with a grade of at least 5 **and** an attendance of at least 80%. Try `grade = 8`, `attendance = 89`.
- Write the same rule with `or`, printing the failing message first.
- Add a full stop to `s = "Hello world"` only if it does not already end with one.

# %%

# %%

# %%

# %% [markdown]
### Exercises

1. **Cat or dog**: replace `cat` with `dog` in a sentence, only if it contains both `love` and `cat`.
2. **Spacecraft launch**: launch only if `fuel` is at least 80, `weather` is `"clear"` and `crew_ready` is `True`.
3. **Quadrants**: given `x` and `y`, print the quadrant, or `The point is on an axis`.
4. **Treasure chest** (one `if` inside another): `has_key` opens the chest; then the treasure goes in only if `inventory_space > 0`. Print `The chest is locked`, `Your inventory is full` or `Treasure collected!`.

# %%

# %%

# %%

# %%

# %% [markdown]
## 8. Challenge: delivery drone

Rules, in this order:

1. If the weather is `"storm"`: `Flight cancelled: storm`.
2. Otherwise, battery below 20: `Recharge required`.
3. Otherwise, distance over 10 needs at least 60 battery; distance of 10 or less needs at least 30: `Delivery approved`.
4. Else: `Insufficient battery for this distance`.

Make every message appear at least once.

# %%
distance = 8
battery = 65
weather = "clear"

# %%

# %% [markdown]
## Next session

You have to open 100 drawers to find your keys. **Do we write `print("Opening drawer ...")` 100 times?**
