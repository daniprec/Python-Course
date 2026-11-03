# %% [markdown]
# Session 10: Iterables and Mutability
## Who won the vote?

The class voted for a delegate. The names were typed by hand.

**Who won?**

# %%
votes = ["Ava", "leo", "AVA", "Nora", "ava", "Leo", "nora ", "Ava"]

# %% [markdown]
- Make all the votes lowercase. Predict first:

```python
votes.lower()
```

- A loop that prints each vote in lowercase. Has `votes` changed?
- Store them instead of printing them. Predict first:

```python
for vote in votes:
    votes.append(vote.lower())
```

# %%

# %%

# %% [markdown]
**How do we build a new structure while we loop over another one?**

# %% [markdown]
## 1. Looping through structures

- Print each song. Then a ranking that starts at 1. Hint: `enumerate()`.
- Print each fruit with its number of letters: `apple has 5 letters.`
- Print each coordinate of the point.
- Unpack the three names into three variables. With two variables?

# %%
playlist = ["Espresso", "APT.", "Birds of a Feather"]
fruits = ["apple", "banana", "cherry"]
point = (4, 7, 2)
names = ("Adam", "María", "Pablo")

# %%

# %%

# %%

# %%

# %% [markdown]
- Print each match as `Lions 2 - 1 Tigers`.
- One welcome message per attendee. In which order? What does `enumerate()` count here?
- The dishes. The prices. Each dish with its price.

# %%
matches = [("Lions", 2, 1, "Tigers"), ("Eagles", 0, 3, "Sharks")]
attendees = {"Maya", "Leo", "Nora"}
menu = {"tacos": 8, "ramen": 12, "pizza": 10}

# %%

# %%

# %%

# %% [markdown]
## 2. Building lists in a loop

Start empty, `append()` inside the loop.

- The first ten powers of 2, from $2^1$. With `for`. With `while`.
- The first 100 Fibonacci numbers.
- Back to the hook: a new list with the clean votes. Hint: `strip()`.

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Identity matrix

A function that returns the $n \times n$ identity matrix as a list of lists.

$$
I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

# %%

# %% [markdown]
## 3. Building dictionaries in a loop

- Back to the hook: count the clean votes. Who won?
- A dictionary that maps each student's name to their mark.

# %%
dict_ids = {
    "Allen": "789",
    "Damian": "123",
    "Ireena": "012",
    "Ludmilla": "456",
}

dict_marks = {
    "123": 45,
    "456": 97,
    "789": 64,
    "012": 56,
}

# %%

# %%

# %% [markdown]
### Exercise: Count football goals

`("Lions", "Tigers", 2, 1)` means Lions scored 2 and Tigers scored 1. A dictionary with the total goals of each team. A team may appear for the first time halfway through.

# %%
results = [
    ("Lions", "Tigers", 2, 1),
    ("Tigers", "Eagles", 0, 0),
    ("Eagles", "Lions", 3, 1),
    ("Lions", "Tigers", 1, 1),
]

# %%

# %% [markdown]
### Exercise: Clues by suspect

A dictionary from each suspect to the list of their clues. Which suspect has the most clues?

# %%
clues = [
    ("camera", "Mara"),
    ("fingerprint", "Leo"),
    ("receipt", "Mara"),
    ("message", "Nora"),
    ("witness statement", "Mara"),
    ("camera", "Leo"),
]

# %%

# %% [markdown]
## 4. List comprehensions

`[f(x) for x in A]` is $\{ f(x) : x \in A \}$. `[f(x) for x in A if p(x)]` is $\{ f(x) : x \in A,\ p(x) \}$.

- The squares of 0 to 9, with a loop and with a comprehension.
- The first ten even numbers.
- $f(x) = (-1)^x x^2$ for $x = 1, \dots, 10$.
- The temperatures in Fahrenheit: $F = C \cdot 9/5 + 32$.
- The clean votes of the hook, in one line.

# %%
celsius = [0, 10, 20, 30]

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Transform and filter

