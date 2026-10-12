import matplotlib.pyplot as plt
import pandas as pd

aapl = pd.read_csv("AAPL.csv", parse_dates=["Date"], index_col="Date")
close = aapl["Close"]

fig, ax = plt.subplots(figsize=(8, 3.5))
close.plot(ax=ax, alpha=0.5, label="weekly close")
close.rolling(window=13).mean().plot(ax=ax, label="13-week rolling mean")
close.resample("QS").mean().plot(ax=ax, drawstyle="steps-post", label="quarterly mean")
ax.set(title="Apple share price", xlabel="", ylabel="US dollars")
ax.legend()
fig.tight_layout()
fig.savefig("price-rolling.png")
plt.show()
