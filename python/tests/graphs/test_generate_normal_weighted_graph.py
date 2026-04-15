import pytest
from paragon.graphs import (
    generate_normal_weighted_graph,
)
from paragon import WeightedGraph


# ================= BASIC FUNCTIONALITY ================= #
def test_basic_weighted_graph_creation():
    g = generate_normal_weighted_graph(vertices=10, edges=20)

    assert isinstance(g, WeightedGraph)
    assert g.vertices() == 10


def test_weight_presence():
    g = generate_normal_weighted_graph(vertices=10, edges=20)

    for neighbors in g.get_adj():
        for v, w in neighbors:
            assert isinstance(v, int)
            assert isinstance(w, float)


# ================= WEIGHT RANGE ================= #
def test_weight_range_uniform():
    g = generate_normal_weighted_graph(
        vertices=10,
        edges=20,
        weight_range=(1.0, 5.0),
        weight_distribution="uniform",
    )

    for neighbors in g.get_adj():
        for _, w in neighbors:
            assert 1.0 <= w <= 5.0


def test_weight_range_normal():
    g = generate_normal_weighted_graph(
        vertices=10,
        edges=20,
        weight_range=(1.0, 10.0),
        weight_distribution="normal",
    )

    for neighbors in g.get_adj():
        for _, w in neighbors:
            assert 1.0 <= w <= 10.0


# ================= DIRECTED / UNDIRECTED ================= #
def test_directed_weighted_graph():
    g = generate_normal_weighted_graph(vertices=10, edges=20, directed=True)

    assert g.is_directed() is True


def test_undirected_symmetry_with_weights():
    g = generate_normal_weighted_graph(vertices=10, edges=20, directed=False)

    adj = g.get_adj()

    for u in range(len(adj)):
        for v, w in adj[u]:
            # check reverse edge exists
            found = False
            for x, w2 in adj[v]:
                if x == u:
                    found = True
                    assert w == w2
            assert found


# ================= NO SELF LOOPS ================= #
def test_no_self_loops_weighted():
    g = generate_normal_weighted_graph(vertices=20, edges=50)

    for u, neighbors in enumerate(g.get_adj()):
        for v, _ in neighbors:
            assert u != v


# ================= NO DUPLICATES ================= #
def test_no_duplicate_weighted_edges():
    g = generate_normal_weighted_graph(vertices=20, edges=50)

    seen = set()

    for u, neighbors in enumerate(g.get_adj()):
        for v, _ in neighbors:
            edge = tuple(sorted((u, v)))
            seen.add(edge)

    assert len(seen) <= 50


# ================= REPRODUCIBILITY ================= #
def test_seed_reproducibility_weighted():
    g1 = generate_normal_weighted_graph(vertices=10, edges=20, seed=42)
    g2 = generate_normal_weighted_graph(vertices=10, edges=20, seed=42)

    assert g1.get_adj() == g2.get_adj()


# ================= PARAM VALIDATION ================= #
def test_invalid_weight_range():
    with pytest.raises(ValueError):
        generate_normal_weighted_graph(
            vertices=10,
            edges=10,
            weight_range=(5.0, 1.0),
        )


def test_invalid_weight_distribution():
    with pytest.raises(ValueError):
        generate_normal_weighted_graph(
            vertices=10,
            edges=10,
            weight_distribution="invalid",
        )


def test_invalid_vertices_weighted():
    with pytest.raises(ValueError):
        generate_normal_weighted_graph(vertices=0, edges=10)


def test_invalid_edges_weighted():
    with pytest.raises(ValueError):
        generate_normal_weighted_graph(vertices=10, edges=-1)


# ================= LARGE GRAPH ================= #
def test_large_weighted_graph():
    g = generate_normal_weighted_graph(vertices=1000, edges=3000)

    assert g.vertices() == 1000