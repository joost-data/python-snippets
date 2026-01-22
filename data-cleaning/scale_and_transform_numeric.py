"""
Scale and transform numeric columns (Min-Max scaling and log transform).
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Assume df already exists

column_name = "ConvertedCompYearly"

if column_name in df.columns:
    scaler = MinMaxScaler()
    df[f"{column_name}_MinMax"] = scaler.fit_transform(df[[column_name]])

    df[f"{column_name}_Log"] = np.log1p(df[column_name])

