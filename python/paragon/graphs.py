"""
Graph Generation Utilities

This module provides helper functions to generate sample graphs
using probabilistic distributions.

Currently supported:
- Normal (Gaussian) distribution based graph generation
"""

import random
from .core import Graph, WeightedGraph
from typing import Optional, Tuple


def generate_normal_graph(
    vertices: int,
    edges: int,
    directed: bool = False,
    mean: Optional[float] = None,
    std: Optional[float] = None,
    seed: Optional[int] = None,
) -> Graph:
    """
    Generate a graph using a normal (Gaussian) distribution.

    This function creates a graph with approximately `edges` edges,
    where node selection follows a normal distribution.

    Parameters
    ----------
    vertices : int
        Number of vertices (V)

    edges : int
        Number of edges (E)

    directed : bool, optional (default=False)
        Whether the graph is directed

    mean : float, optional
        Mean of the normal distribution (default = V/2)

    std : float, optional
        Standard deviation (default = V/6)

    seed : int, optional
        Random seed for reproducibility

    Returns
    -------
    Graph
        Generated graph instance

    Notes
    -----
    - Nodes near the mean will have higher connectivity
    - Useful for testing clustered graph structures
    - Does not guarantee exact E edges (approximate)

    Example
    -------
    >>> from paragon.graphs import generate_normal_graph
    >>> g = generate_normal_graph(vertices=10, edges=20)
    >>> print(g.vertices())
    10
    >>> print(len(g.get_adj()))
    10
    """

    # ================= VALIDATION ================= #
    if not isinstance(vertices, int) or vertices <= 0:
        raise ValueError("vertices must be a positive integer")

    if not isinstance(edges, int) or edges < 0:
        raise ValueError("edges must be a non-negative integer")

    if not isinstance(directed, bool):
        raise TypeError("directed must be a boolean")

    if seed is not None:
        random.seed(seed)

    if mean is None:
        mean = vertices / 2

    if std is None:
        std = max(1.0, vertices / 6)

    if std <= 0:
        raise ValueError("std must be positive")

    # ================= GRAPH INIT ================= #
    g = Graph(vertices=vertices, directed=directed)

    added_edges = set()

    def sample_node() -> int:
        """Sample node using normal distribution."""
        while True:
            x = int(random.gauss(mean, std))
            if 0 <= x < vertices:
                return x

    # ================= EDGE GENERATION ================= #
    attempts = 0
    max_attempts = edges * 10  # avoid infinite loops

    while len(added_edges) < edges and attempts < max_attempts:
        u = sample_node()
        v = sample_node()

        if u == v:
            attempts += 1
            continue

        edge = (u, v) if directed else tuple(sorted((u, v)))

        if edge not in added_edges:
            added_edges.add(edge)
            g.add_edge(u, v)

        attempts += 1

    return g



def generate_normal_weighted_graph(
    vertices: int,
    edges: int,
    directed: bool = False,
    mean: Optional[float] = None,
    std: Optional[float] = None,
    weight_range: Tuple[float, float] = (1.0, 10.0),
    weight_distribution: str = "uniform",
    seed: Optional[int] = None,
) -> WeightedGraph:
    """
    Generate a weighted graph using a normal (Gaussian) distribution.

    Parameters
    ----------
    vertices : int
        Number of vertices

    edges : int
        Number of edges

    directed : bool, default=False

    mean : float, optional
        Mean for node sampling (default = V/2)

    std : float, optional
        Standard deviation (default = V/6)

    weight_range : Tuple[float, float], default=(1.0, 10.0)
        Range of edge weights

    weight_distribution : str, default="uniform"
        Options:
        - "uniform"
        - "normal"

    seed : int, optional

    Returns
    -------
    WeightedGraph

    Example
    -------
    >>> from paragon.graphs import generate_normal_weighted_graph
    >>> g = generate_normal_weighted_graph(10, 20)
    >>> print(g.get_adj()[0])
    [(3, 4.2), (5, 7.1)]
    """

    # ================= VALIDATION ================= #
    if not isinstance(vertices, int) or vertices <= 0:
        raise ValueError("vertices must be positive integer")

    if not isinstance(edges, int) or edges < 0:
        raise ValueError("edges must be non-negative integer")

    if weight_range[0] >= weight_range[1]:
        raise ValueError("invalid weight_range")

    if weight_distribution not in {"uniform", "normal"}:
        raise ValueError("weight_distribution must be 'uniform' or 'normal'")

    if seed is not None:
        random.seed(seed)

    if mean is None:
        mean = vertices / 2

    if std is None:
        std = max(1.0, vertices / 6)

    g = WeightedGraph(vertices=vertices, directed=directed)

    added_edges = set()

    # ================= HELPERS ================= #
    def sample_node():
        while True:
            x = int(random.gauss(mean, std))
            if 0 <= x < vertices:
                return x

    def sample_weight():
        if weight_distribution == "uniform":
            return random.uniform(*weight_range)
        else:
            mu = sum(weight_range) / 2
            sigma = (weight_range[1] - weight_range[0]) / 6
            while True:
                w = random.gauss(mu, sigma)
                if weight_range[0] <= w <= weight_range[1]:
                    return w

    # ================= EDGE GEN ================= #
    attempts = 0
    max_attempts = edges * 10

    while len(added_edges) < edges and attempts < max_attempts:
        u = sample_node()
        v = sample_node()

        if u == v:
            attempts += 1
            continue

        edge = (u, v) if directed else tuple(sorted((u, v)))

        if edge not in added_edges:
            added_edges.add(edge)
            g.add_edge(u, v, sample_weight())

        attempts += 1

    return g