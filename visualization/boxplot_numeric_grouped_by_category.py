"""
Grouped box plot for a numeric column, split by a categorical column,
with optional upper percentile clipping.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assume df already exists

numeric_column = "ConvertedCompYearly"
group_column = "Employment"

clip_quantile = 0.99

df[numeric_column] = pd.to_numeric(df[numeric_column], errors="coerce")

upper = df[numeric_column].quantile(clip_quantile)

groups = []
labels = []

for value in sorted(df[group_column].dropna().unique()):
    subset = df[df[group_column] == value][numeric_column]
    subset = subset.clip(upper=upper).dropna()

    if not subset.empty:
        groups.append(subset)
        labels.append(value)

plt.boxplot(groups, labels=labels)
plt.ylabel(numeric_column)
plt.title(f"{numeric_column} by {group_column}")
plt.xticks(rotation=30)
plt.show()

