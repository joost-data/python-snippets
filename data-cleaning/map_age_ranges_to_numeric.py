"""
Map age range categories to numeric values.
"""

import pandas as pd

# Assume df already exists

age_mapping = {
    "Under 18 years old": 15,
    "18-24 years old": 21,
    "25-34 years old": 30,
    "35-44 years old": 40,
    "45-54 years old": 50,
    "55-64 years old": 60,
    "65 years or older": 70
}

df["AgeNumeric"] = df["Age"].map(age_mapping)

