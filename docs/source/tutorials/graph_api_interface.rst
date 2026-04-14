Graph API Interface
====================

This tutorial provides a complete guide to the **Graph API interface**, covering
initialization methods, edge operations, graph construction, and utility functions.

Overview
--------

The ``Graph`` class represents an **unweighted graph** using an adjacency list
representation. It supports flexible initialization, efficient operations,
and built-in validation for safe usage.

.. note::

   Nodes are indexed from ``0`` to ``V-1`` and the graph can be either
   directed or undirected.

Initialization
--------------

The Graph class supports multiple initialization styles.

1. Initialize with number of vertices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create an empty graph with a fixed number of vertices.

.. code-block:: python

   from paragon import Graph

   g = Graph(vertices=5)
   print(g)

Output:

.. code-block:: text

   Graph(vertices=5, directed=False)


2. Initialize with edges
~~~~~~~~~~~~~~~~~~~~~~~~

Create a graph and initialize it with edges.

.. code-block:: python

   from paragon import Graph
   g = Graph(
       vertices=3,
       edges=[(0, 1), (1, 2)]
   )

   print(g.get_adj())

Output:

.. code-block:: text

   [[1], [0, 2], [1]]


3. Directed graph
~~~~~~~~~~~~~~~~~

Create a directed graph.

.. code-block:: python

   from paragon import Graph
   g = Graph(vertices=3, directed=True)

   g.add_edge(u=0, v=1)
   print(g.get_adj())

Output:

.. code-block:: text

   [[1], [], []]


.. warning::

   - Passing invalid types (e.g., strings instead of integers) raises ``TypeError``  
   - Invalid indices (out-of-range) raise ``ValueError``  

Edge Operations
---------------

add_edge(u, v)
~~~~~~~~~~~~~~

Adds an edge between vertices ``u`` and ``v``.

.. code-block:: python

   from paragon import Graph
   g = Graph(vertices=3)

   g.add_edge(u=0, v=1)
   g.add_edge(u=1, v=2)

   print(g.get_adj())

Output:

.. code-block:: text

   [[1], [0, 2], [1]]


Parameters:

- ``u`` : int — source vertex  
- ``v`` : int — destination vertex  

.. warning::

   - Negative indices are not allowed  
   - Out-of-range indices raise ``ValueError``  
   - Non-integer inputs raise ``TypeError``  

add_edges(edges)
~~~~~~~~~~~~~~~~

Adds multiple edges at once.

.. code-block:: python

   from paragon import Graph
   g = Graph(vertices=4)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (2, 3)
   ])

   print(g.get_adj())

Output:

.. code-block:: text

   [[1], [0, 2], [1, 3], [2]]

add_vertex()
~~~~~~~~~~~~

Adds a new vertex to the graph.

.. code-block:: python

   from paragon import Graph
   g = Graph(vertices=3)

   g.add_vertex()
   print(g.vertices())

Output:

.. code-block:: text

   4

.. note::

   The new vertex is added without edges.

Graph Construction
------------------

build_from_adj_matrix(matrix)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build graph using an adjacency matrix.

.. code-block:: python

   from paragon import Graph
   g = Graph(vertices=3)

   matrix = [
       [0, 1, 0],
       [1, 0, 1],
       [0, 1, 0]
   ]

   g.build_from_adj_matrix(matrix=matrix)
   print(g.get_adj())

Output:

.. code-block:: text

   [[1], [0, 2], [1]]

build_from_adj_list(adjacency)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build graph using adjacency list.

.. code-block:: python

   from paragon import Graph
   g = Graph(vertices=3)

   adjacency = [
       [1, 2],
       [0],
       [0]
   ]

   g.build_from_adj_list(adjacency=adjacency)
   print(g.get_adj())

Output:

.. code-block:: text

   [[1, 2], [0], [0]]

.. tip::

   Use adjacency lists for better performance in sparse graphs.

Graph Information
-----------------

vertices()
~~~~~~~~~~

Returns number of vertices.

.. code-block:: python

   g = Graph(vertices=4)
   print(g.vertices())

Output:

.. code-block:: text

   4

is_directed()
~~~~~~~~~~~~~

Check if graph is directed.

.. code-block:: python

   g = Graph(vertices=3, directed=True)
   print(g.is_directed())

Output:

.. code-block:: text

   True

get_adj()
~~~~~~~~~

Returns adjacency list.

.. code-block:: python

   g = Graph(vertices=3)
   g.add_edge(u=0, v=1)

   print(g.get_adj())

Output:

.. code-block:: text

   [[1], [0], []]

degree(u)
~~~~~~~~~

Returns degree of vertex ``u``.

.. code-block:: python

   g = Graph(vertices=3)
   g.add_edges(edges=[(0, 1), (1, 2)])

   print(g.degree(u=1))

Output:

.. code-block:: text

   2

has_edge(u, v)
~~~~~~~~~~~~~~

Checks if edge exists.

.. code-block:: python

   g = Graph(vertices=3)
   g.add_edge(u=0, v=1)

   print(g.has_edge(u=0, v=1))
   print(g.has_edge(u=1, v=2))

Output:

.. code-block:: text

   True
   False

.. warning::

   Passing invalid node indices will raise ``ValueError``.

Debug Utilities
---------------

