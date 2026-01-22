"""
Count missing values per column and sort descending.
"""

import pandas as pd

# Assume df already exists

missing = df.isna().sum().sort_values(ascending=False)
print(missing.head(15))

