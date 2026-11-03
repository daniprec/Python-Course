# %% [markdown]
# Session 8: Sets
## Two days of check-ins

A workshop records every scan at the door. Some students scan more than once. We do not care about the order of the scans, only about who came.

**Who came on Monday? Who came both days? Who came only on Monday? Who came at least once?**

# %%
monday_check_ins = ["Ava", "Leo", "Ava", "Nora", "Omar", "Leo"]
tuesday_check_ins = ["Leo", "Sara", "Omar", "Sara", "Iris"]

# %% [markdown]
- With what we know: a function that checks with a loop whether a name is in a list.
- Is `"Ava"` in the Monday list? Is there a shorter way?
- Who came on Monday, without repetitions?

# %%

# %%

# %%

# %% [markdown]
**Can we do better?**

# %% [markdown]
## 1. Creating sets

- Monday's unique attendees with `set()`. Print it twice. Compare with the list.
- A set of numbers with curly brackets. Type? Order?
- An empty set. What is `{}`?

# %%

# %%

# %%

# %% [markdown]
## 2. What can go inside a set?

- Strings, numbers, tuples of seats. Mixed types?
- How many items in `{True, False, 1, 0, True}`? Why?
- Which of these can belong to a set? Predict, then check.

```python
42
"Madrid"
(3, 5)
[3, 5]
```

- A set of lists? A list of sets?

# %%

# %%

# %%

# %%

# %% [markdown]
## 3. Properties of sets

### Unordered

- The first color? Predict first:

```python
colors = {"blue", "green", "red"}
colors[0]
```

- Is `"green"` in the set? Is `"pink"`?

# %%

# %%

# %% [markdown]
### Exercise: Check membership

Is `"Python"` in the completed courses? And `"Design"`?

# %%
completed_courses = {"Python", "Economics", "Statistics"}

# %%

# %% [markdown]
### Mutable, no duplicates

- Add `"Sam"`. Remove `"Leo"`. Remove `"Alex"`: `remove()` vs `discard()`?
- How many votes in `{"film", "film", "music", "games", "music"}`?
- `{"Hello", "hello", "World"}`: how many items?

# %%
attendees = {"Maya", "Leo", "Nora"}

# %%

# %%

# %%

# %% [markdown]
### Exercise: Remove duplicate usernames

Convert the list to a set. Compare the lengths.

# %%
usernames = ["alex", "maya", "alex", "sam", "maya"]

# %%

# %% [markdown]
## 4. Operations with sets

| Mathematics | Python | Operator |
|---|---|---|
| $A \cup B$ | `A.union(B)` | <code>A &#124; B</code> |
| $A \cap B$ | `A.intersection(B)` | `A & B` |
| $A \setminus B$ | `A.difference(B)` | `A - B` |
| $A \,\triangle\, B$ | `A.symmetric_difference(B)` | `A ^ B` |

- Every member of either club. Members of both.
- Film-only members. Book-only members. Does the order matter?
- Members of exactly one club.
- Check $|A \cup B| = |A| + |B| - |A \cap B|$.

# %%
film_club = {"Ava", "Leo", "Nora", "Sam"}
book_club = {"Nora", "Sam", "Iris", "Omar"}

# %%

# %%

# %%

# %%

# %% [markdown]
### Exercise: Predict the result

Write the content of each result before running it.

```python
streaming_a = {"Arrival", "Dune", "Moonlight"}
streaming_b = {"Dune", "Past Lives", "Moonlight"}

available_anywhere = streaming_a | streaming_b
available_on_both = streaming_a & streaming_b
only_on_a = streaming_a - streaming_b
```

# %%

# %% [markdown]
### Back to the check-ins

One set expression per question: Monday's unique attendees, both days, only Monday, at least one day, exactly one day.

# %%

# %%

# %% [markdown]
## 5. Practice

### Exercise: Party invitations

Three friends propose guests. Find every proposed guest, the guests proposed by all three, and the guests proposed only by friend 1, only by friend 2, only by friend 3.

# %%
friend_1 = {"Alice", "Emma", "Charlie", "David", "Louis"}
friend_2 = {"Charlie", "David", "Emma", "Frank", "Juan"}
friend_3 = {"David", "Emma", "Alice", "Helen", "Julia"}

# %%

# %%

# %%

# %% [markdown]
### Exercise: Case-insensitive comparison

The code finds no common words. Fix it so capitalization does not matter. Hint: build a lowercase set from each one.

```python
common_words = set_1 & set_2
```

# %%
set_1 = {"TABle", "DOOR", "chain", "wire"}
set_2 = {"pencil", "door", "taBle", "word"}

# %%

# %% [markdown]
## 6. Converting lists, tuples and sets

- `list()`, `tuple()`, `set()` on the list below. Types? Lengths?
- Back to a list: is the original order restored?

# %%
number_list = [1, 2, 2, 3]

# %%

# %%

# %% [markdown]
### Exercise: Choose a movie

A function `choose_movies()` that returns the movies accepted by all four friends.

# %%
friend_1 = ["Inception", "The Matrix", "Interstellar", "Avatar"]
friend_2 = ["The Godfather", "Interstellar", "Titanic", "Arrival"]
friend_3 = ["Interstellar", "Toy Story", "Arrival", "The Dark Knight"]
friend_4 = ["Interstellar", "Star Wars", "Arrival", "The Avengers"]

# %%

# %% [markdown]
### Exercise: Collect every proposal

A function `collect_movies()` that returns a list with every proposed movie, without duplicates.

# %%

# %% [markdown]
## 7. Challenge: choose the structure

| | Syntax | Ordered | Mutable | Duplicates |
|---|---|---|---|---|
| List | `[]` | Yes | Yes | Yes |
| Tuple | `()` | Yes | No | Yes |
| Set | ? | ? | ? | ? |

List, tuple or set? Why?

1. Songs in a playlist.
2. The RGB values of a brand color.
3. Student IDs that entered a building today.
4. Stops along a bus route.
5. Countries represented at an event.

### Exercise: Hiking trip

A group leader checks the route, the summit and the equipment.

- Route: Trailhead, Lake, Summit, Lake, Trailhead
- Summit checkpoint: Summit, 40.426, -3.714
- Required: water, map, jacket, first aid kit
- Packed: water, jacket, snack

1. Store each piece of information with the right structure.
2. The required items that are missing. The packed items that were not required.
3. Pack the map. What is missing now?

# %%

# %%

# %%

# %% [markdown]
## Next session

A set tells us who came. **How many times did each student come?** Ava 3, Leo 2, Nora 1: which structure would you use?
