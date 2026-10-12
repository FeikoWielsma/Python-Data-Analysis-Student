import numpy as np
import pandas as pd
from scipy import stats

auto = pd.read_csv("auto-mpg.csv")


def zscore(series):
    return (series - series.mean()) / series.std()


# pandas .std() divides by n - 1 (ddof=1); scipy divides by n (ddof=0)
print(auto["mpg"].std(), auto["mpg"].std(ddof=0))
print(zscore(auto["mpg"]).head(2).to_numpy())
print(stats.zscore(auto["mpg"])[:2])
print(stats.zscore(auto["mpg"], ddof=1)[:2])

# Missing values: pandas skips them; scipy propagates NaN by default
s = pd.Series([18.0, 15.0, np.nan, 16.0])
print(zscore(s).round(3).tolist())
print(stats.zscore(s, ddof=1))
print(stats.zscore(s, ddof=1, nan_policy="omit").round(3))

# One value has no sample standard deviation
print(pd.Series([20.0]).std())

# Grouping by year and cylinders creates eight single-car groups
by_yr_cyl = auto.groupby(["yr", "cyl"])["mpg"]
print((by_yr_cyl.size() == 1).sum())
print(by_yr_cyl.transform(zscore).isna().sum())
