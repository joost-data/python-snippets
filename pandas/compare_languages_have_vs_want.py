"""
Compare programming languages respondents have worked with vs want to work with.
"""

import pandas as pd

# Assume df already exists

have = (
    df["LanguageHaveWorkedWith"]
    .dropna()
    .str.split(";")
    .explode()
)

want = (
    df["LanguageWantToWorkWith"]
    .dropna()
    .str.split(";")
    .explode()
)

have_counts = have.value_counts().head(10)
want_counts = want.value_counts().head(10)

language_comparison = pd.DataFrame({
    "HaveWorkedWith": have_counts,
    "WantToWorkWith": want_counts
}).fillna(0)

print(language_comparison)

