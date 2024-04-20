import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Book2.csv')

X = df[['I', 'V']]  # Features
y = df['r']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)

# Extract the coefficients
b = model.intercept_  # Intercept (b)
m = m = model.coef_
m_I = model.coef_[0]  # Coefficient for 'I'
m_V = model.coef_[1]  # Coefficient for 'V'

print('Mean Squared Error:', mse)
print("Slope (m):", m)
print("Intercept (b):", b)

# Plot the data points
plt.scatter(df['I'], df['V'], c=df['r'], cmap='viridis', label='Data Points')

# Plot the linear regression line
plt.plot(df['I'], m_I * df['I'] + m_V * df['V'] + b, color='red', label='Linear Regression')

# Add labels and legend
plt.xlabel('I')
plt.ylabel('V')
plt.title('Linear Regression Model')
plt.legend()

# Show plot
plt.show()

