import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
print(auto.head())

splitting = auto.groupby("yr")

print(type(splitting))
print(type(splitting.groups))
print(splitting.groups.keys())
print(splitting.groups.values())
