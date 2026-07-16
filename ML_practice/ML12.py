# well in real ML r2 1.0 is not usual because of a lot of unexactly data
# the real standard should be above 0.8, 0.85 is in fact perfect
# now let's see a "real" situation with unexactly data

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(42)
X_real = np.array([[50], [75], [100], [125], [150], [60], [90], [110], [80], [130]])
Y_real = np.array([100000, 150000, 200000, 250000, 300000, 120000, 175000, 210000, 160000, 260000])

real_model = LinearRegression()
real_model.fit(X_real, Y_real)

Y_pred = real_model.predict(X_real)
r2_real = r2_score(Y_real, Y_pred)
print(f"predicted price for 90m²: {real_model.predict([[90]])[0]:,.0f}")
print(f"R²: {r2_real:.2f}")

for real, pred in zip(Y_real, Y_pred):
    print(f"Real: ${real:,.0f} | Predicto: ${pred:,.0f} | Diferencia: ${abs(real-pred):,.0f}")
""" In this case, as shown in the DF, the data is relatively correct
    so that's why r2 shows 1.0 but as you can see, in the difference part
    it shows a completely split of difference that's really important in real work
"""