from .tracker import TrackedDataFrame


def watch(df):
    return TrackedDataFrame(df)

