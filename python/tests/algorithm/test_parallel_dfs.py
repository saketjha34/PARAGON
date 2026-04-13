import pytest
from paragon import Graph
from paragon.algorithms import parallel_dfs


# BASIC FUNCTIONALITY
def test_dfs_simple_chain():
    """
    0 - 1 - 2 - 3
    """
    g = Graph(4)
    g.add_edges([(0, 1), (1, 2), (2, 3)])

    visited = parallel_dfs(g, 0)

    assert visited == [True, True, True, True]


def test_dfs_disconnected_graph():
    """
    0 - 1   2 - 3
    """
    g = Graph(4)
    g.add_edges([(0, 1), (2, 3)])

    visited = parallel_dfs(g, 0)

    assert visited == [True, True, False, False]


def test_dfs_single_node():
    g = Graph(1)

    visited = parallel_dfs(g, 0)

    assert visited == [True]


# DIRECTED GRAPH
def test_dfs_directed_graph():
    """
    0 -> 1 -> 2
    """
    g = Graph(3, directed=True)
    g.add_edges([(0, 1), (1, 2)])

    visited = parallel_dfs(g, 0)

    assert visited == [True, True, True]


def test_dfs_directed_reverse_not_reachable():
    """
    0 <- 1 <- 2
    """
    g = Graph(3, directed=True)
    g.add_edges([(1, 0), (2, 1)])

    visited = parallel_dfs(g, 0)

    assert visited == [True, False, False]


# CYCLES
def test_dfs_cycle():
    """
    0 - 1 - 2 - 0
    """
    g = Graph(3)
    g.add_edges([(0, 1), (1, 2), (2, 0)])

    visited = parallel_dfs(g, 0)

    assert visited == [True, True, True]


def test_dfs_self_loop():
    g = Graph(2)
    g.add_edge(0, 0)

    visited = parallel_dfs(g, 0)

    assert visited[0] is True


# MULTIPLE COMPONENTS
def test_dfs_multiple_components():
    """
    0-1   2-3   4
    """
    g = Graph(5)
    g.add_edges([(0, 1), (2, 3)])

    visited = parallel_dfs(g, 2)

    assert visited == [False, False, True, True, False]


# THREAD PARAMETER
def test_dfs_with_threads():
    g = Graph(5)
    g.add_edges([(0,1), (1,2), (2,3), (3,4)])

    visited = parallel_dfs(g, 0, threads=2)

    assert visited == [True, True, True, True, True]



# STRESS TEST
def test_dfs_large_chain():
    n = 1000
    g = Graph(n)

    for i in range(n - 1):
        g.add_edge(i, i + 1)

    visited = parallel_dfs(g, 0)

    assert all(visited)


# CONSISTENCY TEST
def test_dfs_repeatability():
    """
    Ensure deterministic output (important for parallel code)
    """
    g = Graph(5)
    g.add_edges([(0,1), (1,2), (2,3), (3,4)])

    v1 = parallel_dfs(g, 0)
    v2 = parallel_dfs(g, 0)

    assert v1 == v2