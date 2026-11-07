# Module 01: Python

Practice Python fundamentals—functions, type hints, collections, and Git—with manufacturing quality examples.

## Exercises

- `defects.py` — logs defects and counts occurrences for Pareto-style analysis.

## Run an exercise

From this directory, run:

```bash
python defects.py
```

## Example

`log_defect` builds a defect log; `count_defects` counts each defect:

```python
count_defects(["scratch", "dent", "scratch", "scratch"])
```

Result:

```text
{'scratch': 3, 'dent': 1}
```

`top_defects` returns the `n` most frequent defects (`n=3` by default):

```python
log = ["dent", "scratch", "chip", "chip", "scratch",
    "deform", "chip", "chip", "chip", "scratch",
    "dent", "scratch"]
top_defects(log)
```

```text
[('chip', 5), ('scratch', 4), ('dent', 2)]
```

## Requirements

- Python 3.10+