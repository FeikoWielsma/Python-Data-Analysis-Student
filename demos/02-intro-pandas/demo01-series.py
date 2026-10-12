import pandas as pd

visitors = pd.Series([139, 237, 326], index=["Sun", "Mon", "Tue"], name="visitors")
print(visitors)
print(visitors.index.tolist())
print(visitors.to_list())
print(visitors.dtype)
