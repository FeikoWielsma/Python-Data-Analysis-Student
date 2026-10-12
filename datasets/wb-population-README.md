# World Bank population and income classification (Exercise 7)

Real World Bank files, retrieved **10 October 2026**, used by Exercise 7.
Re-run `uv run --frozen python datasets/sources/fetch_worldbank_population.py OUTPUT_DIR`
to download them again; it reports whether the bytes still equal this snapshot.
The World Bank refreshes WDI files, so a later download may differ legitimately.

| File | Source | Processing | Rows |
| --- | --- | --- | --- |
| `wb-wdi-population-total.csv` | WDI indicator `SP.POP.TOTL`, Population, total: `https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv`, member `API_SP.POP.TOTL_DS2_en_csv_v2_5254.csv`, WDI "Last Updated Date" 2026-10-08 | None: exact bytes from the archive | 266 |
| `wb-wdi-population-65plus.csv` | WDI indicator `SP.POP.65UP.TO`, Population ages 65 and above, total: same URL pattern, member `API_SP.POP.65UP.TO_DS2_en_csv_v2_16244.csv` | None | 266 |
| `wb-class-economies.csv` | World Bank country classification FY27 (valid 1 July 2026–30 June 2027), [`CLASS_2026_07_15.xlsx`](https://datacatalogfiles.worldbank.org/ddh-published/0037712/DR0095333/CLASS_2026_07_15.xlsx), sheet "List of economies" | Sheet saved as CSV; every value kept as text | 266 |
| `wb-class-groups.csv` | Same workbook (sha256 `260e148f…f6bed1`), sheet "composition" | Sheet saved as CSV | 2,050 |

**Licence and attribution.** The World Bank Data Catalog lists World
Development Indicators, including the classification workbook resources, under
[Creative Commons Attribution 4.0](https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators).
Attribution: "World Bank, World Development Indicators (SP.POP.TOTL,
SP.POP.65UP.TO) and country classifications FY27, CC BY 4.0, accessed
10 October 2026. Classification sheets converted to CSV."

## Variable definitions

WDI files: four metadata lines (`Data Source`, `Last Updated Date`) precede
the header `Country Name, Country Code, Indicator Name, Indicator Code,
1960 … 2025`. Each year column holds the indicator value for that year;
empty means no value. Every line ends with a comma, so pandas creates an
empty `Unnamed: 70` column. The files start with a UTF-8 byte-order mark and
use CRLF line endings. `Country Code` is a three-letter World Bank code; rows
include 217 economies and 49 aggregates such as `WLD` (World) and `HIC`.

`wb-class-economies.csv`: `Economy`, `Code`, `Region`, `Income group`,
`Lending category`. Rows 1–218 are economies (including `TWN`, Taiwan, China);
one completely empty separator row follows; the rest are aggregates with
empty income group. `wb-class-groups.csv`: `WB_Group_Code`, `WB_Group_Name`,
`WB_Country_Code`, `WB_Country_Name`; one row per **membership**, so each
economy appears once per group it belongs to (3–17 times).

## Real imperfections to handle

- Header noise, an empty trailing column and aggregates mixed with economies.
- `FCV` and `INX` appear in WDI but not in the classification; `INX`
  ("Not classified") is an empty placeholder in every year.
- `TWN` is classified (high income) but absent from WDI. The 2024 World,
  High income and East Asia & Pacific aggregates each exceed the sum of their
  published members by 23,412,899, consistent with Taiwan, China being
  included in aggregates although its own row is not published.
- The workbook's blank separator row has every field empty, including `Code`;
  pandas would match an empty key to another empty key in a merge.

## Limitations

Population counts are World Bank estimates, mostly from UN World Population
Prospects and national sources; recent years are revised. Income groups
apply to the FY27 classification and are based on 2025 GNI per capita;
earlier years used other thresholds and memberships.
