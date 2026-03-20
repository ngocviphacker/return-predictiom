import yaml

def load_config(path="configs/params.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
DATA_PATH = "data/raw/data.csv"
PROCESSED_PATH = "data/processed/cleaned.csv"

TEST_SIZE = 0.2
RANDOM_STATE = 42
THRESHOLD = 0.3