"""Download daily prices from Nasdaq and write the course stock fixtures.

Writes datasets/demos/02-intro-pandas/AAPL.csv (weekly AAPL, 2022 onwards) and
datasets/demos/05-advanced-indexing/stocks.csv (three symbols, three days).

    uv run --frozen python datasets/sources/fetch_nasdaq_stocks.py
"""
import json
import urllib.request
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
URL = ('https://api.nasdaq.com/api/quote/{symbol}/historical'
       '?assetclass=stocks&fromdate={start}&todate={end}&limit=9999')


def daily(symbol, start, end):
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
    request = urllib.request.Request(URL.format(symbol=symbol, start=start, end=end),
                                     headers=headers)
    rows = json.load(urllib.request.urlopen(request, timeout=60))['data']['tradesTable']['rows']
    frame = pd.DataFrame(rows).rename(columns={'date': 'Date', 'close': 'Close', 'volume': 'Volume',
                                               'open': 'Open', 'high': 'High', 'low': 'Low'})
    frame['Date'] = pd.to_datetime(frame['Date'], format='%m/%d/%Y')
    for column in ['Open', 'High', 'Low', 'Close']:
        frame[column] = frame[column].str.lstrip('$').str.replace(',', '').astype(float)
    frame['Volume'] = frame['Volume'].str.replace(',', '').astype('int64')
    return frame.set_index('Date').sort_index()[['Open', 'High', 'Low', 'Close', 'Volume']]


def weekly_aapl():
    prices = daily('AAPL', '2022-01-01', '2026-10-09')
    weeks = prices.resample('W-MON', label='left', closed='left').agg(
        {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'}).dropna()
    weeks.index.name = 'Date'
    weeks.round(2).to_csv(ROOT / 'datasets/demos/02-intro-pandas/AAPL.csv', date_format='%Y-%m-%d')


def three_stocks():
    days = ['2026-10-05', '2026-10-06', '2026-10-07']
    frames = []
    for symbol in ['CSCO', 'AAPL', 'MSFT']:
        prices = daily(symbol, days[0], days[-1]).loc[days, ['Close', 'Volume']]
        frames.append(prices.assign(Symbol=symbol).reset_index())
    # Rows come in a different symbol order each day, as in the original fixture,
    # so the slides can show why the MultiIndex needs sorting.
    stocks = pd.concat(frames).set_index(['Date', 'Symbol'])
    order = [(days[0], 'CSCO'), (days[0], 'AAPL'), (days[0], 'MSFT'),
             (days[1], 'AAPL'), (days[1], 'MSFT'), (days[1], 'CSCO'),
             (days[2], 'MSFT'), (days[2], 'CSCO'), (days[2], 'AAPL')]
    stocks = stocks.loc[[(pd.Timestamp(d), s) for d, s in order]].reset_index()
    stocks = stocks[['Date', 'Close', 'Volume', 'Symbol']]
    stocks.to_csv(ROOT / 'datasets/demos/05-advanced-indexing/stocks.csv', index=False,
                  date_format='%Y-%m-%d')


if __name__ == '__main__':
    weekly_aapl()
    three_stocks()
