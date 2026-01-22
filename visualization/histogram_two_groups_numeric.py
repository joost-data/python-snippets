"""
Compare a numeric distribution across two groups using histograms.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assume df already exists

numeric_column = "ConvertedCompYearly"
group_column = "Age_num"

group_a_value = 30
group_b_value = 50

clip_quantile = 0.99
bins = 40

df[numeric_column] = pd.to_numeric(df[numeric_column], errors="coerce")

upper = df[numeric_column].quantile(clip_quantile)

group_a = df[df[group_column] == group_a_value][numeric_column].clip(upper=upper)
group_b = df[df[group_column] == group_b_value][numeric_column].clip(upper=upper)

plt.hist(group_a.dropna(), bins=bins, alpha=0.6, label="Group A")
plt.hist(group_b.dropna(), bins=bins, alpha=0.6, label="Group B")

plt.xlabel(numeric_column)
plt.ylabel("Frequency")
plt.title("Numeric Distribution by Group")
plt.legend()
plt.show()

