import matplotlib.pyplot as plt
import pandas as pd

auto = pd.read_csv("auto-mpg.csv")

origins = ["US", "Europe", "Asia"]
groups = [auto.loc[auto["origin"] == origin, "mpg"] for origin in origins]

fig, ax = plt.subplots(figsize=(6, 4))
ax.boxplot(groups, tick_labels=origins)
ax.set(title="Fuel economy by origin", ylabel="Miles per gallon")
fig.tight_layout()
fig.savefig("boxplot.png")
plt.show()
