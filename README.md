# Module 01: Python

Practice Python fundamentals, functions, type hints, collections, and Git through manufacturing-quality examples.

## Requirements

- Python 3.10+

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate it:
```powershell
# Windows
.venv\Scripts\activate
```

```bash
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the tests:
```bash
pytest
```

## Exercises

- `defects.py` — logs defects and counts occurrences for Pareto-style analysis.

## Run the exercise

From this directory, run:

```bash
python defects.py
```

## Example

`log_defect` builds a defect log, and `count_defects` counts each defect:

```python
count_defects(["scratch", "dent", "scratch", "scratch"])
```

Result:

```text
{'scratch': 3, 'dent': 1}
```

`top_defects` returns the `n` most frequent defects. The default is `n=3`:

```python
log = [
    "dent", "scratch", "chip", "chip", "scratch",
    "deform", "chip", "chip", "chip", "scratch",
    "dent", "scratch",
]
top_defects(log)
```

Result:

```text
[('chip', 5), ('scratch', 4), ('dent', 2)]
```