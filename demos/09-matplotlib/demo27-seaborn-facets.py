import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = pd.read_csv("tips.csv")

sns.set_theme(style="whitegrid")
g = sns.catplot(
    data=tips,
    x="day",
    y="tip",
    hue="sex",
    col="time",
    kind="bar",
    errorbar=("ci", 95),
    seed=0,
    height=3.5,
)
g.savefig("seaborn-facets.png")

print(tips.groupby(["time", "day", "sex"], observed=True).size())
plt.show()
