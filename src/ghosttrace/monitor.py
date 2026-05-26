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

        if ratio > 100 or ratio < 0.01:
            anomalies.append(
                f"Large scale shift detected in '{column}' "
                f"({before_mean:.2f} → {after_mean:.2f})"
            )

    return anomalies