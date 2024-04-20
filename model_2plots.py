import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Book2.csv')

# Extract x and y data
X_I = df[['I']]  # Feature 'I' (current)
X_V = df[['V']]  # Feature 'V' (voltage)
y = df['r']  # Target (resistance)

# Create linear regression models for each feature
model_I = LinearRegression()
model_V = LinearRegression()

# Train the models
model_I.fit(X_I, y)
model_V.fit(X_V, y)

# Extract the coefficients and intercepts
m_I = model_I.coef_[0]  # Slope (m) for 'I'
m_V = model_V.coef_[0]  # Slope (m) for 'V'
b_I = model_I.intercept_  # Intercept (b) for 'I'
b_V = model_V.intercept_  # Intercept (b) for 'V'

# Plot the data points and linear regression lines for 'I' and 'V' separately
fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# Plot for feature 'I'
axes[0].scatter(df['I'], df['r'], c=df['V'], cmap='viridis', label='Data Points')
axes[0].plot(df['I'], m_I * df['I'] + b_I, color='red', label='Linear Regression (I)')
axes[0].set_xlabel('I')
axes[0].set_ylabel('r')
axes[0].set_title('Linear Regression Model for Feature I')
axes[0].legend()

# Plot for feature 'V'
axes[1].scatter(df['V'], df['r'], c=df['I'], cmap='viridis', label='Data Points')
axes[1].plot(df['V'], m_V * df['V'] + b_V, color='blue', label='Linear Regression (V)')
axes[1].set_xlabel('V')
axes[1].set_ylabel('r')
axes[1].set_title('Linear Regression Model for Feature V')
axes[1].legend()

plt.tight_layout()
plt.show()
