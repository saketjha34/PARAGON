from paragon import WeightedGraph

wg = WeightedGraph(vertices=4)

wg.add_edges(edges=[
    (0, 1, 2.5),
    (1, 2, 1.0),
    (2, 3, 3.2)
])

print("Vertices:", wg.vertices())
print("Adjacency:", wg.get_adj())
print("Degree:", wg.degree(u=1))
print("Has edge:", wg.has_edge(u=0, v=1))
wg.print_graph()