"""
Parallel Connected Components

This module provides a Python interface for the high-performance
C++ implementation of parallel connected components in PARAGON.
"""

from typing import List
from ..core import Graph
from .._paragon import parallel_connected_components as _parallel_connected_components


def parallel_connected_components(graph: Graph, threads: int = -1) -> List[int]:
    """
    Compute connected components of a graph in parallel.

    This function assigns a component label to each node such that
    nodes with the same label belong to the same connected component.

    Parameters
    ----------
    graph : Graph
        Input graph (typically undirected).

    threads : int, optional (default = -1)
        Number of threads to use.
        -1 means automatically use hardware concurrency.

    Returns
    -------
    List[int]
        A list where:
        - component[i] = component ID of node i
        - Nodes with the same ID belong to the same component

    Notes
    -----
    - Based on a parallel Shiloach–Vishkin style algorithm.
    - Uses pointer jumping (path compression) for efficiency.
    - Iteratively merges components until convergence.

    Time Complexity
    ---------------
    Approximately O((V + E) log V) in parallel settings.

    Example
    -------
    >>> from paragon import Graph
    >>> from paragon.algorithms import connected_components
    >>> g = Graph(6)
    >>> g.add_edges([(0,1), (1,2), (3,4)])
    >>> connected_components(g)
    [0, 0, 0, 3, 3, 5]
    """
    return _parallel_connected_components(graph, threads)