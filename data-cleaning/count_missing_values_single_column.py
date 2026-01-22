"""
Count missing values for a specific column in a pandas DataFrame.
"""

import pandas as pd

# Assume df is already loaded

column_name = "Employment"

if column_name in df.columns:
    missing_count = df[column_name].isna().sum()
    print(f"Missing values in '{column_name}':", missing_count)
else:
    print(f"Column '{column_name}' not found in DataFrame.")


