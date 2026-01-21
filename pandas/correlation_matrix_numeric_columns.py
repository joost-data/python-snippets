"""
Compute a correlation matrix for numeric columns.
"""

import pandas as pd

# Assume df already exists

numeric_df = df.select_dtypes(include=["number"])

correlation_matrix = numeric_df.corr()

print(correlation_matrix)

