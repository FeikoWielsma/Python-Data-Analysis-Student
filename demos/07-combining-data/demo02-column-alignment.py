import pandas as pd

jan = pd.DataFrame({"id": ["a"], "units": [10]})
feb = pd.DataFrame({"units": [20], "id": ["b"], "channel": ["store"]})

combined = pd.concat([jan, feb], ignore_index=True)
print(combined.to_string(index=False))
shared = pd.concat([jan, feb], join="inner", ignore_index=True)
print("Shared columns:", shared.columns.tolist())
