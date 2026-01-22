"""
Scatter plot templates for numeric analysis:
- optional percentile clipping
- optional trend line
- optional grouping
- optional bubble size encoding
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assume df already exists

# -------------------------------
# Configuration
# -------------------------------

x_col = "Age_num"
y_col = "JobSatPoints_6"

clip_column = None            # e.g. "ConvertedCompYearly"
clip_quantile = 0.99          # set to None to disable

group_column = None           # e.g. "Employment"
size_column = None            # e.g. "Age_num"
add_trendline = False

# -------------------------------
# Data preparation
# -------------------------------

plot_df = df[[x_col, y_col]].copy()

if clip_column:
    df[clip_column] = pd.to_numeric(df[clip_column], errors="coerce")
    upper = df[clip_column].quantile(clip_quantile)
    plot_df[clip_column] = df[clip_column].clip(upper=upper)

plot_df = plot_df.dropna()

# -------------------------------
# Plotting
# -------------------------------

if group_column:
    for value in df[group_column].dropna().unique():
        subset = df[df[group_column] == value]
        plt.scatter(
            subset[x_col],
            subset[y_col],
            alpha=0.4,
            label=value
        )
    plt.legend()

else:
    sizes = plot_df[size_column] * 2 if size_column else None
    plt.scatter(
        plot_df[x_col],
        plot_df[y_col],
        s=sizes,
        alpha=0.4
    )

# -------------------------------
# Trend line (optional)
# -------------------------------

if add_trendline:
    coef = np.polyfit(plot_df[x_col], plot_df[y_col], 1)
    trend = np.poly1d(coef)
    plt.plot(plot_df[x_col], trend(plot_df[x_col]))

# -

