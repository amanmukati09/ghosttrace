import pandas as pd

from ghosttrace import watch


def test_watch_returns_wrapper():
    df = pd.DataFrame({"a": [1, 2]})

    tracked = watch(df)

    assert tracked is not None


def test_column_modification():
    df = pd.DataFrame({"a": [1, 2]})

    tracked = watch(df)

    tracked["a"] = tracked["a"] * 10

    assert tracked["a"].iloc[0] == 10