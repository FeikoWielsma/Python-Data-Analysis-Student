import pandas as pd

weather = pd.read_csv(
    "weather_data_austin_2010.csv",
    parse_dates=["Date"],
    date_format="%Y%m%d %H:%M",
    index_col="Date",
)
evening = pd.date_range("2026-02-11 20:00", periods=4, freq="h")
print(evening)

expected = pd.date_range(weather.index.min(), weather.index.max(), freq="h")
missing = expected.difference(weather.index)
print(len(expected), len(weather))
print(missing)
