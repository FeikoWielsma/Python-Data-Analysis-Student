import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

titanic = pd.read_csv("titanic.csv")
X = titanic[["pclass", "sex", "age", "fare", "embarked"]]
y = titanic["survived"]

prepare = ColumnTransformer(
    [
        (
            "numbers",
            make_pipeline(SimpleImputer(strategy="median"), StandardScaler()),
            ["pclass", "age", "fare"],
        ),
        (
            "categories",
            make_pipeline(
                SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore")
            ),
            ["sex", "embarked"],
        ),
    ]
)
model = make_pipeline(prepare, LogisticRegression(max_iter=1000))
print(cross_val_score(model, X, y, cv=5).round(3))
folds = KFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(model, X, y, cv=folds)
print(scores.round(3), round(scores.mean(), 3))
