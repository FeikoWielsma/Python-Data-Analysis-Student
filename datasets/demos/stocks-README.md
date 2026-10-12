# Stock price fixtures

- `02-intro-pandas/AAPL.csv`: weekly Apple (AAPL) prices from 3 January 2022 to the week of
  5 October 2026. Each row is one trading week labelled by its Monday. `Open` is the first open of the
  week, `High`/`Low` are the weekly extremes, `Close` is the last close, and `Volume` is the
  number of shares traded that week. Prices are in US dollars and are not adjusted for dividends.
- `05-advanced-indexing/stocks.csv`: daily close and volume for CSCO, AAPL and MSFT on
  5–7 October 2026. The rows are deliberately in a different symbol order each day.

Source: the Nasdaq historical quotes service (`api.nasdaq.com`), retrieved 11 October 2026 and
aggregated by `datasets/sources/fetch_nasdaq_stocks.py`. Use the data for teaching only; for any
other use, check Nasdaq's terms.
