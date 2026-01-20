"""
Count and remove duplicate rows from a pandas DataFrame.
"""

import pandas as pd

# Assume df is already loaded

duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")

df = df.drop_duplicates()

print(f"Shape after removing duplicates: {df.shape}")


