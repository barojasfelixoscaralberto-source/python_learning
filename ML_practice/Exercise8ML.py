'''
Carga datos.csv 
usa age como feature y score como target
aplica flujo de entrenamiento con un modelo de regresion lineal
divide 80/20 y evalua con r²
al cargar desde pandas, x deberia ser:
df[["age]]
'''

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("datos.csv")
print(df)

X = np.array(df[["age"]])
Y = np.array(df[["score"]])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=2, random_state=42) #80/20

print(f"Entrenamiento: {len(X_train)} muestras")
print(f"Muestras: {len(X_test)} muestras")

model = LinearRegression()
model.fit(X_train, Y_train)

age = int(input("Introduce una edad: "))
pred = model.predict([[age]])

result = float(pred[0][0]) # two [0] cause is a 2D array
print(f"Con {age} años, tu promedio es de: {result:.2f}")
Y_pred = model.predict(X_test)
print(f"R²: {r2_score(Y_test, Y_pred):.2f}")

