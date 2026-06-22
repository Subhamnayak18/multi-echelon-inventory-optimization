import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw")


def read_walmart_data():
    train = pd.read_csv(RAW_DATA_PATH / "walmart" / "train.csv")
    features = pd.read_csv(RAW_DATA_PATH / "walmart" / "features.csv")
    stores = pd.read_csv(RAW_DATA_PATH / "walmart" / "stores.csv")

    return train, features, stores


def read_dataco_data():
    dataco = pd.read_csv(
        RAW_DATA_PATH / "dataco" / "DataCoSupplyChainDataset.csv",
        encoding="latin1"
    )

    return dataco