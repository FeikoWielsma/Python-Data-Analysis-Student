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

# Each keyword names an output column: name=(column, function)
summary = sales_na.groupby("city").agg(
    rows=("bread", "size"),
    bread_count=("bread", "count"),
    bread_total=("bread", "sum"),
    butter_mean=("butter", "mean"),
)
print(summary)
