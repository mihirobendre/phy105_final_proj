import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Book2.csv')

# Calculate correlation matrix
corr_matrix = df.corr()

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
