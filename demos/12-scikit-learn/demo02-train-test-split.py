import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

auto = pd.read_csv("auto-mpg.csv")
X = auto[["weight", "hp", "yr"]]
y = auto["mpg"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
print(len(X_train), len(X_test))

model = LinearRegression().fit(X_train, y_train)
predicted = model.predict(X_test)
print(round(mean_absolute_error(y_test, predicted), 2), round(r2_score(y_test, predicted), 3))

fig, ax = plt.subplots(figsize=(5, 4.5))
ax.scatter(y_test, predicted, s=12, alpha=0.7)
ax.plot([10, 45], [10, 45], color="black", linestyle="--", linewidth=1)
ax.set(title="Test cars: predicted against actual", xlabel="Actual mpg", ylabel="Predicted mpg")
fig.tight_layout()
fig.savefig("predicted-vs-actual.png")
plt.show()
