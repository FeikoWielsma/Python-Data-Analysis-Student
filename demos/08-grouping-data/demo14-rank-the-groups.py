import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
by_origin = auto.groupby("origin")["mpg"].agg(["size", "mean"]).round(1)
print(by_origin.sort_values("mean", ascending=False))
print(auto.groupby("yr")["mpg"].mean().nlargest(3).round(1))
print(auto["origin"].value_counts())
