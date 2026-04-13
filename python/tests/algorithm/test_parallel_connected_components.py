from paragon import Graph
from paragon.algorithms import parallel_connected_components


# HELPERS
def group_components(labels):
    """
    Convert label array → list of sets (components)
    """
    comp_map = {}
    for i, c in enumerate(labels):
        comp_map.setdefault(c, []).append(i)
    return [set(v) for v in comp_map.values()]


def components_equal(actual, expected):
    """
    Compare components ignoring label values
    """
    actual_sets = [set(x) for x in actual]
    expected_sets = [set(x) for x in expected]

    return sorted(actual_sets) == sorted(expected_sets)


# BASIC TESTS
def test_cc_single_node():
    g = Graph(1)

    labels = parallel_connected_components(g)

    assert labels == [0]


def test_cc_simple_graph():
    """
    0-1   2-3
    """
    g = Graph(4)
    g.add_edges([(0,1), (2,3)])

    labels = parallel_connected_components(g)

    comps = group_components(labels)

    assert components_equal(comps, [{0,1}, {2,3}])


# FULLY CONNECTED
def test_cc_fully_connected():
    g = Graph(5)
    edges = [(i, j) for i in range(5) for j in range(i+1, 5)]
    g.add_edges(edges)

    labels = parallel_connected_components(g)

    comps = group_components(labels)

    assert len(comps) == 1
    assert comps[0] == {0,1,2,3,4}


# CHAIN GRAPH
def test_cc_chain():
    """
    0-1-2-3-4
    """
    g = Graph(5)
    g.add_edges([(0,1), (1,2), (2,3), (3,4)])

    labels = parallel_connected_components(g)

    comps = group_components(labels)

    assert len(comps) == 1


# MULTIPLE COMPONENTS
def test_cc_multiple_components():
    """
    0-1   2-3   4   5-6-7
    """
    g = Graph(8)
    g.add_edges([
        (0,1),
        (2,3),
        (5,6), (6,7)
    ])

    labels = parallel_connected_components(g)

    comps = group_components(labels)

    expected = [
        {0,1},
        {2,3},
        {4},
        {5,6,7}
    ]

    assert components_equal(comps, expected)


# ISOLATED NODES
def test_cc_all_isolated():
    g = Graph(5)

    labels = parallel_connected_components(g)

    comps = group_components(labels)

    assert len(comps) == 5
    for c in comps:
        assert len(c) == 1


# DIRECTED GRAPH (treated as undirected)
def test_cc_directed_graph():
    """
    Even if directed, connectivity is weakly connected
    """
    g = Graph(4, directed=True)
    g.add_edges([(0,1), (2,3)])

    labels = parallel_connected_components(g)

    comps = group_components(labels)

    assert components_equal(comps, [{0,1}, {2,3}])


# SELF LOOPS
def test_cc_self_loops():
    g = Graph(3)
    g.add_edge(0, 0)
    g.add_edge(1, 1)

    labels = parallel_connected_components(g)

    comps = group_components(labels)

    assert components_equal(comps, [{0}, {1}, {2}])


# THREAD CONSISTENCY
def test_cc_threads_consistency():
    g = Graph(6)
    g.add_edges([
        (0,1),
        (1,2),
        (3,4)
    ])

    l1 = parallel_connected_components(g)
    l2 = parallel_connected_components(g)

    comps1 = group_components(l1)
    comps2 = group_components(l2)

    assert components_equal(comps1, comps2)


# LABEL CONSISTENCY
def test_cc_same_component_same_label():
    g = Graph(4)
    g.add_edges([(0,1), (1,2)])

    labels = parallel_connected_components(g)

    assert labels[0] == labels[1] == labels[2]


# STRESS TEST
def test_cc_large_graph():
    n = 200
    g = Graph(n)

    # connect first half
    for i in range(0, 99):
        g.add_edge(i, i+1)

    # connect second half
    for i in range(100, 199):
        g.add_edge(i, i+1)

    labels = parallel_connected_components(g)

    comps = group_components(labels)

    assert len(comps) == 2


# DETERMINISM (IMPORTANT)
def test_cc_repeatability():
    g = Graph(5)
    g.add_edges([(0,1), (2,3)])

    l1 = parallel_connected_components(g)
    l2 = parallel_connected_components(g)

    assert l1 == l2