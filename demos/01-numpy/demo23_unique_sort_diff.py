import numpy as np

a = np.array([3, 1, 3, 2, 1, 3])
print(np.unique(a))
values, counts = np.unique(a, return_counts=True)
print(values, counts)
print(np.sort(a))
print(np.diff(np.array([1, 4, 9, 16])))
