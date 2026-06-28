import os
import pandas as pd

def load_and_clean_data():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "raw_data", "Sample - Superstore.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")

    df = pd.read_csv(file_path, encoding="latin1")

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df.columns = df.columns.str.lower()

    df["order date"] = pd.to_datetime(df["order date"], errors="coerce")
    df = df.dropna(subset=["order date"])

    df["year"] = df["order date"].dt.year
    df["month"] = df["order date"].dt.to_period("M").astype(str)
    df["quarter"] = df["order date"].dt.quarter

    return df
