import pandas as pd

trials = pd.read_csv("trials_01.csv")

print(trials)

stacked = trials.set_index(["treatment", "gender"])
print(stacked)

swapped = stacked.swaplevel(0, 1)
print(swapped)

sorted_trials = swapped.sort_index()
print(sorted_trials)
