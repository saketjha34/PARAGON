Parallel PageRank
=================

This tutorial explains how to compute PageRank scores
using parallel algorithms in PARAGON.

PARAGON provides two implementations:

- Pull based PageRank (standard formulation): ``parallel_pagerank``
- Push based PageRank (BFS-style): ``parallel_pagerank_bfs``


Overview
--------

PageRank assigns a numerical importance score to each node
based on the structure of incoming links.

It is widely used in:

- Web ranking systems  
- Network analysis  
- Influence modeling  


PageRank Formula
----------------

.. math::

   PR(v) = \frac{1 - d}{N} + d \sum_{u \in In(v)} \frac{PR(u)}{deg(u)}

Where:

- :math:`PR(v)` = PageRank of node ``v``  
- :math:`d` = damping factor (typically 0.85)  
- :math:`N` = total number of nodes  
- :math:`In(v)` = incoming neighbors  


Available Functions
-------------------

.. code-block:: python


   from paragon.algorithms import parallel_pagerank, parallel_pagerank_bfs

   parallel_pagerank(graph: Graph, iterations: int =20, damping: float =0.85, threads: int =-1)

   parallel_pagerank_bfs(graph: Graph, iterations: int =20, damping: float =0.85, threads: int =-1)


Parameters
----------

graph : Graph
~~~~~~~~~~~~~

- Input graph (typically directed)  
- Must be instance of ``Graph``  


iterations : int
~~~~~~~~~~~~~~~~

- Number of iterations  
- Must be > 0  


damping : float
~~~~~~~~~~~~~~~

- Damping factor  
- Must satisfy: ``0 < damping < 1``  


threads : int
~~~~~~~~~~~~~

- ``-1`` → use all CPU cores  
- ``>= 1`` → manual control  

.. code-block:: python

   NUM_THREADS = 4


.. note::

   Increasing threads improves performance on large graphs.


.. warning::

   - ``threads = 0`` is invalid  
   - ``threads < -1`` is invalid  
   - Invalid source raises ``ValueError``  


Return Value
------------

.. code-block:: python

   List[float]

Where:

- ``rank[i]`` = PageRank score of node ``i``  


Pull-Based PageRank
-------------------

This is the **standard formulation**.

Each node gathers contributions from incoming neighbors.


Basic Example
~~~~~~~~~~~~~

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_pagerank

   NUM_THREADS = 4

   g = Graph(vertices=4, directed=True)

   g.add_edges(edges=[
       (0, 1),
       (1, 2),
       (2, 0),
       (2, 3)
   ])

   rank = parallel_pagerank(
       graph=g,
       iterations=20,
       damping=0.85,
       threads=NUM_THREADS
   )

   print(rank)

Output:

.. code-block:: text

    [0.21375211534259825, 0.26461796406804194, 0.30787780524676156, 0.21375211534259825]


Push-Based PageRank (BFS-style)
-------------------------------

Each node distributes its rank to outgoing neighbors.

This is similar to a frontier-based propagation.


Basic Example
~~~~~~~~~~~~~

.. code-block:: python

    from paragon import Graph
    from paragon.algorithms import parallel_pagerank_bfs

    NUM_THREADS = 4

    g = Graph(vertices=4, directed=True)

    g.add_edges(edges=[
        (0, 1),
        (1, 2),
        (2, 0),
        (2, 3)
    ])


    rank = parallel_pagerank_bfs(
        graph=g,
        iterations=20,
        damping=0.85,
        threads=NUM_THREADS
    )

    print(rank)

Output:

.. code-block:: text

   [0.21375211534259825, 0.26461796406804194, 0.30787780524676156, 0.21375211534259825]


Advanced Example
----------------

.. code-block:: python

   from paragon import Graph
   from paragon.algorithms import parallel_pagerank

   NUM_THREADS = 4

   g = Graph(vertices=5, directed=True)

   g.add_edges(edges=[
       (0, 1),
       (0, 2),
       (1, 2),
       (2, 3),
       (3, 4),
       (4, 2)
   ])

   rank = parallel_pagerank(
       graph=g,
       iterations=30,
       damping=0.85,
       threads=NUM_THREADS
   )

   print(rank)

Output (approx):

.. code-block:: text

   [0.030000000000000006, 0.04275000000000001, 0.3262401686773977, 0.3079527579413452, 0.29305707338125764]


Algorithm Details
-----------------

PageRank is computed iteratively until convergence.

At each iteration:

- Update rank values  
- Normalize contributions  
- Apply damping factor  


Technique
~~~~~~~~~

- **Iterative relaxation**
- **Parallel node updates**
- **Probability-based ranking**

Pseudocode (Pull-Based)
~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \textbf{Initialize:} \\
   \quad PR(v) \gets \frac{1}{N}

.. math::

   \textbf{for } k = 1 \text{ to iterations:} \\
   \quad \textbf{for each } v \in V: \\
   \qquad PR(v) \gets \frac{1 - d}{N} + d \sum_{u \in In(v)} \frac{PR(u)}{deg(u)}


Pseudocode (Push-Based)
~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \textbf{Initialize:} \\
   \quad PR(v) \gets \frac{1}{N}

.. math::

   \textbf{for } k = 1 \text{ to iterations:} \\
   \quad \textbf{for each } u \in V: \\
   \qquad \textbf{for each } v \in Adj(u): \\
   \qquad\quad PR(v) += \frac{PR(u)}{deg(u)}


Comparison
----------

+----------------------+------------------+------------------+
| Feature              | Pull-Based       | Push-Based       |
+======================+==================+==================+
| Strategy             | Incoming edges   | Outgoing edges   |
+----------------------+------------------+------------------+
| Stability            | High             | Moderate         |
+----------------------+------------------+------------------+
| Memory contention    | Low              | Medium           |
+----------------------+------------------+------------------+
| Best for             | General use      | Sparse graphs    |
+----------------------+------------------+------------------+

Time Complexity
---------------

.. code-block:: text

   O(iterations × (V + E))

Best Practices
--------------

- Use pull-based PageRank for stability  
- Use push-based version for sparse graphs  
- Tune ``iterations`` and ``threads`` carefully  

.. tip::

   PageRank typically converges within 20–50 iterations.

.. warning::

   Improper damping values may lead to unstable results.

.. seealso::

   - :doc:`parallel_bfs`
   - :doc:`parallel_dfs`
   - :doc:`parallel_connected_components`
   - :doc:`../graph_api_interface`