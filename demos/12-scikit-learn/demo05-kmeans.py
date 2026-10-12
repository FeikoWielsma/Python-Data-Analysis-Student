import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

auto = pd.read_csv("auto-mpg.csv")
features = StandardScaler().fit_transform(auto[["weight", "mpg"]])
auto["cluster"] = KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(features)
print(auto.groupby(["cluster", "origin"]).size().unstack(fill_value=0))

fig, ax = plt.subplots(figsize=(5.5, 4.5))
for cluster, group in auto.groupby("cluster"):
    ax.scatter(group["weight"], group["mpg"], s=12, label=f"cluster {cluster}")
ax.set(
    title="Three groups of cars, found without labels",
    xlabel="Weight (lb)",
    ylabel="Miles per gallon",
)
ax.legend()
fig.tight_layout()
fig.savefig("kmeans.png")
plt.show()
