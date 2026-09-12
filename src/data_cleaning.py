import pandas as pd
from .config import cleaned_file

def clean_data(df):
    df = df.copy()

    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    print("\nDuplicate rows:", df.duplicated().sum())

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Change timestamp column to date/time format
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], errors="coerce"
    )

    # Fill missing numeric values with median
    number_columns = df.select_dtypes(include="number").columns

    for col in number_columns:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing text values with mode
    text_columns = df.select_dtypes(include="object").columns

    for col in text_columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Remove rows where timestamp is missing
    df = df.dropna(subset=["Timestamp"])

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    df.to_csv(cleaned_file, index=False)

    return df
