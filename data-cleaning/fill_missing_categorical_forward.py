"""
Forward-fill missing values in a categorical column.
"""

import pandas as pd

# Assume df is already loaded

column_name = "CodingActivities"

if column_name in df.columns:
    missing_before = df[column_name].isna().sum()
    print(f"Missing values before fill: {missing_before}")

    df[column_name] = df[column_name].ffill()

    missing_after = df[column_name].isna().sum()
    print(f"Missing values after fill: {missing_after}")
else:
    print(f"Column '{column_name}' not found.")


