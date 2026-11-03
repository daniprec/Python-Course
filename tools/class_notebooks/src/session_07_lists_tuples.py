# %% [markdown]
# Session 7: Lists and Tuples
## A reading tracker

You keep track of the books you want to read. Today there are three. Tomorrow you buy a fourth, next week you finish one, and you like to see them in alphabetical order.

Your train ticket is different: passenger, destination and departure time. Nobody should change it by accident.

**How do we store a collection that changes, and one that must not?**

# %%
book_1 = "Beloved"
book_2 = "Dune"
book_3 = "The Hobbit"

# %% [markdown]
- With what we know: one variable per book. Add a fourth? Print them in order? How many are there?

# %%

# %% [markdown]
**Can we do better?**

# %% [markdown]
## 1. Creating lists

- The three books in one variable. Type?
- Can a list mix types? A name, an age and a boolean.
- A weekly schedule: one list of subjects per day. How many brackets?
- Anything can go in a list. Even `print`?

# %%

# %%

# %%

# %%

# %% [markdown]
## 2. Indexing and slicing

Lists are **ordered**, like strings.

- First fruit? Second? Last?
- The fruits from position 1 to 3. The first two. From position 3 to the end.
- The first subject of Tuesday. The first letter of the second fruit.

# %%
fruits = ["apple", "banana", "cherry", "pineapple", "watermelon"]

weekly_schedule = [
    ["Python", "Design"],
    ["Economics", "Writing"],
    ["Statistics", "Python"],
]

# %%

# %%

# %%

# %% [markdown]
### Exercise: Predict the output

Write the three lines it prints before running it.

```python
shows = ["Severance", "The Bear", "Andor", "Arcane"]

print(shows[0])
print(shows[-2])
print(shows[1:3])
```

# %%

# %% [markdown]
## 3. Mutable, with duplicates

- Replace the first fruit with `"orange"`. Can we do the same with the first letter of a string?
- `x[0] = "hello"` runs without error. What can `x` be?
- Can a list hold the same value twice?

```python
name = "adolfo"
name[0] = "A"
```

# %%

# %%

# %%

# %% [markdown]
### Operations with lists

- Join the morning and the afternoon tasks with `+`.
- Add `"study"` to the tasks. Predict first:

```python
tasks = ["check email", "attend class"]
tasks = tasks + "study"
```

- `["work", "break"] * 3`? And the matrix below times 2: is it $2M$?
- `len()` of the schedule? Of Monday?

# %%
morning_tasks = ["check email", "attend class"]
afternoon_tasks = ["study", "go to the gym"]

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Conference schedule

Print the number of days, the number of sessions on day 2, and the first session of day 2.

# %%
schedule = [
    ["Opening", "Data Ethics", "Networking"],
    ["Python Lab", "Career Panel", "Closing"],
]

# %%

# %% [markdown]
## 4. List methods

Most list methods change the list **in place**.

- Add a track at the end. Add two tracks. Insert one at position 1.
- `append(["A", "B"])` vs `extend(["A", "B"])`?
- Remove `"Leo"`. Which one goes? Cancel the guest in position 1 and keep their name. Clear the list.
- Where is the first `"maybe"`? How many `"yes"`?
- Sort the cities. Reverse them. Sort the animals by their last letter (`key=`).

# %%
playlist = ["Intro", "Night Drive"]
guests = ["Ava", "Leo", "Nora", "Leo"]
responses = ["yes", "no", "yes", "maybe", "yes"]
cities = ["Tokyo", "Lima", "Berlin", "Accra"]
animals = ["Dog", "Cat", "Bird", "Horse"]

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Build a watchlist

Add `"Arrival"` at the end, `"Spirited Away"` at the beginning, then `"Moonlight"` and `"Dune"` in one operation.

# %%
watchlist = ["Past Lives", "The Matrix"]

# %%

# %% [markdown]
### Exercise: Sort by length

Sort the podcasts from shortest to longest title. Hint: `key=len`.

# %%
podcasts = ["Radiolab", "Today Explained", "Serial", "99% Invisible"]

# %%

# %% [markdown]
### Exercise: Fix the program

Two destinations should be added separately. Fix one line.

```python
destinations = ["Lisbon", "Seoul"]
destinations.append(["Cairo", "Oslo"])
```

# %%

# %% [markdown]
## 5. Tuples

- The days of the week as a tuple. Type? Compare with a list.
- Which of these are tuples? Predict, then check.

```python
a = ("weekend")
b = ("weekend",)
c = "weekend",
d = ["weekend"]
```

- First and last weekday. Monday to Wednesday.
- Make Monday a Sunday. Predict first:

```python
weekdays[0] = "Sunday"
```

# %%
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# %%

# %%

# %%

# %% [markdown]
### Operations and methods

- Join the two tuples. Repeat `"stand up"` three times. Length? Is `"class"` in the plan?
- Which list methods are left for a tuple?

# %%
morning = ("coffee", "email")
afternoon = ("class", "study")

# %%

# %%

# %% [markdown]
### Exercise: Analyze a vote

Number of votes for `"film"`. Position of the first vote for `"games"`.

# %%
votes = ("music", "film", "games", "film", "film", "music")

# %%

# %% [markdown]
## 6. Packing and unpacking

- Pack the passenger, destination and time of the train ticket in one tuple.
- Unpack it into three variables. What if we use two variables?
- What does a function with `return a, b` return?

# %%

# %%

# %%

# %% [markdown]
### Exercise: Unpack a media record

Unpack into `title`, `creator`, `year` and print: `Spirited Away was created by Hayao Miyazaki in 2001.`

# %%
film = ("Spirited Away", "Hayao Miyazaki", 2001)

# %%

# %% [markdown]
### Exercise: Fix the itinerary

Replace `"Rome"` with `"Florence"`. Hint: `list()` and `tuple()`.

# %%
itinerary = ("Milan", "Rome", "Venice")

# %%

# %% [markdown]
### Exercise: Event summary

A function `event_summary()` that receives an event and a city and returns both in title case.

```python
event, city = event_summary("design week", "barcelona")
```

# %%

# %% [markdown]
## 7. Challenge

| | Syntax | Ordered | Mutable | Duplicates |
|---|---|---|---|---|
| List | `[]` | ? | ? | ? |
| Tuple | `()` | ? | ? | ? |

### Reading tracker

Back to the hook. Start with three books, add a fourth, remove one finished book and keep its title in `finished_book`, sort the rest. Print the finished book, the list and how many books are left.

# %%

# %% [markdown]
### Library record

A tuple `book` with a title, an author and a year. Unpack it, print a sentence, print its length, check whether the author is in it.

# %%

# %% [markdown]
## Next session

A workshop scans every student at the door. Some students scan twice. **Who came on Monday, and who came both days?**
