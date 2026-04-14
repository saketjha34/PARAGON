Introduction to Graphs
======================

Graphs are fundamental mathematical structures used to model relationships
between entities. They are widely used in computer science, physics,
social sciences, and engineering.


Graph Definition
----------------

A **graph** is formally defined as:

.. math::

   G = (V, E)

where:

- :math:`V` is a finite set of vertices (nodes)
- :math:`E \subseteq V \times V` is a set of edges

Each edge represents a relationship between two vertices.


Vertices and Edges
------------------

Let:

.. math::

   V = \{v_1, v_2, \dots, v_n\}

be the set of vertices.

An edge is defined as:

.. math::

   e = (u, v), \quad u, v \in V

Thus, the edge set is:

.. math::

   E = \{(u, v) \mid u, v \in V\}


Types of Graphs
---------------

Graphs can be categorized based on edge properties.


Undirected Graph
~~~~~~~~~~~~~~~~

In an undirected graph, edges have no direction:

.. math::

   (u, v) = (v, u)

Thus:

.. math::

   E \subseteq \{\{u, v\} \mid u, v \in V\}


Directed Graph (Digraph)
~~~~~~~~~~~~~~~~~~~~~~~~

In a directed graph, edges are ordered pairs:

.. math::

   (u, v) \neq (v, u)

Here:

.. math::

   E \subseteq V \times V

Each edge has a direction from :math:`u` to :math:`v`.


Weighted Graph
--------------

A **weighted graph** assigns a numerical value to each edge.

.. math::

   G = (V, E, w)

where:

.. math::

   w : E \rightarrow \mathbb{R}

is a weight function.

Each edge is represented as:

.. math::

   (u, v, w(u,v))


Example (Weighted Edge Set)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   E = \{(0,1,2.5), (1,2,1.2), (2,3,3.7)\}


Use Cases of Weighted Graphs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Weighted graphs are used when relationships have costs or distances:

- Shortest path problems  
- Network routing  
- Transportation systems  
- Resource optimization  
- Recommendation systems  


Graph Properties
----------------

Degree
~~~~~~

The degree of a vertex :math:`v` is:

.. math::

   \deg(v) = |\{ u \mid (v, u) \in E \}|

For directed graphs:

- In-degree:

.. math::

   \deg^{-}(v)

- Out-degree:

.. math::

   \deg^{+}(v)

Path
~~~~

A path is a sequence of vertices:

.. math::

   v_1 \rightarrow v_2 \rightarrow \dots \rightarrow v_k

such that:

.. math::

   (v_i, v_{i+1}) \in E


Cycle
~~~~~

A cycle is a path where:

.. math::

   v_1 = v_k


Connectivity
~~~~~~~~~~~~

A graph is **connected** if:

.. math::

   \forall u, v \in V, \exists \text{ a path from } u \text{ to } v


Graph Density
-------------

The density of a graph is defined as:

.. math::

   D = \frac{2|E|}{|V|(|V| - 1)}

Graph Representations
---------------------

Graphs can be represented in different ways.

Adjacency List
~~~~~~~~~~~~~~

For each vertex:

.. math::

   \text{Adj}(u) = \{ v \mid (u, v) \in E \}

Adjacency Matrix
~~~~~~~~~~~~~~~~

A matrix :math:`A` where:

.. math::

   A[i][j] =
   \begin{cases}
   1 & \text{if } (i,j) \in E \\
   0 & \text{otherwise}
   \end{cases}

For weighted graphs:

.. math::

   A[i][j] = w(i,j)


Summary
-------

Graphs provide a powerful abstraction for modeling relationships.
Understanding their mathematical formulation, types, and properties
is essential for designing efficient algorithms and systems.

.. note::

   This section focuses on the theoretical foundation of graphs.
   Practical implementations and algorithms are discussed in later sections.