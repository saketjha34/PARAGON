WeightedGraph API Interface
============================

This tutorial provides a complete guide to the **WeightedGraph API interface**,
covering initialization, weighted edge operations, graph construction, and utility methods.

Overview
--------

The ``WeightedGraph`` class extends the Graph structure by associating
a **weight (float)** with each edge.

It is commonly used in applications involving costs, distances, or priorities.

.. note::

   - Nodes are indexed from ``0`` to ``V-1``  
   - Edge weights are stored as floating-point values  
   - Supports both directed and undirected graphs  

Initialization
--------------

1. Initialize weighted graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from paragon import WeightedGraph

   wg = WeightedGraph(vertices=4)
   print(wg)

Output:

.. code-block:: text

   WeightedGraph(vertices=4, edges=0, directed=False)

2. Directed weighted graph
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from paragon import WeightedGraph
   wg = WeightedGraph(vertices=3, directed=True)

   wg.add_edge(u=0, v=1, w=2.5)
   print(wg.get_adj())

Output:

.. code-block:: text

   [[(1, 2.5)], [], []]

.. warning::

   - Vertices must be a positive integer  
   - Invalid node indices raise ``ValueError``  
   - Invalid weight types raise ``TypeError``  

Edge Operations
---------------

add_edge(u, v, w)
~~~~~~~~~~~~~~~~~

Adds a weighted edge.

.. code-block:: python

   from paragon import WeightedGraph
   wg = WeightedGraph(vertices=3)

   wg.add_edge(u=0, v=1, w=2.5)
   wg.add_edge(u=1, v=2, w=1.2)

   print(wg.get_adj())

Output:

.. code-block:: text

   [[(1, 2.5)], [(0, 2.5), (2, 1.2)], [(1, 1.2)]]

Parameters:

- ``u`` : int — source vertex  
- ``v`` : int — destination vertex  
- ``w`` : float — edge weight  

.. warning::

   - Weight must be numeric (int or float)  
   - Negative indices are not allowed  
   - Out-of-range indices raise ``ValueError``  

add_edges(edges)
~~~~~~~~~~~~~~~~

Add multiple weighted edges.

.. code-block:: python
    
   from paragon import WeightedGraph   
   wg = WeightedGraph(vertices=4)

   wg.add_edges(edges=[
       (0, 1, 2.5),
       (1, 2, 1.0),
       (2, 3, 3.2)
   ])

   print(wg.get_adj())

Output:

.. code-block:: text

   [[(1, 2.5)], [(0, 2.5), (2, 1.0)], [(1, 1.0), (3, 3.2)], [(2, 3.2)]]

add_vertex()
~~~~~~~~~~~~

Add a new vertex.

.. code-block:: python

   from paragon import WeightedGraph   
   wg = WeightedGraph(vertices=2)
   wg.add_vertex()

   print(wg.vertices())

Output:

.. code-block:: text

   3

Graph Construction
------------------

build_from_adj_list(adjacency)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build graph using weighted adjacency list.

.. code-block:: python

   from paragon import WeightedGraph   
   wg = WeightedGraph(vertices=3)

   adjacency = [
       [(1, 2.5)],
       [(0, 2.5), (2, 1.2)],
       [(1, 1.2)]
   ]

   wg.build_from_adj_list(adjacency=adjacency)
   print(wg.get_adj())

Output:

.. code-block:: text

   [[(1, 2.5)], [(0, 2.5), (2, 1.2)], [(1, 1.2)]]


build_from_adj_matrix(matrix)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build graph using weighted adjacency matrix.

.. code-block:: python

   from paragon import WeightedGraph   
   wg = WeightedGraph(vertices=3)

   matrix = [
       [0, 2.5, 0],
       [2.5, 0, 1.2],
       [0, 1.2, 0]
   ]

   wg.build_from_adj_matrix(matrix=matrix)
   print(wg.get_adj())

Output:

.. code-block:: text

   [[(1, 2.5), (1, 2.5)], [(0, 2.5), (0, 2.5), (2, 1.2), (2, 1.2)], [(1, 1.2), (1, 1.2)]]


.. tip::

   Use adjacency lists for sparse graphs and matrices for dense graphs.


Graph Information
-----------------

vertices()
~~~~~~~~~~

Returns number of vertices.

.. code-block:: python

   from paragon import WeightedGraph

   wg = WeightedGraph(vertices=4)
   print(wg.vertices())

Output:

.. code-block:: text

   4

is_directed()
~~~~~~~~~~~~~

Check if graph is directed.

.. code-block:: python

   wg = WeightedGraph(vertices=3, directed=True)
   print(wg.is_directed())

Output:

.. code-block:: text

   True

get_adj()
~~~~~~~~~

Returns weighted adjacency list.

.. code-block:: python

   wg = WeightedGraph(vertices=3)
   wg.add_edge(u=0, v=1, w=2.5)

   print(wg.get_adj())

Output:

.. code-block:: text

   [[(1, 2.5)], [(0, 2.5)], []]

degree(u)
~~~~~~~~~

Returns degree of vertex.

.. code-block:: python

   wg = WeightedGraph(vertices=3)
   wg.add_edges(edges=[
       (0, 1, 2.5),
       (1, 2, 1.0)
   ])

   print(wg.degree(u=1))

Output:

.. code-block:: text

   2

has_edge(u, v)
~~~~~~~~~~~~~~

Checks if edge exists.

