from src.remove_duplicates import remove_duplicates
from src.missing_values import fill_mean
from src.transformation import normalize
from src.outliers import remove_outliers_iqr

def clean_data(df):
    df = remove_duplicates(df)
    df = fill_mean(df, 'column_name')  # Replace 'column_name' with the actual column name
    df = normalize(df, 'column_name')  # Replace 'column_name' with the actual column name
    df = remove_outliers_iqr(df, 'column_name')  # Replace 'column_name' with the actual column name
    return df