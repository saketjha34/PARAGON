Python API Reference
====================

This page provides the complete Python API reference for PARAGON.

Core Data Structures
--------------------

.. automodule:: paragon.core

.. autoclass:: paragon.Graph
   :members:
   :special-members: __init__, __repr__, __str__, __len__, __contains__, __getitem__, __iter__, __eq__, __ne__, __bool__, __copy__, __deepcopy__
   :show-inheritance:

.. autoclass:: paragon.WeightedGraph
   :members:
   :special-members: __init__, __repr__, __str__, __len__, __contains__, __getitem__, __iter__, __eq__, __ne__, __bool__, __copy__, __deepcopy__
   :show-inheritance:

Graph Generators
----------------

.. automodule:: paragon.graphs

.. autofunction:: paragon.graphs.generate_normal_graph

.. autofunction:: paragon.graphs.generate_normal_weighted_graph


Graph Algorithms
----------------

.. automodule:: paragon.algorithms

Traversal Algorithms
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: paragon.algorithms.parallel_bfs

.. autofunction:: paragon.algorithms.parallel_dfs


Connectivity Algorithms
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: paragon.algorithms.parallel_connected_components


Shortest Path Algorithms
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: paragon.algorithms.parallel_dijkstra


Ranking Algorithms
~~~~~~~~~~~~~~~~~~

.. autofunction:: paragon.algorithms.parallel_pagerank

.. autofunction:: paragon.algorithms.parallel_pagerank_bfs


Subgraph Algorithms
~~~~~~~~~~~~~~~~~~~

.. autofunction:: paragon.algorithms.parallel_triangle_count


Utilities
---------

.. note::

   All algorithms support thread-level parallelism.

.. code-block:: python

    from paragon.graphs import generate_normal_graph
    from paragon.algorithms import parallel_bfs

    NUM_THREADS = 4
    g = generate_normal_graph(vertices=10, edges=50)

    dist = parallel_bfs(graph=g, source=0, threads=NUM_THREADS)
    print(dist)

.. tip::

   Use higher thread counts for better performance on multicore systems.


.. warning::

   - Invalid inputs will raise Python exceptions  
   - Ensure correct graph type (Graph vs WeightedGraph)  
   - Some algorithms require specific constraints (e.g., non-negative weights)  