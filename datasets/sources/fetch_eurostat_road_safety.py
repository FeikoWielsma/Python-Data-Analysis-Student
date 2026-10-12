"""Re-download the committed Eurostat road-safety extracts and compare their hashes.

Usage, from the course root (network access required):

    uv run --frozen python datasets/sources/fetch_eurostat_road_safety.py OUTPUT_DIR

The files are the unchanged SDMX-CSV responses of the two queries below.
Eurostat revises data and refreshes the LAST UPDATE column, so a later download
can legitimately differ from the committed snapshot retrieved on 2026-10-10.
The script never overwrites files in datasets/; inspect and copy deliberately.
"""
import sys
from hashlib import sha256
from pathlib import Path
from urllib.request import urlopen

API = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/'
GEOS = ('AT+BE+BG+CH+CY+CZ+DE+DK+EE+EL+ES+EU27_2020+FI+FR+HR+HU+IE+IS+IT+LI'
        '+LT+LU+LV+ME+MT+NL+NO+PL+PT+RO+RS+SE+SI+SK')
DOWNLOADS = {
    # Every dimension, every reported geo, reference years 2023 and 2024.
    'eurostat-road-deaths-2023-2024.csv':
        API + 'tran_sf_roadus/A.....?format=SDMX-CSV&startPeriod=2023&endPeriod=2024',
    # Population on 1 January 2024, all ages, both sexes and total, for the
    # same geos as the road-death table (including its EU27_2020 aggregate).
    'eurostat-population-2024.csv':
        API + f'demo_pjan/A.NR..T+F+M.{GEOS}?format=SDMX-CSV&startPeriod=2024&endPeriod=2024',
}
COMMITTED = Path(__file__).resolve().parents[1]


def main(output):
    output.mkdir(parents=True, exist_ok=True)
    for name, url in DOWNLOADS.items():
        data = urlopen(url, timeout=180).read()
        (output / name).write_bytes(data)
        committed = COMMITTED / name
        same = committed.exists() and committed.read_bytes() == data
        print(f'{name}: {len(data)} bytes, sha256 {sha256(data).hexdigest()}, '
              f'identical to committed snapshot: {same}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(Path(sys.argv[1]))
