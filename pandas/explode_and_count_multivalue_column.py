"""
Split a multi-value column and count occurrences by group.
"""

import pandas as pd

# Assume df already exists

lang_df = df[["Country", "LanguageHaveWorkedWith"]].dropna()

lang_df = lang_df.assign(
    Language=lang_df["LanguageHaveWorkedWith"].str.split(";")
).explode("Language")

top_languages = (
    lang_df.groupby(["Country", "Language"])
    .size()
    .reset_index(name="Count")
    .sort_values(["Country", "Count"], ascending=[True, False])
)

print(top_languages.head())

