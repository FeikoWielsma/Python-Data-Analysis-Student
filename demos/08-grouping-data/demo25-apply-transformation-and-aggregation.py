import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
groups = auto.groupby("yr")["mpg"]
mean = groups.transform("mean")
std = groups.transform("std", ddof=1)
result = auto[["yr", "name"]].copy()
result["mpg_z"] = (auto["mpg"] - mean) / std.where(std > 0)
result = result[["mpg_z", "yr", "name"]]
assert result.index.equals(auto.index)
assert result[["yr", "name"]].equals(auto[["yr", "name"]])
assert result["mpg_z"].groupby(result["yr"]).mean().abs().max() < 1e-12
print(result.head())
