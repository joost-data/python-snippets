"""
Common SQLite queries executed via pandas.read_sql_query().
"""

import pandas as pd

# Assume `conn` is an active sqlite3 connection

# Count rows in a table
query = "SELECT COUNT(*) FROM main"
df_count = pd.read_sql_query(query, conn)
print(df_count)

# List all tables in the database
query = """
SELECT name AS table_name
FROM sqlite_master
WHERE type = 'table'
"""
df_tables = pd.read_sql_query(query, conn)
print(df_tables)

# Group and count by a column
query = """
SELECT Age, COUNT(*) AS count
FROM main
GROUP BY Age
ORDER BY Age
"""
df_age_counts = pd.read_sql_query(query, conn)
print(df_age_counts)

# Inspect table schema (DDL)
table_name = "main"
query = f"""
SELECT sql
FROM sqlite_master
WHERE name = '{table_name}'
"""
df_schema = pd.read_sql_query(query, conn)
print(df_schema.iat[0, 0])

