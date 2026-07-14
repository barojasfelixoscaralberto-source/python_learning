'''
Crea un Dataframe con datos de 5 estudiantes: name, grade (0-100), subject
Filtra los que tienen grade mayor a 70 
Muestra solo sus nombres y calificaciones
'''
"""PART ONE"""
import pandas as pd

data = {
    "name": ["Oscar", "Angy", "Maria", "Pedro", "Yorii"],
    "grade": [90, 100, 80, 35, 60],
    "subject": ["ISC", "IPI", "FCA", "ISC", "QFB"]
}

df = pd.DataFrame(data)
# print(df[df["grade"] >= 70]) as normal filter
print(df[df["grade"] >= 70][["name", "grade"]])