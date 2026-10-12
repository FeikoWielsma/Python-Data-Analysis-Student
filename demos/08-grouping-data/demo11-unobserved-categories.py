import numpy as np
import pandas as pd

# Monday has a missing bread value; the last row has no weekday
sales_na = pd.DataFrame(
    {
        "weekday": ["Sun", "Sun", "Mon", "Mon", np.nan],
        "city": ["Austin", "Dallas", "Austin", "Dallas", "Austin"],
        "bread": [139, 237, 326, np.nan, 210],
        "butter": [20, 45, 70, 98, 33],
    }
)

# Houston is a known city without sales_na
cities = ["Austin", "Dallas", "Houston"]
sales_na["city"] = pd.Categorical(sales_na["city"], categories=cities)

# pandas 3 defaults to observed=True; pandas 2 defaults to False
print(sales_na.groupby("city", observed=True)["bread"].sum())
print(sales_na.groupby("city", observed=False)["bread"].sum())
print(sales_na.groupby("city", observed=False).size())
