# %% [markdown]
# Session 11: Debugging Clinic
## Mostly correct code

An AI writes hundreds of lines in seconds. They run. The numbers look plausible. Your job is to spot the small mistake that changes the result.

Modules 1 and 2 only. No NumPy.

**The code runs. Is it correct?**

Work in pairs and swap roles after each exercise:

- **Domain expert:** states the expected behaviour and chooses edge cases.
- **Debugger:** traces the program and proposes the smallest fix.

For every exercise:

1. Predict: expected behaviour, smallest failing input, first variable to inspect.
2. Run the tests.
3. Bug report: observed, expected, smallest failing input, violated assumption, root cause.
4. Change the smallest amount of code.
5. Add one regression test.

No AI assistant until your pair has written its prediction and its smallest failing input.

Run the test helpers once. They report failures without stopping the notebook.

# %%
def check_equal(label, function, expected):
    """Run a zero-argument function and report whether it returns the expected value."""
    try:
        actual = function()
    except Exception as error:
        print(f"FAIL {label}: {type(error).__name__}: {error}")
        return False
    if actual == expected:
        print(f"PASS {label}: {actual!r}")
        return True
    print(f"FAIL {label}: expected {expected!r}, obtained {actual!r}")
    return False


def check_raises(label, function, error_type):
    """Run a zero-argument function and report whether it raises the expected exception."""
    try:
        function()
    except error_type:
        print(f"PASS {label}: raised {error_type.__name__}")
        return True
    except Exception as error:
        print(f"FAIL {label}: raised {type(error).__name__}, not {error_type.__name__}")
        return False
    print(f"FAIL {label}: no exception was raised")
    return False

# %% [markdown]
| Concepts | Exercises |
|---|---|
| Numbers, arithmetic and precedence | 1, 8 |
| Strings, slicing and conversion | 2, 4 |
| Conditionals and loops | 3, 6, 7 |
| Functions, returns, type hints and defaults | 1, 4, 7 |
| Lists, tuples, mutability and aliasing | 5 |
| Sets | 6 |
| Dictionaries | 7, 8 |
| Recursion and generators | 9 |

# %% [markdown]
## 1. A plausible discount

A 10% discount on 100 euros should return 90. The result is a plausible number, but wrong.

# %%
def apply_discount(price: float, discount: float = 0.10) -> float:
    return price * 1 - discount

# %%
check_equal("default discount", lambda: apply_discount(100), 90.0)
check_equal("custom discount", lambda: apply_discount(50, 0.15), 42.5)
check_equal("no discount", lambda: apply_discount(25, 0), 25)

# %% [markdown]
- Predict, bug report, minimal fix, regression test.

# %%

# %%

# %% [markdown]
## 2. The missing digit

`"The Office S02E12"` should become `("The Office", 2, 12)`. It works for single-digit episodes, so the bug survives ordinary testing.

# %%
def parse_episode(code: str) -> tuple:
    clean = code.strip().upper()
    s_position = clean.rfind("S")
    e_position = clean.find("E", s_position)

    name = clean[:s_position].strip().title()
    season = int(clean[s_position + 1 : e_position])
    episode = int(clean[e_position + 1])
    return name, season, episode

# %%
check_equal("single-digit episode", lambda: parse_episode("Friends S03E7"), ("Friends", 3, 7))
check_equal("two-digit episode", lambda: parse_episode("The Office S02E12"), ("The Office", 2, 12))
check_equal("surrounding spaces", lambda: parse_episode("  Dark S01E10  "), ("Dark", 1, 10))

# %% [markdown]
- Predict, bug report, minimal fix, regression test.

# %%

# %%

# %% [markdown]
## 3. A message frozen in time

The "take it or double it" game. The money returned is correct, but every message still offers 1 euro.

# %%
def simulate_offer(decisions: list[str]) -> tuple:
    value = 1
    messages = []
    message = f"I offer you {value} euros"

    for answer in decisions:
        messages.append(message)
        if answer.lower() == "take it":
            return value, messages
        elif answer.lower() == "double it":
            value *= 2

    return None, messages

# %%
decisions = ["double it", "double it", "take it"]
check_equal("value taken", lambda: simulate_offer(decisions)[0], 4)
check_equal(
    "offers shown",
    lambda: simulate_offer(decisions)[1],
    ["I offer you 1 euros", "I offer you 2 euros", "I offer you 4 euros"],
)

# %% [markdown]
- Predict, bug report, minimal fix, regression test.

# %%

# %%

# %% [markdown]
## 4. A type hint is not a conversion

A past-exam function: round a positive number without `round()`. The type hint says `str`, but the caller passes a float.

# %%
def custom_round(num: str) -> int:
    if "." in num:
        integer, decimals = num.split(".")
        if int(decimals[0]) >= 5:
            return int(integer) + 1
        return int(integer)
    return int(num)

# %%
check_equal("float below half", lambda: custom_round(3.14159), 3)
check_equal("string above half", lambda: custom_round("4.8"), 5)
check_equal("integer", lambda: custom_round(7), 7)

