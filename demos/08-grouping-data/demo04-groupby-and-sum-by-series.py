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

print(sales.groupby(customers))
print(sales.groupby(customers)["bread"])
print(sales.groupby(customers)["bread"].sum())
