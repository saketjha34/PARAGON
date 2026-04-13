# PARAGON Benchmark

| Algorithm                      | Configuration (V, E) | Time (Sequential) | Time (Parallel) | Speedup       | Key Observations                                                                                                       |
| ------------------------------ | -------------------- | ----------------- | --------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **SSSP (Parallel Relaxation)** | (3000, 10,000)       | 398 ms            | 5 ms            | **~80×**   | Sequential behaves like Bellman–Ford (O(V·E)); parallel version uses early stopping + edge relaxation → massive gains. |
| **PageRank**                   | (20, 20,000,000)     | 3026 ms           | 1180 ms         | **~2.5×**   | Highly parallelizable (no dependencies, uniform work). Limited by memory bandwidth & synchronization barriers.         |
| **Connected Components (CC)**  | (20, 20,000,000)     | 1451 ms           | 876 ms          | **~1.65×** | Parallelism helps only for dense graphs. Sequential DFS is cache-efficient for small graphs.                           |
| **Triangle Counting**          | (20, 200,000)        | ~12,500 ms        | ~3,600 ms       | **~3.4×**  | Perfect for parallelism: independent work, no sync, heavy computation. CPU cores fully utilized.                       |


| Workload Type                          | Parallel Benefit               |
| -------------------------------------- | -------------------------------|
| High compute (Triangle Counting)       | Excellent                      |
| Iterative dense (PageRank)             | Good                           |
| Irregular / low work (CC small graphs) | Limited                        |
| Relaxation-heavy (SSSP naive)          | Huge (but depends on baseline) |