.. code-block:: python

   wg = WeightedGraph(vertices=3)
   wg.add_edge(u=0, v=1, w=2.5)

   print(wg.has_edge(u=0, v=1))
   print(wg.has_edge(u=1, v=2))

Output:

.. code-block:: text

   True
   False

.. warning::

   Invalid node indices will raise ``ValueError``.


Debug Utilities
---------------

print_graph()
~~~~~~~~~~~~~

Print graph.

.. code-block:: python

   wg = WeightedGraph(vertices=3)
   wg.add_edges(edges=[
       (0, 1, 2.5),
       (1, 2, 1.0)
   ])

   wg.print_graph()

Output:

.. code-block:: text

   0 : (1, 2.5) 
   1 : (0, 2.5) (2, 1) 
   2 : (1, 1) 


Representation & Dunder Methods
-------------------------------

__repr__()
~~~~~~~~~~

Returns developer-friendly representation.

.. code-block:: python

   wg = WeightedGraph(vertices=3)
   print(wg)

Output:

.. code-block:: text

   WeightedGraph(vertices=3, edges=0, directed=False)

__len__()
~~~~~~~~~

Returns number of vertices.

.. code-block:: python

   wg = WeightedGraph(vertices=4)
   print(len(wg))

Output:

.. code-block:: text

   4

__contains__()
~~~~~~~~~~~~~~

Checks if node exists.

.. code-block:: python

   wg = WeightedGraph(vertices=3)

   print(1 in wg)
   print(5 in wg)

Output:

.. code-block:: text

   True
   False

__getitem__()
~~~~~~~~~~~~~

Returns neighbors with weights.

.. code-block:: python

   wg = WeightedGraph(vertices=3)
   wg.add_edges(edges=[
       (0, 1, 2.5),
       (1, 2, 1.2)
   ])

   print(wg[1])

Output:

.. code-block:: text

   [(0, 2.5), (2, 1.2)]

__iter__()
~~~~~~~~~~

Iterates over nodes.

.. code-block:: python

   wg = WeightedGraph(vertices=3)

   for node in wg:
       print(node)

Output:

.. code-block:: text

   0
   1
   2

__eq__ / __ne__()
~~~~~~~~~~~~~~~~~

Compares graphs.

.. code-block:: python

   wg1 = WeightedGraph(vertices=3)
   wg2 = WeightedGraph(vertices=3)

   print(wg1 == wg2)

   wg2.add_edge(u=0, v=1, w=2.0)

   print(wg1 != wg2)

Output:

.. code-block:: text

   True
   True

__copy__ / __deepcopy__()
~~~~~~~~~~~~~~~~~~~~~~~~~

Creates copies of the graph.

.. code-block:: python

   import copy

   wg = WeightedGraph(vertices=3)
   wg.add_edge(u=0, v=1, w=2.5)

   wg2 = copy.copy(wg)
   wg3 = copy.deepcopy(wg)

   print(wg2.get_adj())
   print(wg3.get_adj())

Output:

.. code-block:: text

   [[], [], []]
   [[(1, 2.5)], [(0, 2.5)], []]

.. note::

   ``copy.copy`` creates a shallow copy (structure only), while
   ``copy.deepcopy`` creates a fully independent copy including edges.

Complete Dunder Methods Example
-------------------------------

The following example demonstrates how all dunder methods work together.

.. code-block:: python

   from paragon import WeightedGraph
   import copy

   wg = WeightedGraph(vertices=4)

   wg.add_edges(edges=[
       (0, 1, 2.5),
       (1, 2, 1.0),
       (2, 3, 3.2)
   ])

   # Length
   print(len(wg))

   # Contains
   print(2 in wg)

   # Indexing
   print(wg[1])

   # Iteration
   for node in wg:
       print(node)

   # String representation
   print(wg)

   # Equality
   wg2 = copy.deepcopy(wg)
   print(wg == wg2)

Output:

.. code-block:: text

   4
   True
   [(0, 2.5), (2, 1.0)]
   0
   1
   2
   3
   WeightedGraph(vertices=4, edges=6, directed=False)
   True

.. tip::

   Dunder methods make the WeightedGraph behave like native Python
   collections, improving readability and usability.


Complete Example
----------------

.. code-block:: python

   from paragon import WeightedGraph

   wg = WeightedGraph(vertices=4)

   wg.add_edges(edges=[
       (0, 1, 2.5),
       (1, 2, 1.0),
       (2, 3, 3.2)
   ])

   print("Vertices:", wg.vertices())
   print("Adjacency:", wg.get_adj())
   print("Degree:", wg.degree(u=1))
   print("Has edge:", wg.has_edge(u=0, v=1))


Output:

.. code-block:: text

   Vertices: 4
   Adjacency: [[(1, 2.5)], [(0, 2.5), (2, 1.0)], [(1, 1.0), (3, 3.2)], [(2, 3.2)]]
   Degree: 2
   Has edge: True
   0 : (1, 2.5) 
   1 : (0, 2.5) (2, 1) 
   2 : (1, 1) (3, 3.2) 
   3 : (2, 3.2) 


Best Practices
--------------

- Use ``add_edges`` for batch insertion  
- Use adjacency list for performance  
- Validate weights before insertion  

.. tip::

   Weighted graphs are ideal for shortest path algorithms like Dijkstra.

.. seealso::

   - :doc:`graph_api_interface`
   - :doc:`../getting_started`
   - :doc:`../tutorials/index`