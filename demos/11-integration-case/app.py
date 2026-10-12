"""Optional local app for the integration case.

Run from the datasets folder:
    cd datasets
    uv run --project .. --frozen streamlit run ../demos/11-integration-case/app.py
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

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


@st.cache_data
def build_table(sex):
    """Steps 3-8 of the case: one row per country and age group."""
    names = {"TIME_PERIOD": "year", "OBS_VALUE": "value"}
    deaths = pd.read_csv("eurostat-road-deaths-2023-2024.csv").rename(columns=names)
    population = pd.read_csv("eurostat-population-2024.csv").rename(columns=names)
    counts = deaths.loc[
        deaths["unit"].eq("NR")
        & deaths["pers_cat"].eq("TOTAL")
        & deaths["year"].eq(2024)
        & deaths["sex"].eq(sex)
        & deaths["geo"].ne("EU27_2020")
        & deaths["age"].ne("TOTAL")
    ]
    counts = counts.assign(age_group=counts["age"].map(AGE_CODES))
    counts = counts[["geo", "age_group", "value"]].rename(columns={"value": "deaths"})
    people = population.loc[population["sex"].eq(sex) & population["geo"].ne("EU27_2020")]
    ages = people.loc[~people["age"].isin(["TOTAL", "UNK"])]
    years = ages["age"].replace({"Y_LT1": "Y0", "Y_OPEN": "Y100"}).str[1:].astype(int)
    ages = ages.assign(age_group=pd.cut(years, BINS, right=False, labels=LABELS[:-1]))
    bands = (
        ages.groupby(["geo", "age_group"], observed=True)["value"]
        .sum()
        .reset_index(name="population")
    )
    bands["age_group"] = bands["age_group"].astype(str)
    cells = pd.MultiIndex.from_product(
        [sorted(people["geo"].unique()), LABELS], names=["geo", "age_group"]
    )
    table = cells.to_frame(index=False).merge(bands, how="left", validate="one_to_one")
    return table.merge(counts, how="left", validate="one_to_one")


def summarize(table):
    """Step 10: deaths per million inhabitants of the countries that report each group."""
    table = table.assign(reported_population=table["population"].where(table["deaths"].notna()))
    grouped = table.groupby(pd.Categorical(table["age_group"], categories=LABELS), observed=False)
    summary = pd.DataFrame(
        {
            "countries": grouped.size(),
            "reported": grouped["deaths"].count(),
            "deaths": grouped["deaths"].sum(),
            "population": grouped["reported_population"].sum(min_count=1),
        }
    )
    summary["per_million"] = (summary["deaths"] / summary["population"] * 1_000_000).round(1)
    return summary


st.title("Road deaths by age group, 2024")
st.caption("Eurostat tran_sf_roadus and demo_pjan, retrieved 10 October 2026.")
sex = st.selectbox("Sex", ["T", "F", "M"])
table = build_table(sex)
countries = st.multiselect(
    "Countries", sorted(table["geo"].unique()), default=sorted(table["geo"].unique())
)
selected = table.loc[table["geo"].isin(countries)]
summary = summarize(selected)
st.metric("Recorded deaths", int(selected["deaths"].sum()))
st.dataframe(summary)

shown = summary.loc[summary["per_million"].notna()]
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(shown.index.astype(str), shown["per_million"])
ax.set(ylabel="Road deaths per million inhabitants")
st.pyplot(fig)
plt.close(fig)
st.download_button(
    "Download the selected cells",
    selected.to_csv(index=False),
    file_name="road-deaths-cells.csv",
    mime="text/csv",
)
