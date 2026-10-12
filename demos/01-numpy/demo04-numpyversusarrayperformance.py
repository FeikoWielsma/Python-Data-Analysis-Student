import timeit

import numpy as np

# Add two sequences of SIZE numbers: a list comprehension versus a NumPy array.
# Inputs are built once before timing; only the addition (including creating
# the result list or array) is timed. Times are the best of REPEAT runs.

SIZE = 1_000_000
REPEAT = 5

L1 = list(range(SIZE))
L2 = list(range(SIZE))
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)


def list_version():
    return [x + y for x, y in zip(L1, L2)]


def array_version():
    return A1 + A2


def ms_per_call(func):
    timer = timeit.Timer(func)
    loops, _ = timer.autorange()
    return min(timer.repeat(repeat=REPEAT, number=loops)) / loops * 1000


print("Same result:", np.array_equal(np.array(list_version()), array_version()))

list_ms = ms_per_call(list_version)
array_ms = ms_per_call(array_version)
print(f"List comprehension: {list_ms:8.3f} ms")
print(f"NumPy addition    : {array_ms:8.3f} ms")
print(f"On this machine the NumPy version was about {list_ms / array_ms:.0f} times faster.")
