import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")

by_year = degrees.set_index("year")

fig, ax = plt.subplots(figsize=(7, 4))
by_year.plot(ax=ax)
ax.set(title="Degrees awarded to women", xlabel="Year", ylabel="% women")
ax.legend(["Physical Sciences", "Computer Science", "Health", "Education"], ncols=2)
fig.tight_layout()
fig.savefig("pandas-several-columns.png")
plt.show()
