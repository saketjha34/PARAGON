import pytest
from paragon import Graph
from paragon.algorithms import parallel_pagerank_bfs
from paragon.algorithms import parallel_pagerank



# HELPERS
def approx_equal(a, b, eps=1e-6):
    return abs(a - b) < eps


def sum_close_to_one(rank):
    return approx_equal(sum(rank), 1.0)


# BASIC TESTS
def test_pagerank_bfs_single_node():
    g = Graph(1)

    rank = parallel_pagerank_bfs(g, iterations=10, damping=0.85)

    assert len(rank) == 1
    assert approx_equal(rank[0], 1.0)


def test_pagerank_bfs_two_nodes():
    g = Graph(2)
    g.add_edges([(0, 1), (1, 0)])

    rank = parallel_pagerank_bfs(g, iterations=50, damping=0.85)

    assert approx_equal(rank[0], rank[1])
    assert sum_close_to_one(rank)


# STRUCTURAL TESTS
def test_pagerank_bfs_chain():
    """
    0 -> 1 -> 2 -> 3
    """
    g = Graph(4, directed=True)
    g.add_edges([(0,1), (1,2), (2,3)])

    rank = parallel_pagerank_bfs(g, iterations=100, damping=0.85)

    assert rank[3] > rank[2] > rank[1] > rank[0]
    assert sum_close_to_one(rank)


def test_pagerank_bfs_cycle():
    g = Graph(3, directed=True)
    g.add_edges([(0,1), (1,2), (2,0)])

    rank = parallel_pagerank_bfs(g, iterations=100, damping=0.85)

    assert approx_equal(rank[0], rank[1])
    assert approx_equal(rank[1], rank[2])
    assert sum_close_to_one(rank)


def test_pagerank_bfs_star():
    """
    incoming star
    """
    g = Graph(5, directed=True)
    g.add_edges([(1,0), (2,0), (3,0), (4,0)])

    rank = parallel_pagerank_bfs(g, iterations=100, damping=0.85)

    center = rank[0]
    others = rank[1:]

    assert all(center > x for x in others)
    assert sum_close_to_one(rank)


# DISCONNECTED GRAPH
def test_pagerank_bfs_disconnected():
    g = Graph(4, directed=True)
    g.add_edges([(0,1), (2,3)])

    rank = parallel_pagerank_bfs(g, iterations=100, damping=0.85)

    assert len(rank) == 4
    assert sum_close_to_one(rank)


# NON-NEGATIVE
def test_pagerank_bfs_non_negative():
    g = Graph(5, directed=True)
    g.add_edges([(0,1), (1,2), (2,3), (3,4)])

    rank = parallel_pagerank_bfs(g, iterations=50, damping=0.85)

    assert all(r >= 0 for r in rank)


# THREAD SAFETY
def test_pagerank_bfs_threads():
    g = Graph(6, directed=True)
    g.add_edges([
        (0,1), (1,2), (2,3),
        (3,4), (4,5)
    ])

    r1 = parallel_pagerank_bfs(g, iterations=50, damping=0.85, threads=1)
    r2 = parallel_pagerank_bfs(g, iterations=50, damping=0.85, threads=4)

    # results should be similar
    diff = sum(abs(a - b) for a, b in zip(r1, r2))
    assert diff < 1e-3


# CONSISTENCY WITH PULL VERSION
def test_pagerank_bfs_vs_standard():
    """
    Push vs Pull should produce similar results
    """
    g = Graph(5, directed=True)
    g.add_edges([
        (0,1), (0,2),
        (1,3), (2,3),
        (3,4)
    ])

    r_push = parallel_pagerank_bfs(g, iterations=100, damping=0.85)
    r_pull = parallel_pagerank(g, iterations=100, damping=0.85)

    diff = sum(abs(a - b) for a, b in zip(r_push, r_pull))

    assert diff < 0.05  # allow small numerical differences


# INVALID INPUTS
def test_pagerank_bfs_invalid_iterations():
    g = Graph(3)

    with pytest.raises(Exception):
        parallel_pagerank_bfs(g, iterations=-1, damping=0.85)


def test_pagerank_bfs_invalid_damping():
    g = Graph(3)

    with pytest.raises(Exception):
        parallel_pagerank_bfs(g, iterations=10, damping=1.5)


# STRESS TEST
def test_pagerank_bfs_large_graph():
    n = 100
    g = Graph(n, directed=True)

    for i in range(n - 1):
        g.add_edge(i, i + 1)

    rank = parallel_pagerank_bfs(g, iterations=50, damping=0.85)

    assert len(rank) == n
    assert sum_close_to_one(rank)