"""
Line chart template for grouped median analysis.

Supports:
- grouping by numeric or ordered column
- median aggregation
- optional percentile clipping
- optional range filtering
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assume df already exists

# =========================
# CONFIGURATION
# =========================

group_column = "Age_mid"              # e.g. Age_mid, WorkExp
value_column = "ConvertedCompYearly"  # metric to aggregate

clip_quantile = 0.99                  # set to None to disable clipping
min_group = None                      # e.g. 25
max_group = None                      # e.g. 45

# =========================
# DATA PREPARATION
# =========================

work_df = df[[group_column, value_column]].copy()
work_df[value_column] = pd.to_numeric(work_df[value_column], errors="coerce")

# Optional clipping
if clip_quantile:
    upper = work_df[value_column].quantile(clip_quantile)
    work_df = work_df[work_df[value_column] <= upper]

# Drop missing group values
work_df = work_df.dropna(subset=[group_column])

# Group and aggregate
grp = (
    work_df
    .groupby(group_column)[value_column]
    .median()
    .sort_index()
)

# Optional range filtering
if min_group is not None:
    grp = grp[grp.index >= min_group]

if max_group is not None:
    grp = grp[grp.index <= max_group]

# =========================
# PLOTTING
# =========================

plt.figure()
plt.plot(grp.index, grp.values, marker="o")
plt.xlabel(group_column)
plt.ylabel(f"Median {value_column}")
plt.title(f"Median {value_column} by {group_column}")
plt.show()

