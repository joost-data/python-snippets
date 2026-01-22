"""
Safely convert a salary column to numeric values.
"""

import pandas as pd

# Assume df already exists

column_name = "ConvertedCompYearly"

if column_name in df.columns:
    df[column_name] = pd.to_numeric(df[column_name], errors="coerce")
    print(f"Converted '{column_name}' to numeric.")
else:
    print(f"Column '{column_name}' not found.")

