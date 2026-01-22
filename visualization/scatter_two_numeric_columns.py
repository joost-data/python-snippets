"""
Scatter plot for two numeric variables.
"""

import matplotlib.pyplot as plt
import pandas as pd

# Assume df already exists

df["WorkExp"] = pd.to_numeric(df["WorkExp"], errors="coerce")

plt.scatter(df["Age_num"], df["WorkExp"], alpha=0.5)
plt.xlabel("Age")
plt.ylabel("Work Experience (Years)")
plt.title("Age vs Work Experience")
plt.show()


