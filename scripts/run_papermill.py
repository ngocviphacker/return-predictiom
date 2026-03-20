import papermill as pm

notebooks = [
    "notebooks/01_eda.ipynb",
    "notebooks/02_preprocessing.ipynb",
    "notebooks/03_modeling.ipynb",
    "notebooks/04_association.ipynb",
    "notebooks/05_clustering.ipynb"
]

for nb in notebooks:
    output = nb.replace("notebooks", "outputs")
    print("Running:", nb)

    pm.execute_notebook(
        nb,
        output
    )