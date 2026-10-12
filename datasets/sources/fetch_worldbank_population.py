"""Re-download the World Bank files used by Exercise 7 and re-derive the CSVs.

Usage, from the course root (network access required):

    uv run --frozen python datasets/sources/fetch_worldbank_population.py OUTPUT_DIR

The two WDI indicator CSVs are copied unchanged from the official download
archives. The classification workbook is converted sheet by sheet to CSV,
keeping every value as text exactly as stored. The World Bank refreshes WDI
files, so a later download can differ from the snapshot retrieved 2026-10-10.
The script never overwrites files in datasets/; inspect and copy deliberately.
"""
import sys
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

import pandas as pd

WDI = 'https://api.worldbank.org/v2/en/indicator/{code}?downloadformat=csv'
INDICATORS = {
    'wb-wdi-population-total.csv': 'SP.POP.TOTL',
    'wb-wdi-population-65plus.csv': 'SP.POP.65UP.TO',
}
CLASS = ('https://datacatalogfiles.worldbank.org/ddh-published/0037712/'
         'DR0095333/CLASS_2026_07_15.xlsx')
SHEETS = {
    'wb-class-economies.csv': 'List of economies',
    'wb-class-groups.csv': 'composition',
}
COMMITTED = Path(__file__).resolve().parents[1]


def report(output, name, data):
    (output / name).write_bytes(data)
    committed = COMMITTED / name
    same = committed.exists() and committed.read_bytes() == data
    print(f'{name}: {len(data)} bytes, sha256 {sha256(data).hexdigest()}, '
          f'identical to committed snapshot: {same}')


def main(output):
    output.mkdir(parents=True, exist_ok=True)
    for name, code in INDICATORS.items():
        archive = ZipFile(BytesIO(urlopen(WDI.format(code=code), timeout=180).read()))
        [member] = [n for n in archive.namelist() if n.startswith(f'API_{code}_')]
        print(f'{code}: archive member {member}')
        report(output, name, archive.read(member))
    workbook = urlopen(CLASS, timeout=180).read()
    print(f'CLASS workbook: {len(workbook)} bytes, sha256 {sha256(workbook).hexdigest()}')
    for name, sheet in SHEETS.items():
        frame = pd.read_excel(BytesIO(workbook), sheet_name=sheet, dtype=str,
                              keep_default_na=False)
        report(output, name, frame.to_csv(index=False, lineterminator='\n').encode('utf-8'))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(Path(sys.argv[1]))
