import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")

# pyplot interface: functions act on the current figure
plt.plot(degrees["year"], degrees["computer_science"])
plt.title("Computer Science")
plt.show()

# Object-oriented interface: methods on explicit Figure and Axes objects
fig, ax = plt.subplots()
ax.plot(degrees["year"], degrees["computer_science"])
ax.set_title("Computer Science")
fig.savefig("two-interfaces.png")
plt.show()
