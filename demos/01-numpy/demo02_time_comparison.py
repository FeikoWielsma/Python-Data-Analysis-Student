import timeit

import numpy as np

# One of the main advantages of NumPy is its advantage in time compared to standard Python.
# Both versions below add the same two sequences element by element.
# The inputs are created once, outside the timed code, so only the addition is timed.
# Each version is timed several times and the fastest run is reported.

size_of_vec = 1_000_000
REPEAT = 5

X_list = list(range(size_of_vec))
Y_list = list(range(size_of_vec))
X_array = np.arange(size_of_vec)
Y_array = np.arange(size_of_vec)


def pure_python_version():
    Z = []
    for i in range(len(X_list)):
        Z.append(X_list[i] + Y_list[i])
    return Z


def numpy_version():
    return X_array + Y_array


def seconds_per_call(func):
    timer = timeit.Timer(func)
    loops, _ = timer.autorange()  # enough calls for a measurable total
    return min(timer.repeat(repeat=REPEAT, number=loops)) / loops


# Compare like with like: both versions must give the same answer.
print("Same result:", np.array_equal(np.array(pure_python_version()), numpy_version()))

t1 = seconds_per_call(pure_python_version)
t2 = seconds_per_call(numpy_version)
print(f"Python loop: {t1 * 1000:8.3f} ms per call (best of {REPEAT})")
print(f"NumPy      : {t2 * 1000:8.3f} ms per call (best of {REPEAT})")
print(f"On this machine NumPy was about {t1 / t2:.0f} times faster for {size_of_vec:,} elements.")
