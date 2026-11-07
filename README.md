# Module 01: Python

Python fundamentals exercises: functions, type hints, collections, and Git workflow, applied to manufacturing quality examples.

## Exercises

- `defects.py` — logs defects and counts occurrences for Pareto-style analysis.

## Run an exercise

From this directory, run:

```bash
python defects.py
```

## Example

`log_defect` builds a defect log for `count_defects`. You can also pass a list directly:

```python
count_defects(["scratch", "dent", "scratch", "scratch"])
```

Result:

```text
{'scratch': 3, 'dent': 1}
```

## Requirements

- Python 3.10+