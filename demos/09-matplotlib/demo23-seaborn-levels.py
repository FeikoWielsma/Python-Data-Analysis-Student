import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = pd.read_csv("tips.csv")

fig, ax = plt.subplots()
sns.boxplot(data=tips, x="day", y="tip", ax=ax)

g = sns.catplot(data=tips, x="day", y="tip", col="time", kind="box", height=3.5)
print(type(g).__name__)
g.savefig("seaborn-catplot.png")
plt.show()
