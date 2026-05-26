import pandas as pd

from ghosttrace import watch


df = pd.DataFrame(
    {
        "salary": [50000, 60000, 70000],
    }
)

df = watch(df)

df["salary"] = df["salary"] / 1000

print(df)

df.trace_report()