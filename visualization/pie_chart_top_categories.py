"""
Pie chart for top N categories.
"""

import matplotlib.pyplot as plt

# Assume df already exists

top_n = 5
top_db = df["DatabaseWantToWorkWith"].value_counts().head(top_n)

plt.pie(top_db.values, labels=top_db.index, autopct="%1.1f%%")
plt.title(f"Top {top_n} Databases Respondents Want to Learn")
plt.show()

