import pandas as pd

sales = pd.DataFrame(
    {
        "weekday": ["Sun", "Sun", "Mon", "Mon"],
        "city": ["Austin", "Dallas", "Austin", "Dallas"],
        "bread": [139, 237, 326, 456],
        "butter": [20, 45, 70, 98],
    }
)
print(sales)

customers = pd.Series(["Dave", "Alice", "Bob", "Alice"])
print(customers)


def data_range(series):
    return series.max() - series.min()


print(sales.groupby("weekday")[["bread", "butter"]].agg(data_range))

print(sales.groupby(customers)[["bread", "butter"]].agg({"bread": "sum", "butter": data_range}))
