# Last one was about numbers, now let's see classifiers
# For this one I'll use KNN

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 0 means failed, 1 is for approved
# hours_study = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# another way, but on real work they just give u the CSV data
hours_study = np.arange(1, 11).reshape(-1, 1)
result = np.array([0,0,0,0,1,1,1,1,1,1])

X_train, X_test, Y_train, Y_test = train_test_split(hours_study, result, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(Y_test, Y_pred):.2f}")
print(f"Prediction for 4.5hours: {model.predict([[4.5]])[0]}")

