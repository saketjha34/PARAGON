"""
Parallel Triangle Counting

This module provides a Python interface for the high-performance
C++ implementation of triangle counting in PARAGON.
"""

from ..core import Graph
from .._paragon import triangle_count_parallel as _triangle_count_parallel


def parallel_triangle_count(graph: Graph, threads: int = -1) -> int:
    """
    Count the number of triangles in an undirected graph.

    A triangle is a set of three nodes (u, v, w) such that all
    three edges exist between them.

    Parameters
    ----------
    graph : Graph
        Input graph (must be undirected).

    threads : int, optional (default = -1)
        Number of threads to use.
        -1 means automatically use hardware concurrency.

    Returns
    -------
    int
        Total number of triangles in the graph.

    Notes
    -----
    - Uses parallel intersection-based counting.
    - Avoids duplicate counting using node ordering (u < v < w).
    - Efficient for large sparse graphs.

    Time Complexity
    ---------------
    Depends on graph density; typically near O(E * sqrt(E)).

    Example
    -------
    >>> from paragon import Graph
    >>> from paragon.algorithms import parallel_triangle_count
    >>> g = Graph(4)
    >>> g.add_edges([(0,1), (1,2), (2,0), (2,3)])
    >>> parallel_triangle_count(g)
    1
    """
    return _triangle_count_parallel(graph, threads)