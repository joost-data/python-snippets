"""
Normalize a numeric column using median imputation,
Min-Max scaling, and Z-score normalization.
"""

import pandas as pd

# Assume df is already loaded

column_name = "ConvertedCompYearly"

if column_name in df.columns:
    # Handle missing values using median
    median_value = df[column_name].median()
    df[column_name] = df[column_name].fillna(median_value)

    # Min-Max normalization
    min_val = df[column_name].min()
    max_val = df[column_name].max()
    df[f"{column_name}_MinMax"] = (
        (df[column_name] - min_val) / (max_val - min_val)
    )

    # Z-score normalization
    mean_val = df[column_name].mean()
    std_val = df[column_name].std()
    df[f"{column_name}_Zscore"] = (
        (df[column_name] - mean_val) / std_val
    )

    print("Normalization complete.")
else:
    print(f"Column '{column_name}' not found.")

