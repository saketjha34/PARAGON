Parallel Connected Components
=============================

This tutorial explains how to compute connected components
in a graph using ``parallel_connected_components``


Overview
--------

Connected components identify groups of nodes such that
each node in a group is reachable from every other node.

PARAGON uses a parallel Shiloach Vishkin style algorithm
based on pointer jumping and hooking.


Function Signature
------------------

.. code-block:: python

   from paragon.algorithms import parallel_connected_components
   parallel_connected_components(graph: Graph, threads: int = -1)


Parameters
----------

graph : Graph
~~~~~~~~~~~~~

The input graph.

- Must be an instance of ``Graph``  
- Should be undirected for meaningful components  


threads : int, optional
~~~~~~~~~~~~~~~~~~~~~~~

Number of threads to use.

- ``-1`` → use all CPU cores  
- ``>= 1`` → manual control  

.. code-block:: python

   NUM_THREADS = 4


.. note::

   The algorithm uses thread-level parallelism to update component labels.


.. warning::

   - ``threads = 0`` is invalid  
   - ``threads < -1`` is invalid  
   - Invalid graph type raises ``TypeError``  


Return Value
------------

.. code-block:: python

   List[int]

Where:

- ``comp[i]`` = component identifier (representative node) of vertex ``i``  


Basic Example
-------------

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_connected_components

   NUM_THREADS = 4

   g = Graph(vertices=6)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (3, 4)
   ])

   comp = parallel_connected_components(
       graph=g,
       threads=NUM_THREADS
   )

   print(comp)

Output:

.. code-block:: text

   [0, 0, 0, 3, 3, 5]

Explanation:

- Component 1 → {0, 1, 2}  
- Component 2 → {3, 4}  
- Component 3 → {5}  


Advanced Example
----------------

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_connected_components

   NUM_THREADS = 4

   g = Graph(vertices=8)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (2, 3),
       (4, 5),
       (6, 7)
   ])

   comp = parallel_connected_components(
       graph=g,
       threads=NUM_THREADS
   )

   print(comp)

Output:

.. code-block:: text

   [0, 0, 0, 0, 4, 4, 6, 6]


Algorithm Details
-----------------

The algorithm uses a **label propagation approach**
based on pointer jumping.


Technique
~~~~~~~~~

- **Hooking**: merge smaller component into larger one  
- **Pointer jumping**: compress paths to speed up convergence  
- **Parallel updates** across all vertices  


Pseudocode
~~~~~~~~~~

.. math::

   \textbf{Initialize:} \\
   \quad parent[v] \gets v \ \forall v \in V

.. math::

   \textbf{repeat until convergence:}

.. math::

   \quad \textbf{parallel for each } u \in V: \\
   \qquad \textbf{for each } v \in Adj(u): \\
   \qquad\quad \textbf{if } parent[u] \neq parent[v]: \\
   \qquad\quad\quad parent[\max(parent[u], parent[v])] \gets \min(parent[u], parent[v])

.. math::

   \quad \textbf{parallel for each } u \in V: \\
   \qquad \textbf{while } parent[u] \neq parent[parent[u]]: \\
   \qquad\quad parent[u] \gets parent[parent[u]]


.. note::

   Pointer jumping rapidly reduces tree height, enabling fast convergence.


Time Complexity
---------------

.. code-block:: text

   O((V + E) log V)  (parallelized)

Best Practices
--------------

- Use on **undirected graphs**  
- Use sufficient threads for faster convergence  
- Works well for large sparse graphs  

.. tip::

   This algorithm is widely used in parallel graph processing systems
   due to its scalability.

.. warning::

   Results depend on internal merging order but always produce
   correct component groupings.

.. seealso::

   - :doc:`parallel_bfs`
   - :doc:`parallel_dfs`
   - :doc:`../graph_api_interface`