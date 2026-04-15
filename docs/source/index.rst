PARAGON Documentation
=====================

Parallel Graph Engine for High Performance Computing

Overview
--------

PARAGON is a high performance graph processing engine built using a hybrid
C++ + Python architecture. The core engine is implemented in `C++` with
parallel execution capabilities, enabling efficient processing of large scale
graphs using multicore CPUs. Python bindings powered by *pybind11* provide a
clean and user friendly interface, making PARAGON both powerful and accessible.

The project is designed with a focus on performance, scalability, and modularity.
It leverages `thread-level` parallelism, efficient memory usage, and optimized
graph traversal techniques to accelerate computation-heavy workloads. PARAGON
serves as a foundation for building advanced graph analytics systems and
research-oriented applications.

Currently, PARAGON supports a range of essential graph algorithms, including:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- PageRank (push and pull variants)
- Connected Components
- Single Source Shortest Path (SSSP)
- Triangle Counting

With a growing ecosystem of features, PARAGON aims to evolve into a complete
parallel graph processing framework.

Getting Started
---------------

To begin using PARAGON, follow the installation instructions and run your first
graph program:

- :doc:`install`: Complete installation guide for Linux, macOS, and Windows  
- :doc:`getting_started`: Learn how to create graphs and run algorithms  
- :doc:`tutorials/index`: Explore in depth tutorials and examples

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   getting_started
   tutorials/index
   benchmarks