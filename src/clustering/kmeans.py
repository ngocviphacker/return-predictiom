from sklearn.cluster import KMeans
import pandas as pd

def run_kmeans(df):
    df_cluster = df[['CustomerID', 'Quantity', 'UnitPrice']]

    df_group = df_cluster.groupby('CustomerID').sum()

    kmeans = KMeans(n_clusters=4, random_state=42)
    df_group['Cluster'] = kmeans.fit_predict(df_group)

    print("Cluster counts:")
    print(df_group['Cluster'].value_counts())

    df_group.to_csv("data/output/clusters.csv")