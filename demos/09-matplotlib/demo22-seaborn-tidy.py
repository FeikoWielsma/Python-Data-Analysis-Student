import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = pd.read_csv("tips.csv")
print(tips.head(3))

fig, ax = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", ax=ax)
ax.set(xlabel="Total bill (USD)", ylabel="Tip (USD)")
fig.tight_layout()
fig.savefig("seaborn-scatter.png")
plt.show()
