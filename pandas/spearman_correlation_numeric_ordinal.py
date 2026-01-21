"""
Calculate Spearman correlation between numeric experience and ordinal satisfaction.
"""

import pandas as pd

# Assume df already exists

df_corr = df.copy()

df_corr["YearsCodePro"] = df_corr["YearsCodePro"].replace({
    "Less than 1 year": 0.5,
    "More than 50 years": 50
})

df_corr["YearsCodePro"] = pd.to_numeric(df_corr["YearsCodePro"], errors="coerce")

df_corr = df_corr.dropna(subset=["YearsCodePro", "JobSat"])

corr = df_corr["YearsCodePro"].corr(df_corr["JobSat"], method="spearman")

print("Spearman correlation:", corr)

