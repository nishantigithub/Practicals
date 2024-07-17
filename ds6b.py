import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example data
X_multiple = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])  # Multiple predictors
y_multiple = np.array([3, 5, 7, 8, 10])  # Target variable (dependent variable)

# Create a multiple linear regression model
model_multiple = LinearRegression()

# Fit the model to the data
model_multiple.fit(X_multiple, y_multiple)

# Make predictions
y_pred_multiple = model_multiple.predict(X_multiple)

# Print the coefficients and intercept of the regression model
coefficients = model_multiple.coef_
intercept = model_multiple.intercept_
print("Coefficients (Slopes):", coefficients)
print("Intercept:", intercept)

# Calculate and print R-squared
r_squared_multiple = model_multiple.score(X_multiple, y_multiple)
print("R-squared:", r_squared_multiple)

# Plot the actual data and predicted values
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.scatter(X_multiple[:, 0], X_multiple[:, 1], y_multiple, label='Actual data', color='blue')
ax.scatter(X_multiple[:, 0], X_multiple[:, 1], y_pred_multiple, label='Predicted data', color='red')
ax.set_xlabel('X1 (Predictor 1)')
ax.set_ylabel('X2 (Predictor 2)')
ax.set_zlabel('y (Dependent Variable)')
ax.set_title('Multiple Linear Regression')
ax.legend()
plt.show()