print_graph()
~~~~~~~~~~~~~

Prints graph structure.

.. code-block:: python

   g = Graph(vertices=3)
   g.add_edges(edges=[(0, 1), (1, 2)])

   g.print_graph()

Output:

.. code-block:: text

   0 : 1 
   1 : 0 2 
   2 : 1 

.. tip::

   Useful for debugging small graphs and verifying structure.


Representation & Dunder Methods
-------------------------------

Python provides special methods (called *dunder methods*) that allow objects
to behave like built-in types. The Graph class implements several of these
methods to provide a clean and intuitive interface.

__repr__()
~~~~~~~~~~

Returns a developer-friendly string representation of the graph.

.. code-block:: python

   g = Graph(vertices=5)
   print(g)

Output:

.. code-block:: text

   Graph(vertices=5, edges=0, directed=False)

__len__()
~~~~~~~~~

Returns the number of vertices in the graph.

.. code-block:: python

   g = Graph(vertices=4)
   print(len(g))

Output:

.. code-block:: text

   4

__contains__(node)
~~~~~~~~~~~~~~~~~~

Checks whether a node exists in the graph.

.. code-block:: python

   g = Graph(vertices=3)

   print(1 in g)
   print(5 in g)

Output:

.. code-block:: text

   True
   False


__getitem__(node)
~~~~~~~~~~~~~~~~~

Returns neighbors of a node.

.. code-block:: python

   g = Graph(vertices=3)
   g.add_edges(edges=[(0, 1), (1, 2)])

   print(g[1])

Output:

.. code-block:: text

   [0, 2]


__iter__()
~~~~~~~~~~

Allows iteration over graph nodes.

.. code-block:: python

   g = Graph(vertices=3)

   for node in g:
       print(node)

Output:

.. code-block:: text

   0
   1
   2


__eq__(other)
~~~~~~~~~~~~~

Checks if two graphs are equal.

.. code-block:: python

   g1 = Graph(vertices=3)
   g2 = Graph(vertices=3)

   print(g1 == g2)

Output:

.. code-block:: text

   True

__ne__(other)
~~~~~~~~~~~~~

Checks if two graphs are not equal.

.. code-block:: python

   print(g1 != g2)

Output:

.. code-block:: text

   False

__bool__()
~~~~~~~~~~

Checks if graph is non-empty.

.. code-block:: python

   g = Graph(vertices=3)

   if g:
       print("Graph is not empty")

Output:

.. code-block:: text

   Graph is not empty

__copy__() and __deepcopy__()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create copies of the graph.

.. code-block:: python

   import copy

   g = Graph(vertices=3)
   g.add_edge(u=0, v=1)

   g2 = copy.copy(g)
   g3 = copy.deepcopy(g)

   print(g2.get_adj())
   print(g3.get_adj())

Output:

.. code-block:: text

   [[1], [0], []]
   [[1], [0], []]


.. note::

   ``copy.copy`` creates a shallow copy, while ``copy.deepcopy`` creates a fully
   independent copy of the graph.

Complete Dunder Methods Example
-------------------------------

The following example demonstrates how all dunder methods work together.

.. code-block:: python

   from paragon import Graph
   import copy

   g = Graph(vertices=4)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (2, 3)
   ])

   # Length
   print(len(g))

   # Contains
   print(2 in g)

   # Indexing
   print(g[1])

   # Iteration
   for node in g:
       print(node)

   # String representation
   print(g)

   # Equality
   g2 = copy.deepcopy(g)
   print(g == g2)

Output:

.. code-block:: text

   4
   True
   [0, 2]
   0
   1
   2
   3
   0: [1]
   1: [0, 2]
   2: [1, 3]
   3: [2]
   True

.. tip::

   Dunder methods make your Graph class behave like native Python collections,
   improving readability and usability.


Complete Example
----------------

.. code-block:: python

   from paragon import Graph

   g = Graph(vertices=4)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (2, 3)
   ])

   print("Vertices:", g.vertices())
   print("Adjacency:", g.get_adj())
   print("Degree of 1:", g.degree(u=1))
   print("Has edge (0,1):", g.has_edge(u=0, v=1))

   g.print_graph()

Output:

.. code-block:: text

   Vertices: 4
   Adjacency: [[1], [0, 2], [1, 3], [2]]
   Degree of 1: 2
   Has edge (0,1): True
   0 : 1 
   1 : 0 2 
   2 : 1 3 
   3 : 2 

Best Practices
--------------

- Use ``add_edges`` instead of multiple ``add_edge`` calls for efficiency  
- Prefer adjacency lists for large sparse graphs  
- Always validate input data before constructing graphs  

- Use ``len(graph)`` instead of ``graph.vertices()`` for cleaner code  
- Use ``graph[node]`` for quick adjacency access  
- Use ``node in graph`` for safe existence checks  
- Prefer ``copy.deepcopy`` when modifying graphs independently  

.. warning::

   Invalid node indices or malformed inputs will raise explicit errors.
   Ensure all vertices lie in the valid range ``[0, V-1]``.

.. tip::

   Use directed graphs when modeling one-way relationships such as
   web links, dependencies, or workflows.

.. seealso::

   - :doc:`weighted_graph_api_interface`  
   - :doc:`../getting_started`  
   - :doc:`../tutorials/index`