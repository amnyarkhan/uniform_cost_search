

---

````markdown
# Uniform Cost Search (UCS)

This repository contains a Python implementation of **Uniform Cost Search** that works on a graph provided as a CSV file.

---

## Requirements

- Python 3.8+
- `pip`

---

## Environment Setup (Using Pipenv)

### 1. Install `pipenv`

```bash
pip install pipenv
````

### 2. Verify installation

```bash
pipenv --version
```

---

## Create and Activate the Virtual Environment

Navigate to the **project folder** and run:

```bash
pipenv shell
```

Since the `Pipfile.lock` already exists, install dependencies with:

```bash
pipenv install
```

---

## How to Run the Program

Use the following command in the terminal:

```bash
python ucs.py --file <path_to_graph_csv> --start <start_node> --goal <goal_node>
```

### Example

```bash
python ucs.py --file graph.csv --start A --goal D
```

---

## Arguments Explained

* `--file`
  Path to the CSV file representing the graph (adjacency matrix).

* `--start`
  Start node (must exist in the CSV).

* `--goal`
  Goal node (must exist in the CSV).

---

## Notes

* The CSV file must be a **square adjacency matrix**.
* Row labels and column labels must match exactly.
* Edge weights are used as costs for Uniform Cost Search.

---

## License

This project is for educational purposes.

```

---



