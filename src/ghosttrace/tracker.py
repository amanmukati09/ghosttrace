import pandas as pd

from copy import deepcopy
from datetime import datetime
from typing import Any
from .monitor import detect_anomalies
from .reports import generate_report
from .utils import dataframe_stats
from rich.console import Console

console = Console()


class TrackedDataFrame:
    def __init__(self, df: pd.DataFrame):
        self._df = df
        self._history: list[dict[str, Any]] = []
        self._operations: list[str] = []


    def __getattr__(self, name):
        return getattr(self._df, name)

    def snapshot(self, operation: str):
        self._operations.append(operation)

        snapshot = {
            "timestamp": datetime.now(),
            "operation": operation,
            "shape": self._df.shape,
            "stats": dataframe_stats(self._df),
            "data": deepcopy(self._df),
        }

        self._history.append(snapshot)

    def history(self):
        return self._history
    def operations(self):
        return self._operations

    def trace_report(self):
        generate_report(self._history)

    def __getitem__(self, key):
        return self._df[key]

    def __setitem__(self, key, value):
        self.snapshot(f"Before modifying column: {key}")
        self._df[key] = value

        anomalies = detect_anomalies(
            self._history[-1]["data"],
            self._df,
        )

        if anomalies:
            console.print("\n[bold red]GhostTrace Warning[/bold red]")

        for anomaly in anomalies:
            console.print(f"[yellow]- {anomaly}[/yellow]")
            

    
    def drop(self, *args, **kwargs):
        self.snapshot("Before drop operation")

        result = self._df.drop(*args, **kwargs)

        self._df = result

        return self
    
    def __repr__(self):
        return (
            f"TrackedDataFrame("
            f"snapshots={len(self._history)}, "
            f"shape={self._df.shape}"
            f")\n\n"
            f"{repr(self._df)}"
        )


    def rename(self, *args, **kwargs):
        self.snapshot("Before rename operation")

        result = self._df.rename(*args, **kwargs)

        self._df = result

        return self