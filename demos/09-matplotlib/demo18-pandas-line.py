import matplotlib.pyplot as plt
import pandas as pd

aapl = pd.read_csv("AAPL.csv", parse_dates=["Date"], index_col="Date")

fig, ax = plt.subplots(figsize=(7, 3.5))
aapl["Close"].plot(ax=ax)
ax.set(title="Apple weekly close", xlabel="", ylabel="US dollars")
fig.tight_layout()
fig.savefig("pandas-line.png")
plt.show()
