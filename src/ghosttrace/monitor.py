import pandas as pd


def detect_anomalies(before: pd.DataFrame, after: pd.DataFrame):
    anomalies = []

    numeric_columns = before.select_dtypes(include="number").columns

    for column in numeric_columns:
        before_mean = before[column].mean()
        after_mean = after[column].mean()

        if before_mean == 0:
            continue

        ratio = after_mean / before_mean

        if ratio > 100:
            anomalies.append(
                f"Extreme increase detected in '{column}' "
                f"({before_mean:.2f} → {after_mean:.2f})"
            )

        elif ratio < 0.01:
            anomalies.append(
                f"Extreme reduction detected in '{column}' "
                f"({before_mean:.2f} → {after_mean:.2f})"
            )

        before_nulls = before[column].isna().sum()
        after_nulls = after[column].isna().sum()

        if after_nulls > before_nulls:
            anomalies.append(
                f"New null values introduced in '{column}' "
                f"({before_nulls} → {after_nulls})"
            )

    return anomalies