import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Book2.csv')


x = df.iloc[:, 0]  # Assuming x is in the first column
y = df.iloc[:, 1]  # Assuming y is in the second column
z = df.iloc[:, 2]  # Assuming z is in the third column
color = z

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=color, cmap='viridis')

plt.colorbar(scatter, label='Voltage')

# Set labels
ax.set_xlabel('I')
ax.set_ylabel('r')
ax.set_zlabel('V')

plt.title('3D Scatter Plot with Color Scale')
plt.show()
