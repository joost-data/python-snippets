def explore_dataframe(df, head_rows=5):
    """
    Perform basic exploratory checks on a DataFrame.
    Prints shape, column types, and preview rows.
    """
    print("Shape:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

    print("Data types:")
    print(df.dtypes, "\n")

    print(f"First {head_rows} rows:")
    print(df.head(head_rows))

