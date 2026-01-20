"""
Inspect compensation-related columns using summary statistics and skewness.
"""

import pandas as pd

# Assume df is already loaded

comp_columns = ["CompTotal", "ConvertedCompYearly"]

existing_columns = [c for c in comp_columns if c in df.columns]

if existing_columns:
    print("Summary statistics:")
    print(df[existing_columns].describe())

    print("\nSkewness:")
    print(df[existing_columns].skew())
else:
    print("No compensation columns found.")

