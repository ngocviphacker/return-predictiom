import pandas as pd

def preprocess(df):
    df = df.dropna(subset=['CustomerID'])

    df['Return'] = df['InvoiceNo'].astype(str).apply(
        lambda x: 1 if x.startswith('C') else 0
    )

    df = df[df['Quantity'] != 0]

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    return df