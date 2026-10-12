import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

titanic = pd.read_csv("titanic.csv").dropna(subset=["age", "fare"])
X = titanic[["pclass", "age", "fare"]].assign(male=titanic["sex"].eq("male").astype(int))
y = titanic["survived"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0, stratify=y
)

model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
predicted = model.predict(X_test)
print(round(accuracy_score(y_test, predicted), 3))
print(round(1 - y_test.mean(), 3))
print(confusion_matrix(y_test, predicted))
print(model.predict_proba(X_test.head(3)).round(2))
