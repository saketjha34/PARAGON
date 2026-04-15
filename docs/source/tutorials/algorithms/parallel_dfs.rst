Parallel Depth First Search (DFS)
=================================

This tutorial explains how to use the parallel DFS algorithm
to explore a graph using concurrent traversal ``parallel_dfs``.

Overview
--------

Depth-First Search (DFS) explores a graph by going as deep as possible
along each branch before backtracking.
In PARAGON, DFS is implemented using a parallel work stealing approach
with a shared stack.


Function Signature
------------------

.. code-block:: python

   from paragon.algorithms import parallel_dfs
   parallel_dfs(graph: Graph, source: int, threads: int = -1)


Parameters
----------

graph : Graph
~~~~~~~~~~~~~

The input graph.

- Must be an instance of ``Graph``  
- Should be unweighted  


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

   PARAGON uses thread-level parallelism to explore multiple branches
   of the graph concurrently.


.. warning::

   - ``threads = 0`` is invalid  
   - ``threads < -1`` is invalid  
   - Invalid source raises ``ValueError``  

Return Value
------------

.. code-block:: python

   List[bool]

Where:

- ``visited[i] = True`` if node ``i`` is reachable  
- ``visited[i] = False`` otherwise  


Basic Example
-------------

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_dfs

   NUM_THREADS = 4

   g = Graph(vertices=5)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (2, 3)
   ])

   visited = parallel_dfs(
       graph=g,
       source=0,
       threads=NUM_THREADS
   )

   print(visited)

Output:

.. code-block:: text

   [True, True, True, True, False]


Advanced Example
----------------

Parallel DFS on a branching graph.

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_dfs

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

   visited = parallel_dfs(
       graph=g,
       source=0,
       threads=NUM_THREADS
   )

   print(visited)

Output:

.. code-block:: text

   [True, True, True, True, True, True, True]


Algorithm Details
-----------------

Parallel DFS uses a shared stack with concurrent workers.

Each thread:

- Pops a node from the stack  
- Marks it visited using atomic operation  
- Pushes unvisited neighbors back to the stack  


Technique
~~~~~~~~~

- **Shared stack-based traversal**
- **Atomic visited array**
- **Mutex-protected stack**
- **Thread-level parallelism**


Pseudocode
~~~~~~~~~~

.. math::

   \textbf{Initialize:} \\
   \quad \text{visited}[v] \gets \text{False} \ \forall v \in V \\
   \quad \text{visited}[s] \gets \text{True} \\
   \quad S \gets \{s\}

.. math::

   \textbf{Spawn threads:}

.. math::

   \textbf{Each thread executes:} \\
   \quad \textbf{while } S \neq \emptyset: \\
   \qquad \text{pop } u \text{ from } S \\
   \qquad \textbf{for each } v \in Adj(u): \\
   \qquad\quad \textbf{if } \text{visited}[v] = \text{False}: \\
   \qquad\quad\quad \text{visited}[v] \gets \text{True} \\
   \qquad\quad\quad \text{push } v \text{ into } S


.. note::

   Multiple threads explore different branches simultaneously,
   improving performance on large graphs.


Time Complexity
---------------

.. code-block:: text

   O(V + E)  (parallelized)


Best Practices
--------------

- Use DFS for reachability and traversal
- Use appropriate thread count  
- Prefer adjacency list representation  


.. tip::

   Parallel DFS can significantly speed up exploration in large,
   highly branching graphs.


.. warning::

   - Invalid source node will raise ``ValueError``  
   - Non-Graph input will raise ``TypeError``  


.. seealso::

   - :doc:`parallel_bfs`
   - :doc:`pagerank`
   - :doc:`../graph_api_interface`