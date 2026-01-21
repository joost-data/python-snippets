"""
Inspect dataframe structure and identify missing values.
"""

import pandas as pd

# Assume df already exists

# Overview of dataframe structure
df.info()

# Count missing values per column (sorted)
missing_values = df.isna().sum().sort_values(ascending=False)

print("\nTop columns with missing values:")
print(missing_values.head(10))

