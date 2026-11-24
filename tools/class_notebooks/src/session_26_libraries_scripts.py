# %% [markdown]
# Session 26: Libraries and Scripts
## A landscape made from numbers

We want to study a function of two variables on a square region. Evaluating it
point by point would require nested loops. NumPy can evaluate the whole grid at
once.

**Can broadcasting turn two one-dimensional axes into a two-dimensional surface?**

# %% [markdown]
Today we will:

- create a square grid with broadcasting;
- evaluate a function on every point of the grid;
- visualise the surface and two one-dimensional cross-sections;
- organise the work into functions;
- move the program to a script and reuse its functions elsewhere.

## 1. Import the libraries

- Import NumPy as `np`.
- Import Matplotlib's plotting interface as `plt`.
- Check the versions of both libraries.

# %%

# %% [markdown]
## 2. Make two broadcast-ready axes

We will study the square region $-5 \leq x \leq 5$ and $-5 \leq y \leq 5$.

### Exercise: The right shapes

Create two arrays with 500 points each:

- `x` should have shape `(1, 500)`;
- `y` should have shape `(500, 1)`.

Hints: start with `np.linspace()`, then use `None` or `np.newaxis` to add a
dimension. Print the shapes and check that they are different.

# %%

# %% [markdown]
## 3. Let broadcasting build the surface

Use the function

$$z = \sin(x)\cos(y) + 0.1(x^2 + y^2).$$

### Exercise: One expression, many points

- Calculate `z` directly from `x` and `y`, without a loop.
- Print `z.shape`. It should be `(500, 500)`.
- Explain which dimensions NumPy compares when it broadcasts `(1, 500)` with
  `(500, 1)`.

# %%

# %% [markdown]
## 4. See the surface

### Exercise: A square colour plot

Use `plt.imshow()` to display `z` as a square colour plot.

Your plot should:

- show the real `x` and `y` values on the axes;
- place negative `y` values below positive `y` values;
- use equal scaling on both axes;
- include a colour bar labelled `z`.

Hints: `extent`, `origin="lower"`, `aspect="equal"`, and `cmap="viridis"`.

# %%

# %% [markdown]
## 5. Look along each axis

The surface contains many one-dimensional waves. Take two cross-sections:

- fix `y` at its middle value and plot `z[mid_y, :]` against `x`;
- fix `x` at its middle value and plot `z[:, mid_x]` against `y`.

### Exercise: Three views of one function

Create one figure with three panels:

1. the colour plot of the whole surface;
2. the horizontal cross-section, labelled `z(x, y=0)`;
3. the vertical cross-section, labelled `z(x=0, y)`.

Give every panel a title and labelled axes. Use `plt.tight_layout()`.

# %%

# %% [markdown]
## 6. Turn the calculation into functions

### Exercise: A reusable surface tool

Write these functions:

```python
make_grid(x_start, x_stop, y_start, y_stop, n)
evaluate_surface(x, y)
summarize_surface(z)
```

Requirements:

- `make_grid` returns `x` with shape `(1, n)` and `y` with shape `(n, 1)`;
- `evaluate_surface` returns the broadcast surface with shape `(n, n)`;
- `summarize_surface` returns the minimum and maximum values of `z`;
- none of the functions should plot or print.

# %%

# %%

# %%

# %% [markdown]
## 7. Use the functions in a program

Write a `main()` function that:

- creates a grid from `-5` to `5` with 500 points;
- evaluates the surface;
- prints the shapes of `x`, `y`, and `z`;
- prints the minimum and maximum values;
- creates the three-panel visualisation.

Then add the main guard:

```python
if __name__ == "__main__":
    main()
```

# %%

# %% [markdown]
## 8. Move the program into a script

Create a file named `surface.py` in the same folder as this notebook.

- Copy the imports and function definitions into the file.
- Add `main()` and the main guard.
- Run it from the VS Code terminal with `python surface.py`.
- Change the function to `np.sin(x) * np.cos(y)` and compare the new surface.

# %% [markdown]
## 9. Import the analysis functions

Create a second file named `compare_surfaces.py`.

- Import `make_grid`, `evaluate_surface`, and `summarize_surface` from `surface.py`.
- Analyze grids with `n = 10`, `n = 100`, and `n = 500`.
- Print the shape and minimum/maximum for each result.
- Explain why importing `surface.py` does not automatically run its `main()`.

# %%

# %% [markdown]
## Challenge: Change the surface

Modify `evaluate_surface` to study one of these functions:

$$z = \sin(x^2 + y^2)$$

or

$$z = \cos(x) + \sin(y).$$

Keep the same grid, functions, script, and three-panel visualisation. What
changes in the shape? What stays the same in the program?

# %%

# %% [markdown]
## Next session

Today one pair of broadcast-ready axes created a whole surface. Next time we
will organise several scripts into folders and build our own library.

