# %% [markdown]
# Session 14: Introduction to NumPy
## Grading the midterm

You are the professor. The midterm had 11 exercises:

| Exercises | Type | Points each |
|---|---|---|
| 1-2 | Open problems | 20 |
| 3-5 | Debugging | 10 |
| 6-11 | Multiple choice | 5 |

Each exercise is marked from `0` to `1`. One row per student, one column per exercise.

**How do we ask this table for one student, one exercise, or a block of both?**

# %%
students = ["Alice", "Bruno", "Chloe", "Diego", "Emma", "Farid"]

marks_list = [
    [0.75, 1, 0.5, 1, 0.5, 1, 1, 0, 1, 1, 1],  # Alice
    [0.5, 0.25, 1, 0.5, 0, 1, 0, 1, 1, 0, 1],  # Bruno
    [1, 1, 1, 1, 0.5, 1, 1, 1, 0, 1, 1],  # Chloe
    [0.25, 0.5, 0, 0.5, 0.5, 0, 1, 0, 1, 0, 1],  # Diego
    [1, 0.75, 0.5, 1, 1, 1, 0, 1, 1, 1, 1],  # Emma
    [0.5, 0.5, 0.5, 0, 1, 1, 1, 0, 0, 1, 0],  # Farid
]

# %% [markdown]
## 1. With what we know

- All the marks of Alice?
- How did the class do in **exercise 4**?
- The open problems (exercises 1 and 2) of Bruno, Chloe and Diego?
- Exercise 11 for the last three students?

# %%

# %%

# %%

# %%

# %% [markdown]
**Can we do better?**

# %% [markdown]
## 2. NumPy

- What do we need to import?

# %%

# %% [markdown]
## 3. Creating arrays

- Turn the points of each exercise into an array.
- Turn Alice's marks (a tuple) into an array.

# %%
weights_list = [20, 20, 10, 10, 10, 5, 5, 5, 5, 5, 5]
alice_tuple = (0.75, 1, 0.5, 1, 0.5, 1, 1, 0, 1, 1, 1)

# %%

# %% [markdown]
- What if the student IDs come in a set?

# %%
ids_set = {101, 102, 103}

# %% [markdown]
- Diego's debugging marks are `0`, `0.5`, `0.5`. What happens with `np.array(0, 0.5, 0.5)`?

# %%

# %% [markdown]
### Data types

- We typed `1` and `0`. Why does NumPy print `1.` and `0.`?
- Multiple choice is only `0` or `1`. Debugging can be `0.5`. Which type does each array get?

# %%
chloe_mc = [1, 1, 1, 0, 1, 1]
chloe_debugging = [1, 1, 0.5]

# %%

# %%

# %% [markdown]
- Why not put the names inside the table?
- You cannot read Farid's answer to exercise 2 and type `"?"`. What happens?
- Can we force the type?

# %%
farid_list = [0.5, "?", 0.5, 0]

# %%

# %%

# %%

# %% [markdown]
### More dimensions

- One student is 1D. The whole class?
- What if we forget one of Diego's marks?

# %%
broken_list = [
    [0.75, 1, 0.5, 1, 0.5, 1, 1, 0, 1, 1, 1],
    [0.25, 0.5, 0, 0.5, 0.5, 0, 1, 0, 1, 0],  # Diego: only 10 marks
]

# %%

# %%

# %% [markdown]
- Two campuses (Madrid, Segovia), two students each, two open problems. How many brackets?

| | Student 1 | Student 2 |
|---|---|---|
| Madrid | 0.75, 1 | 0.5, 0.25 |
| Segovia | 1, 0.5 | 0.25, 0.75 |

# %%

# %% [markdown]
## 4. Describing an array

- How many dimensions? How many rows and columns? How many marks? Which type?
- Which number of the shape must `weights` match?
- A late student and a bonus exercise 12: new shape and size?
- And the two campuses?

# %%

# %%

# %%

# %% [markdown]
## 5. Arrays without typing them

- An empty table for the other group: 30 students, 11 exercises.
- A perfect exam.
- The exercise numbers, 1 to 11.
- The rubric of the open problems: `0, 0.25, 0.5, 0.75, 1`.

# %%

# %%

# %%

# %%

# %% [markdown]
- Version A goes to odd seats. The room has 30 seats.
- The debugging rubric: `0, 0.5, 1`. With `linspace`? With `arange`?

# %%

# %%

# %% [markdown]
## 6. Indexing: one mark

- The value of exercise 1? Alice's mark in exercise 4?
- Chloe's whole exam? Chloe in exercise 5?
- Diego in exercise 1, without counting rows?

# %%

# %%

# %%

