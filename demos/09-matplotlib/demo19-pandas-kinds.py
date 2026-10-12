import matplotlib.pyplot as plt
import pandas as pd

auto = pd.read_csv("auto-mpg.csv")

fig, axes = plt.subplots(2, 2, figsize=(8, 6), layout="constrained")
auto.groupby("origin")["mpg"].mean().plot.bar(ax=axes[0, 0], rot=0, title="bar")
auto["mpg"].plot.hist(ax=axes[0, 1], bins=20, title="hist")
auto.plot.scatter(x="weight", y="mpg", s=8, ax=axes[1, 0], title="scatter")
auto[["mpg", "accel"]].plot.box(ax=axes[1, 1], title="box")
fig.savefig("pandas-kinds.png")
plt.show()
