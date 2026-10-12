import pandas as pd
from sklearn.linear_model import LinearRegression

auto = pd.read_csv("auto-mpg.csv")
X = auto[["weight"]]
y = auto["mpg"]

model = LinearRegression()
model.fit(X, y)
print(model.coef_, model.intercept_)

new_cars = pd.DataFrame({"weight": [2500, 4000]})
print(model.predict(new_cars).round(1))
