import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Input feature (independent variable)
y = np.array([2, 4, 5, 4, 5])  # Target variable (dependent variable)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Print the slope and intercept of the regression line
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Plot the data and regression line
plt.scatter(X, y, label='Actual data')
plt.plot(X, y_pred, color='red', label='Linear Regression')
plt.xlabel('X (Independent Variable)')
plt.ylabel('y (Dependent Variable)')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
