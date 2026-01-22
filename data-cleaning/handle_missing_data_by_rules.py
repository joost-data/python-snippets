"""
Handle missing data using explicit, defensible rules.
"""

import pandas as pd

# Assume df already exists

# Drop rows missing critical categorical outcomes
df = df.dropna(subset=["Employment", "JobSat"])

# Fill missing RemoteWork with neutral category
if "RemoteWork" in df.columns:
    df["RemoteWork"] = df["RemoteWork"].fillna("Unknown")

# Convert YearsCodePro to numeric
if "YearsCodePro" in df.columns:
    df["YearsCodePro"] = pd.to_numeric(df["YearsCodePro"], errors="coerce")

# Inspect remaining missing values
print(
    df[["Employment", "RemoteWork", "JobSat", "YearsCodePro"]]
    .isna()
    .sum()
)

