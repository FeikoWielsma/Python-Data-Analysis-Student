import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
print(auto.head())

print(auto.groupby("yr")["mpg"].mean())
