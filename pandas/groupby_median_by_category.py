"""
Calculate median values grouped by a categorical column.
"""

import pandas as pd

# Assume df already exists

result = (
    df.groupby("ExperienceRange")["JobSat"]
    .median()
    .reset_index()
)

print(result)

