import pandas as pd
from copy import deepcopy


class TrackedDataFrame:
    def __init__(self, df: pd.DataFrame):
        self._df = df
        self._history = []

    def snapshot(self, operation: str):
        self._history.append(
            {
                "operation": operation,
                "data": deepcopy(self._df),
            }
        )

    def trace_report(self):
        print("[ghosttrace]")
        print(f"Snapshots stored: {len(self._history)}")

    def __getitem__(self, key):
        return self._df[key]

    def __setitem__(self, key, value):
        self.snapshot(f"Before modifying column: {key}")
        self._df[key] = value

    def __repr__(self):
        return repr(self._df)