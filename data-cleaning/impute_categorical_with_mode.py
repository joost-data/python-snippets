"""
Impute categorical columns using the most frequent value (mode).
"""

import pandas as pd

# Assume df already exists

column_name = "RemoteWork"

if column_name in df.columns:
    df[column_name] = df[column_name].fillna(df[column_name].mode()[0])

