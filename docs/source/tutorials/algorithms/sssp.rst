Parallel Single Source Shortest Path (SSSP)
===========================================

This tutorial explains how to compute shortest paths from a source node
in a weighted graph using ``parallel_dijkstra``.

Overview
--------

The Single Source Shortest Path (SSSP) problem computes the minimum distance
from a given source node to all other nodes in a graph.

PARAGON implements a parallel relaxation based approach inspired by
the Bellman-Ford algorithm.


Function Signature
------------------

.. code-block:: python

   from paragon.algorithms import parallel_dijkstra
   parallel_dijkstra(graph: WeightedGraph, source: int, threads: int = -1)

Parameters
----------

graph : WeightedGraph
~~~~~~~~~~~~~~~~~~~~~

The input graph.

- Must be an instance of ``WeightedGraph``  
- Edge weights must be **non-negative**  


source : int
~~~~~~~~~~~~

Starting node.

- Must satisfy: ``0 <= source < graph.vertices()``  


threads : int, optional
~~~~~~~~~~~~~~~~~~~~~~~

Number of threads to use.

- ``-1`` → use all CPU cores  
- ``>= 1`` → manual control  

.. code-block:: python

   NUM_THREADS = 4

.. note::

   Parallel relaxation allows multiple edges to be processed simultaneously,
   improving performance on large graphs.


.. warning::

   - Negative edge weights are not supported  
   - Invalid source raises ``ValueError``  
   - ``threads = 0`` is invalid  


Return Value
------------

.. code-block:: python

   List[float]

Where:

- ``dist[i]`` = shortest distance from source to node ``i``  
- ``dist[i] = INF`` if node is unreachable  


Basic Example
-------------

.. code-block:: python

   from paragon import WeightedGraph
   from paragon.algorithms import parallel_dijkstra

   NUM_THREADS = 4

   g = WeightedGraph(vertices=4)

   g.add_edges(edges=[
       (0, 1, 1.0),
       (1, 2, 2.0),
       (0, 3, 4.0)
   ])

   dist = parallel_dijkstra(
       graph=g,
       source=0,
       threads=NUM_THREADS
   )

   print(dist)

Output:

.. code-block:: text

   [0.0, 1.0, 3.0, 4.0]


Explanation:

- Node 0 → distance 0  
- Node 1 → 1  
- Node 2 → 3 (via 1)  
- Node 3 → 4  

Advanced Example
----------------

.. code-block:: python

   from paragon import WeightedGraph
   from paragon.algorithms import parallel_dijkstra

   NUM_THREADS = 4

   g = WeightedGraph(vertices=6)

   g.add_edges(edges=[
       (0, 1, 2.0),
       (0, 2, 4.0),
       (1, 2, 1.0),
       (1, 3, 7.0),
       (2, 4, 3.0),
       (4, 3, 2.0),
       (3, 5, 1.0)
   ])

   dist = parallel_dijkstra(
       graph=g,
       source=0,
       threads=NUM_THREADS
   )

   print(dist)

Output:

.. code-block:: text

   [0.0, 2.0, 3.0, 8.0, 6.0, 9.0]


Algorithm Details
-----------------

The algorithm uses parallel edge relaxation.

At each iteration:

- Each thread processes a subset of nodes  
- Edges are relaxed in parallel  
- Distances are updated if a shorter path is found  

The algorithm stops early when no updates occur.


Technique
~~~~~~~~~

- Parallel relaxation (Bellman-Ford style)
- Early stopping optimization
- Thread-level parallelism


Pseudocode
~~~~~~~~~~

.. math::

   \textbf{Initialize:} \\
   \quad dist[v] \gets \infty \ \forall v \in V \\
   \quad dist[s] \gets 0

.. math::

   \textbf{for } i = 1 \text{ to } V-1: \\
   \quad \textbf{parallel for each } u \in V: \\
   \qquad \textbf{for each } (u, v, w) \in E: \\
   \qquad\quad \textbf{if } dist[u] + w < dist[v]: \\
   \qquad\quad\quad dist[v] \gets dist[u] + w

.. note::

   Unlike classical Dijkstra, this version is more parallel-friendly
   and avoids priority queues.


Time Complexity
---------------

.. code-block:: text

   O(V × E)  (parallelized)


Best Practices
--------------

- Use for weighted graphs with non-negative weights 
- Suitable for parallel environments  
- Use appropriate thread count  


.. tip::

   Works well when graph is large and parallel hardware is available.


.. warning::

   Using negative weights may produce incorrect results.

.. seealso::

   - :doc:`parallel_bfs`
   - :doc:`parallel_dfs`    
   - :doc:`parallel_connected_components`
   - :doc:`../weighted_graph_api_interface`