"""
Impute missing values in a categorical column using the mode.
"""

import pandas as pd

# Assume df is already loaded

column_name = "Employment"

if column_name in df.columns:
    most_frequent_value = df[column_name].mode()[0]
    df[column_name] = df[column_name].fillna(most_frequent_value)

    print(
        f"Missing values in '{column_name}' filled with mode:",
        most_frequent_value
    )
else:
    print(f"Column '{column_name}' not found in DataFrame.")


