"""
Detect outliers using the IQR method.
"""

import pandas as pd

# Assume df already exists

column_name = "ConvertedCompYearly"

comp_df = df.dropna(subset=[column_name])

Q1 = comp_df[column_name].quantile(0.25)
Q3 = comp_df[column_name].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = comp_df[
    (comp_df[column_name] < lower_bound) |
    (comp_df[column_name] > upper_bound)
]

print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
print("Number of IQR outliers:", len(outliers))

