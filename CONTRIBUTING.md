# Contributing to PARAGON
Thank you for your interest in contributing to PARAGON: Parallel Graph Engine 
This document will help you set up the project, run tests, and contribute effectively.


##  Project Overview

PARAGON is a high-performance parallel graph processing engine written in C++ with Python bindings via pybind11.

# Prerequisites

## Python
- Python 3.9 – 3.11 (recommended: 3.11)

## C++ Toolchain

### Linux
```bash
sudo apt-get install build-essential cmake ninja-build
```

### Windows

* Install:
  * Visual Studio Build Tools OR MinGW
  * Ninja (`pip install ninja`)


## Python Dependencies

```bash
pip install -r requirements.txt
```

#  Running Locally

## 1. Build C++ + Run Tests

```bash
cmake -B build -G Ninja -DBUILD_TESTS=ON
cmake --build build
```

###  Run tests

#### Linux

```bash
./build/run_tests
```

#### Windows

```bash
build\run_tests.exe
```

## 2. Run Examples

```bash
cmake -B build -G Ninja -DBUILD_EXAMPLES=ON
cmake --build build
```

Run:

```bash
build/example_bfs
build/example_dfs
```

## 3. Run Benchmarks

```bash
cmake -B build -G Ninja -DBUILD_BENCHMARKS=ON
cmake --build build
```

# Python Development

## Install locally (editable)

```bash
pip install -e .
```

## Test Python API

```python
from paragon import Graph
from paragon.algorithms import dfs

g = Graph(5)
g.add_edges([(0,1), (1,2), (2,3)])

print(dfs(g, 0))
```

# Publishing to PyPI (Maintainers Only)

We use a **manual release script** for full control.

## Release Steps

### 1. Update version

Edit:

```toml
pyproject.toml
```

```toml
version = "0.1.X"
```


### 2. Run release script

```bash
python release.py 0.1.X
```

This will:

*  Update version
*  Clean build artifacts
*  Build wheel + sdist
*  Upload to PyPI
*  Tag GitHub release


## Authentication

Set environment variables:

### Windows

```bash
set TWINE_USERNAME=__token__
set TWINE_PASSWORD=pypi-xxxxxxxxxxxx
```

### Linux/Mac

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-xxxxxxxxxxxx
```

#  CI Checks

Every Pull Request runs:

*  C++ build
*  Tests (Linux + Windows)
*  PR fails if tests fail


#  Contribution Guidelines


## 🔹 Code Style

### C++

* Use modern C++17
* Avoid `bits/stdc++.h`
* Prefer explicit includes

### Python

* Type hints required
* Add docstrings for all public APIs


##  Pull Requests

Before opening PR:

* [ ] Code builds locally
* [ ] Tests pass
* [ ] No unnecessary files
* [ ] Clean commit history


# Tips

* Use **Ninja** for faster builds
* Prefer **Python 3.11**
* Keep C++ and Python APIs consistent

# Need Help?

Open an issue or start a discussion!


# Thank You

Your contributions help make PARAGON faster, better, and more scalable!