"""
Understanding nunique() and axis when inspecting duplicate rows.

Goal:
Identify which columns have identical values across duplicate rows.
"""

import pandas as pd

# Assume df already exists

# Select all rows involved in duplication
duplicate_rows = df.loc[df.duplicated(keep=False)]

# Count unique values PER COLUMN (default behavior)
unique_counts = duplicate_rows.nunique(dropna=False)

print("Number of unique values per column in duplicate rows:")
print(unique_counts)

"""
IMPORTANT EXPLANATION

DataFrame.nunique() defaults to axis=0, meaning:
- It operates COLUMN-WISE
- You get one value per column

These two lines are equivalent:
    duplicate_rows.nunique()
    duplicate_rows.nunique(axis=0)

You only need axis=1 if you want ROW-WISE uniqueness,
which is NOT what you want when analyzing duplicates.
"""

# Columns where all duplicate rows have the same value
identical_columns = unique_counts[unique_counts == 1].index.tolist()

print("\nColumns with identical values across duplicate rows:")
print(identical_columns)

