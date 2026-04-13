"""
Parallel Single Source Shortest Path (SSSP)

This module provides a Python interface for the high-performance
C++ implementation of parallel shortest path computation in PARAGON.
"""

from typing import List
from ..core import WeightedGraph
from .._paragon import parallel_dijkstra as _parallel_dijkstra


def parallel_dijkstra(graph: WeightedGraph, source: int, threads: int = -1) -> List[float]:
    """
    Compute shortest paths from a source node in a weighted graph.

    This function computes the shortest distance from the source node
    to all other nodes using a parallel relaxation-based approach.

    Parameters
    ----------
    graph : WeightedGraph
        Input weighted graph with non-negative edge weights.

    source : int
        Starting node.

    threads : int, optional (default = -1)
        Number of threads to use.
        -1 means automatically use hardware concurrency.

    Returns
    -------
    List[float]
        A list where:
        - dist[i] = shortest distance from source to node i
        - dist[i] = large value (INF) if unreachable

    Notes
    -----
    - Uses parallel edge relaxation (similar to Bellman-Ford).
    - Stops early if no updates occur in an iteration.
    - Works only for graphs with non-negative weights.

    Time Complexity
    ---------------
    O(V × E) worst case, with early stopping in practice.

    Example
    -------
    >>> from paragon import WeightedGraph
    >>> from paragon.algorithms import parallel_dijkstra
    >>> g = WeightedGraph(4)
    >>> g.add_edges([(0,1,1.0), (1,2,2.0), (0,3,4.0)])
    >>> parallel_dijkstra(g, 0)
    [0.0, 1.0, 3.0, 4.0]
    """
    return _parallel_dijkstra(graph, source, threads)