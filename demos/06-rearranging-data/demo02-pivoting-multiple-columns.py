import pandas as pd

trials = pd.read_csv("trials_01.csv")

print(trials)

t = trials.pivot(index="treatment", columns="gender")
print(t)
