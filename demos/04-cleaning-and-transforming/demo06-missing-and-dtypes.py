import pandas as pd

visits = pd.DataFrame({"city": ["Paris", "Berlin", "Rome"], "visitors": [139, 237, 326]})
print(visits["visitors"].dtype)
visits.loc[1, "visitors"] = float("nan")
print(visits["visitors"].dtype)
print(visits)

counts = pd.Series([139, None, 326], dtype="Int64")
print(counts)
