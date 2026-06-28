import pandas as pd


def business_kpis(df):
    print("\n========== KPI METRICS ==========")
    print(f"Total Sales: {df['sales'].sum():.2f}")
    print(f"Total Orders: {len(df)}")
    print(f"Average Sales: {df['sales'].mean():.2f}")


def region_sales(df):
    return df.groupby("region")["sales"].sum().reset_index()


def category_sales(df):
    return df.groupby("category")["sales"].sum().reset_index()


def subcategory_sales(df):
    return df.groupby("sub-category")["sales"].sum().reset_index()


def monthly_sales(df):
    df = df.copy()

    date_col = None
    for col in df.columns:
        if "order date" in col or "date" in col:
            date_col = col
            break

    if date_col is None:
        raise ValueError("No date column found")

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col])

    df["month"] = df[date_col].dt.to_period("M").astype(str)

    return df.groupby("month")["sales"].sum().reset_index()