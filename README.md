# GhostTrace

Track and detect suspicious pandas dataframe transformations.

GhostTrace helps developers debug silent dataframe corruption,
unexpected scaling issues, and transformation anomalies.

## Features

- Track dataframe mutations
- Detect suspicious numeric shifts
- Generate readable reports
- Lightweight and local-first
- Simple API

---

## Installation

```bash
pip install ghosttrace
```

---

## Quick Start

```python
import pandas as pd

from ghosttrace import watch

df = pd.DataFrame(
    {
        "salary": [50000, 60000, 70000]
    }
)

df = watch(df)

df["salary"] = df["salary"] / 1000

df.trace_report()
```

---

## Example Output

```text
[ghosttrace warning]
- Large scale shift detected in 'salary'

GhostTrace Report
```

---

## Development

Clone repository:

```bash
git clone YOUR_REPO_URL
```

Install dependencies:

```bash
uv sync
```

Run tests:

```bash
uv run pytest
```

---

## License

MIT