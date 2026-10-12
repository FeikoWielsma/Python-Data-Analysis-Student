import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

titanic = pd.read_csv("titanic.csv")

fig, axes = plt.subplots(1, 2, figsize=(9, 3.5), layout="constrained")
sns.barplot(
    data=titanic,
    x="pclass",
    y="survived",
    hue="sex",
    estimator="mean",
    errorbar=("ci", 95),
    seed=0,
    ax=axes[0],
)
sns.countplot(data=titanic, x="pclass", hue="sex", ax=axes[1])
axes[0].set(title="Survival rate, 95% CI", ylabel="share survived")
axes[1].set(title="Passengers", ylabel="count")
fig.savefig("seaborn-estimates.png")

rates = titanic.groupby(["pclass", "sex"])["survived"].agg(["size", "mean"])
print(rates.round(3))
plt.show()
