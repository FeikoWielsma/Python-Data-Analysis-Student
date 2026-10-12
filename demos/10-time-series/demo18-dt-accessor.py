import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"])
print(sales.head(3))
print(sales["Date"].dt.hour.head(3).tolist())
print(sales["Date"].dt.day_name().head(3).tolist())
print(sales["Date"].dt.strftime("%d %b %H:%M").head(3).tolist())
print(
    sales.groupby(sales["Date"].dt.day_name())["Units"].sum().sort_values(ascending=False).head(3)
)
