from src.data_loader import load_csv
from src.pipeline import clean_data

def main():

    # Cargar datos
    df = load_csv("data/raw/zoo2.csv")

    # Mostrar información del dataset
    df.head()
    df.info()
    df.describe()

    # Limpiar datos
    if input("Do you want to clean the dataset? (y/n): ").lower() == "y":
        clean_df = clean_data(df)
        print("Dataset cleaned successfully!")
    else:
        print("Skipping data cleaning.")

    # Save cleaned dataset
    if input("Do you want to save the cleaned dataset? (y/n): ").lower() == "y":
        clean_df.to_csv(
            "data/processed/clean_zoo2.csv",
            index=False
        )
        print("Dataset saved successfully!")

if __name__ == "__main__":
    main()