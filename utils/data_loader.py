import pandas as pd

def load_data():

    df = pd.read_csv(
        "data/indian_roads_dataset.csv"
    )

    return df