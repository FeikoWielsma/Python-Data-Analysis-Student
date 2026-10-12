"""Integration case, step by step: road deaths per million inhabitants by age group, 2024."""

import matplotlib.pyplot as plt
import pandas as pd

print("--- Step 1: look at the raw files")
raw = pd.read_csv("eurostat-road-deaths-2023-2024.csv")
print(raw.shape)
print(raw[["unit", "sex", "age", "pers_cat", "geo", "TIME_PERIOD", "OBS_VALUE"]].head(3))
print(raw["unit"].unique().tolist())
print(raw["age"].unique().tolist())
print(raw["geo"].nunique(), "EU27_2020" in set(raw["geo"]))

print("--- Step 2: constants")
AGE_CODES = {
    "Y_LT15": "Under 15",
    "Y15-17": "15-17",
    "Y18-24": "18-24",
    "Y25-49": "25-49",
    "Y50-64": "50-64",
    "Y_GE65": "65+",
    "UNK": "Unknown age",
}
LABELS = list(AGE_CODES.values())
BINS = [0, 15, 18, 25, 50, 65, float("inf")]
print(LABELS)

print("--- Step 3: load with types")
names = {"TIME_PERIOD": "year", "OBS_VALUE": "value", "OBS_FLAG": "flag"}
deaths = pd.read_csv(
    "eurostat-road-deaths-2023-2024.csv",
    usecols=["unit", "sex", "age", "pers_cat", "geo", "TIME_PERIOD", "OBS_VALUE"],
    dtype={"TIME_PERIOD": "Int64", "OBS_VALUE": "Int64"},
).rename(columns=names)
population = pd.read_csv(
    "eurostat-population-2024.csv",
    usecols=["sex", "age", "geo", "TIME_PERIOD", "OBS_VALUE", "OBS_FLAG"],
    dtype={"TIME_PERIOD": "Int64", "OBS_VALUE": "Int64"},
).rename(columns=names)
print(deaths.shape, population.shape)
print(deaths["value"].isna().sum(), population["value"].isna().sum())
print(population["flag"].value_counts())

print("--- Step 4: keep the death counts we need")
counts = deaths.loc[
    deaths["unit"].eq("NR")
    & deaths["pers_cat"].eq("TOTAL")
    & deaths["year"].eq(2024)
    & deaths["sex"].eq("T")
    & deaths["geo"].ne("EU27_2020")
]
COUNTRIES = sorted(counts["geo"].unique())
totals = counts.loc[counts["age"].eq("TOTAL")].set_index("geo")["value"]
counts = counts.loc[counts["age"].ne("TOTAL")]
print(len(COUNTRIES), len(counts), totals.sum())

print("--- Step 5: age codes become labels")
counts = counts.assign(age_group=counts["age"].map(AGE_CODES))
counts = counts[["geo", "age_group", "value"]].rename(columns={"value": "deaths"})
print(counts.head(4))
print(counts["age_group"].isna().sum())

print("--- Step 6: band the population")
people = population.loc[population["sex"].eq("T") & population["geo"].ne("EU27_2020")]
ages = people.loc[~people["age"].isin(["TOTAL", "UNK"])]
years = ages["age"].replace({"Y_LT1": "Y0", "Y_OPEN": "Y100"}).str[1:].astype(int)
ages = ages.assign(age_group=pd.cut(years, BINS, right=False, labels=LABELS[:-1]))
bands = (
    ages.groupby(["geo", "age_group"], observed=True)["value"].sum().reset_index(name="population")
)
bands["age_group"] = bands["age_group"].astype(str)
print(len(ages) // len(COUNTRIES), "ages per country ->", len(bands) // len(COUNTRIES), "bands")
print(bands.head(3))

print("--- Step 7: check the bands against the published totals")
published = people.loc[people["age"].eq("TOTAL")].set_index("geo")["value"]
banded = bands.groupby("geo")["population"].sum()
print((banded == published).all())
print(bands.loc[bands["geo"].eq("NL") & bands["age_group"].eq("Under 15"), "population"].iloc[0])

print("--- Step 8: one grid of cells, two left merges")
cells = pd.MultiIndex.from_product([COUNTRIES, LABELS], names=["geo", "age_group"])
table = cells.to_frame(index=False)
table = table.merge(bands, how="left", validate="one_to_one")
table = table.merge(counts, how="left", validate="one_to_one", indicator=True)
print(len(table), table["_merge"].value_counts().to_dict())
recorded = table.groupby("geo")["deaths"].sum().loc[totals.index]
print((recorded == totals).all(), recorded.sum())

print("--- Step 9: the missing cells")
missing = table.loc[table["deaths"].isna()]
print(missing["geo"].value_counts().to_dict())
print(
    table.loc[
        table["geo"].isin(["LI", "ME"]) & table["age_group"].eq("Unknown age"), ["geo", "deaths"]
    ]
)

print("--- Step 10: summary and rate per million")
table["reported_population"] = table["population"].where(table["deaths"].notna())
grouped = table.groupby("age_group", sort=False)
summary = pd.DataFrame(
    {
        "countries": grouped.size(),
        "reported": grouped["deaths"].count(),
        "deaths": grouped["deaths"].sum(),
        "population": grouped["reported_population"].sum(min_count=1),
    }
)
summary["missing"] = summary["countries"] - summary["reported"]
summary["per_million"] = (summary["deaths"] / summary["population"] * 1_000_000).round(1)
summary = summary[["countries", "reported", "missing", "deaths", "population", "per_million"]]
print(summary)
print(summary["deaths"].sum())

print("--- Step 11: compare with Eurostat and with an independent calculation")
rates = deaths.loc[
    deaths["unit"].eq("P_MHAB")
    & deaths["sex"].eq("T")
    & deaths["pers_cat"].eq("TOTAL")
    & deaths["year"].eq(2024)
    & deaths["age"].isin(list(AGE_CODES)[:-1])
]
rates = rates.assign(age_group=rates["age"].map(AGE_CODES))
mine = table.assign(rate=table["deaths"] / table["population"] * 1_000_000)
both = mine.merge(rates, on=["geo", "age_group"], validate="one_to_one")
print((both["rate"].round() == both["value"]).sum(), "of", len(both), "country rates match")

expected = pd.read_csv("road-deaths-expected-summary.csv").set_index("age_group")
print(
    (expected["deaths"] == summary["deaths"]).all(),
    (expected["per_million"].round(1) == summary["per_million"]).all(),
)

print("--- Step 12: the chart")
shown = summary.loc[summary["per_million"].notna()]
fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
bars = ax.bar(shown.index, shown["per_million"])
labels = [
    f"{deaths:,} deaths\n{people / 1e6:.1f} M people"
    for deaths, people in zip(shown["deaths"], shown["population"])
]
ax.bar_label(bars, labels=labels, fontsize=9, padding=3)
unknown = summary.loc["Unknown age", "deaths"]
ax.set(
    ylim=(0, shown["per_million"].max() * 1.3),
    ylabel="Road deaths per million inhabitants",
    xlabel=f"Age group. Not shown: {unknown} deaths of unknown age; "
    f"LI and ME report no age breakdown.",
    title="Road deaths by age group, 2024, 33 European countries (Eurostat)",
)
fig.savefig("road-deaths-by-age.png", dpi=160)
plt.show()
