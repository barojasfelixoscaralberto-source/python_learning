'''
Tienes datos de estudiantes con tres features: horas de estudio, horas de sueño y asistencia(%)
el target es aprobaron o no
divide los datos 80/20
entrena un random forest con 50 arboles 
muestra el accuracy
muestra la importancia de cada feature con su nombre "horas_estudio"
predice si un estudiante con 7 horas de estudio, 8 de sueño y 85% de asistencia aprueba o no
'''

import numpy as np

np.random.seed(42)
X = np.column_stack([
    np.random.randint(1, 10, 50),   # horas de estudio
    np.random.randint(4, 10, 50),   # horas de sueño
    np.random.randint(50, 100, 50)  # asistencia %
])
y = ((X[:, 0] * 2 + X[:, 2] / 10) > 15).astype(int)

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#flujo, 1. Arboles, 2. Entrena, 3. Evalua

model = RandomForestClassifier(n_estimators=50, random_state=42)

# entrena

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, Y_train)

# Evaluate
Y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(Y_test, Y_pred):.2f}")

importance = model.feature_importances_

feature_names = ["horas_estudio", "horas_sueño", "asistencia"]
print("Importancia de cada feature: ")
for i, im in enumerate(importance):
    print(f"{feature_names[i]}: {im:.3f}")

pred = model.predict([[7, 8, 85]])
if pred[0] == 1:
    print("El estudiante aprueba")
else:
    print("El estudiante reprueba")
