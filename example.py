import pandas as pd

from ghosttrace import watch


df = pd.DataFrame(
    {
        "salary": [50000, 60000, 70000],
        "age": [25, 30, 35],
    }
)

df = watch(df)

df["salary"] = df["salary"] / 1000

df["age"] = df["age"] * 1000

print(df)

df.trace_report()