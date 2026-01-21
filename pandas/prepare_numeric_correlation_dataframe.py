"""
Prepare a clean numeric DataFrame for correlation analysis.
"""

import pandas as pd

# Assume df already exists

columns = ["ConvertedCompYearly", "WorkExp", "JobSatPoints_1"]

corr_df = df[columns].dropna()

print("Rows available for correlation:", len(corr_df))

