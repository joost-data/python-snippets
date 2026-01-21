"""
Calculate the median of a numeric column for a filtered subset of rows.
"""

import pandas as pd

# Assume df already exists

filtered_df = df[df["Employment"] == "Employed, full-time"]

median_value = filtered_df["ConvertedCompYearly"].median()

print("Median annual compensation (full-time):", median_value)

