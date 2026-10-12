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

# Rows with a missing key are dropped by default (dropna=True)
print(sales_na.groupby("weekday").size().sum())
print(len(sales_na))
print(sales_na.groupby("weekday", dropna=False).size())
