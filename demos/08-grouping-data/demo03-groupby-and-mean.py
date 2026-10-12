import pandas as pd

sales = pd.DataFrame(
    {
        "weekday": ["Sun", "Sun", "Mon", "Mon"],
        "city": ["Austin", "Dallas", "Austin", "Dallas"],
        "bread": [139, 237, 326, 456],
        "butter": [20, 45, 70, 98],
    }
)

print(sales.groupby(["city", "weekday"]).mean())
