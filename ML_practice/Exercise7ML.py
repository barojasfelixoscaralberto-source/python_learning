'''
Crea un modelo que prediga el salario de una persona segun sus años de experiencia
usando los datos brindados
'''

experiencia = [1,2,3,5,7,9,10,12,15,12]
salarios = [25000,30000,35000,45000,55000,65000,70000,80000,95000,120000]

'''
Aplica 80/20 y evalua con r²
'''

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

experience = np.array(experiencia).reshape(-1, 1) # feature must be 2D array
salary = np.array(salarios) # Y

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(experience, salary, test_size=0.2, random_state=42)

print(f"Entrenamiento: {len(x_train)} muestras")
print(f"Muestras: {len(x_test)} muestras")

model = LinearRegression()
model.fit(x_train, y_train)

print("Bienvenido, calcula tu salario con tu experiencia")
years_of_experience = int(input("Introduzca los años de experiencia: "))

prediction = model.predict([[years_of_experience]])

print(f"Con {years_of_experience} su salario es ${prediction[0]:,.2f}")
y_pred = model.predict(x_test)
print(f"R²: {r2_score(y_test, y_pred):.2f}")