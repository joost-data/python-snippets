"""
Histogram for a numeric column.
"""

import matplotlib.pyplot as plt
import pandas as pd

# Assume df already exists

column = "CompTotal"
df[column] = pd.to_numeric(df[column], errors="coerce")

plt.hist(df[column].dropna(), bins=50)
plt.xlabel(column)
plt.ylabel("Frequency")
plt.title(f"Distribution of {column}")
plt.show()

