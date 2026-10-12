import pandas as pd

with open("station-readings.txt") as file:
    print(file.read())

readings = pd.read_csv("station-readings.txt", sep=";", skiprows=2, comment="#")
print(readings)

same = pd.read_csv("station-readings.txt", sep=";", header=2, comment="#")
print(same.equals(readings))
