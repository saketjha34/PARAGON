Get Started with PARAGON
========================

This guide will help you quickly get started with **PARAGON** and understand
how to create graphs and run algorithms using the Python API.

PARAGON is designed for **high-performance parallel graph processing**, and
all major algorithms support configurable threading for efficient execution.


Links to Other Helpful Resources
-------------------------------

Before getting started, you may find these resources useful:

- :doc:`install` Linux, macOS, and Windows  
- :doc:`benchmarks` Performance benchmarks and analysis  

.. note::

   PARAGON is built for **thread-level parallelism**.  
   Always use the ``threads`` parameter in algorithms to fully utilize
   multicore CPUs and achieve maximum performance.


Basic Usage
-----------

PARAGON provides a simple and intuitive Python interface for working with graphs.

Creating a Graph
~~~~~~~~~~~~~~~~

.. code-block:: python

   from paragon import Graph

   # Number of threads for parallel execution
   NUM_THREADS = 4

   # Create an undirected graph with 4 vertices
   g = Graph(4)

   # Add edges
   g.add_edge(0, 1)
   g.add_edge(1, 2)
   g.add_edge(2, 3)

   print("Adjacency List:", g.get_adj())

Expected output:

.. code-block:: text

   Adjacency List: [[1], [0, 2], [1, 3], [2]]

.. note::

   Graph creation itself is lightweight, but algorithms executed on this graph
   will leverage **parallel execution using NUM_THREADS**.


Working with Weighted Graphs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from paragon import WeightedGraph

   NUM_THREADS = 4

   # Create a directed weighted graph
   wg = WeightedGraph(4, directed=True)

   # Add weighted edges
   wg.add_edge(0, 1, 2.5)
   wg.add_edge(1, 2, 1.2)
   wg.add_edge(2, 3, 3.7)

   print("Weighted Adjacency:", wg.get_adj())

Expected output:

.. code-block:: text

   Weighted Adjacency: [[(1, 2.5)], [(2, 1.2)], [(3, 3.7)], []]

.. note::

   Weighted graphs are commonly used with parallel algorithms such as
   shortest path computation, where **thread-level parallelism** significantly
   improves performance.


Running a Parallel Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PARAGON algorithms are designed to run in parallel using multiple threads.

.. code-block:: python

   from paragon import WeightedGraph
   from paragon.algorithms import parallel_dijkstra

   # Define number of threads
   NUM_THREADS = 4

   wg = WeightedGraph(4, directed=True)

   wg.add_edges([
       (0, 1, 1.0),
       (1, 2, 2.0),
       (0, 3, 4.0),
       (2, 3, 1.0)
   ])

   # Run parallel SSSP
   dist = parallel_dijkstra(wg, source=0, threads=NUM_THREADS)

   print("Shortest distances:", dist)

Expected output:

.. code-block:: text

   Shortest distances: [0.0, 1.0, 3.0, 4.0]

.. note::

   The ``threads`` parameter controls the degree of parallelism.
   Increasing the number of threads enables **true concurrent execution**
   and improves performance on multicore systems.


Next Steps
----------

Now that you understand the basics, you can:

- Run BFS, DFS, PageRank, and Triangle Counting in parallel  
- Experiment with different thread counts to analyze performance  
- Use larger graphs to fully leverage PARAGON's parallel engine  


.. tip::

   For best performance, set ``NUM_THREADS`` close to the number of CPU cores
   available on your system.

   PARAGON is optimized for **pure concurrency and thread-level parallelism**,
   making it highly efficient for large-scale graph processing.