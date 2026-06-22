def fill_mean(df, column):
    if df[column].dtype in ['float64', 'int64']:
        df[column] = df[column].fillna(df[column].mean())
    else:
        raise ValueError(f"Column '{column}' is not numeric and cannot be filled with mean.")
    return df

