import pandas as pd

from .tracker import TrackedDataFrame

__version__ = "0.1.1"

def watch(df: pd.DataFrame) -> TrackedDataFrame:
    """
    Wrap a pandas DataFrame with tracking capabilities.
    """
    return TrackedDataFrame(df)