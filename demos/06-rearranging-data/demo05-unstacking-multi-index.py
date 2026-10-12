import pandas as pd

trials = pd.read_csv("trials_01.csv")

print(trials)

trials = trials.set_index(["treatment", "gender"])
print(trials)

t = trials.unstack(level="gender")
print(t)

s = trials.unstack(level=1)
print(s)
