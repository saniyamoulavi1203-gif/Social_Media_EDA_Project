import pandas as pd
from .config import data_file

def load_data():
    df = pd.read_csv(data_file)
    return df
