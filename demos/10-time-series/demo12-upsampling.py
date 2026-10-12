import pandas as pd

weather = pd.read_csv(
    "weather_data_austin_2010.csv",
    parse_dates=["Date"],
    date_format="%Y%m%d %H:%M",
    index_col="Date",
)
daily = weather["Temperature"].resample("D").mean().head(2).round(1)
print(daily)
print(daily.resample("6h").asfreq())
print(daily.resample("6h").ffill())
print(daily.resample("6h").interpolate())
