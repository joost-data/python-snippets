"""
Drop rows where all specified key columns are missing.
"""

import pandas as pd

# Assume df already exists

key_columns = ["Employment", "JobSat", "YearsCodePro"]

df_clean = df.dropna(subset=key_columns, how="all")

print("Shape after cleaning:", df_clean.shape)

