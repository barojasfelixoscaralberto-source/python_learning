# now let's see train/test split
import numpy as np
X_real = np.array([[50], [75], [100], [125], [150], 
                   [60], [90], [110], [80], [130]]) #m²
y_real = np.array([100000, 150000, 200000, 250000, 300000,
                   120000, 175000, 210000, 160000, 260000]) # $$$

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_real, y_real, test_size =0.2, random_state = 42)

print(f"Entrenamiento: {len(X_train)} muestras") # training means what the model gets to predict the next thing
print(f"Prueba: {len(X_test)} muestras") # this means the predicting thing
# the regular should be between 80/20 or 70/30

# now let's see if that r2 still beings 1.0

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Training just with training data (8 samples)
model3 = LinearRegression()
model3.fit(X_train, y_train)

# Now valuates with prove samples (2 samples)
y_pred_test = model3.predict(X_test)
r2 = r2_score(y_test, y_pred_test)
print(f"R² en prueba: {r2:.2f}")