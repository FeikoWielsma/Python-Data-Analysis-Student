import pandas as pd

times = pd.Series(pd.to_datetime(["2026-03-08 02:30", "2026-11-01 01:30"]))
print(times.dt.tz_localize("America/Chicago", nonexistent="shift_forward", ambiguous="NaT"))
try:
    times.dt.tz_localize("America/Chicago")
except Exception as error:
    print(type(error).__name__, error)
