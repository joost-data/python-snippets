"""
Load a CSV file into a SQLite database table.
"""

import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("survey-data.csv")

# Create SQLite DB connection
conn = sqlite3.connect("survey-data.sqlite")

# Write dataframe to database
df.to_sql("main", conn, if_exists="replace", index=False)

print("Data written to SQLite database (table: main).")

# IMPORTANT: do not close conn yet if further SQL operations follow

