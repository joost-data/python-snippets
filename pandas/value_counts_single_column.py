"""
Count values for a single categorical column.
"""

import pandas as pd

# Assume df already exists

column_name = "MainBranch"

if column_name in df.columns:
    counts = df[column_name].value_counts()
    print(counts)
else:
    print(f"Column '{column_name}' not found.")

