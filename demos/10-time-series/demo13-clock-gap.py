import pandas as pd

weather = pd.read_csv(
    "weather_data_austin_2010.csv",
    parse_dates=["Date"],
    date_format="%Y%m%d %H:%M",
    index_col="Date",
)
hourly = weather["Temperature"].asfreq("h")
print(hourly.isna().sum())
print(hourly.loc["2010-03-14 01:00":"2010-03-14 05:00"])