# %% [markdown]
- What is `marks[-1, 0]`?
- Does `marks_list[2, 4]` work?
- Two exam versions stored in a list. What is `versions[1][0, 2]`?

# %%
version_A_list = [[1, 0.5, 0], [0.25, 1, 1]]
version_B_list = [[0.75, 0, 1], [1, 0.5, 0.5]]

# %%

# %%

# %%

# %% [markdown]
## 7. Changing values: arrays are mutable

- Diego asks for a revision: exercise 3 goes up to `0.5`.
- Emma asks for a revision: exercise 2 deserves full marks.

# %%

# %%

# %% [markdown]
### The type does not change

- Diego's debugging marks, typed on their own. Which type? Give him `0.5` in the first one.
- How do we fix it?
- Type `"?"` for Farid's exercise 2 in `marks`. What happens? Compare with Farid's `"?"` at creation.

# %%
diego_debugging_list = [0, 1, 0]

# %%

# %%

# %%

# %% [markdown]
### Two names, one array

- `first_student = draft[0]`. Change one of its marks. What happens to `draft`?
- How do we keep `draft` untouched?

# %%
draft_list = [[1, 0.5, 0], [0.25, 1, 1]]

# %%

# %%

# %% [markdown]
### Exercise: The Backup

Without running it, what does this print? Then fix it: `original` keeps the old marks, and the partial credit is stored.

```python
bruno_mc = np.array([1, 0, 1, 1])
original = bruno_mc

bruno_mc[1] = 1     # question 2 was right after all
bruno_mc[2] = 0.75  # partial credit in question 3

print(original)
```

# %%

# %% [markdown]
## 8. Slicing: rows, columns, blocks

- The three parts of the exam, in `weights`.
- Exercise 4 for the whole class. Bruno's whole exam.
- Back to the beginning: open problems of Bruno, Chloe and Diego.

# %%

# %%

# %%

# %% [markdown]
- Version A sat in odd seats (every other student, starting with Alice).
- The pile of exams, last delivered on top.
- Version B: Bruno, Diego, Farid.
- Exercise 1 for Farid, Emma and Diego, in that order.
- What does `marks[::2, 5:]` select? Which shape?

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
- A machine grades the multiple choice. Fill an empty table for 3 students.

# %%
first_student = [1, 0.5, 1, 0.5, 1, 1, 0, 1, 1, 1, 1]
mc_machine = [
    [1, 1, 0, 1, 1, 0],  # second student
    [0, 1, 1, 1, 0, 1],  # third student
]

# %%

# %%

# %% [markdown]
## 9. Challenge: Madrid and Segovia

Dimensions: **campus**, **student**, **exercise**.

1. Shape, dimensions, size. What does each number mean?
2. The second student of Segovia.
3. Multiple choice (exercises 6-11) of everyone in Madrid.
4. Exercise 1 for everyone, both campuses. Shape?
5. Fourth student of Madrid: exercise 2 deserves a `1`.
6. Open problems of the first two students of each campus.

# %%
exam_list = [
    [
        [1, 0.75, 1, 0.5, 1, 1, 1, 0, 1, 1, 1],  # Madrid
        [0.25, 0.5, 0.5, 0, 0.5, 1, 0, 0, 1, 1, 0],
        [0.75, 0.75, 1, 1, 0.5, 0, 1, 1, 1, 0, 1],
        [0.5, 0, 0, 0.5, 1, 1, 1, 1, 0, 1, 1],
    ],
    [
        [0.5, 1, 0.5, 1, 1, 1, 1, 1, 1, 0, 1],  # Segovia
        [1, 1, 1, 0.5, 1, 1, 0, 1, 1, 1, 1],
        [0, 0.25, 0.5, 0.5, 0, 0, 1, 0, 1, 0, 0],
        [0.75, 0.5, 1, 1, 0.5, 1, 1, 0, 0, 1, 1],
    ],
]

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
## 10. Extra: an image is also an array

`0` is black, `1` is white.

# %%
import matplotlib.pyplot as plt
import numpy as np


def show(image):
    """Display a 2D array as a grayscale image (0 = black, 1 = white)."""
    plt.imshow(image, cmap="gray", vmin=0, vmax=1)
    plt.axis("off")
    plt.show()

# %%
smiley = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
)

# %% [markdown]
- Show `smiley`. What is its shape?

# %%

# %% [markdown]
- Draw a face on an 8x8 black canvas: two eyes and a smile.
- Upside down? Mirrored?
- A chessboard with only two assignments.

# %%

# %%

# %%

# %% [markdown]
## Next session

We have the marks and the points of each exercise. **What is the final grade of each student?**

