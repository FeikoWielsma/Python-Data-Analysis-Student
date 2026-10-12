import pandas as pd

cities = ["Paris", "Berlin", "Paris", "Berlin"]
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ["Sun", "Sun", "Mon", "Mon"]
labels = ["city", "signups", "visitors", "weekday"]
columns = [cities, signups, visitors, weekdays]
users = pd.DataFrame(dict(zip(labels, columns)))
print(users)
