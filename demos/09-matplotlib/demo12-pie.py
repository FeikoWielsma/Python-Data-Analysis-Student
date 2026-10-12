import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv("titanic.csv")
counts = titanic["pclass"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(4.5, 4.5))
ax.pie(
    counts.to_numpy(),
    labels=["1st class", "2nd class", "3rd class"],
    autopct="%1.0f%%",
    startangle=90,
    counterclock=False,
)
ax.set_title("Titanic passengers by class")
fig.savefig("pie.png")
plt.show()
