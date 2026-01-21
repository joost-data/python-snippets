"""
Remove outliers from a numeric column using the IQR method.
"""

import pandas as pd

# Assume df already exists

column_name = "ConvertedCompYearly"

Q1 = df[column_name].quantile(0.25)
Q3 = df[column_name].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_no_outliers = df[
    (df[column_name] >= lower_bound) &
    (df[column_name] <= upper_bound)
]

print("Rows before:", len(df))
print("Rows after outlier removal:", len(df_no_outliers))