# %% [markdown]
- Predict, bug report, minimal fix, regression test.
- Fix the function or fix the caller?

# %%

# %%

# %% [markdown]
## 5. The tuple changed without changing

Return an updated roster without changing the original list. The list is also stored inside a tuple that represents a trip.

# %%
def add_traveller(roster: list[str], name: str) -> list[str]:
    updated = roster
    updated.append(name)
    return updated

# %%
def roster_example():
    """Build a roster and a trip, then add a traveller."""
    original = ["Ana", "Luis"]
    trip = (original, "Madrid")
    updated = add_traveller(original, "Eva")
    return original, updated, trip


check_equal("original list", lambda: roster_example()[0], ["Ana", "Luis"])
check_equal("updated list", lambda: roster_example()[1], ["Ana", "Luis", "Eva"])
check_equal("list inside tuple", lambda: roster_example()[2], (["Ana", "Luis"], "Madrid"))

# %% [markdown]
- Predict, bug report, minimal fix, regression test.
- Tuples are immutable. How did the trip change?

# %%

# %%

# %% [markdown]
## 6. Attendance without duplicates

Three sorted lists: attended and submitted, attended but did not submit, submitted but did not attend. No duplicate names.

# %%
def attendance_report(attended: list[str], submitted: list[str]) -> tuple:
    attended_set = set(attended)
    submitted_set = set(submitted)

    both = attended_set.union(submitted_set)
    no_submission = submitted_set.difference(attended_set)
    no_attendance = attended_set.difference(submitted_set)

    return sorted(both), sorted(no_submission), sorted(no_attendance)

# %%
attended = ["Ana", "Luis", "Ana", "Marta"]
submitted = ["Luis", "Eva", "Eva", "Ana"]

check_equal(
    "attendance report",
    lambda: attendance_report(attended, submitted),
    (["Ana", "Luis"], ["Marta"], ["Eva"]),
)

# %% [markdown]
- Predict, bug report, minimal fix, regression test.
- How many bugs? Draw the Venn diagram.

# %%

# %%

# %% [markdown]
## 7. The dictionary that never starts

Count the words, ignoring case. The first version fails on the first new word. A partial fix may still return after one word.

# %%
def word_frequencies(words: list[str]) -> dict:
    frequencies = {}

    for word in words:
        clean = word.lower()
        count = frequencies.get(clean)
        frequencies[clean] = count + 1
        return frequencies

# %%
check_equal("empty input", lambda: word_frequencies([]), {})
check_equal(
    "repeated words",
    lambda: word_frequencies(["AI", "code", "ai", "Debug"]),
    {"ai": 2, "code": 1, "debug": 1},
)

# %% [markdown]
- Predict, bug report, minimal fix, regression test.

# %%

# %%

# %% [markdown]
## 8. The wrong top student

Return the student with the highest average. Break exact ties alphabetically. It is often right, but truncated averages create false ties.

# %%
def top_student(grades: dict[str, list[float]]) -> str:
    best_name = ""
    best_average = float("-inf")

    for name, scores in grades.items():
        average = sum(scores) // len(scores)
        if average >= best_average:
            best_name = name
            best_average = average

    return best_name

# %%
grades = {
    "Luis": [9.0, 8.9],
    "Ana": [8.9, 8.9],
    "Marta": [8.0, 8.5],
}
check_equal("close averages", lambda: top_student(grades), "Luis")

tied = {"Zoe": [9, 9], "Ana": [9, 9]}
check_equal("alphabetical tie", lambda: top_student(tied), "Ana")

# %% [markdown]
- Predict, bug report, minimal fix, regression test.
- Does the result depend on the order of the dictionary?

# %%

# %%

# %% [markdown]
## 9. Challenge

### The missing base case

It works for $n \geq 1$, but $0! = 1$. Negative numbers should raise a `ValueError`.

# %%
def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)

# %%
check_equal("factorial of five", lambda: factorial(5), 120)
check_equal("factorial of zero", lambda: factorial(0), 1)
check_raises("negative input", lambda: factorial(-1), ValueError)

# %%

# %% [markdown]
### The generator stops one step early

Yield the powers of two up to the limit, included.

# %%
def powers_of_two(limit: int):
    value = 1
    while value < limit:
        yield value
        value *= 2

# %%
check_equal("limit between powers", lambda: list(powers_of_two(10)), [1, 2, 4, 8])
check_equal("inclusive limit", lambda: list(powers_of_two(8)), [1, 2, 4, 8])

# %%

# %% [markdown]
### Bug exchange

Take one fixed function and add **one subtle bug**: valid syntax, passes at least one ordinary test, fails on an edge case, at most two changed lines. Give another pair the requirement and the passing tests. They find the failing input, explain it and add a regression test.

# %%

# %% [markdown]
### Exit ticket

1. Which result today looked plausible but was wrong?
2. What domain knowledge exposed it?
3. What coding intuition helped you find the cause?
4. Before trusting AI-generated code, what will you test first?

# %% [markdown]
## Next session

Homework session. **Can you explain your code to the class?**
