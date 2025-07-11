# Package Sorter

A simple Python utility function that classifies packages based on their dimensions and mass.

## Function Overview

The `sort()` function determines whether a package is:

- `standard`: Not bulky or heavy
- `special`: Either bulky or heavy
- `rejected`: Both bulky and heavy

Invalid input (zero or negative values) raises a `ValueError`.

## Usage

```python
from main import sort

# Example
result = sort(width=1, height=1, length=160, mass=1)
print(result)  # special
