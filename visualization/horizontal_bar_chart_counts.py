"""
Horizontal bar chart for category counts.
"""

import matplotlib.pyplot as plt

# Assume df already exists

branch_counts = df["MainBranch"].value_counts()

plt.barh(branch_counts.index, branch_counts.values)
plt.xlabel("Count")
plt.title("Main Branch Distribution")
plt.show()

