import pandas as pd

weather = pd.read_csv(
    "weather_data_austin_2010.csv",
    parse_dates=["Date"],
    date_format="%Y%m%d %H:%M",
    index_col="Date",
)
hourly = weather["Temperature"].asfreq("h")
print(hourly.ffill().loc["2010-03-14 02:00":"2010-03-14 04:00"])
print(hourly.interpolate(method="time").loc["2010-03-14 02:00":"2010-03-14 04:00"])
