"""
Parallel Depth-First Search (DFS)

This module provides a Python interface for the high-performance
C++ implementation of parallel DFS in PARAGON.
"""

from typing import List
from ..core import Graph
from .._paragon import parallel_dfs as _parallel_dfs


def parallel_dfs(graph: Graph, source: int, threads: int = -1) -> List[bool]:
    """
    Perform parallel depth-first search (DFS) on a graph.

    This function explores all nodes reachable from the given source
    using a parallel, multi-threaded approach.

    Parameters
    ----------
    graph : Graph
        Input graph (unweighted).

    source : int
        Starting node for DFS traversal.

    threads : int, optional (default = -1)
        Number of threads to use.
        -1 means automatically use hardware concurrency.

    Returns
    -------
    List[bool]
        A boolean list where:
        - visited[i] = True → node i is reachable from source
        - visited[i] = False → node i is not reachable

    Notes
    -----
    - Uses a shared work stack across threads.
    - Thread-safe via atomic visited array and mutex-protected stack.
    - Efficient for large graphs with multiple connected regions.

    Time Complexity
    ---------------
    O(V + E) (parallelized)

    Example
    -------
    >>> from paragon import Graph
    >>> from paragon.algorithms import parallel_dfs
    >>> g = Graph(5)
    >>> g.add_edges([(0,1), (1,2), (2,3)])
    >>> parallel_dfs(g, 0)
    [True, True, True, True, False]
    """
    return _parallel_dfs(graph, source, threads)