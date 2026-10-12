import numpy as np

a = np.array([4, 15, 8, 23, 16, 42])
mask = a > 10
print(mask)
print(a[mask])
print(np.nonzero(mask)[0])
print(np.count_nonzero(mask))
print(a[(a > 10) & (a < 30)])
print(np.where(a > 10, a, 0))
