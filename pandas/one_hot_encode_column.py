"""
One-hot encode a categorical column and optionally drop the original.
"""

import pandas as pd

# Assume df already exists

column_name = "Employment"

if column_name in df.columns:
    dummies = pd.get_dummies(df[column_name], prefix=column_name)
    df = pd.concat([df, dummies], axis=1)
    df.drop(columns=[column_name], inplace=True)

