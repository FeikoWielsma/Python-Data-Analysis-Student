import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = pd.read_csv("tips.csv")

fig, axes = plt.subplots(1, 2, figsize=(9, 3.5), layout="constrained")
sns.histplot(data=tips, x="total_bill", hue="time", stat="count", ax=axes[0])
sns.histplot(data=tips, x="total_bill", hue="time", stat="density", common_norm=False, ax=axes[1])
sns.kdeplot(data=tips, x="total_bill", hue="time", common_norm=False, ax=axes[1])
axes[0].set_title('stat="count"')
axes[1].set_title('stat="density", common_norm=False')
fig.savefig("seaborn-distributions.png")
plt.show()
