Parallel Breadth First Search (BFS)
===================================

This tutorial explains how to use the parallel BFS algorithm
to compute shortest distances in an unweighted graph using ``parallel_bfs``.


Overview
--------

Breadth-First Search (BFS) is used to traverse a graph level by level.
In PARAGON, BFS is implemented using a parallel level-synchronous approach.

This allows multiple nodes at the same level to be processed concurrently,
leading to significant performance improvements on large graphs.


Function Signature
------------------

.. code-block:: python

   from paragon.algorithms import parallel_bfs
   parallel_bfs(graph: Graph, source: int, threads: int = -1)

Parameters
----------

graph : Graph
~~~~~~~~~~~~~

The input graph.

- Must be an instance of ``Graph``  
- Should be **unweighted**  
- Must contain at least one vertex  

source : int
~~~~~~~~~~~~

Starting node for traversal.

- Must be a valid node index  
- Range: ``0 <= source < graph.vertices()``  


threads : int, optional
~~~~~~~~~~~~~~~~~~~~~~~

Number of threads to use.

- ``-1`` → automatically uses all available CPU cores  
- ``>= 1`` → manually specify number of threads  

.. code-block:: python

   NUM_THREADS = 4

.. note::

   PARAGON uses thread-level parallelism. Increasing threads allows
   better utilization of multicore CPUs.

.. warning::

   - ``threads = 0`` is invalid  
   - ``threads < -1`` is invalid  
   - Invalid thread values will raise ``ValueError``  


Return Value
------------

.. code-block:: python

   List[int]

Where:

- ``dist[i]`` = shortest distance from source to node ``i``  
- ``dist[i] = -1`` if node is unreachable  

Basic Example
-------------

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_bfs

   NUM_THREADS = 4

   g = Graph(vertices=5)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (2, 3)
   ])

   distances = parallel_bfs(
       graph=g,
       source=0,
       threads=NUM_THREADS
   )

   print(distances)

Output:

.. code-block:: text

   [0, 1, 2, 3, -1]

Explanation:

- Node 0 → distance 0  
- Node 1 → distance 1  
- Node 2 → distance 2  
- Node 3 → distance 3  
- Node 4 → unreachable  

Advanced Example
----------------

This example demonstrates BFS on a more complex graph
with multiple branches.

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_bfs

   NUM_THREADS = 4

   g = Graph(vertices=7)

   g.add_edges(edges=[
       (0, 1),
       (0, 2),
       (1, 3),
       (2, 4),
       (3, 5),
       (4, 6)
   ])

   distances = parallel_bfs(
       graph=g,
       source=0,
       threads=NUM_THREADS
   )

   print(distances)

Output:

.. code-block:: text

   [0, 1, 1, 2, 2, 3, 3]

Explanation:

- Level 0 → [0]  
- Level 1 → [1, 2]  
- Level 2 → [3, 4]  
- Level 3 → [5, 6]  

Each level is processed in parallel.

Algorithm Details
-----------------

The parallel BFS in PARAGON uses a level-synchronous (frontier-based) traversal.

At each step, all nodes in the current frontier are processed in parallel
to discover the next level.


Technique
~~~~~~~~~

- **Frontier-based traversal** (level by level)
- **Atomic updates** to avoid duplicate visits
- **Parallel processing** of nodes at each level

Pseudocode
~~~~~~~~~~

.. math::

   \textbf{Initialize:} \\
   \quad \text{dist}[v] \gets -1 \ \forall v \in V \\
   \quad \text{dist}[s] \gets 0 \\
   \quad \text{frontier} \gets \{s\} \\
   \quad \ell \gets 0

.. math::

   \textbf{While } \text{frontier} \neq \emptyset: \\
   \quad \text{next\_frontier} \gets \emptyset \\
   \quad \textbf{parallel for each } u \in \text{frontier}: \\
   \qquad \textbf{for each } v \in Adj(u): \\
   \qquad\quad \textbf{if } \text{dist}[v] = -1: \\
   \qquad\quad\quad \text{dist}[v] \gets \ell + 1 \\
   \qquad\quad\quad \text{add } v \text{ to next\_frontier} \\
   \quad \text{frontier} \gets \text{next\_frontier} \\
   \quad \ell \gets \ell + 1

.. note::

   All nodes in the same level are processed concurrently,
   enabling efficient parallel traversal.

Time Complexity
---------------

.. code-block:: text

   O(V + E)  (parallelized)

Best Practices
--------------

- Use BFS for **unweighted shortest paths**  
- Set ``threads`` close to number of CPU cores  
- Use adjacency lists for better performance  

.. tip::

   For very large graphs, parallel BFS can provide significant speedup
   compared to sequential BFS.

.. warning::

   - Invalid source node will raise ``ValueError``  
   - Passing non-Graph object will raise ``TypeError``  

.. seealso::

   - :doc:`parallel_dfs`
   - :doc:`parallel_pagerank`
   - :doc:`../graph_api_interface`
   - :doc:`../weighted_graph_api_interface`