import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Training data
# X and Y are regular variables but in ML they are used by default with that name
# x being the prediction data and y the target
X = np.array([[50], [75], [100], [125], [150]]) #m**2
Y = np.array([100000, 150000, 200000, 250000, 300000]) #$$$

# Here the ml model is created and trains with the data
model = LinearRegression()
model.fit(X,Y) # fit means "take the data"

# Now it should recognize patterns, let's see its prediction
prediction = model.predict([[90]])
print(f"the price for 90m² is: ${prediction[0]:,.0f}")
print(f"the price for 90m² is: ${prediction[0]:,.2f}")
print(f"the price for 90m² is: ${prediction[0]}")
# [0] prevents presenting in print the []
# : starts the format
# , separates the numbers by ,
# nf rounds the float by the n numbers after the period

# Just a reminder that everything in ML is Linear Algebra so
# Slope of a line is with coef_[]
""" Shows the changing data of the prices"""
# Intercept of a line is with intercept_
""" Shows the y touch, this is a lineal line so the intercept == 0"""
print(f"Pendiente: {model.coef_[0]:,.2f}")
print(f"Intercepto: {model.intercept_:,.2f}")

from sklearn.metrics import r2_score
# r2 shows how good is the model giving the data from 0 to 1
# 0.0 being all invented data
# 1.0 means that the data showed is perfectly calculated
# all > 0.8 is considered "good"
y_pred = model.predict(X)
r2 = r2_score(Y, y_pred)
print(f"R²: {r2:.2f}")