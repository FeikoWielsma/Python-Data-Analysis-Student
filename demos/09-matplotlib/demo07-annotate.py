import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")

cs = degrees["computer_science"]
peak_year = degrees.loc[cs.idxmax(), "year"]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(degrees["year"], cs)
ax.annotate(
    f"Peak: {cs.max()}% in {peak_year}",
    xy=(peak_year, cs.max()),
    xytext=(peak_year + 5, cs.max() + 3),
    arrowprops={"arrowstyle": "->", "color": "black"},
)
ax.text(1971, 15, "Source: US degree statistics", fontsize=9, color="gray")
ax.set(ylim=(0, 45), xlabel="Year", ylabel="% of degrees awarded to women")
fig.tight_layout()
fig.savefig("annotate.png")
plt.show()
