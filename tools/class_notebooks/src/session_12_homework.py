# %% [markdown]
# Session 12: Homework Review
## Explain your code

The exercises below are the mandatory Module 2 homework exercises, the red boxes of the [homework page](https://daniprec.github.io/Python-Course/modules/structures/homework_structures.html). Each round, a random student is assigned a random exercise and solves it on the projector, explaining every line.

**Can you explain your code to the class?**

1. Run the first two cells.
2. Type the students present today in `ls_students`.
3. Run the draw cell once per round. A student and an exercise leave their lists once drawn.
4. After each round, append the score to `scores`.

# %%
import random

ls_exercises = [
    "Function as a List Transformer",
    "Sort Bus Lines by Mean Time",
    "Sort Tuples by Age",
    "Class Sets",
    "Second Largest Distinct Number",
    "Find Pairs with a Target Sum",
    "Encrypted Code",
    "Student Gradebook",
    "Word Frequency Counter",
    "Merge Dictionaries",
]

# %%
ls_students = []
scores = []

# %%
if ls_students and ls_exercises:
    student = random.choice(ls_students)
    ls_students.remove(student)
    exercise = random.choice(ls_exercises)
    ls_exercises.remove(exercise)
    print(student, "->", exercise)
else:
    print("No students or exercises left.")

# %%

# %%

# %%
if scores:
    print(f"Mean score: {sum(scores) / len(scores):.2f} ({len(scores)} rounds)")

# %% [markdown]
## Next session

Module 3 starts. **How do we grade a whole class at once, without a single loop?**
