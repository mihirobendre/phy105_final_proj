import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Book2.csv')

# Display the DataFrame
print(df)
sns.pairplot(df)
plt.show()
