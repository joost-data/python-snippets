"""
Count missing values for all columns in a pandas DataFrame.
"""

import pandas as pd

# Assume df is already loaded

missing_values = df.isna().sum()

print("Missing values per column:")
print(missing_values)


