import pandas as pd

aapl = pd.read_csv("AAPL.csv", parse_dates=["Date"], index_col="Date")
close = aapl["Close"].tail(8)
table = pd.DataFrame(
    {
        "close": close,
        "rolling": close.rolling(window=4).mean(),
        "partial": close.rolling(window=4, min_periods=2).mean(),
        "centered": close.rolling(window=3, center=True).mean(),
    }
)
print(table.round(2))
