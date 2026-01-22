"""
Create experience ranges from YearsCodePro.
"""

import pandas as pd

# Assume df already exists and YearsCodePro is numeric

bins = [0, 5, 10, 20, 100]
labels = ["0-5", "5-10", "10-20", "20+"]

df["ExperienceRange"] = pd.cut(
    df["YearsCodePro"],
    bins=bins,
    labels=labels,
    right=False
)

