#include <vector>
#include <atomic>
#include <mutex>
#include <utility>      // move

#include "../include/parallel_bfs.hpp"
#include "../include/engine.hpp"

/*
    Level-synchronous parallel BFS
*/
std::vector<int> parallel_bfs(
    const Graph& graph,
    int source,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    // Distance array (atomic for thread safety)
    std::vector<std::atomic<int>> dist(V);
    for (int i = 0; i < V; i++)
        dist[i] = -1;

    // Initialize source
    dist[source] = 0;

    std::vector<int> frontier;
    frontier.push_back(source);

    int level = 0;

    while (!frontier.empty()) {
        std::vector<int> next_frontier;
        std::mutex frontier_mutex;

        engine::parallel_for(
            0,
            (int)frontier.size(),
            threads,
            [&](int idx) {
                int u = frontier[idx];

                for (int v : adj[u]) {
                    int expected = -1;

                    if (dist[v].compare_exchange_strong(expected, level + 1)) {
                        std::lock_guard<std::mutex> lock(frontier_mutex);
                        next_frontier.push_back(v);
                    }
                }
            }
        );

        frontier = std::move(next_frontier);
        level++;
    }

    // Convert atomic<int> to int
    std::vector<int> result(V);
    for (int i = 0; i < V; i++)
        result[i] = dist[i].load();

    return result;
}