from paragon.graphs import generate_normal_graph, generate_normal_weighted_graph

g = generate_normal_graph(vertices=10, edges=20, directed=True, seed=42)

wg = generate_normal_weighted_graph(
    vertices=10, edges=20, directed=True, seed=42)

print(g.vertices())
g.print_graph()

print(wg.vertices())
wg.print_graph()