1. Rescale `data` linearly to $[0, 1]$.
2. The squares of the values of `numbers` above their mean.
3. The squares of the odd values of `numbers`.

# %%
data = [3.5, 7.2, 1.8, 5.0, 6.3]
numbers = [12, 5, 8, 21, 3, 17]

# %%

# %%

# %%

# %% [markdown]
## 5. `split()` and `join()`

- The message as a list of words. Join them back with hyphens.
- The acronym of `"north atlantic treaty organization"`.
- `",".join([1, 2, 3])`? How do we fix it?

# %%
message = "python makes data fun"

# %%

# %%

# %%

# %% [markdown]
### Exercise: Common words

Which words appear in both speeches? Hint: `split()` and sets.

# %%
speech_1 = "change requires courage and action"
speech_2 = "our action will create change"

# %%

# %% [markdown]
## 6. Functions can mutate their arguments

| Mutable | Immutable |
|---|---|
| list, dict, set | int, float, bool, str, tuple |

- `append()` vs `+`: what changes, what is returned? Predict first:

```python
my_list = [1, 2, 3]
my_list = my_list.append(4)
```

- `y = x`, then change `x`. Does `y` change? With integers? With lists?
- A function `add_guest()` that appends a name. What does it return? What happens to `guests`?
- The same with a set and with a dictionary.

# %%
guests = ["Maya", "Leo"]

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Mutation or rebinding?

Predict both outputs. Which function changes the original list?

```python
def mutate(items: list):
    items.append("new")


def rebind(items: list):
    items = items + ["new"]


a = ["old"]
b = ["old"]
mutate(a)
rebind(b)
print(a, b)
```

# %%

# %% [markdown]
## 7. Protecting mutable objects

- A function that returns the list with a new item and leaves the original unchanged. Hint: `copy()`.
- Copy the playlist, change the title of the copy, add a song to the copy. What changed in the original?
- Repeat so the original stays unchanged. Hint: `from copy import deepcopy`.

# %%
study_playlist = {"title": "Study", "songs": ["Lofi 1", "Lofi 2"]}

# %%

# %%

# %%

# %% [markdown]
### Exercise: Protect the original set

Complete `add_tag_safely()` so it returns an updated set without changing `tags`.

```python
def add_tag_safely(tags: set, new_tag: str) -> set:
    ...
```

# %%

# %% [markdown]
## 8. Mutable default parameters

- Run both calls. Why does the second order contain pizza?

```python
def create_order(item: str, order: list = []):
    order.append(item)
    return order


print(create_order("pizza"))
print(create_order("tacos"))
```

- Repair `create_order()` with `None` as the default.

# %%

# %%

# %% [markdown]
### Exercise: Shared dictionary

How many keys does `animal_sounds` have at the end? Then fix `add_entry()`.

```python
def add_entry(key, value, records: dict = {}) -> dict:
    records[key] = value
    return records


clothes = add_entry("shirt", "blue")
clothes = add_entry("pants", "green", clothes)

animal_sounds = add_entry("dog", "woof")
animal_sounds = add_entry("cat", "meow", animal_sounds)
```

# %%

# %% [markdown]
## 9. Challenge

### Notification preferences

A function `enable_notification(name, preferences)`. `preferences` is an optional set; if missing, create a new one. Separate calls without a set must not share data.

# %%

# %% [markdown]
### Top chart

A string with one line per artist, from most to least played: `1. Taylor Swift (1250M plays)`. Hint: `sort()` with `key=`, `enumerate()`, `join()`.

# %%
artists = [
    ["Taylor Swift", 1250],
    ["Bad Bunny", 980],
    ["Drake", 1120],
    ["The Weeknd", 890],
    ["Central Cee", 650],
    ["Rosalia", 1030],
    ["Billie Eilish", 720],
    ["JID", 540],
    ["Quevedo", 25],
    ["Kendrick Lamar", 800],
]

# %%

# %% [markdown]
## Next session

Code written by an AI runs without errors and gives plausible numbers. **Is it correct?**
