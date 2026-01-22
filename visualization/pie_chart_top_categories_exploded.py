"""
Pie chart template for top-N categorical distributions.

Supports:
- single-value categorical columns
- multi-value columns separated by ';' (explode pattern)
"""

import pandas as pd
import matplotlib.pyplot as plt

# Assume df already exists

# =========================
# CONFIGURATION
# =========================

column = "LanguageHaveWorkedWith"   # column to analyze
top_n = 5
explode_values = True              # set False for single-value columns

# =========================
# DATA PREPARATION
# =========================

series = df[column].dropna()

if explode_values:
    series = (
        series
        .str.split(";")
        .explode()
    )

counts = series.value_counts().head(top_n)

# =========================
# PLOTTING
# =========================

plt.pie(
    counts.values,
    labels=counts.index,
    autopct="%1.1f%%"
)

plt.title(f"Top {top_n} {column}")
plt.show()

