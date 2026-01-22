"""
Drop duplicate rows based on specific columns (business keys).

Use this when a combination of columns should uniquely identify a row.
"""

import pandas as pd

# Assume df already exists
# df = pd.read_csv("your_dataset.csv")

# Columns that together should be unique
subset_columns = ["Country", "Employment", "RemoteWork"]

# Count duplicates based on the subset
duplicate_count = df.duplicated(subset=subset_columns).sum()
print("Duplicate rows based on columns:", duplicate_count)

# Inspect duplicate rows before dropping (optional but recommended)
duplicate_rows = df[df.duplicated(subset=subset_columns, keep=False)]
print("\nSample duplicate rows:")
print(duplicate_rows.head())

# Drop duplicates (keep first occurrence)
df = df.drop_duplicates(subset=sub

