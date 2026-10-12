import argparse
import timeit

import numpy as np

# Sum the same values along each axis, stored in C (row-major) and F (column-major) order.
# Default size is 2000 x 2000 (two arrays, about 64 MB in total).
# Use --large for the original 10000 x 10000 (two arrays, about 1.6 GB in total).

parser = argparse.ArgumentParser(description="C versus F order: sum along each axis")
parser.add_argument("--large", action="store_true", help="use the original 10000 x 10000 size")
parser.add_argument("--size", type=int, default=2000, help="rows and columns (default 2000)")
args = parser.parse_args()
n = 10_000 if args.large else args.size
REPEAT = 5

rng = np.random.default_rng(42)
c = rng.standard_normal((n, n))  # C order is the default
f = np.asfortranarray(c)  # same values, F order
print(c.shape, f"{(c.nbytes + f.nbytes) / 1e6:.0f} MB in total")

for axis in (0, 1):
    # Same values, same result; only the memory layout differs
    print("Same sums:", np.allclose(c.sum(axis=axis), f.sum(axis=axis)))


def ms_per_call(func):
    timer = timeit.Timer(func)
    loops, _ = timer.autorange()
    return min(timer.repeat(repeat=REPEAT, number=loops)) / loops * 1000


for name, a in (("C", c), ("F", f)):
    for axis in (0, 1):
        ms = ms_per_call(lambda: a.sum(axis=axis))
        print(f"{name} order axis = {axis}: {ms:8.3f} ms per sum")

print("Timings are observations on this machine; compare the four lines with each other.")
