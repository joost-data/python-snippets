"""
Impute missing values in a categorical column using the majority value.
"""

import pandas as pd

# Assume df is already loaded

column_name = "RemoteWork"

if column_name in df.columns:
    majority_value = df[column_name].value_counts().idxmax()
    df[column_name] = df[column_name].fillna(majority_value)

    print(f"Missing values in '{column_name}' after imputation:",
          df[column_name].isnull().sum())
else:
    print(f"Column '{column_name}' not found.")

