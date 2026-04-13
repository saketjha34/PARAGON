"""
Parallel Breadth-First Search (BFS)

This module provides a Python interface for the high-performance
C++ implementation of parallel BFS in PARAGON.
"""

from typing import List
from ..core import Graph
from .._paragon import parallel_bfs as _parallel_bfs


def parallel_bfs(graph: Graph, source: int, threads: int = -1) -> List[int]:
    """
    Perform parallel breadth-first search (BFS) on a graph.

    This function computes the shortest distance from the source
    node to all other nodes in an unweighted graph using a
    level-synchronous parallel approach.

    Parameters
    ----------
    graph : Graph
        Input graph (unweighted).

    source : int
        Starting node for BFS traversal.

    threads : int, optional (default = -1)
        Number of threads to use.
        -1 means automatically use hardware concurrency.

    Returns
    -------
    List[int]
        A list where:
        - dist[i] = shortest distance from source to node i
        - dist[i] = -1 if node i is unreachable

    Notes
    -----
    - Uses level-synchronous traversal (frontier-based).
    - Each level is processed in parallel across threads.
    - Thread-safe using atomic distance updates and mutex-protected frontier.

    Time Complexity
    ---------------
    O(V + E) (parallelized)

    Example
    -------
    >>> from paragon import Graph
    >>> from paragon.algorithms import parallel_bfs
    >>> g = Graph(5)
    >>> g.add_edges([(0,1), (1,2), (2,3)])
    >>> parallel_bfs(g, 0)
    [0, 1, 2, 3, -1]
    """
    return _parallel_bfs(graph, source, threads)