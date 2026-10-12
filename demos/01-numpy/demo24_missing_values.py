import numpy as np

temps = np.array([17.4, 15.9, np.nan, 14.1])
print(temps.mean())
print(np.nanmean(temps).round(2))
print(np.isnan(temps))
print(np.isnan(temps).sum())
print(np.nan == np.nan)  # noqa: PLW0177  (the point of the demo)
