"""
Print value counts for selected columns.
"""

import pandas as pd

# Assume df already exists

columns = ["Employment", "JobSat", "YearsCodePro"]

for col in columns:
    if col in df.columns:
        print(f"\nValue counts for {col}:")
        print(df[col].value_counts(dropna=False).head(10))

