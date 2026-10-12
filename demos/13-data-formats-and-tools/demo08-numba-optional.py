from timeit import timeit

import numpy as np
from numba import njit


def sum_squares(values):
    total = 0.0
    for value in values:
        total += value * value
    return total


compiled = njit(sum_squares)
values = np.random.default_rng(0).random(1_000_000)
compiled(values)  # the first call compiles the function

print(round(sum_squares(values), 3), round(compiled(values), 3), round(np.sum(values**2), 3))
for label, call in [
    ("Python loop", lambda: sum_squares(values)),
    ("Numba", lambda: compiled(values)),
    ("NumPy", lambda: np.sum(values**2)),
]:
    print(f"{label}: {timeit(call, number=5) / 5 * 1000:.2f} ms")
