"""
Inspect basic structure and summary statistics of a pandas DataFrame.
"""

import pandas as pd

# Assume df is already loaded
# df = pd.read_csv("your_dataset.csv")

# Show column types, non-null counts, and memory usage
df.info()

print("\nSummary statistics (including categorical columns):")
print(df.describe(include="all"))

