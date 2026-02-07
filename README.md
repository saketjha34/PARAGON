# PARAGON — Parallel Graph Engine

**PARAGON (PARAllel Graph ENgine)** is a high-performance **C++ parallel graph processing engine** 
that implements and benchmarks core graph algorithms on multicore CPUs.

The project focuses on:

* efficient parallel execution
* algorithm-level parallelism
* scalable graph analytics
* reproducible performance evaluation


## Project Structure

```
PARAGON/
├── include/        # Public headers
├── src/            # Core engine & algorithms
├── examples/       # Usage examples
├── benchmark/      # Performance benchmarks
├── tests/          # Unit tests
├── CMakeLists.txt
└── README.md
```


## Implemented Algorithms

| Algorithm                          | Parallel Strategy           | Use Case                    |
| ---------------------------------- | --------------------------- | --------------------------- |
| Breadth-First Search (BFS)         | Frontier-level parallelism  | Reachability, traversal     |
| PageRank (Pull)                    | Vertex-level parallelism    | Ranking, influence          |
| PageRank (Push/BFS-style)          | Edge-level parallelism      | Large web graphs            |
| Connected Components               | Hooking + pointer jumping   | Clustering, segmentation    |
| Single Source Shortest Path (SSSP) | Parallel edge relaxation    | Routing, network analysis   |
| Triangle Counting                  | Vertex-level + intersection | Graph analytics, clustering |


## Parallelism Model

PARAGON uses a lightweight parallel execution engine based on:

* static work partitioning
* thread-level parallelism
* per-thread local aggregation
* barrier synchronization when required

Parallelism is applied at different levels depending on the algorithm:

* **Vertex-level**: PageRank, Triangle Counting
* **Edge-level**: SSSP, PageRank (push)
* **Frontier-level**: BFS
* **Structure-level**: Connected Components



## 🛠️ Build & Installation (CMake)

### Requirements

* C++17 compatible compiler (GCC / MinGW)
* CMake ≥ 3.16

### Build Steps

```bash
git clone https://github.com/saketjha34/PARAGON.git
cd PARAGON
mkdir build
cd build
cmake -G "MinGW Makefiles" ..
cmake --build .
```

All executables are generated in the `build/` directory.


## Running Tests

```bash
cd build
run_tests
```


## Running Examples

```bash
example_bfs
example_pagerank
example_parallel_pagerank_bfs
example_connected_components
example_sssp
example_triangle_count
```

Each example uses a deterministic graph definition.


## Running Benchmarks

```bash
benchmark_sssp
benchmark_pagerank
benchmark_connected_components
benchmark_triangle_count
```


## Benchmark Results

Benchmarks were executed using **8 threads** on a multicore CPU.

### Single Source Shortest Path (SSSP)

```
V = 3000, E = 10000
```

| Version    | Time   |
| ---------- | ------ |
| Sequential | 398 ms |
| Parallel   | 5 ms   |

**Speedup:** ~79×

Parallelism is applied through concurrent edge relaxations and early convergence.


### PageRank

```
V = 20, E = 20,000,000
```

| Version    | Time    |
| ---------- | ------- |
| Sequential | 3026 ms |
| Parallel   | 1180 ms |

**Speedup:** ~2.6×

Parallelism is applied at the vertex and edge levels with synchronization per iteration.


### Connected Components

```
V = 20, E = 20,000,000
```

| Version    | Time    |
| ---------- | ------- |
| Sequential | 1451 ms |
| Parallel   | 876 ms  |

**Speedup:** ~1.65×

Uses a parallel hooking and pointer-jumping strategy.


### Triangle Counting

```
V = 20, E = 200,000
```

| Version    | Time     |
| ---------- | -------- |
| Sequential | 12478 ms |
| Parallel   | 3598 ms  |

**Speedup:** ~3.4×

Parallelism is applied through independent adjacency list intersections.