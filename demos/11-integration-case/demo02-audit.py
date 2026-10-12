"""Audit a plausible assistant-style proposal. The proposal is intentionally wrong."""

import pandas as pd

deaths = pd.read_csv("eurostat-road-deaths-2023-2024.csv").rename(
    columns={"TIME_PERIOD": "year", "OBS_VALUE": "value"}
)
population = pd.read_csv("eurostat-population-2024.csv").rename(
    columns={"TIME_PERIOD": "year", "OBS_VALUE": "value"}
)
BINS = [0, 15, 18, 25, 50, 65, float("inf")]
CODES = ["Y_LT15", "Y15-17", "Y18-24", "Y25-49", "Y50-64", "Y_GE65"]

# --- The proposal: it runs and returns plausible rates
rows = deaths.loc[
    deaths["year"].eq(2024)
    & deaths["sex"].eq("T")
    & deaths["pers_cat"].eq("TOTAL")
    & deaths["age"].ne("TOTAL")
]
years = pd.to_numeric(population["age"].str[1:], errors="coerce")
bands = population.assign(age=pd.cut(years, BINS, right=False, labels=CODES))
bands = (
    bands.loc[bands["sex"].eq("T")]
    .groupby(["geo", "age"], observed=True, as_index=False)["value"]
    .sum()
)
joined = rows.merge(bands.astype({"age": "str"}), on=["geo", "age"], suffixes=("", "_population"))
answer = joined.groupby("age").agg(deaths=("value", "sum"), population=("value_population", "sum"))
answer["per_million"] = (answer["deaths"] / answer["population"] * 1_000_000).round(1)
print(answer)

# --- Check 1: grain. Are these country counts, one row per cell?
print(joined["unit"].unique().tolist(), "EU27_2020" in set(joined["geo"]))
print(joined.duplicated(["geo", "age"]).sum(), "repeated cells")

# --- Check 2: ages. Which population labels did errors='coerce' turn into NaN?
lost = population.loc[years.isna(), "age"].unique().tolist()
print(lost)

# --- Check 3: reconciliation. Do all deaths and countries survive the join?
all_countries = set(deaths["geo"]) - {"EU27_2020"}
print(sorted(all_countries - set(joined["geo"])))
print("UNK" in set(joined["age"]))

expected = pd.read_csv("road-deaths-expected-summary.csv")
print(expected[["age_group", "deaths", "per_million"]].round(1))
