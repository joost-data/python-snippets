"""
Bubble plot template for categorical frequency analysis.

Supports:
- exploded multi-value columns (e.g. "Python;SQL")
- categorical or numeric X/Y axes
- bubble size driven by frequency or a numeric column
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assume df already exists

# =========================
# CONFIGURATION
# =========================

x_column = "Age_num"                 # numeric or categorical
y_column = "Language"                # categorical
explode_column = "LanguageHaveWorkedWith"

size_column = "count"                # usually frequency
alpha = 0.5
clip_numeric = None                  # e.g. "ConvertedCompYearly"
clip_quantile = 0.99                 # used only if clip_numeric is set

# =========================
# DATA PREPARATION
# =========================

work_df = df.copy()

# Optional numeric clipping
if clip_numeric:
    work_df[clip_numeric] = pd.to_numeric(work_df[clip_numeric], errors="coerce")
    upper = work_df[clip_numeric].quantile(clip_quantile)
    work_df[clip_numeric] = work_df[clip_numeric].clip(upper=upper)

# Explode multi-value column if provided
if explode_column:
    work_df = (
        work_df
        .dropna(subset=[explode_column, x_column])
        .assign(Category=work_df[explode_column].str.split(";"))
        .explode("Category")
    )
    y_column = "Category"

# Group and count
plot_df = (
    work_df
    .groupby([x_column, y_column])
    .size()
    .reset_index(name="count")
)

# =========================
# PLOTTING
# =========================

plt.scatter(
    plot_df[x_column],
    plot_df[y_column],
    s=plot_df[size_column],
    alpha=alpha
)

plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title("Bubble Plot of Categorical Frequency")
plt.show()

