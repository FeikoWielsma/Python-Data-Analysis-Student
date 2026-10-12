import numpy as np

a = np.array([10, 20, 30])
b = np.append(a, [40, 50])
print(a)
print(b)
print(np.concatenate([a, b]))

values = []
for x in range(3):
    values.append(x * 10)  # noqa: PERF401  (shows the loop pattern)
print(np.array(values))
