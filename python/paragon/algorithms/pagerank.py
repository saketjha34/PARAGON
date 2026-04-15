"""
Parallel PageRank Algorithms

This module provides Python interfaces for high-performance
C++ implementations of PageRank in PARAGON.
"""

from typing import List
from ..core import Graph
from .._paragon import (
    parallel_pagerank as _parallel_pagerank,
    parallel_pagerank_bfs as _parallel_pagerank_bfs,
)


def parallel_pagerank(
    graph: Graph,
    iterations: int = 20,
    damping: float = 0.85,
    threads: int = -1,
) -> List[float]:
    """
    Compute PageRank scores using a parallel pull-based approach.

    This method updates each node’s rank by aggregating contributions
    from incoming neighbors (reverse adjacency).

    Parameters
    ----------
    graph : Graph
        Input graph (typically directed).

    iterations : int, optional (default = 20)
        Number of PageRank iterations.

    damping : float, optional (default = 0.85)
        Damping factor (probability of following links).

    threads : int, optional (default = -1)
        Number of threads to use.
        -1 means automatically use hardware concurrency.

    Returns
    -------
    List[float]
        PageRank score for each node.

    Notes
    -----
    - Pull-based computation using incoming edges.
    - Stable and widely used formulation.
    - Parallelized across nodes.

    Time Complexity
    ---------------
    O(iterations × (V + E))

    Example
    -------
    >>> from paragon import Graph
    >>> from paragon.algorithms import pagerank
    >>> g = Graph(4, directed=True)
    >>> g.add_edges([(0,1), (1,2), (2,0), (2,3)])
    >>> parallel_pagerank(g)
    [0.25, 0.25, 0.25, 0.25]
    """
    # Graph validation
    if not isinstance(graph, Graph):
        raise TypeError("graph must be an instance of Graph")

    # Iterations validation
    if not isinstance(iterations, int):
        raise TypeError("iterations must be an integer")

    if iterations <= 0:
        raise ValueError("iterations must be a positive integer")

    # Damping validation
    if not isinstance(damping, (int, float)):
        raise TypeError("damping must be a numeric value")

    if not (0.0 < damping < 1.0):
        raise ValueError("damping must be between 0 and 1 (exclusive)")

    # Threads validation
    if not isinstance(threads, int):
        raise TypeError("threads must be an integer")

    if threads == 0:
        raise ValueError("threads must be >= 1 or -1")

    if threads < -1:
        raise ValueError("threads must be -1 (auto) or a positive integer")

    return _parallel_pagerank(graph, iterations, damping, threads)


def parallel_pagerank_bfs(
    graph: Graph,
    iterations: int = 20,
    damping: float = 0.85,
    threads: int = -1,
) -> List[float]:
    """
    Compute PageRank using a push-based (BFS-style) parallel approach.

    Each node distributes its rank to its outgoing neighbors,
    similar to a frontier expansion strategy.

    Parameters
    ----------
    graph : Graph
        Input graph (typically directed).

    iterations : int, optional (default = 20)
        Number of PageRank iterations.

    damping : float, optional (default = 0.85)
        Damping factor.

    threads : int, optional (default = -1)
        Number of threads to use.

    Returns
    -------
    List[float]
        PageRank score for each node.

    Notes
    -----
    - Push-based computation (each node distributes rank).
    - Uses per-thread local buffers to avoid contention.
    - Efficient for sparse graphs.

    Time Complexity
    ---------------
    O(iterations × (V + E))

    Example
    -------
    >>> from paragon.algorithms import parallel_pagerank_bfs
    >>> parallel_pagerank_bfs(g)
    [0.25, 0.25, 0.25, 0.25]
    """
    # Graph validation
    if not isinstance(graph, Graph):
        raise TypeError("graph must be an instance of Graph")

    # Iterations validation
    if not isinstance(iterations, int):
        raise TypeError("iterations must be an integer")

    if iterations <= 0:
        raise ValueError("iterations must be a positive integer")

    # Damping validation
    if not isinstance(damping, (int, float)):
        raise TypeError("damping must be a numeric value")

    if not (0.0 < damping < 1.0):
        raise ValueError("damping must be between 0 and 1 (exclusive)")

    # Threads validation
    if not isinstance(threads, int):
        raise TypeError("threads must be an integer")

    if threads == 0:
        raise ValueError("threads must be >= 1 or -1")

    if threads < -1:
        raise ValueError("threads must be -1 (auto) or a positive integer")

    return _parallel_pagerank_bfs(graph, iterations, damping, threads)