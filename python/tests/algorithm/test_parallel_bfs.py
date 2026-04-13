from paragon import Graph
from paragon.algorithms import  parallel_bfs


# BASIC FUNCTIONALITY
def test_bfs_simple_chain():
    """
    0 - 1 - 2 - 3
    """
    g = Graph(4)
    g.add_edges([(0, 1), (1, 2), (2, 3)])

    dist = parallel_bfs(g, 0)

    assert dist == [0, 1, 2, 3]


def test_bfs_disconnected_graph():
    """
    0 - 1   2 - 3
    """
    g = Graph(4)
    g.add_edges([(0, 1), (2, 3)])

    dist = parallel_bfs(g, 0)

    assert dist == [0, 1, -1, -1]


def test_bfs_single_node():
    g = Graph(1)

    dist = parallel_bfs(g, 0)

    assert dist == [0]


# DIRECTED GRAPH
def test_bfs_directed_graph():
    """
    0 -> 1 -> 2
    """
    g = Graph(3, directed=True)
    g.add_edges([(0, 1), (1, 2)])

    dist = parallel_bfs(g, 0)

    assert dist == [0, 1, 2]


def test_bfs_directed_reverse_not_reachable():
    """
    0 <- 1 <- 2
    """
    g = Graph(3, directed=True)
    g.add_edges([(1, 0), (2, 1)])

    dist = parallel_bfs(g, 0)

    assert dist == [0, -1, -1]


# CYCLES
def test_bfs_cycle():
    """
    0 - 1 - 2 - 0
    """
    g = Graph(3)
    g.add_edges([(0, 1), (1, 2), (2, 0)])

    dist = parallel_bfs(g, 0)

    # shortest paths
    assert dist[0] == 0
    assert dist[1] == 1
    assert dist[2] == 1


def test_bfs_self_loop():
    g = Graph(2)
    g.add_edge(0, 0)

    dist = parallel_bfs(g, 0)

    assert dist[0] == 0


# MULTIPLE COMPONENTS
def test_bfs_multiple_components():
    """
    0-1   2-3   4
    """
    g = Graph(5)
    g.add_edges([(0, 1), (2, 3)])

    dist = parallel_bfs(g, 2)

    assert dist == [-1, -1, 0, 1, -1]


# THREAD PARAMETER
def test_bfs_with_threads():
    g = Graph(5)
    g.add_edges([(0,1), (1,2), (2,3), (3,4)])

    dist = parallel_bfs(g, 0, threads=4)

    assert dist == [0, 1, 2, 3, 4]



# STRESS TEST
def test_bfs_large_chain():
    n = 1000
    g = Graph(n)

    for i in range(n - 1):
        g.add_edge(i, i + 1)

    dist = parallel_bfs(g, 0)

    assert dist[0] == 0
    assert dist[n - 1] == n - 1


# CONSISTENCY TEST
def test_bfs_repeatability():
    """
    BFS should be deterministic
    """
    g = Graph(6)
    g.add_edges([
        (0,1), (0,2),
        (1,3), (2,3),
        (3,4), (4,5)
    ])

    d1 = parallel_bfs(g, 0)
    d2 = parallel_bfs(g, 0)

    assert d1 == d2


# LEVEL PROPERTY VALIDATION
def test_bfs_level_property():
    """
    For every edge (u, v):
    dist[v] <= dist[u] + 1
    """
    g = Graph(6)
    g.add_edges([
        (0,1), (0,2),
        (1,3), (2,3),
        (3,4), (4,5)
    ])

    dist = parallel_bfs(g, 0)
    adj = g.get_adj()

    for u in range(len(adj)):
        for v in adj[u]:
            if dist[u] != -1:
                assert dist[v] <= dist[u] + 1