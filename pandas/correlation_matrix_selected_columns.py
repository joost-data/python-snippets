"""
Compute a correlation matrix for selected numeric columns.
"""

import pandas as pd

# Assume corr_df already exists (prepared beforehand)

correlation_matrix = corr_df.corr()

print(correlation_matrix)

