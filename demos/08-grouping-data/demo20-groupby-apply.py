import pandas as pd

auto = pd.read_csv("auto-mpg.csv")


def chevy_mean(group):
    chevy = group["name"].str.contains("chevrolet")
    return group.loc[chevy, "mpg"].mean()


print(auto.groupby("yr")[["name", "mpg"]].apply(chevy_mean).head(4))


def heaviest(group):
    return group.nlargest(1, "weight")


print(auto.groupby("origin")[["name", "weight"]].apply(heaviest))
