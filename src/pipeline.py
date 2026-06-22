from src.remove_duplicates import remove_duplicates
from src.missing_values import fill_mean
from src.transformation import normalize
from src.outliers import remove_outliers_iqr

def clean_data(df):
    df = remove_duplicates(df)
    print("Duplicates removed successfully!")
    print(f'Choose one option for column to fill \n {df.iloc[0,:]} ')
    df = fill_mean(df, input())  # Replace 'column_name' with the actual column name
    print("Missing values filled successfully!")
    print(f'Choose one option for column to normalize \n {df.iloc[0,:]}: ')
    df = normalize(df, input())  # Replace 'column_name' with the actual column name
    print(f'Choose one option for column to remove outliers \n {df.iloc[0,:]}: ')
    df = remove_outliers_iqr(df, input())  # Replace 'column_name' with the actual column name
    print("Outliers removed successfully!")
    return df