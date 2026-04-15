Supported Python Data Structures
================================

This page provides a support matrix for various input types
used across PARAGON APIs.


Markers
-------

- **T** : Supported
- **F** : Not supported
- **NE** : Invalid for the use case  
- **Conv** : Supported after conversion  
- **FF** : Planned future support  


Table Header
------------

- **Graph APIs** → Graph / WeightedGraph construction  
- **Algorithms** → BFS, DFS, PageRank, etc.  
- **Generators** → Graph generation utilities  
- **Weighted** → WeightedGraph compatibility  


Support Matrix
--------------

+--------------------------+------------+-------------+-------------+-----------+
| Input Type               | Graph APIs | Algorithms  | Generators  | Weighted  |
+==========================+============+=============+=============+===========+
| Graph                    | T          | T           | F           | NE        |
+--------------------------+------------+-------------+-------------+-----------+
| WeightedGraph            | T          | Partial     | F           | T         |
+--------------------------+------------+-------------+-------------+-----------+
| list of edges [(u,v)]    | T          | Conv        | T           | NE        |
+--------------------------+------------+-------------+-------------+-----------+
| list of weighted edges   | T          | Conv        | T           | T         |
| [(u,v,w)]                |            |             |             |           |
+--------------------------+------------+-------------+-------------+-----------+
| adjacency list           | T          | Conv        | T           | Partial   |
| [[v1,v2], ...]           |            |             |             |           |
+--------------------------+------------+-------------+-------------+-----------+
| weighted adjacency list  | T          | Conv        | T           | T         |
| [[(v,w)], ...]           |            |             |             |           |
+--------------------------+------------+-------------+-------------+-----------+
| adjacency matrix         | T          | Conv        | F           | Partial   |
| (list of lists)          |            |             |             |           |
+--------------------------+------------+-------------+-------------+-----------+
| tuple                    | Conv       | Conv        | T           | Conv      |
+--------------------------+------------+-------------+-------------+-----------+
| set                      | F          | F           | F           | F         |
+--------------------------+------------+-------------+-------------+-----------+
| dict                     | Conv       | Conv        | F           | Conv      |
+--------------------------+------------+-------------+-------------+-----------+
| numpy.ndarray            | FF         | FF          | FF          | FF        |
+--------------------------+------------+-------------+-------------+-----------+
| pandas.DataFrame         | FF         | FF          | FF          | FF        |
+--------------------------+------------+-------------+-------------+-----------+


- Most algorithms require a **Graph or WeightedGraph instance**  
- Other formats must be converted before use  
- Generators return ready to use graph objects  


.. seealso::

   - :doc:`../tutorials/graph_api_interface`
   - :doc:`../tutorials/weighted_graph_api_interface`
   - :doc:`../tutorials/algorithms/index`