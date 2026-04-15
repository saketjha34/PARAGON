Benchmarks
==========

This section presents empirical benchmark results for PARAGON
across multiple graph algorithms.

The results highlight the performance gains achieved through
thread-level parallelism.



.. list-table:: Benchmark Summary
   :header-rows: 1
   :widths: 20 15 12 12 10 31

   * - Algorithm
     - Config (V,E)
     - Sequential
     - Parallel
     - Speedup
     - Key Observations

   * - SSSP (Parallel Relaxation)
     - (3000, 10000)
     - 398 ms
     - 5 ms
     - ~80x
     - Early stopping + parallel edge relaxation gives massive performance improvement.

   * - PageRank
     - (20, 20000000)
     - 3026 ms
     - 1180 ms
     - ~2.5x
     - Highly parallelizable but limited by memory bandwidth and synchronization overhead.

   * - Connected Components
     - (20, 20000000)
     - 1451 ms
     - 876 ms
     - ~1.65x
     - Gains depend on graph density; sequential DFS is efficient for smaller graphs.

   * - Triangle Counting
     - (20, 200000)
     - ~12500 ms
     - ~3600 ms
     - ~3.4x
     - Highly compute-intensive and parallel-friendly with minimal synchronization overhead.


Analysis
--------

SSSP (Parallel Relaxation)
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Achieves **~80× speedup**, the highest among all algorithms  
- Sequential version behaves like Bellman-Ford (O(V × E))  
- Parallel version benefits from:
  - Early stopping  
  - Parallel edge relaxation  

.. note::

   This demonstrates the power of parallelization for iterative relaxation algorithms.

PageRank
~~~~~~~~

- Moderate speedup (~2.5×)  
- Work is evenly distributed across nodes  
- Performance limited by:
  - Memory bandwidth  
  - Synchronization barriers  

.. tip::

   Increasing thread count beyond a point may not improve performance significantly.


Connected Components
~~~~~~~~~~~~~~~~~~~~

- Lower speedup (~1.65×) compared to other algorithms  
- Sequential DFS is already efficient due to:
  - Cache locality  
  - Low overhead  

.. note::

   Parallel gains improve with **larger and denser graphs**.

Triangle Counting
~~~~~~~~~~~~~~~~~

- Strong speedup (~3.4×)  
- Highly parallelizable due to:
  - Independent edge processing  
  - Minimal synchronization  

.. tip::

   Triangle counting benefits from multi-core systems significantly.

Key Takeaways
-------------

- Algorithms with **independent workloads** scale better  
- Synchronization-heavy algorithms show limited gains  
- Memory bandwidth becomes a bottleneck for large graphs  
- PARAGON excels in **compute-heavy parallel workloads**

Example Benchmark Code
----------------------

.. code-block:: python

    import time
    from paragon.graphs import generate_normal_graph
    from paragon.algorithms import parallel_bfs

    NUM_THREADS = 8

    g = generate_normal_graph(vertices=30, edges=100000)

    start = time.perf_counter()
    parallel_bfs(graph=g, source=0, threads=NUM_THREADS)
    end = time.perf_counter()

    elapsed_microseconds = (end - start) * 1_000_000

    print(f"Execution Time: {elapsed_microseconds:.2f} µs")

.. warning::

   Benchmark results may vary depending on:
   - Hardware configuration  
   - Graph structure  
   - Thread scheduling  

.. seealso::

   - :doc:`tutorials/algorithms/index`
   - :doc:`python_package/python_api`
   - :doc:`python_package/index`