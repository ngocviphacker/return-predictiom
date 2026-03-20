import pandas as pd

def load_data():
    df = pd.read_csv("data/raw/data.csv", encoding='latin1')
    print("Loaded data:", df.shape)
    return df