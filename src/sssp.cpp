#include <vector>
#include <algorithm>

#include "../include/sssp.hpp"
#include "../include/engine.hpp"

static const double INF = 1e18;

std::vector<double> parallel_dijkstra(
    const WeightedGraph& graph,
    int source,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getWeightedAdj();

    std::vector<double> dist(V, INF);
    dist[source] = 0.0;

    threads = engine::get_thread_count(threads);
    bool changed = true;

    /*
        Parallel relaxation loop
        Similar to Bellman-Ford but parallel
        Early stops when no update occurs
    */
    for (int iter = 0; iter < V - 1 && changed; iter++) {
        changed = false;

        engine::parallel_for(0, V, threads, [&](int u) {
            if (dist[u] == INF) return;

            for (auto& edge : adj[u]) {
                int v = edge.first;
                double w = edge.second;

                double nd = dist[u] + w;

                if (nd < dist[v]) {
                    dist[v] = nd;
                    changed = true;
                }
            }
        });
    }

    return dist;
}