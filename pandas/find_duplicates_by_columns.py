"""
Find and remove duplicate rows using pandas.

This file is a reference for common one-liners and patterns
used to identify, inspect, and remove duplicates in datasets.
"""

import pandas as pd

# Example: load any dataset
df = pd.read_csv("your_dataset.csv")

# --------------------------------------------------
# 1. IDENTIFY DUPLICATES
# --------------------------------------------------

# Count fully duplicated rows (entire row must be identical)
df.duplicated().sum()

# See which rows are duplicates (True = duplicate)
df.duplicated()

# View only duplicate rows
df[df.duplicated()]

# View duplicates INCLUDING the first occurrence
df[df.duplicated(keep=False)]

# --------------------------------------------------
# 2. DUPLICATES BASED ON SPECIFIC COLUMNS
# --------------------------------------------------

# Count duplicates based on selected columns
df.duplicated(subset=["MainBranch", "Employment", "RemoteWork"]).sum()

# View those duplicate rows
df[df.duplicated(subset=["MainBranch", "Employment", "RemoteWork"])]

# View all rows involved in duplication (keep=False)
df[df.duplicated(
    subset=["MainBranch", "Employment", "RemoteWork"],
    keep=False
)]

# --------------------------------------------------
# 3. ANALYSE DUPLICATES
# --------------------------------------------------

# Check which countries appear most in duplicate rows
df[df.duplicated()].value_counts("Country")

# Check employment distribution among duplicates
df[df.duplicated()].value_counts("Employment")

# --------------------------------------------------
# 4. REMOVE DUPLICATES
# --------------------------------------------------

# Remove fully duplicated rows
df_no_duplicates = df.drop_duplicates()

# Remove duplicates based on selected columns
df_no_duplicates = df.drop_duplicates(
    subset=["MainBranch", "Employment", "RemoteWork"]
)

# Keep the LAST occurrence instead of the first
df_no_duplicates = df.drop_duplicates(
    subset=["MainBranch", "Employment", "RemoteWork"],
    keep="last"
)

# --------------------------------------------------
# 5. VERIFY RESULT
# --------------------------------------------------

# Confirm no duplicates remain
df_no_duplicates.duplicated().sum()
