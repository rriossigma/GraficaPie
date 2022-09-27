import pandas as pd
import matplotlib as plt

df = pd.read_csv('athlete_events.csv')

agrupado = df.groupby(["Year", "Medal", "Season"])
#agrupado["Total_Medals"] = agrupado["Medal_Gold"] + agrupado["Medal_Silver"] + agrupado["Medal_Bronze"]

print(agrupado)