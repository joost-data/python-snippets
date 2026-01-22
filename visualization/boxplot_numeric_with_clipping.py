"""
Box plot for a numeric column with optional upper percentile clipping.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assume df already exists

column = "ConvertedCompYearly"
clip_quantile = 0.99  # set to None if no clipping

df[column] = pd.to_numeric(df[column], errors="coerce")

values = df[column]

if clip_quantile is not None:
    upper = values.quantile(clip_quantile)
    values = values.clip(upper=upper)

plt.boxplot(values.dropna(), vert=True)
plt.ylabel(f"{column}")
plt.title(f"Box Plot of {column}")
plt.show()

