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
    # Validate graph
    if not isinstance(graph, WeightedGraph):
        raise TypeError("graph must be an instance of WeightedGraph")

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

    # Validate weights (non-negative)
    adj = graph.get_adj()
    for neighbors in adj:
        for _, w in neighbors:
            if w < 0:
                raise ValueError("Negative edge weights are not supported")

    return _parallel_dijkstra(graph, source, threads)