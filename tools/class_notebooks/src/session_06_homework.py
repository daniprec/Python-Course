# %% [markdown]
# Session 6: Homework Review
## Who goes to the board?

Review session for Module 1. Students come to the board, one at a time, and solve a homework exercise they have not seen in class: [Python Fundamentals homework](https://danielprecioso.com/Python-Course/modules/python-fundamentals/homework_fundamentals.html).

**Can you explain every line of your code?**

How to use this notebook:

1. Run the cell with the exercises.
2. Type the names of the students present in `students`, and run it.
3. Run the draw cell once per turn: it picks a student and an exercise, and removes both from the lists.
4. Add each mark (0 to 10) to `scores`. The last cell gives the class average.

Rerun steps 1 and 2 to start again.

# %%
import random

# %%
# Homework exercises without a solution on the website
exercises = [
    "Polynomial Operation",
    "Simplified Polynomial Operation",
    "Trigonometric Angle Formatter",
    "Character Replacement",
    "Substring Detection",
    "Angle Quadrant Checker",
    "Fraction Formatter",
    "Quadratic Equation Solver",
    "Pythagorean Triple Checker",
    "Palindrome Checker (Advanced)",
    "Reversed Number",
    # "Prime Number Checker",  # Done in class
    "Perfect Number Checker",
    "Largest Prime Factor",
    # "Sum of Divisors",  # Part of Amicable Numbers
    "Amicable Numbers",
    "Digital Root",
    "Number of Collatz Steps",
    "Happy Numbers",
]

# %%
students = []

# %%
# Draw one student and one exercise
if students and exercises:
    student = random.choice(students)
    students.remove(student)
    exercise = random.choice(exercises)
    exercises.remove(exercise)
    print(f"{student}: {exercise}")
else:
    print("No students or exercises left.")

# %%
scores = []

# %%
if scores:
    print(f"{len(scores)} presentations, average {sum(scores) / len(scores):.2f}")

# %% [markdown]
## Next session

A class has 30 students, each with a grade. **Do we need 30 variables?**
