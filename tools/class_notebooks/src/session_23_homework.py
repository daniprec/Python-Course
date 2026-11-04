# %% [markdown]
# Session 23: Homework Review

Exercises from [Problem Set 3: NumPy](https://daniprec.github.io/Python-Course/modules/numpy/homework_numpy.html). The mandatory ones (red boxes) were done in class and are commented out.

1. Fill in `ls_students`.
2. Run the assignment cell: a random student gets a random exercise.
3. The student solves it at the board and explains the code.
4. Add the score to `scores`. Repeat from step 2.

# %%
import random

import numpy as np

# %%
ls_exercises = [
    # Introduction to NumPy
    "Shadowing the NumPy Alias",
    "Replacing a Sum Loop",
    "Array Dimensions",
    "Image Shape",
    "Empty Arrays",
    "Array-Creation Debugging",
    "Battleship",
    # "Holiday Lights",  # Done in class
    # Array Arithmetic and Broadcasting
    "Matrix Multiplication",
    "Assigning One Value to a Row",
    "Fixing Vector Addition",
    "Broadcasting a Row Vector",
    "Incompatible Shapes",
    "Row and Column Assignment",
    "Final Grades with Any Weights",
    "Factorial, Revisited",
    "Polynomial Operation, Revisited",
    # "Sum Square Difference",  # Done in class
    # "Distinct Powers",  # Done in class
    # Loading and Saving Data
    "Text and Binary Formats",
    "Join Daily Recordings",
    # Array Manipulation
    "Exam Versions",
    "Joining Two Vectors",
    "Predicting a Reshape",
    "Vertical Stacking",
    "Sliding Windows",
    "reshape() Does Not Modify in Place",
    "Fibonacci Array Debugging",
    "Concatenating an Empty Array",
    "Points per Part",
    # "Largest Product in a Series",  # Done in class
    # Masking
    "Mask Length",
    "Filtering Values",
    "Selecting Even Values",
    "Replacing Selected Values",
    "Selecting Odd Values",
    "Combining Two Conditions",
    "Mixed Data Types",
    "Three Ways to Select Positions",
    "Bonus Points",
    "Character Replacement, Revisited",
    "Prime Number Checker, Revisited",
    "Amicable Numbers, Revisited",
    # "Sieve of Eratosthenes",  # Done in class
    # "Goldbach's Conjecture",  # Done in class
    # Random Numbers and Fancy Indexing
    "A 50% Event",
    "Simulating Dice Rolls",
    "Replacing the First and Last Values",
    "Repeated Fancy Indices",
    "Correcting Row and Column Indices",
    "Extracting a Diagonal",
    "Reversing an Array",
    "Top-Left Subarray",
    "Random Seeds and Reassignment",
    "Monty Hall Columns",
    "Passing by Guessing",
    "Encrypted Code, Revisited",
    # "Secret Santa",  # Done in class
    # Statistics and Simulation
    "Row Means",
    "Means Along Every Axis",
    "Normalizing a Vector",
    "Accumulation or One Final Total?",
    "Exercise Report",
    "Bus Lines, Revisited",
    # "Dice Duel",  # Done in class
    # Linear Algebra
    "A Matrix Times Its Inverse",
    "Finding Eigenvalues",
    "Recover the Weights",
    # "Fibonacci with Matrices",  # Done in class
    # Vectorization
    "Element-Wise Comparison",
    "Broadcasting a Column and a Row",
    "Broadcasting Failure",
    "Vectorize the Grader",
    "Pythagorean Triples, Revisited",
    # "Low Points",  # Done in class
]

# %%
ls_students = []

# %%
if ls_students and ls_exercises:
    # Pick a random student and remove them from the list
    student = random.choice(ls_students)
    ls_students.remove(student)
    print(student)

    # Pick a random exercise and remove it from the list
    exercise = random.choice(ls_exercises)
    ls_exercises.remove(exercise)
    print(exercise)
else:
    print("No students or exercises left.")

# %%
scores = []

if scores:
    print(np.mean(scores))
