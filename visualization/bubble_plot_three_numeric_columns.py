"""
Bubble plot using a third numeric variable as size.
"""

import matplotlib.pyplot as plt
import pandas as pd

# Assume df already exists

df["TimeSearching"] = pd.to_numeric(df["TimeSearching"], errors="coerce")
df["Frustration"] = pd.to_numeric(df["Frustration"], errors="coerce")

plt.scatter(
    df["TimeSearching"],
    df["Frustration"],
    s=df["Age_num"] * 2,
    alpha=0.5
)
plt.xlabel("Time Searching")
plt.ylabel("Frustration")
plt.title("Time Searching vs Frustration (Bubble Size = Age)")
plt.show()

