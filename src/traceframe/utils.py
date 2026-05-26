import pandas as pd


def dataframe_stats(df: pd.DataFrame):
    stats = {}

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        stats[column] = {
            "mean": float(df[column].mean()),
            "min": float(df[column].min()),
            "max": float(df[column].max()),
            "std": float(df[column].std()),
        }

    return stats
