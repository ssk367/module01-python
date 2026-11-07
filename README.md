# Module 01: Python Fundamentals

Python fundamentals exercises (functions, type hints, collections, testing, and Git workflow) applied to manufacturing quality problems.

## Requirements

- Python 3.10+

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate it:

   ```powershell
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
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
   pytest -v
   ```

## Project structure

| File | Purpose |
|---|---|
| `defects.py` | Log defects and rank them for Pareto-style analysis |
| `spc.py` | Calculate Individuals (I-MR) chart control limits using the moving-range method |
| `test_defects.py`, `test_spc.py` | Automated tests (pytest) |

## Examples

### Defect analysis (`defects.py`)

`count_defects` counts each defect type:

```python
count_defects(["scratch", "dent", "scratch", "scratch"])
# {'scratch': 3, 'dent': 1}
```

`top_defects` returns the `n` most frequent defects (default `n=3`):

```python
log = [
    "dent", "scratch", "chip", "chip", "scratch",
    "deform", "chip", "chip", "chip", "scratch",
    "dent", "scratch",
]
top_defects(log)
# [('chip', 5), ('scratch', 4), ('dent', 2)]
```

Run the demo: `python defects.py`

### SPC control limits (`spc.py`)

`individual_limits` returns `(LCL, center line, UCL)`, with sigma estimated as MR̄ / d₂ (d₂ = 1.128):

```python
individual_limits([10.3, 12.1, 11.6, 13.3, 12.0])
# (8.34, 11.86, 15.38)  ← rounded to 2 decimals
```

Raises `ValueError` if fewer than two readings are given, since a moving range needs a pair.