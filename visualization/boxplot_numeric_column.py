"""
Box plot for a numeric column.
"""

import matplotlib.pyplot as plt

# Assume df already exists

plt.boxplot(df["Age_num"].dropna())
plt.ylabel("Age")
plt.title("Box Plot of Age")
plt.show()

