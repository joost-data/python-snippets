def column_mean(df, column):
    """
    Return the mean of a numeric column.
    """
    return df[column].mean()


def unique_values(df, column):
    """
    Return unique values in a column.
    """
    return df[column].unique()

