"""
Impute numeric columns using the median (robust to outliers).
"""

import pandas as pd

# Assume df already exists

numeric_columns = ["ConvertedCompYearly", "WorkExp"]

for col in numeric_columns:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

