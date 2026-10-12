import pandas as pd

users = pd.DataFrame(
    {
        "city": ["Paris", "Berlin", "Paris", "Berlin"],
        "signups": [7, 12, 3, 5],
        "visitors": [139, 237, 326, 456],
        "weekday": ["Sun", "Sun", "Mon", "Mon"],
    }
)
users["fees"] = 0
print(users)
