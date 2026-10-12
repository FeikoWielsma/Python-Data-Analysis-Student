import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

aapl = pd.read_csv("AAPL.csv", parse_dates=["Date"])

fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(aapl["Date"], aapl["Close"])
locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
ax.set(title="Apple weekly close", ylabel="US dollars")
fig.tight_layout()
fig.savefig("dates.png")
plt.show()
