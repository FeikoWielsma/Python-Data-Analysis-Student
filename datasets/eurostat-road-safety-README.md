# Eurostat road deaths and population (2023–2024)

Real, published European statistics used by Exercise 13 and the Integration
Case (module 11). Retrieved **10 October 2026** from the Eurostat SDMX 2.1 API.
The two CSV files are the **unchanged API responses**; nothing was edited.

| File | Eurostat dataset | Query (all as SDMX-CSV) | Rows | Eurostat update |
| --- | --- | --- | --- | --- |
| `eurostat-road-deaths-2023-2024.csv` | `tran_sf_roadus`, Persons killed in road accidents by age, sex and category of persons involved, [doi:10.2908/TRAN_SF_ROADUS](https://doi.org/10.2908/TRAN_SF_ROADUS) | `tran_sf_roadus/A.....`, years 2023–2024, every dimension and geo | 12,254 | 25 Aug 2026 |
| `eurostat-population-2024.csv` | `demo_pjan`, Population on 1 January by age and sex, [doi:10.2908/DEMO_PJAN](https://doi.org/10.2908/DEMO_PJAN) | `demo_pjan/A.NR..T+F+M.{34 geos}`, year 2024 | 10,500 | 25 Sep 2026 |

The 34 population geos are exactly those in the road-death table: EU27
members, `CH`, `IS`, `LI`, `NO`, `ME`, `RS` and the `EU27_2020` aggregate.
Re-run `uv run --frozen python datasets/sources/fetch_eurostat_road_safety.py OUTPUT_DIR`
to repeat the queries; it reports whether the bytes still equal this snapshot.
Eurostat revises data, so a later download may differ legitimately.

**Licence and attribution.** Eurostat's
[copyright notice](https://ec.europa.eu/eurostat/help/copyright-notice)
authorises reuse of its statistical data for commercial or non-commercial
purposes, provided the source is acknowledged, under Commission Decision
2011/833/EU. Its non-commercial exceptions (data from sources other than
Eurostat, countries outside the EU/EFTA/candidate countries, certain trade
data) do not apply to these geos. The road-death figures are compiled by the
European Commission's DG MOVE in its CARE database and disseminated by
Eurostat; the dataset metadata states no separate restriction. Attribution:

> Source: Eurostat, doi:10.2908/TRAN_SF_ROADUS and doi:10.2908/DEMO_PJAN,
> accessed 10 October 2026. Unmodified extracts; course calculations are our own.
> Eurostat is not responsible for these calculations or interpretations.

## Variable definitions

SDMX-CSV columns shared by both files: `DATAFLOW` (dataset and version),
`LAST UPDATE` (Eurostat release time, `dd/mm/yy HH:MM:SS`, a source date),
`freq` (`A` annual), `geo` (country code; Greece is `EL`; `EU27_2020` is
the sum of the 27 member states, not a country), `TIME_PERIOD` (reference
year), `OBS_VALUE` (the number), `OBS_FLAG` (`e` estimated, `p` provisional,
`ep` both; empty if none) and `CONF_STATUS` (always empty here).

| File / column | Codes and meaning |
| --- | --- |
| deaths / `unit` | `NR` number of persons killed; `P_MHAB` Eurostat's rate per million inhabitants. **Never add the two.** |
| deaths / `sex` | `T` total, `F`, `M`, `UNK` not recorded; `T = F + M + UNK` |
| deaths / `age` | `Y_LT15`, `Y15-17`, `Y18-24`, `Y25-49`, `Y50-64`, `Y_GE65`, `UNK` (age not recorded) and `TOTAL` (their sum) |
| deaths / `pers_cat` | `DRIV` driver, `PAS` passenger, `PED` pedestrian, `UNK` not recorded, `TOTAL` (their sum) |
| population / `age` | Single years `Y_LT1` (under 1), `Y1`–`Y99`, `Y_OPEN` (100+), `UNK` and `TOTAL` |
| population / `sex` | `T`, `F`, `M`; population on **1 January 2024** |

A road death means a person killed immediately or dying within 30 days of an
injury road accident, excluding suicides; some countries apply correction
coefficients ([Eurostat metadata](https://ec.europa.eu/eurostat/cache/metadata/en/tran_sf_road_esms.htm)).
Deaths count a calendar year; population is a 1 January stock.

## Real imperfections to handle

- Totals and aggregates share columns with the detail: `TOTAL` rows,
  `T` sex and `EU27_2020` double count if summed with their parts.
- Counts and rates share `OBS_VALUE`; only `unit` distinguishes them.
- Missing data are **absent rows**, not empty values: Liechtenstein and
  Montenegro report 2024 deaths only as `TOTAL` and `UNK` (age, sex and
  road-user category not recorded), so their 2024 age bands do not exist. `LT` and `EU27_2020` have no
  `UNK` population row. No `OBS_VALUE` is empty in either file.
- The two tables use different age categories; single-year population must
  be banded (`Y_LT1` is 0, `Y_OPEN` is 100+) before it can be joined.
- Population flags: Romania estimated, Poland and EU27 estimated provisional,
  France provisional. Road deaths carry no flags in this extract.
- Eurostat publishes `P_MHAB` = 15 for the EU27 aggregate in 2024 although
  19,933 deaths among about 449 million people is about 44 per million;
  the country values are consistent. Do not trust one published number alone.

## Integration case (module 11)

Research question: **in 2024, how many road deaths per million inhabitants were
recorded in each age group across the 33 countries?** One analysis row is
one country and age group (33 × 7 = 231). Policy: use `unit == 'NR'`,
`pers_cat == 'TOTAL'`, year 2024, one sex, and drop `EU27_2020`. Band the
population as Under 15, 15–17, 18–24, 25–49, 50–64 and 65+, matching the
death codes. Keep absent counts missing, never zero. Keep unknown-age deaths
in their own group without a denominator; do not allocate them. Divide each
group's deaths by the population of the countries that report that group.

Checks: banded population equals each country's published `TOTAL`; deaths
(bands plus unknown age) equal each country's `TOTAL` row (20,875 in all);
`EU27_2020` (19,933) equals the sum of its 27 members.
`road-deaths-expected-summary.csv` is a **derived test oracle**, computed from these
files by the independent DuckDB SQL in `sources/derive_road_deaths_expected.py`.
In addition, all 186 country × age rates match Eurostat's `P_MHAB` values
after rounding. Totals for sex `T`: 18–24 has 2,518 deaths among 35,122,676
people (71.7 per million); 183 deaths have unknown age.

## Exercise 13

Task: for 2024 (`unit NR`, `sex T`, `age TOTAL`, countries only), count the
deaths per road-user category and the number of countries that report
each. In 2024 categories `DRIV`, `PAS` and `PED` are absent for
Liechtenstein and Montenegro; the `TOTAL` category is excluded because it sums the others.

## Limitations

Rates per inhabitant are not risk per kilometre travelled; exposure,
transport mode, enforcement and 30-day correction practices differ between
countries and ages. Small countries have very small counts (Liechtenstein
had 3 deaths). Association between age and rate does not establish a cause.
