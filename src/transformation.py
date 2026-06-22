def normalize(df, column):
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()

    df[[column]] = scaler.fit_transform(df[[column]])  # 👈 clave aquí

    return df