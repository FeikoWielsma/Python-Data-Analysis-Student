import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
print(auto[["mpg", "cyl", "weight", "yr", "origin", "name"]].head())
print(auto.shape)
