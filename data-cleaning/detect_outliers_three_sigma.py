"""
Detect outliers using the 3-sigma rule.
"""

import pandas as pd

# Assume df already exists

column_name = "ConvertedCompYearly"

comp_df = df.dropna(subset=[column_name])

mean_val = comp_df[column_name].mean()
std_val = comp_df[column_name].std()

upper_threshold = mean_val + 3 * std_val

outliers = comp_df[comp_df[column_name] > upper_threshold]

print("Mean:", mean_val)
print("Std:", std_val)
print("Upper threshold (3σ):", upper_threshold)
print("Number of high outliers:", len(outliers))

