"""
Identify compensation-related columns in a DataFrame.
"""

import pandas as pd

# Assume df is already loaded

compensation_columns = [
    col for col in df.columns
    if "Comp" in col or "Salary" in col
]

print("Compensation-related columns:")
print(compensation_columns)

