# Contributing to PARAGON
Thank you for your interest in contributing to PARAGON: Parallel Graph Engine 
This document will help you set up the project, run tests, and contribute effectively.


##  Project Overview
PARAGON is a high-performance parallel graph processing engine written in C++ with Python bindings via pybind11.


## Prerequisites (for Local Development)

To develop PARAGON locally (C++ + Python), you need a working setup for:

```text
✔ Python environment
✔ C++ compiler toolchain
✔ Build system (CMake + Ninja)
✔ Python ↔ C++ binding support (pybind11)
```

### Python Requirements

* **Python version:** `3.9 – 3.11` (recommended: **3.11**)
* Ensure Python is added to PATH


### C++ Toolchain

#### Linux (Ubuntu/Debian)

Install:

```bash
sudo apt-get update
sudo apt-get install -y build-essential cmake ninja-build
```

Includes:

* `g++` → compiler
* `make` → build tool (fallback)
* `cmake` → build system
* `ninja` → fast build backend (recommended)


#### Windows

##### Option 1 (Recommended): MSVC Toolchain

Install **Visual Studio Build Tools**
 
[Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Select during installation:

```text
✔ Desktop development with C++
✔ MSVC v143 (or latest)
✔ Windows 10/11 SDK
✔ CMake tools for Windows
```


### Build Tools

#### CMake (Required)

Minimum version: **3.16+**

Check:

Ubuntu:
```bash
sudo apt install -y cmake
cmake --version
```

Windows:
```bash
pip install cmake
cmake --version
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

# Python Development Setup

## 1. Create a Virtual Environment

```bash
python -m venv .venv
```

* Creates an isolated Python environment inside `.venv/`
* Keeps project dependencies separate from system Python

## 2. Activate the Virtual Environment

### Linux / macOS:

```bash
source .venv/bin/activate
```

### Windows:

```bash
.venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

* Installs all required Python dependencies for development
* Includes tools like `pytest`, `pybind11`, etc.

## 4. Install PARAGON in Editable Mode

```bash
pip install -e .
```

* Installs the package **in development mode**
* Any changes you make in the source code are immediately reflected
* No need to reinstall after every change

## 5. Build the Package (Optional but Recommended)

```bash
python -m build
```

* Builds distributable files:

  * `.whl` (wheel)
  * `.tar.gz` (source)

```text
dist/
├── paragon_engine-0.x.x-py3-none-any.whl
└── paragon_engine-0.x.x.tar.gz
```

## 6. Run Tests

```bash
pytest python/tests -v
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

*  C++ build, pytest test
*  Tests (Linux + Windows)
*  PR fails if tests fail


#  Contribution Guidelines

## Code Style

### C++

* Use modern C++17
* Avoid `bits/stdc++.h`
* Prefer explicit includes

### Python

* Type hints required
* Add docstrings for all public APIs

##  Pull Requests

Before opening a PR:

* [ ] Code builds locally
* [ ] Tests pass
* [ ] No unnecessary files
* [ ] Clean commit history


# Need Help?

Open an issue or start a discussion!


# Thank You

Your contributions help make PARAGON faster, better, and more scalable!