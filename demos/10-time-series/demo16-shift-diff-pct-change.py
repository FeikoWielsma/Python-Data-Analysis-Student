import pandas as pd

aapl = pd.read_csv("AAPL.csv", parse_dates=["Date"], index_col="Date")
close = aapl["Close"].tail(5)
print(
    pd.DataFrame(
        {
            "close": close,
            "previous": close.shift(1),
            "change": close.diff(),
            "pct": close.pct_change().mul(100).round(2),
        }
    )
)
