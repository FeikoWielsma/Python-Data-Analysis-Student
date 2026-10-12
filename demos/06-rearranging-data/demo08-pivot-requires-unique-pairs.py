import pandas as pd

more_trials = pd.read_csv("trials_03.csv")
print(more_trials)

s = more_trials.pivot(index="treatment", columns="gender", values="response")
print(s.index)
print(s)
