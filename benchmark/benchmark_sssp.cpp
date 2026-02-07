#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/sssp.hpp"
#include "benchmark_utils.hpp"

// Sequential Bellman-Ford
vector<double> sssp_seq(const WeightedGraph& g, int src) {
    int V = g.vertices();
    auto& adj = g.getWeightedAdj();
    vector<double> dist(V, 1e18);
    dist[src] = 0;

    for (int i = 0; i < V - 1; i++) {
        for (int u = 0; u < V; u++) {
            for (auto& [v, w] : adj[u]) {
                dist[v] = min(dist[v], dist[u] + w);
            }
        }
    }
    return dist;
}

int main() {
    int V = 3000;
    int E = 10000;

    cout << "=== SSSP Benchmark ===\n";
    auto g = generate_random_weighted_graph(V, E, true);

    long long t1 = time_ms([&]() {
        sssp_seq(g, 0);
    });

    long long t2 = time_ms([&]() {
        parallel_dijkstra(g, 0, 8);
    });

    cout << "Sequential SSSP: " << t1 << " ms\n";
    cout << "Parallel SSSP  : " << t2 << " ms\n";
}