import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"])
central = sales["Date"].dt.tz_localize("America/Chicago")
print(central.head(3))
eastern = central.dt.tz_convert("America/New_York")
print(eastern.head(3))
print(sales["Date"].iloc[7], "->", eastern.iloc[7])
