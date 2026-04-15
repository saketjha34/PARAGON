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

    # Validate graph
    if not isinstance(graph, Graph):
        raise TypeError("graph must be an instance of Graph")

    # Validate source
    if not isinstance(source, int):
        raise TypeError("source must be an integer")

    if source < 0 or source >= graph.vertices():
        raise ValueError(f"Invalid source node: {source}")

    # Validate threads
    if not isinstance(threads, int):
        raise TypeError("threads must be an integer")

    if threads == 0:
        raise ValueError("threads must be >= 1 or -1")

    if threads < -1:
        raise ValueError("threads must be -1 (auto) or a positive integer")

    return _parallel_dfs(graph, source, threads)