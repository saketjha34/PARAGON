from paragon import Graph
from paragon.algorithms import parallel_triangle_count as triangle_count


# BASIC TESTS
def test_triangle_empty_graph():
    g = Graph(5)

    count = triangle_count(g)

    assert count == 0


def test_triangle_single_triangle():
    """
    0 - 1
     \ /
      2
    """
    g = Graph(3)
    g.add_edges([(0,1), (1,2), (2,0)])

    count = triangle_count(g)

    assert count == 1


def test_triangle_two_triangles():
    """
    0-1-2 forms 1 triangle
    2-3-4 forms another
    """
    g = Graph(5)
    g.add_edges([
        (0,1), (1,2), (2,0),
        (2,3), (3,4), (4,2)
    ])

    count = triangle_count(g)

    assert count == 2


# NO TRIANGLE
def test_triangle_chain():
    """
    0 - 1 - 2 - 3
    """
    g = Graph(4)
    g.add_edges([(0,1), (1,2), (2,3)])

    count = triangle_count(g)

    assert count == 0


def test_triangle_star():
    """
        1
        |
    2 - 0 - 3
        |
        4
    """
    g = Graph(5)
    g.add_edges([(0,1), (0,2), (0,3), (0,4)])

    count = triangle_count(g)

    assert count == 0


# COMPLETE GRAPH
def test_triangle_complete_graph_3():
    g = Graph(3)
    g.add_edges([(0,1), (1,2), (2,0)])

    assert triangle_count(g) == 1


def test_triangle_complete_graph_4():
    """
    Complete graph K4 has 4 triangles
    """
    g = Graph(4)
    edges = [(i, j) for i in range(4) for j in range(i+1, 4)]
    g.add_edges(edges)

    count = triangle_count(g)

    assert count == 4


def test_triangle_complete_graph_5():
    """
    K5 has 10 triangles
    """
    g = Graph(5)
    edges = [(i, j) for i in range(5) for j in range(i+1, 5)]
    g.add_edges(edges)

    count = triangle_count(g)

    assert count == 10


# DISCONNECTED GRAPH
def test_triangle_disconnected():
    g = Graph(6)
    g.add_edges([
        (0,1), (1,2), (2,0),   # triangle 1
        (3,4), (4,5), (5,3)    # triangle 2
    ])

    count = triangle_count(g)

    assert count == 2


# SELF LOOPS / DUPLICATES
def test_triangle_self_loop():
    g = Graph(3)
    g.add_edges([(0,1), (1,2), (2,0)])
    g.add_edge(0, 0)

    count = triangle_count(g)

    assert count == 1


# THREAD CONSISTENCY
def test_triangle_threads():
    g = Graph(6)
    g.add_edges([
        (0,1), (1,2), (2,0),
        (3,4), (4,5), (5,3)
    ])

    c1 = triangle_count(g)
    c2 = triangle_count(g)

    assert c1 == c2


# LARGE GRAPH
def test_triangle_large_graph():
    n = 50
    g = Graph(n)

    # create triangles in groups of 3
    for i in range(0, n - 2, 3):
        g.add_edges([
            (i, i+1),
            (i+1, i+2),
            (i+2, i)
        ])

    count = triangle_count(g)

    assert count == (n // 3)


# ORDER INDEPENDENCE
def test_triangle_order_independence():
    g = Graph(3)
    g.add_edges([(0,2), (2,1), (1,0)])

    count = triangle_count(g)

    assert count == 1