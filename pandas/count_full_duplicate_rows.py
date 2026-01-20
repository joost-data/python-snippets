"""
Count and inspect fully duplicated rows in a pandas DataFrame.

A fully duplicated row means the entire row is identical to a previous row.
"""

import pandas as pd

# Example: assume df already exists (e.g. loaded from a CSV earlier)
# df = pd.read_csv("your_data.csv")

# Count how many rows are exact duplicates
num_full_duplicates = df.duplicated().sum()
print("Number of fully duplicated rows:", num_full_duplicates)

# Inspect the first few duplicated rows
duplicate_rows = df[df.duplicated()]
print("\nFirst duplicated rows:")
print(duplicate_rows.head())
