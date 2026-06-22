from src.data_loader import load_csv
from src.pipeline import clean_data

def main():

    # Cargar datos
    df = load_csv("data/raw/zoo2.csv")

    # Limpiar datos
    clean_df = clean_data(df)

    # Guardar resultado
    clean_df.to_csv(
        "data/processed/clean_zoo2.csv",
        index=False
    )

    print("Dataset cleaned successfully!")

if __name__ == "__main__":
    main()