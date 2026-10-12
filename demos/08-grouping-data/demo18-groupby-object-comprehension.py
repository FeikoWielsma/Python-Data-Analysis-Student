import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
print(auto.head())

splitting = auto.groupby("yr")

chevy_means = {
    year: group.loc[group["name"].str.contains("chevrolet"), "mpg"].mean()
    for year, group in splitting
}

print(pd.Series(chevy_means))
