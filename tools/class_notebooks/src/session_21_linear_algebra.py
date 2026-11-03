# %% [markdown]
# Session 21: Linear Algebra
## A picture is worth a thousand words

| | Size |
|---|---|
| Plain text, 1000 words | 5 KB |
| RGB photo, 700 x 465 pixels | 950 KB |

A grayscale photo of $N \times N$ pixels is a matrix: $N^2$ numbers. JPEG compresses it by throwing some information away.

**Can we store the same picture with fewer numbers, using only linear algebra?**

# %%
import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests


def load_image(url: str, color: bool = False) -> np.ndarray:
    """Download an image as a NumPy array (grayscale by default, RGB if color=True)."""
    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype="uint8")
    if color:
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)


def show_image(img: np.ndarray):
    """Display a grayscale or RGB image (pixel values from 0 to 255)."""
    if img.ndim == 3:
        plt.imshow(np.clip(img, 0, 255).astype(np.uint8))
    else:
        plt.imshow(img, cmap="gray", vmin=0, vmax=255)
    plt.axis("off")
    plt.show()


url_img = "https://raw.githubusercontent.com/daniprec/Python-Course/main/img/"
url_dog = url_img + "dog_nice.png"
url_beach = url_img + "beach.jpg"

# %% [markdown]
- Load the dog and show it. Shape? Type? How many numbers do we store?

# %%

# %% [markdown]
First, the tools.

## 1. Matrix operations

- `A @ x`, `A.T`. What is the difference between `A @ A` and `A * A`?
- Solve $A\mathbf{x} = \mathbf{b}$ with `np.linalg.solve()`. Check the answer.
- Why not `np.linalg.inv(A) @ b`?

# %%
A = np.array([[2, 1], [1, 3]])
x = np.array([4, -1])
b = np.array([7, 5])

# %%

# %%

# %% [markdown]
### Exercise: Solve a 2x2 System

$$
\begin{aligned}
3x + 2y &= 12,\\
x - y &= 1.
\end{aligned}
$$

Solve it and verify the result with `@`.

# %%

# %% [markdown]
## 2. Eigenvalues and eigenvectors

$A\mathbf{v} = \lambda\mathbf{v}$.

- Eigenvalues and eigenvectors of $A$ with `np.linalg.eigh()`. Are the eigenvectors rows or columns?
- Check $A\mathbf{v} = \lambda\mathbf{v}$ for each pair. Hint: `np.allclose()`.
- `np.linalg.eig()` vs `np.linalg.eigh()`: when can we use each one?

# %%
A = np.array([[2, 1], [1, 2]])

# %%

# %%

# %%

# %% [markdown]
## 3. Eigen decomposition of an image

$A = Q\,\Lambda\,Q^{-1}$, with $\Lambda$ the diagonal matrix of eigenvalues.

- Eigen decomposition needs a square matrix. Crop the dog to a square `img`.
- Eigenvalues and eigenvectors of `img` with `np.linalg.eig()`. Shapes? `dtype`?
- Reconstruct the image and show it. What goes wrong?

# %%

# %%

# %%

# %% [markdown]
**The eigenvalues of a symmetric matrix are real.**

## 4. Making it symmetric

$$
M = \begin{pmatrix} 0 & A^T \\ A & 0 \end{pmatrix}
$$

- Build `M`: zeros of double size, the image bottom-left, its transpose top-right. Show it.
- Decompose `M` with `np.linalg.eigh()`. Reconstruct it as $Q\,\Lambda\,Q^T$. Why $Q^T$ and not $Q^{-1}$?
- Crop the bottom-left corner. Is it our dog?

# %%

# %%

# %%

# %% [markdown]
## 5. Compression: keep the top k

- Keep the `k = 20` eigenvalues with the largest absolute value, and their eigenvectors. Hint: `np.argsort()`.
- Reconstruct, crop and show. Try `k = 5, 50, 100`.
- How many numbers do we store now?

# %%

# %%

# %%

# %% [markdown]
### Exercise: Measure the Compression

How many values have we eliminated? Give the number and the percentage of the original image size. For an $N \times N$ image, when does this compression pay off?

# %%

# %% [markdown]
## 6. Singular value decomposition (SVD)

$A = U\,\Sigma\,V^T$, for a matrix of **any** shape.

- SVD of the full (non-square) dog: `np.linalg.svd(dog, full_matrices=False)`. Shapes of `U`, `S`, `Vt`?
- Reconstruct the image.
- Keep the top `k = 50` singular values. How many numbers do we store? Compare with section 5.

# %%

# %%

# %%

# %% [markdown]
### Exercise: Compress an RGB Image

Load the beach with `color=True` and compress it, keeping the top `k` singular values. Hint: shape `(height, width, 3)`.

# %%

# %%

# %% [markdown]
## 7. Challenge: Verify an Eigen Decomposition

`B = M + M.T` with the matrix below.

1. Eigenvalues and eigenvectors of `B` with `np.linalg.eigh()`.
2. Check $B\mathbf{v} = \lambda\mathbf{v}$ for every pair with `np.allclose()`.
3. Reconstruct `B` as $Q\,\Lambda\,Q^T$ and compare.

# %%
M = np.array([[1, 2, 0], [0, 3, 1], [4, 0, 2]])

# %%

# %% [markdown]
## Next session

Our Monty Hall simulation loops over the games one by one. One million games take a while. **Can we play them all at once, without a loop?**
