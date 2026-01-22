"""
Bar chart of median values for selected columns.
"""

import matplotlib.pyplot as plt
import pandas as pd

# Assume df already exists

df["TimeAnswering"] = pd.to_numeric(df["TimeAnswering"], errors="coerce")

subset = df[(df["Age_num"] >= 30) & (df["Age_num"] <= 35)]
medians = subset[["TimeSearching", "TimeAnswering"]].median()

plt.bar(["Searching", "Answering"], medians)
plt.ylabel("Minutes")
plt.title("Median Time Searching vs Answering (Age 30–35)")
plt.show()

