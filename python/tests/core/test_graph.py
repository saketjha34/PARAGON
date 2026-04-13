import pytest

from paragon import Graph, WeightedGraph


# GRAPH TESTS
def test_graph_constructor_basic():
    g = Graph(5)
    assert g.vertices() == 5
    assert not g.is_directed()


def test_graph_constructor_adj_list():
    g = Graph([[1, 2], [0], [0]])
    assert g.vertices() == 3
    assert g.has_edge(0, 1)
    assert g.has_edge(0, 2)


def test_graph_constructor_edge_list():
    g = Graph(3, [(0, 1), (1, 2)])
    assert g.has_edge(0, 1)
    assert g.has_edge(1, 2)


def test_graph_add_edge_undirected():
    g = Graph(3)
    g.add_edge(0, 1)

    assert g.has_edge(0, 1)
    assert g.has_edge(1, 0)


def test_graph_add_edge_directed():
    g = Graph(3, directed=True)
    g.add_edge(0, 1)

    assert g.has_edge(0, 1)
    assert not g.has_edge(1, 0)


def test_graph_add_edges():
    g = Graph(4)
    g.add_edges([(0, 1), (1, 2), (2, 3)])

    assert g.has_edge(0, 1)
    assert g.has_edge(1, 2)
    assert g.has_edge(2, 3)


def test_graph_degree():
    g = Graph(4)
    g.add_edges([(0, 1), (0, 2), (0, 3)])

    assert g.degree(0) == 3
    assert g.degree(1) == 1


def test_graph_add_vertex():
    g = Graph(2)
    g.add_vertex()

    assert g.vertices() == 3


def test_graph_build_from_adj_list():
    g = Graph(3)
    g.build_from_adj_list([[1], [0, 2], [1]])

    assert g.has_edge(1, 2)
    assert g.has_edge(2, 1)


def test_graph_build_from_adj_matrix():
    g = Graph(1)
    g.build_from_adj_matrix([
        [0, 1],
        [1, 0]
    ])

    assert g.has_edge(0, 1)
    assert g.has_edge(1, 0)


def test_graph_invalid_edge():
    g = Graph(2)

    with pytest.raises(Exception):
        g.add_edge(0, 5)


# WEIGHTED GRAPH TESTS
def test_weighted_constructor():
    g = WeightedGraph(5)
    assert g.vertices() == 5


def test_weighted_add_edge():
    g = WeightedGraph(3)
    g.add_edge(0, 1, 2.5)

    adj = g.get_adj()
    assert len(adj[0]) == 1
    assert adj[0][0][0] == 1
    assert adj[0][0][1] == 2.5


def test_weighted_add_edge_directed():
    g = WeightedGraph(3, directed=True)
    g.add_edge(0, 1, 1.0)

    assert g.has_edge(0, 1)
    assert not g.has_edge(1, 0)


def test_weighted_add_edges():
    g = WeightedGraph(4)
    g.add_edges([
        (0, 1, 1.5),
        (1, 2, 2.5),
        (2, 3, 3.5),
    ])

    assert g.has_edge(0, 1)
    assert g.has_edge(1, 2)
    assert g.has_edge(2, 3)


def test_weighted_degree():
    g = WeightedGraph(3)
    g.add_edge(0, 1, 1.0)
    g.add_edge(0, 2, 2.0)

    assert g.degree(0) == 2


def test_weighted_build_from_adj_list():
    g = WeightedGraph(1)

    g.build_from_adj_list([
        [(1, 2.5)],
        [(0, 2.5), (2, 3.0)],
        [(1, 3.0)]
    ])

    adj = g.get_adj()

    # don't rely on order
    found = any(v == 2 and w == 3.0 for v, w in adj[1])
    assert found


def test_weighted_build_from_adj_matrix():
    g = WeightedGraph(1)

    g.build_from_adj_matrix([
        [0, 1.5, 0],
        [1.5, 0, 2.5],
        [0, 2.5, 0]
    ])

    adj = g.get_adj()

    found = any(v == 2 and w == 2.5 for v, w in adj[1])
    assert found


def test_weighted_add_vertex():
    g = WeightedGraph(2)
    g.add_vertex()

    assert g.vertices() == 3
    assert len(g.get_adj()) == 3


def test_weighted_invalid_edge():
    g = WeightedGraph(2)

    with pytest.raises(Exception):
        g.add_edge(0, 5, 1.0)


# STRESS TEST
def test_graph_small_stress():
    n = 100
    g = Graph(n)

    for i in range(n - 1):
        g.add_edge(i, i + 1)

    for i in range(n - 1):
        assert g.has_edge(i, i + 1)