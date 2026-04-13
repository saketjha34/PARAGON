# from paragon import Graph
# from paragon.algorithms import parallel_dfs
# from paragon.algorithms import parallel_bfs
# from paragon.algorithms import parallel_connected_components
# from paragon.algorithms import pagerank
# from paragon.algorithms import pagerank_bfs
# from paragon.algorithms import parallel_dijkstra
# from paragon import WeightedGraph
# from paragon.algorithms import parallel_triangle_count

# g = Graph(5)
# g.add_edges([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
# visited = parallel_dfs(g, 0)
# print("Visited nodes:", visited)

# components = parallel_connected_components(g, 8)
# print("Connected components:", components)

# distances = parallel_bfs(g, 0)
# print("Shortest distances:", distances)

# rank = pagerank(g)
# print("PageRank scores:", rank)

# rank_bfs = pagerank_bfs(g)
# print("PageRank scores (BFS):", rank_bfs)

# wg = WeightedGraph(5)
# wg.add_edges([(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 0, 1)])

# d = parallel_dijkstra(wg, 1)
# print("Shortest paths from node 1:", d)


# t = parallel_triangle_count(g)
# print("Number of triangles in the graph:", t)


# from paragon import Graph

# g = Graph(5)
# g.print_graph()
# g.add_edge(0, 1)  # Adding an edge between vertices 0 and 1
# print("Vertices in the graph:", g.vertices())
# print("Edges in the graph:", g.has_edge(0, 1))
# print("Degree of vertex 1:", g.degree(1))
# print("Adjacency List:", g.get_adj())
# g.add_vertex()
# g.has_edge(0, 1)
# g.build_from_adj_list([[1], [0, 2], [1, 3], [2, 4], [3]])
# print("Adjacency List after building from matrix:", g.get_adj())
# g.print_graph()

# from paragon.algorithms import pagerank


from paragon import WeightedGraph
from paragon.algorithms import parallel_dijkstra

g = WeightedGraph(6)

g.add_edges([
    (0, 1, 4.0),
    (0, 2, 2.0),
    (1, 3, 5.0),
    (2, 1, 1.0),
    (2, 3, 8.0),
    (3, 4, 3.0),
    (4, 5, 1.0)
])

dist = parallel_dijkstra(g, 0)

for i, d in enumerate(dist):
    print(f"Distance from 0 → {i}: {d}")

# from paragon import WeightedGraph

# g = WeightedGraph(5, directed=True)
# g.add_edge(0, 1, 2.5)  # Adding a weighted edge between vertices 0 and 1
# # g.build_from_adj_list([
# #     [(1, 2.5)],           # node 0
# #     [(0, 2.5), (2, 3.0)], # node 1
# #     [(1, 3.0), (3, 4.0)], # node 2
# #     [(2, 4.0)],           # node 3
# #     []                    # node 4
# # ])
# print("Weighted Adjacency List:", g.get_adj())
# print("Is directed:", g.is_directed())
# g.print_graph()
# print("Has edge (0, 1):", g.has_edge(0, 1))

# print("Degree of vertex 1:", g.degree(1))
# print("Vertices in the graph:", g.vertices())
# print("Weighted Adjacency List:", g.get_adj())
# print("Edges in the graph:", g.has_edge(0, 1))
# print("Degree of vertex 1:", g.degree(1))
# print("Adjacency List:", g.get_adj())
# print("Weighted Adjacency List:", g.get_adj())
# print("Has edge (0, 1):", g.has_edge(0, 1))