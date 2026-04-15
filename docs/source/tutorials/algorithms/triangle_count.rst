Parallel Triangle Counting
==========================

This tutorial explains how to count the number of **triangles**
in a graph using a parallel algorithm.


Overview
--------

A triangle is a set of three nodes ``(u, v, w)``
such that all three edges exist:

- (u, v)
- (v, w)
- (u, w)

Triangle counting is widely used in:

- Social network analysis  
- Graph clustering  
- Community detection  


Function Signature
------------------

.. code-block:: python

   from paragon.algorithms import parallel_triangle_count
   parallel_triangle_count(graph: Graph, threads: int = -1)


Parameters
----------

graph : Graph
~~~~~~~~~~~~~

The input graph.

- Must be an instance of ``Graph``  
- Should be **undirected**  


threads : int, optional
~~~~~~~~~~~~~~~~~~~~~~~

Number of threads to use.

- ``-1`` → use all CPU cores  
- ``>= 1`` → manual control  

.. code-block:: python

   NUM_THREADS = 4


.. note::

   Parallel execution divides nodes across threads
   to count triangles concurrently.


.. warning::

   - ``threads = 0`` is invalid  
   - ``threads < -1`` is invalid  


Return Value
------------

.. code-block:: python

   int

Where:

- Returns total number of triangles in the graph  


Basic Example
-------------

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_triangle_count

   NUM_THREADS = 4

   g = Graph(vertices=4)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (2, 0),  # triangle (0,1,2)
       (2, 3)
   ])

   count = parallel_triangle_count(
       graph=g,
       threads=NUM_THREADS
   )

   print(count)

Output:

.. code-block:: text

   1


Advanced Example
----------------

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_triangle_count

   NUM_THREADS = 4

   g = Graph(vertices=6)

   g.add_edges(edges=[
       (0, 1), (1, 2), (2, 0),   # triangle 1
       (2, 3), (3, 4), (4, 2),   # triangle 2
       (4, 5)
   ])

   count = parallel_triangle_count(
       graph=g,
       threads=NUM_THREADS
   )

   print(count)

Output:

.. code-block:: text

   2

Algorithm Details
-----------------

The algorithm counts triangles using intersection of adjacency lists.

For each edge ``(u, v)``:

- Count common neighbors of ``u`` and ``v``  
- Each common neighbor forms a triangle  

To avoid duplicates:

- Only process edges where ``v > u``  
- Use ordering constraints  

Technique
~~~~~~~~~

- **Adjacency list sorting**
- **Intersection-based counting**
- **Work partitioning across threads**
- **Avoid duplicate counting via ordering**

Pseudocode
~~~~~~~~~~

.. math::

   \textbf{Initialize:} \\
   \quad \text{Sort adjacency list of each node}

.. math::

   \textbf{parallel for each } u \in V: \\
   \quad \textbf{for each } v \in Adj(u): \\
   \qquad \textbf{if } v > u: \\
   \qquad\quad \text{count common neighbors of } u \text{ and } v \\
   \qquad\quad \text{add to total}

.. note::

   Intersection can be computed efficiently using
   two-pointer technique on sorted adjacency lists.


Time Complexity
---------------

.. math::

   O\left(\sum_{(u,v)} \min(\deg(u), \deg(v))\right)

.. note::

   The complexity depends on the degree distribution of the graph.


Best Practices
--------------

- Use on undirected graphs  
- Sort adjacency lists for efficiency  
- Use sufficient threads for speed  


.. tip::

   Triangle counting is faster on sparse graphs
   with small degree nodes.


.. warning::

   Graph must not contain duplicate edges,
   otherwise triangles may be overcounted.

.. seealso::

   - :doc:`parallel_bfs`
   - :doc:`parallel_dfs`
   - :doc:`parallel_connected_components`
   - :doc:`../graph_api_interface`