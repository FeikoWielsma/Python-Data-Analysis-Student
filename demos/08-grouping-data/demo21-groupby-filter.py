import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
counts = auto["cyl"].value_counts().sort_index()
print(counts)

common = auto.groupby("cyl").filter(lambda group: len(group) >= 10)
print(common["cyl"].value_counts().sort_index())
print(len(auto), len(common))
