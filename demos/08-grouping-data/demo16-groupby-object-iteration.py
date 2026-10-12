import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
print(auto.head())

splitting = auto.groupby("yr")

for group_name, group in splitting:
    avg = group["mpg"].mean()
    print(group_name, avg)
