def remove_outliers_iqr(df, column):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    if df[column].dtype not in ['int64', 'float64']:
        raise ValueError(f"Column '{column}' must be numeric.")
    else:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        return df[
            (df[column] >= Q1 - 1.5 * IQR) &
            (df[column] <= Q3 + 1.5 * IQR)
        ]