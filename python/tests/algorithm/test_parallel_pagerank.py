import pytest
from paragon import Graph
from paragon.algorithms import parallel_pagerank


# HELPERS
def approx_equal(a, b, eps=1e-6):
    return abs(a - b) < eps


# BASIC FUNCTIONALITY
def test_pagerank_single_node():
    g = Graph(1)

    rank = parallel_pagerank(g, iterations=10, damping=0.85)

    assert len(rank) == 1
    assert approx_equal(rank[0], 1.0)


def test_pagerank_two_nodes_bidirectional():
    """
    0 <-> 1
    Equal importance
    """
    g = Graph(2)
    g.add_edges([(0, 1), (1, 0)])

    rank = parallel_pagerank(g, iterations=50, damping=0.85)

    assert approx_equal(rank[0], rank[1])
    assert approx_equal(sum(rank), 1.0)


# CHAIN GRAPH
def test_pagerank_chain():
    """
    0 -> 1 -> 2 -> 3
    Node 3 should have highest rank
    """
    g = Graph(4, directed=True)
    g.add_edges([(0,1), (1,2), (2,3)])

    rank = parallel_pagerank(g, iterations=100, damping=0.85)

    assert rank[3] > rank[2] > rank[1] > rank[0]
    assert approx_equal(sum(rank), 1.0)


# STAR GRAPH
def test_pagerank_star():
    """
        1
        ↑
    2 ← 0 → 3
        ↓
        4

    Center (0) should dominate
    """
    g = Graph(5, directed=True)
    g.add_edges([
        (1,0), (2,0), (3,0), (4,0)
    ])

    rank = parallel_pagerank(g, iterations=100, damping=0.85)

    center = rank[0]
    others = rank[1:]

    assert all(center > x for x in others)
    assert approx_equal(sum(rank), 1.0)


# CYCLE GRAPH
def test_pagerank_cycle():
    """
    0 -> 1 -> 2 -> 0
    All equal
    """
    g = Graph(3, directed=True)
    g.add_edges([(0,1), (1,2), (2,0)])

    rank = parallel_pagerank(g, iterations=100, damping=0.85)

    assert approx_equal(rank[0], rank[1])
    assert approx_equal(rank[1], rank[2])
    assert approx_equal(sum(rank), 1.0)


# DISCONNECTED GRAPH
def test_pagerank_disconnected():
    """
    Two components
    """
    g = Graph(4, directed=True)
    g.add_edges([(0,1), (2,3)])

    rank = parallel_pagerank(g, iterations=100, damping=0.85)

    assert len(rank) == 4
    assert approx_equal(sum(rank), 1.0)


# NO NEGATIVE VALUES
def test_pagerank_non_negative():
    g = Graph(5, directed=True)
    g.add_edges([(0,1), (1,2), (2,3), (3,4)])

    rank = parallel_pagerank(g, iterations=50, damping=0.85)

    assert all(r >= 0 for r in rank)


# DAMPING EFFECT
def test_pagerank_damping_effect():
    g = Graph(3, directed=True)
    g.add_edges([(0,1), (1,2)])

    r1 = parallel_pagerank(g, iterations=50, damping=0.85)
    r2 = parallel_pagerank(g, iterations=50, damping=0.50)

    # distributions should differ
    assert any(abs(a - b) > 1e-6 for a, b in zip(r1, r2))


# ITERATION EFFECT (CONVERGENCE)
def test_pagerank_convergence():
    g = Graph(4, directed=True)
    g.add_edges([(0,1), (1,2), (2,3), (3,0)])

    r1 = parallel_pagerank(g, iterations=10, damping=0.85)
    r2 = parallel_pagerank(g, iterations=100, damping=0.85)

    # later iterations should stabilize
    diff = sum(abs(a - b) for a, b in zip(r1, r2))
    assert diff < 0.5  # loose bound (convergence behavior)


# INVALID INPUT
def test_pagerank_invalid_iterations():
    g = Graph(3)

    with pytest.raises(Exception):
        parallel_pagerank(g, iterations=-1, damping=0.85)


def test_pagerank_invalid_damping():
    g = Graph(3)

    with pytest.raises(Exception):
        parallel_pagerank(g, iterations=10, damping=1.5)


# STRESS TEST
def test_pagerank_large_graph():
    n = 100
    g = Graph(n, directed=True)

    for i in range(n - 1):
        g.add_edge(i, i + 1)

    rank = parallel_pagerank(g, iterations=50, damping=0.85)

    assert len(rank) == n
    assert approx_equal(sum(rank), 1.0)