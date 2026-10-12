"""Derive datasets/road-deaths-expected-summary.csv with an independent DuckDB SQL query.

Usage, from the course root (offline):

    uv run --frozen python datasets/sources/derive_road_deaths_expected.py [OUTPUT_CSV]

This deliberately shares no code with demos/11-integration-case/demo01-steps.py, so
it can serve as a test oracle for the pandas implementation. Without an
argument it prints the result and compares it with the committed file.
"""
import sys
from pathlib import Path

import duckdb

DATASETS = Path(__file__).resolve().parents[1]
DEATHS = DATASETS / 'eurostat-road-deaths-2023-2024.csv'
POPULATION = DATASETS / 'eurostat-population-2024.csv'
EXPECTED = DATASETS / 'road-deaths-expected-summary.csv'

SQL = """
WITH
groups(ord, age_group, code) AS (VALUES
    (1, 'Under 15', 'Y_LT15'), (2, '15-17', 'Y15-17'), (3, '18-24', 'Y18-24'),
    (4, '25-49', 'Y25-49'), (5, '50-64', 'Y50-64'), (6, '65+', 'Y_GE65'),
    (7, 'Unknown age', 'UNK')),
pop_raw AS (
    SELECT geo, age, CAST(OBS_VALUE AS BIGINT) AS people
    FROM read_csv($population, header = true, all_varchar = true)
    WHERE sex = 'T' AND TIME_PERIOD = '2024' AND geo <> 'EU27_2020'
      AND age NOT IN ('TOTAL', 'UNK')),
pop_years AS (
    SELECT geo, people,
           CASE age WHEN 'Y_LT1' THEN 0 WHEN 'Y_OPEN' THEN 100
                ELSE CAST(substr(age, 2) AS INTEGER) END AS years
    FROM pop_raw),
pop_bands AS (
    SELECT geo, people,
           CASE WHEN years < 15 THEN 'Under 15' WHEN years < 18 THEN '15-17'
                WHEN years < 25 THEN '18-24' WHEN years < 50 THEN '25-49'
                WHEN years < 65 THEN '50-64' ELSE '65+' END AS age_group
    FROM pop_years),
population AS (
    SELECT geo, age_group, SUM(people) AS population FROM pop_bands GROUP BY ALL),
deaths AS (
    SELECT d.geo, g.age_group, CAST(d.OBS_VALUE AS BIGINT) AS deaths
    FROM read_csv($deaths, header = true, all_varchar = true) AS d
    JOIN groups AS g ON g.code = d.age
    WHERE d.unit = 'NR' AND d.pers_cat = 'TOTAL' AND d.sex = 'T'
      AND d.TIME_PERIOD = '2024' AND d.geo <> 'EU27_2020'),
cells AS (
    SELECT c.geo, g.ord, g.age_group, p.population, d.deaths
    FROM (SELECT DISTINCT geo FROM pop_raw) AS c
    CROSS JOIN groups AS g
    LEFT JOIN population AS p ON p.geo = c.geo AND p.age_group = g.age_group
    LEFT JOIN deaths AS d ON d.geo = c.geo AND d.age_group = g.age_group)
SELECT age_group,
       COUNT(*) AS countries,
       COUNT(deaths) AS reported,
       COUNT(*) - COUNT(deaths) AS missing,
       SUM(deaths) AS deaths,
       SUM(CASE WHEN deaths IS NOT NULL THEN population END) AS population,
       SUM(deaths) * 1e6 / SUM(CASE WHEN deaths IS NOT NULL THEN population END)
           AS per_million
FROM cells
GROUP BY ord, age_group
ORDER BY ord
"""


def expected_summary():
    with duckdb.connect() as con:
        result = con.execute(SQL, {'deaths': str(DEATHS), 'population': str(POPULATION)}).df()
    # SQL sums are wide numbers; store whole-number counts as nullable integers.
    return result.astype({'deaths': 'Int64', 'population': 'Int64'})


if __name__ == '__main__':
    result = expected_summary()
    text = result.to_csv(index=False, lineterminator='\n')
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(text, encoding='utf-8', newline='\n')
    print(result.to_string(index=False))
    print('Identical to committed oracle:',
          EXPECTED.exists() and EXPECTED.read_text(encoding='utf-8') == text)
