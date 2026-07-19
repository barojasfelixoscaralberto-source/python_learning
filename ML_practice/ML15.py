import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random

# Creates the model with 100 trees
np.random.seed(42)
X = np.random.randint(0, 10, size=(100, 3))
Y = (X[:,0] + X[:,1] > X[:,2]).astype(int)

# trains the model
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# evaluates the model
Y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(Y_test, Y_pred):.2f}")
# here the accuracy shows a float because it evaluates 100 tress and their accuracies

# Feature importance means wich trees were the most important to take the desicion in the prediction

importances = model.feature_importances_
print("Importancia de cada feature: ")
for i, imp in enumerate(importances):
    print(f"Feature: {i}: {imp:.3f}")