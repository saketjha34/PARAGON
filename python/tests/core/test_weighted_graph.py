import pytest
from paragon import WeightedGraph


# HELPERS
def has_weighted_edge(adj, u, v, w):
    """Check if weighted edge exists (order-independent)."""
    return any(x == v and abs(wt - w) < 1e-9 for x, wt in adj[u])


# CONSTRUCTOR TESTS
def test_constructor_basic():
    g = WeightedGraph(5)

    assert g.vertices() == 5
    assert not g.is_directed()


def test_constructor_directed():
    g = WeightedGraph(3, directed=True)

    assert g.is_directed()


# EDGE OPERATIONS
def test_add_edge():
    g = WeightedGraph(3)

    g.add_edge(0, 1, 2.5)

    adj = g.get_adj()

    assert has_weighted_edge(adj, 0, 1, 2.5)
    assert g.has_edge(0, 1)


def test_add_edge_undirected():
    g = WeightedGraph(3)

    g.add_edge(0, 1, 1.0)

    adj = g.get_adj()

    assert has_weighted_edge(adj, 0, 1, 1.0)
    assert has_weighted_edge(adj, 1, 0, 1.0)
    assert g.has_edge(1, 0)


def test_add_edge_directed():
    g = WeightedGraph(3, directed=True)

    g.add_edge(0, 1, 1.0)

    assert g.has_edge(0, 1)
    assert not g.has_edge(1, 0)


def test_add_edges_bulk():
    g = WeightedGraph(4)

    g.add_edges([
        (0, 1, 1.5),
        (1, 2, 2.5),
        (2, 3, 3.5),
    ])

    assert g.has_edge(0, 1)
    assert g.has_edge(1, 2)
    assert g.has_edge(2, 3)


# BUILD METHODS
def test_build_from_adj_list():
    g = WeightedGraph(1)

    g.build_from_adj_list([
        [(1, 2.5)],
        [(0, 2.5), (2, 3.0)],
        [(1, 3.0)],
    ])

    adj = g.get_adj()

    assert has_weighted_edge(adj, 1, 2, 3.0)
    assert has_weighted_edge(adj, 0, 1, 2.5)


def test_build_from_adj_matrix():
    g = WeightedGraph(1)

    g.build_from_adj_matrix([
        [0, 1.5, 0],
        [1.5, 0, 2.5],
        [0, 2.5, 0],
    ])

    adj = g.get_adj()

    assert has_weighted_edge(adj, 1, 2, 2.5)
    assert has_weighted_edge(adj, 0, 1, 1.5)


# DEGREE + CONSISTENCY
def test_degree():
    g = WeightedGraph(3)

    g.add_edge(0, 1, 1.0)
    g.add_edge(0, 2, 2.0)

    assert g.degree(0) == 2


def test_has_edge_consistency():
    g = WeightedGraph(3)

    g.add_edge(0, 1, 5.0)

    assert g.has_edge(0, 1)


# ADD VERTEX
def test_add_vertex():
    g = WeightedGraph(2)

    g.add_vertex()

    assert g.vertices() == 3
    assert len(g.get_adj()) == 3


# EXCEPTION TESTS
def test_invalid_edge_index():
    g = WeightedGraph(2)

    with pytest.raises(Exception):
        g.add_edge(0, 5, 1.0)


def test_invalid_weight_type():
    g = WeightedGraph(2)

    with pytest.raises(TypeError):
        g.add_edge(0, 1, "invalid")


# COMPLEX GRAPH
def test_complex_graph_structure():
    g = WeightedGraph(5)

    g.add_edges([
        (0, 1, 1.0),
        (0, 2, 2.0),
        (1, 3, 3.0),
        (2, 3, 4.0),
        (3, 4, 5.0),
    ])

    assert g.has_edge(3, 4)
    assert g.degree(3) == 3


# STRESS TEST
def test_small_stress():
    n = 100
    g = WeightedGraph(n)

    for i in range(n - 1):
        g.add_edge(i, i + 1, float(i))

    for i in range(n - 1):
        assert g.has_edge(i, i + 1)