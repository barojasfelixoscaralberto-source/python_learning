'''
Carga datos.csv
muestra el describe() y filtra solo los de culiacan con score >= 75
'''
import pandas as pd
import numpy as np

df = pd.read_csv("datos.csv")
print(round(df.describe(), 2))
print(df[(df["score"] >= 75) & (df["city"] == "Culiacán")])