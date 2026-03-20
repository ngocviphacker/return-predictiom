from src.data.load_data import load_data
from src.data.preprocess import preprocess
from src.features.build_features import build_features

from src.models.train_model import train_all_models
from src.association.apriori import run_apriori
from src.clustering.kmeans import run_kmeans

import src.data.load_data as test
print(dir(test))

def main():
    print("=== LOAD DATA ===")
    df = load_data()

    print("=== PREPROCESS ===")
    df = preprocess(df)

    print("=== FEATURE ===")
    df_model = build_features(df)

    print("=== MODEL ===")
    train_all_models(df_model)

    print("=== ASSOCIATION ===")
    run_apriori(df)

    print("=== CLUSTERING ===")
    run_kmeans(df)

    print("DONE")

if __name__ == "__main__":
    main()