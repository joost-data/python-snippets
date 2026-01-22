"""
Histogram for a numeric column with upper percentile clipping.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assume df already exists

column = "ConvertedCompYearly"
clip_quantile = 0.99
bins = 50

df[column] = pd.to_numeric(df[column], errors="coerce")

upper = df[column].quantile(clip_quantile)
values = df[column].clip(upper=upper)

plt.hist(values.dropna(), bins=bins)
plt.xlabel(f"{column} (clipped at {int(clip_quantile * 100)}th percentile)")
plt.ylabel("Frequency")
plt.title(f"Distribution of {column}")
plt.show()

