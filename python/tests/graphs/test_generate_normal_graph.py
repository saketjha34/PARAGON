import pytest
from paragon.graphs import generate_normal_graph
from paragon import Graph


# ================= BASIC FUNCTIONALITY ================= #
def test_basic_graph_creation():
    g = generate_normal_graph(vertices=10, edges=20)

    assert isinstance(g, Graph)
    assert g.vertices() == 10


def test_edge_count_approximation():
    g = generate_normal_graph(vertices=10, edges=20)

    total_edges = sum(len(adj) for adj in g.get_adj())

    # Undirected graph stores edges twice
    assert total_edges >= 10  # lower bound sanity
    assert total_edges <= 40  # upper bound sanity


# ================= DIRECTED / UNDIRECTED ================= #
def test_directed_graph():
    g = generate_normal_graph(vertices=10, edges=20, directed=True)

    assert g.is_directed() is True


def test_undirected_symmetry():
    g = generate_normal_graph(vertices=10, edges=20, directed=False)

    adj = g.get_adj()

    for u in range(len(adj)):
        for v in adj[u]:
            assert u in adj[v]


# ================= NO SELF LOOPS ================= #
def test_no_self_loops():
    g = generate_normal_graph(vertices=20, edges=50)

    for u, neighbors in enumerate(g.get_adj()):
        for v in neighbors:
            assert u != v


# ================= NO DUPLICATE EDGES ================= #
def test_no_duplicate_edges():
    g = generate_normal_graph(vertices=20, edges=50)

    seen = set()

    for u, neighbors in enumerate(g.get_adj()):
        for v in neighbors:
            edge = tuple(sorted((u, v)))
            seen.add(edge)

    # Number of unique edges <= requested edges
    assert len(seen) <= 50


# ================= REPRODUCIBILITY ================= #
def test_seed_reproducibility():
    g1 = generate_normal_graph(vertices=10, edges=20, seed=42)
    g2 = generate_normal_graph(vertices=10, edges=20, seed=42)

    assert g1.get_adj() == g2.get_adj()


# ================= PARAM VALIDATION ================= #
def test_invalid_vertices():
    with pytest.raises(ValueError):
        generate_normal_graph(vertices=0, edges=10)


def test_invalid_edges():
    with pytest.raises(ValueError):
        generate_normal_graph(vertices=10, edges=-5)


def test_invalid_directed_type():
    with pytest.raises(TypeError):
        generate_normal_graph(vertices=10, edges=10, directed="yes")


def test_invalid_std():
    with pytest.raises(ValueError):
        generate_normal_graph(vertices=10, edges=10, std=0)


# ================= DISTRIBUTION SANITY ================= #
def test_nodes_within_range():
    g = generate_normal_graph(vertices=50, edges=100)

    for u, neighbors in enumerate(g.get_adj()):
        assert 0 <= u < 50
        for v in neighbors:
            assert 0 <= v < 50


# ================= STRESS TEST ================= #
def test_large_graph_generation():
    g = generate_normal_graph(vertices=1000, edges=3000)

    assert g.vertices() == 1000