# %% [markdown]
# Session 9: Dictionaries
## Nora's score

Three students and their scores are stored in two lists. The order of one list matches the order of the other.

**Print Nora's score without using a position such as `scores[1]`.**

# %%
students = ["Leo", "Nora", "Maya"]
scores = [80, 95, 75]

# %% [markdown]
- With what we know: find Nora's position first.
- A new student joins between Leo and Nora. What breaks?

# %%

# %%

# %% [markdown]
**Can we look a value up by its name instead of by its position?**

# %% [markdown]
## 1. Creating dictionaries

- The three scores as `key: value` pairs. Type? Nora's score?
- An empty dictionary. And an empty set?
- Is this a set or a dictionary?

```python
{1, 2, 3, "four": 4}
```

# %%

# %%

# %%

# %% [markdown]
### Exercise: Gamer profile

Store a profile: username `pixel_panda`, level `12`, online `True`.

# %%

# %% [markdown]
### Exercise: Set or dictionary?

Store the unique genres of a playlist, and then the minutes per genre: pop 18, rock 12, jazz 7.

# %%

# %% [markdown]
## 2. Keys and values

Keys: unique and immutable. Values: anything.

- A course with a title, a number of students, a boolean, a list of topics and a room tuple.
- A variable as a key.
- Classrooms by `(day, time)`. And with a list as key? Predict first.
- The same key twice: which value stays? The same value twice?

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: An order

Store this order: 2 tacos, 1 ramen, 2 lemonades. Which are the keys?

# %%

# %% [markdown]
## 3. Accessing values

- The name and the age.
- Predict first. Dictionaries keep insertion order, so is there a position `0`?

```python
person[0]
```

- Keys `3`, `4`, `5`: what is `numbers[3]`? And `numbers[0]`?
- The email? With `get()`? With a default message?

# %%
person = {
    "name": "John",
    "age": 25,
    "city": "New York",
}

numbers = {
    3: "three",
    4: "four",
    5: "five",
}

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Read a record

Print the title and the year of the book. How much do three student tickets cost?

# %%
book = {
    "title": "Kindred",
    "author": "Octavia Butler",
    "year": 1979,
}

ticket_prices = {"adult": 12, "student": 8, "child": 6}

# %%

# %%

# %% [markdown]
### Exercise: Translate

Translate `"fire"` and `"unicorn"` to Spanish. Print `"?"` when a word is missing.

# %%
spanish = {"fire": "fuego", "love": "amor", "laugh": "risa"}

# %%

# %% [markdown]
## 4. Mutable

- Somebody listens to `"The Lion King"`: one more play. A new song gets its first play.
- Can we add an item to a list the same way? Predict first:

```python
numbers_list = [0, 1, 2, 3]
numbers_list[4] = 4
```

- Count one play of `"Bad Guy"`, which is not there yet. Hint: `get()` with a default.
- Remove a song with `del`. Remove one with `pop()` and keep its plays.

# %%
plays = {
    "Bohemian Rhapsody": 1000,
    "The Lion King": 500,
}

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Update an event

Change the venue to `"Main Hall"`, add `"sold_out": False`, remove the dress code.

# %%
event = {
    "name": "Data Night",
    "venue": "Room 2",
    "dress_code": "Casual",
}

# %%

# %% [markdown]
### Exercise: Leaderboard

Maya scores 40 more points. Alex joins with 75. Remove Leo and keep his points.

# %%
leaderboard = {"Maya": 120, "Leo": 95}

# %%

# %% [markdown]
## 5. Membership and views

- Is `"name"` in `person`? Is `"John"`? How do we find `"John"`?
- The keys, the values and the items of the product. Type of each?
- Lower the price to `69.99` and add a colour, in one call. Hint: `update()`.
- Loop over the product. What do we get? And over `.items()`?

# %%
product = {
    "name": "Headphones",
    "price": 79.99,
    "stock": 14,
}

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Predict the output

```python
settings = {"theme": "dark", "language": "English", "notifications": True}

print("theme" in settings)
print("dark" in settings)
print("dark" in settings.values())
```

# %%

# %% [markdown]
### Exercise: Open the gate

Print `Gate opened!` only if the inventory contains a gold key.

# %%
inventory = {"torch": 1, "gold key": 1, "potion": 3}

# %%

# %% [markdown]
### Exercise: Display a profile

Print each pair as `username: maya_21`, one per line. Then the total views of the videos.

# %%
profile = {
    "username": "maya_21",
    "level": 8,
    "premium": True,
}

views = {"dance": 1500, "recipe": 2300, "challenge": 1800}

# %%

# %%

# %% [markdown]
## 6. Nested dictionaries

- Maya's name. Leo's grade.
- Change Maya's grade to `9.1`. Add `"graduated": False` to Leo's record.
- Pedri, from the second dictionary. What is `players["Barcelona"][2][3]`?

# %%
students = {
    "S001": {
        "name": "Maya",
        "programme": "Data Science",
        "grade": 8.7,
    },
    "S002": {
        "name": "Leo",
        "programme": "Economics",
        "grade": 7.9,
    },
}

players = {
    "Real Madrid": ["Courtois", "Mbappe", "Vinicius"],
    "Barcelona": ["Lamine", "Raphinha", "Pedri"],
}

# %%

# %%

# %%

# %% [markdown]
## 7. Converting to a dictionary

- A list of `(key, value)` tuples into a dictionary.
- Which structure does `.items()` give back?

# %%
pairs = [("name", "Pipo"), ("age", 10), ("city", "Seville")]

# %%

# %%

# %% [markdown]
### Exercise: Convert a menu

Convert the pairs into a dictionary. Price of the salad?

# %%
menu_pairs = [
    ("soup", 6.50),
    ("salad", 8.00),
    ("pasta", 12.50),
]

# %%

# %% [markdown]
## 8. Challenge

| | Syntax | Ordered | Mutable | Duplicates | Access |
|---|---|---|---|---|---|
| List | `[]` | Yes | Yes | Yes | Position |
| Tuple | `()` | Yes | No | Yes | Position |
| Set | `{a, b}`, `set()` | No | Yes | No | Membership |
| Dictionary | ? | ? | ? | ? | ? |

### Count words

A dictionary with the number of times each word appears: `{"python": 3, "data": 2, "model": 1}`.

# %%
words = ["python", "data", "python", "model", "data", "python"]

# %%

# %% [markdown]
### Design the data structure

A football tournament app stores: the registered teams, the players of each team, the goals of each player, the two teams of each match, and the teams each club has already faced. Which structure for each one? Why?

# %%

# %% [markdown]
## Next session

A class vote: `["Ava", "leo", "AVA", "Nora", "ava", "Leo"]`. **Who won?**
