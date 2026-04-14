import pytest
from paragon import Graph, WeightedGraph
import copy


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

# ================= INIT VALIDATION ================= #
def test_invalid_vertex_count_type():
    with pytest.raises(TypeError):
        Graph("5")


def test_invalid_vertex_count_negative():
    with pytest.raises(ValueError):
        Graph(-1)


def test_invalid_edges_format():
    with pytest.raises(TypeError):
        Graph(3, edges=[(0, 1, 2)])  # invalid tuple size


def test_invalid_edges_out_of_range():
    with pytest.raises(ValueError):
        Graph(3, edges=[(0, 5)])


def test_invalid_adj_list_type():
    with pytest.raises(TypeError):
        Graph("not a list")


def test_invalid_adj_list_structure():
    with pytest.raises(TypeError):
        Graph([1, 2, 3])  # not list of lists


def test_invalid_adj_list_values():
    with pytest.raises(ValueError):
        Graph([[1, 2], [0, 5]])  # 5 out of range


# ================= EDGE VALIDATION ================= #
def test_add_edge_invalid_type():
    g = Graph(3)

    with pytest.raises(TypeError):
        g.add_edge(0, "1")


def test_add_edge_negative_index():
    g = Graph(3)

    with pytest.raises(ValueError):
        g.add_edge(-1, 2)


def test_add_edge_out_of_range():
    g = Graph(3)

    with pytest.raises(ValueError):
        g.add_edge(0, 5)


# ================= NODE VALIDATION ================= #
def test_degree_invalid_node():
    g = Graph(3)

    with pytest.raises(ValueError):
        g.degree(5)


def test_has_edge_invalid_node():
    g = Graph(3)

    with pytest.raises(ValueError):
        g.has_edge(0, 10)


# ================= MATRIX VALIDATION ================= #
def test_invalid_matrix_not_list():
    g = Graph(3)

    with pytest.raises(TypeError):
        g.build_from_adj_matrix("not a matrix")


def test_invalid_matrix_not_square():
    g = Graph(3)

    with pytest.raises(ValueError):
        g.build_from_adj_matrix([
            [0, 1],
            [1, 0],
            [0, 1]
        ])


def test_invalid_matrix_values():
    g = Graph(3)

    with pytest.raises(TypeError):
        g.build_from_adj_matrix([
            [0, 1, 0],
            [1, "x", 1],
            [0, 1, 0]
        ])


# ================= ADJ LIST BUILD VALIDATION ================= #
def test_build_adj_list_invalid_structure():
    g = Graph(3)

    with pytest.raises(TypeError):
        g.build_from_adj_list([1, 2, 3])


def test_build_adj_list_invalid_value():
    g = Graph(3)

    with pytest.raises(ValueError):
        g.build_from_adj_list([
            [1],
            [2],
            [5]  # invalid
        ])


# ================= __len__ ================= #

def test_len():
    g = Graph(vertices=5)
    assert len(g) == 5


# ================= __contains__ ================= #

def test_contains():
    g = Graph(vertices=3)

    assert 0 in g
    assert 2 in g
    assert 3 not in g
    assert -1 not in g
    assert "1" not in g


# ================= __getitem__ ================= #

def test_getitem():
    g = Graph(vertices=3)
    g.add_edges(edges=[(0, 1), (1, 2)])

    assert g[1] == [0, 2]

def test_getitem_invalid():
    g = Graph(vertices=3)

    with pytest.raises(ValueError):
        _ = g[5]


# ================= __iter__ ================= #

def test_iter():
    g = Graph(vertices=4)

    nodes = list(iter(g))
    assert nodes == [0, 1, 2, 3]


# ================= __repr__ ================= #

def test_repr():
    g = Graph(vertices=3)

    r = repr(g)

    assert "Graph(" in r
    assert "vertices=3" in r
    assert "directed=False" in r


# ================= __eq__ / __ne__ ================= #

def test_eq():
    g1 = Graph(vertices=3)
    g2 = Graph(vertices=3)

    assert g1 == g2


def test_ne():
    g1 = Graph(vertices=3)
    g2 = Graph(vertices=3)
    g2.add_edge(u=0, v=1)

    assert g1 != g2


# ================= __bool__ ================= #

def test_bool():
    g = Graph(vertices=3)

    assert bool(g) is True

def test_bool_empty_like():
    # Graph always has vertices > 0 in your design
    g = Graph(vertices=1)
    assert bool(g)


# ================= __copy__ ================= #

def test_copy():
    g = Graph(vertices=3)
    g.add_edge(u=0, v=1)

    g2 = copy.copy(g)

    assert g2 == g
    assert g2 is not g


# ================= __deepcopy__ ================= #

def test_deepcopy():
    g = Graph(vertices=3)
    g.add_edge(u=0, v=1)

    g2 = copy.deepcopy(g)

    assert g2 == g
    assert g2 is not g

    # modify original → deepcopy should not change
    g.add_edge(u=1, v=2)

    assert g2 != g


# ================= EDGE CASE ================= #

def test_getitem_after_modification():
    g = Graph(vertices=3)
    g.add_edge(u=0, v=1)

    assert g[0] == [1]

    g.add_edge(u=0, v=2)

    assert sorted(g[0]) == [1, 2]