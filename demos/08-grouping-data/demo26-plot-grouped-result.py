import matplotlib.pyplot as plt
import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
mean_mpg = auto.groupby("yr")["mpg"].mean()

fig, ax = plt.subplots(figsize=(8, 4))
mean_mpg.plot.bar(ax=ax, rot=0)
ax.set(
    title="Average fuel economy rose from 1970 to 1982",
    xlabel="Model year (19xx)",
    ylabel="Miles per gallon",
)
fig.tight_layout()
fig.savefig("mean-mpg-by-year.png", dpi=150)
plt.show()
