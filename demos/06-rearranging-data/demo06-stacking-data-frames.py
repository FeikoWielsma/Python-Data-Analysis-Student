import pandas as pd

trials = pd.read_csv("trials_01.csv").set_index(["treatment", "gender"])
wide = trials.unstack(level="gender")
restored = wide.stack(level="gender")
print(restored)

sparse = trials.drop(index=("B", "M"))
expanded = sparse.unstack("gender").stack("gender")
print(expanded)
print(len(sparse), len(expanded))
