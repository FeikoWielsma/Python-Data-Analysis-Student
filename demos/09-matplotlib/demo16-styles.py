import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")

print(plt.style.available[:6])

with plt.style.context("ggplot"):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(degrees["year"], degrees["health"], label="Health")
    ax.plot(degrees["year"], degrees["education"], label="Education")
    ax.set(title="Style 'ggplot'", ylabel="% women")
    ax.legend()
    fig.tight_layout()
    fig.savefig("styles.png")
plt.show()
