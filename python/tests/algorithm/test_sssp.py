from paragon import WeightedGraph
from paragon.algorithms import parallel_dijkstra

INF = 1e18

# HELPERS
def approx_equal(a, b, eps=1e-6):
    return abs(a - b) < eps

# BASIC TESTS
def test_sssp_single_node():
    g = WeightedGraph(1)

    dist = parallel_dijkstra(g, 0)

    assert len(dist) == 1
    assert approx_equal(dist[0], 0.0)


def test_sssp_simple_chain():
    """
    0 --1--> 1 --2--> 2 --3--> 3
    """
    g = WeightedGraph(4, directed=True)
    g.add_edges([
        (0,1,1.0),
        (1,2,2.0),
        (2,3,3.0)
    ])

    dist = parallel_dijkstra(g, 0)

    assert dist == [0.0, 1.0, 3.0, 6.0]


# MULTIPLE PATHS
def test_sssp_multiple_paths():
    """
    0 -> 1 (1)
    0 -> 2 (4)
    1 -> 2 (2)
    """
    g = WeightedGraph(3, directed=True)
    g.add_edges([
        (0,1,1.0),
        (0,2,4.0),
        (1,2,2.0)
    ])

    dist = parallel_dijkstra(g, 0)

    # shortest path to 2 is via 1
    assert dist[2] == 3.0


# UNDIRECTED GRAPH
def test_sssp_undirected():
    g = WeightedGraph(3, directed=False)
    g.add_edges([
        (0,1,1.0),
        (1,2,2.0)
    ])

    dist = parallel_dijkstra(g, 0)

    assert dist == [0.0, 1.0, 3.0]


# DISCONNECTED GRAPH
def test_sssp_disconnected():
    g = WeightedGraph(4, directed=True)
    g.add_edges([
        (0,1,1.0),
        (2,3,2.0)
    ])

    dist = parallel_dijkstra(g, 0)

    assert dist[0] == 0.0
    assert dist[1] == 1.0
    assert dist[2] >= INF / 10   # unreachable
    assert dist[3] >= INF / 10


# ZERO WEIGHTS
def test_sssp_zero_weight_edges():
    g = WeightedGraph(3, directed=True)
    g.add_edges([
        (0,1,0.0),
        (1,2,0.0)
    ])

    dist = parallel_dijkstra(g, 0)

    assert dist == [0.0, 0.0, 0.0]


# SELF LOOP
def test_sssp_self_loop():
    g = WeightedGraph(2, directed=True)
    g.add_edge(0, 0, 5.0)

    dist = parallel_dijkstra(g, 0)

    assert dist[0] == 0.0


# THREAD TEST
def test_sssp_threads_consistency():
    g = WeightedGraph(5, directed=True)
    g.add_edges([
        (0,1,1.0),
        (1,2,2.0),
        (2,3,3.0),
        (3,4,4.0)
    ])

    d1 = parallel_dijkstra(g, 0, threads=1)
    d2 = parallel_dijkstra(g, 0, threads=4)

    for a, b in zip(d1, d2):
        assert approx_equal(a, b)


# RELAXATION PROPERTY
def test_sssp_relaxation_property():
    """
    For every edge (u, v, w):
    dist[v] <= dist[u] + w
    """
    g = WeightedGraph(5, directed=True)
    g.add_edges([
        (0,1,2.0),
        (1,2,3.0),
        (0,3,10.0),
        (3,4,1.0),
        (2,4,2.0)
    ])

    dist = parallel_dijkstra(g, 0)
    adj = g.get_adj()

    for u in range(len(adj)):
        for v, w in adj[u]:
            if dist[u] < INF:
                assert dist[v] <= dist[u] + w + 1e-9



# STRESS TEST
def test_sssp_large_chain():
    n = 200
    g = WeightedGraph(n, directed=True)

    for i in range(n - 1):
        g.add_edge(i, i + 1, 1.0)

    dist = parallel_dijkstra(g, 0)

    assert dist[0] == 0.0
    assert dist[n - 1] == n - 1


# CONSISTENCY
def test_sssp_repeatability():
    g = WeightedGraph(5, directed=True)
    g.add_edges([
        (0,1,1.0),
        (0,2,5.0),
        (1,2,2.0),
        (2,3,1.0),
        (3,4,3.0)
    ])

    d1 = parallel_dijkstra(g, 0)
    d2 = parallel_dijkstra(g, 0)

    assert d1 == d2