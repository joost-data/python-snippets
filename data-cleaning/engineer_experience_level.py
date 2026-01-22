"""
Create experience level categories from YearsCodePro.
"""

import pandas as pd

# Assume df already exists

df["YearsCodePro"] = pd.to_numeric(df["YearsCodePro"], errors="coerce")

def experience_level(years):
    if pd.isna(years):
        return "Unknown"
    elif years < 3:
        return "Junior"
    elif years < 7:
        return "Mid"
    elif years < 15:
        return "Senior"
    else:
        return "Expert"

df["ExperienceLevel"] = df["YearsCodePro"].apply(experience_level)

