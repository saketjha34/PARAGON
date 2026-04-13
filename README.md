# PARAGON: Parallel Graph Processing Engine

[![License](https://img.shields.io/github/license/saketjha34/PARAGON.svg)](https://github.com/saketjha34/PARAGON/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/paragon-engine)](https://pypi.org/project/paragon-engine/)
[![GitHub issues](https://img.shields.io/github/issues/saketjha34/PARAGON.svg)](https://github.com/saketjha34/PARAGON/issues)


PARAGON is a high-performance parallel graph processing engine written in modern C++ with Python bindings via pybind11.
It provides scalable implementations of core graph algorithms like:

* Parallel BFS / DFS
* Connected Components
* PageRank (Pull + Push)
* Single Source Shortest Path (SSSP)
* Triangle Counting

Designed for:

* Multicore CPUs
* Large-scale graphs
* Systems + algorithm engineering

# Installation

## IMPORTANT

### Windows users:

You **MUST use MSVC (Visual Studio Build Tools)**

MinGW WILL FAIL
Python 3.13 + MinGW is incompatible


## Recommended Setup

### Python version

* Python 3.8 – 3.11 (RECOMMENDED)


Avoid Python 3.13 for now (ABI issues with pybind11 + MinGW)

##  Windows Setup

### 1. Install Visual Studio Build Tools

Download: [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Select:

* ✔ C++ build tools
* ✔ MSVC compiler
* ✔ Windows SDK

### 2. Install package

```bash
pip install paragon-engine
```

## Linux / Mac

### Install dependencies

```bash
sudo apt install build-essential cmake python3-dev
pip install pybind11 scikit-build-core
```

Then:

```bash
pip install paragon-engine
```

# Quick Start

## Example: Parallel BFS + DFS
```python
from paragon import Graph
from paragon.algorithms import parallel_bfs, parallel_dfs

NUM_THREADS = 4

g = Graph(5)
g.add_edges([
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4)
])

distance = parallel_bfs(graph=g, source=0, threads=NUM_THREADS)
print(distance)

visited = parallel_dfs(graph=g, source=0, threads=NUM_THREADS)
print(visited)
```

# API Overview

## Graph

```python
from paragon import Graph

g = Graph(5)
g.add_edge(0, 1)  # Adding an edge between vertices 0 and 1
g.add_edges([(1, 2), (2, 3)])  # Adding multiple edges at once

print("Vertices in the graph:", g.vertices())
print("Edges in the graph:", g.has_edge(0, 1))
print("Degree of vertex 1:", g.degree(1))
print("Adjacency List:", g.get_adj())
```

## WeightedGraph

```python
from paragon import WeightedGraph

g = WeightedGraph(5)
g.add_edge(0, 1, 2.5)  # Adding a weighted edge between vertices 0 and 1
g.add_edges([(1, 2, 3.0), (2, 3, 4.0)])  # Adding multiple weighted edges at once

print("Vertices in the graph:", g.vertices())
print("Edges in the graph:", g.has_edge(0, 1))
print("Degree of vertex 1:", g.degree(1))
print("Adjacency List:", g.get_adj())
```


## Example: Shortest Path (SSSP)

```python
from paragon import WeightedGraph
from paragon.algorithms import parallel_dijkstra

g = WeightedGraph(6)

g.add_edges([
    (0, 1, 4.0),
    (0, 2, 2.0),
    (1, 3, 5.0),
    (2, 1, 1.0),
    (2, 3, 8.0),
    (3, 4, 3.0),
    (4, 5, 1.0)
])

dist = parallel_dijkstra(g, 0)

for i, d in enumerate(dist):
    print(f"Distance from 0 → {i}: {d}")
```

# Parallel Engine Features

* Thread pool via `std::thread`
* Work partitioning (chunking)
* Atomic operations for safety
* Barrier synchronization
* Lock-based + lock-free hybrid design

# Performance

PARAGON achieves:

* Significant speedup on multicore CPUs
* Efficient memory access patterns
* Cache-aware adjacency traversal

#  Development

## Run examples (C++)

```bash
cmake -B build -G Ninja -DBUILD_TESTS=ON -DBUILD_EXAMPLES=ON -DBUILD_BENCHMARKS=ON
```

Then

```bash
cmake --build build
```

## Build locally

```bash
pip install -e .
```

## Build wheel

```bash
python -m build
```

# Contributing
PRs welcome!
For more details, see [CONTRIBUTING.md](CONTRIBUTING.md)
Suggested areas:

* New algorithms (e.g., SCC, MST)
* Performance optimizations
* Python API improvements
* Documentation

# Author
**Jha Saket Sunil**