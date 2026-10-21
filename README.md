# DATA 4000 Assignment 5

This repository contains two terminal-based Python programs. Both prompt for
your student key and use the sum of its stripped characters' Unicode code
points as a seed.

## Requirements

- Python 3.x
- `requests` for the inventory API spot check

Install the dependency with:

```bash
pip install requests
```

## Running the programs

Run each program from a terminal in the repository directory:

```bash
python3 pos_checkout.py
python3 inventory_spotcheck.py
```

## Example: `pos_checkout.py`

Example interaction (input appears after each prompt):

```text
Student key: A
Item name (or DONE to finish): Campus hoodie
Unit price: 25
Quantity: 2
Item name (or DONE to finish): Notebook
Unit price: 2.50
Quantity: 2
Item name (or DONE to finish): DONE
Seed: 65
Units: 4
Subtotal: $55.00
Discount: 0%
Perk applied: YES
Total: $52.00
```

## Example: `inventory_spotcheck.py`

The API response may change over time; this example shows a successful run
returning five songs.

```text
Student key: A
SKU: PEN-01
On hand: 4
REORDER
SKU: NOTE-02
On hand: 20
OK
SKU: DONE
Seed: 65
Threshold: 9
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: drake
Songs returned: 5
API status: OK
```