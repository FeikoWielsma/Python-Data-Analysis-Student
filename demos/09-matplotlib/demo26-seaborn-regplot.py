import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

auto = pd.read_csv("auto-mpg.csv")

fig, ax = plt.subplots(figsize=(6, 4))
sns.regplot(data=auto, x="weight", y="mpg", seed=0, scatter_kws={"s": 10}, ax=ax)
ax.set(xlabel="Weight (lb)", ylabel="Miles per gallon")
fig.tight_layout()
fig.savefig("seaborn-regplot.png")
plt.show()
