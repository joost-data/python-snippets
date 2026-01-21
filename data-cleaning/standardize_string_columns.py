"""
Standardize string-based columns (strip whitespace, normalize casing).
"""

import pandas as pd

# Assume df already exists

# Standardize Country
if "Country" in df.columns:
    df["Country"] = df["Country"].str.strip().str.title()

# Standardize Education Level
if "EdLevel" in df.columns:
    df["EdLevel"] = df["EdLevel"].str.strip()

