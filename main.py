import time
from paragon.graphs import generate_normal_graph
from paragon.algorithms import parallel_bfs

NUM_THREADS = 8

g = generate_normal_graph(vertices=30, edges=100000)

start = time.perf_counter()
parallel_bfs(graph=g, source=0, threads=NUM_THREADS)
end = time.perf_counter()

elapsed_microseconds = (end - start) * 1_000_000

print(f"Execution Time: {elapsed_microseconds:.2f} µs")