import pandas as pd

filepath = "ISSN_D_tot.csv"
col_names = ["year", "month", "day", "dec_date", "sunspots", "definite"]
sunspots = pd.read_csv(filepath, header=None, names=col_names, na_values={"sunspots": [" -1"]})
sunspots["date"] = pd.to_datetime(sunspots[["year", "month", "day"]])
sunspots = sunspots.drop(columns=["year", "month", "day"]).set_index("date")
sunspots = sunspots[["sunspots", "definite"]]

sunspots.to_csv("sunspots.csv")
sunspots.to_csv("sunspots.tsv", sep="\t")
sunspots.to_excel("sunspots.xlsx")

restored = pd.read_csv("sunspots.csv", parse_dates=["date"], index_col="date")
print(restored.dtypes)

summary = pd.DataFrame(
    {
        "statistic": ["mean", "std"],
        "sunspots": [sunspots["sunspots"].mean(), sunspots["sunspots"].std()],
    }
)
summary.to_csv("summary.csv", index=False, float_format="%.2f")
with open("summary.csv") as file:
    print(file.read())
