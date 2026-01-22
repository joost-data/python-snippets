"""
Stacked bar chart template for grouped metrics.

Supports:
- median aggregation
- optional numeric clipping
- normalized percentage distributions
- top-N grouping with 'Other'
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assume df already exists

# =========================
# CONFIGURATION
# =========================

group_column = "Age"                       # e.g. Age, Employment
value_columns = ["JobSatPoints_6", "JobSatPoints_7"]

use_median = True                          # False → use normalized percentages
clip_column = None                         # e.g. "ConvertedCompYearly"
clip_quantile = 0.99

top_n = None                               # e.g. 6 for top categories
other_label = "Other"

# =========================
# DATA PREPARATION
# =========================

work_df = df.copy()

# Optional numeric clipping
if clip_column:
    work_df[clip_column] = pd.to_numeric(work_df[clip_column], errors="coerce")
    upper = work_df[clip_column].quantile(clip_quantile)
    work_df[clip_column] = work_df[clip_column].clip(upper=upper)

# Optional top-N grouping
if top_n:
    top_values = work_df[group_column].value_counts().head(top_n).index
    work_df[group_column] = work_df[group_column].where(
        work_df[group_column].isin(top_values), other_label
    )

# =========================
# AGGREGATION
# =========================

if use_median:
    grp = (
        work_df
        .groupby(group_column)[value_columns]
        .median()
        .dropna()
    )
else:
    grp = (
        pd.crosstab(
            work_df[group_column],
            work_df[value_columns[0]],
            normalize="index"
        ) * 100
    )

# =========================
# PLOTTING
# =========================

bottom = np.zeros(len(grp))

for col in grp.columns:
    plt.bar(grp.index.astype(str), grp[col], bottom=bottom, label=col)
    bottom += grp[col].values

plt.ylabel("Value" if use_median else "Percentage")
plt.title("Stacked Bar Chart by Group")
plt.xticks(rotation=40, ha="right")
plt.legend()
plt.show()

