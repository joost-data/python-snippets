"""
Create a crosstab between two categorical columns.
"""

import pandas as pd

# Assume df already exists

crosstab = pd.crosstab(df["Employment"], df["EdLevel"])

print(crosstab)

