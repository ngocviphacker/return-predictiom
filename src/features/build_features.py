import pandas as pd

def build_features(df):
    df_model = df[['UnitPrice', 'Country', 'Return']]

    df_model = pd.get_dummies(df_model, columns=['Country'], drop_first=True)

    return df_model