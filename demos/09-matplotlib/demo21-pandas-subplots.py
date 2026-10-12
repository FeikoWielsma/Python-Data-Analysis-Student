import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")

by_year = degrees.set_index("year")

axes = by_year.plot(
    subplots=True,
    layout=(2, 2),
    figsize=(8, 5),
    sharex=True,
    legend=False,
    title=list(by_year.columns),
)
fig = axes[0, 0].figure
fig.tight_layout()
fig.savefig("pandas-subplots.png")
plt.show()
