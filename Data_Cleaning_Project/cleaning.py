import pandas as pd


def load_and_clean_data():
    # Load dataset (update file name if needed)
    df = pd.read_csv("raw_data/Sample - Superstore.csv", encoding="latin1")

    # ---------------------------
    # CLEANING
    # ---------------------------
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Standardize column names
    df.columns = df.columns.str.lower()

    # Convert date column
    df["order date"] = pd.to_datetime(df["order date"], errors="coerce")

    # Remove rows with invalid dates
    df = df.dropna(subset=["order date"])

    # ---------------------------
    # FEATURE ENGINEERING (INDUSTRY LEVEL)
    # ---------------------------
    df["year"] = df["order date"].dt.year
    df["month"] = df["order date"].dt.to_period("M").astype(str)
    df["quarter"] = df["order date"].dt.quarter

    return df