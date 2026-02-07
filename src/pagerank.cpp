#include <bits/stdc++.h>
using namespace std;

#include "../include/pagerank.hpp"
#include "../include/engine.hpp"

vector<double> parallel_pagerank(
    const Graph& graph,
    int iterations,
    double damping,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    if (V == 0)
        return {};

    // Build reverse adjacency list (incoming edges)
    vector<vector<int>> incoming(V);
    for (int u = 0; u < V; u++) {
        for (int v : adj[u]) {
            incoming[v].push_back(u);
        }
    }

    vector<double> rank(V, 1.0 / V);
    vector<double> new_rank(V, 0.0);

    threads = engine::get_thread_count(threads);

    for (int iter = 0; iter < iterations; iter++) {

        engine::parallel_for(0, V, threads, [&](int v) {
            double sum = 0.0;

            for (int u : incoming[v]) {
                if (!adj[u].empty())
                    sum += rank[u] / adj[u].size();
            }

            new_rank[v] = (1.0 - damping) / V + damping * sum;
        });

        // Barrier reached here (all threads joined)
        rank.swap(new_rank);
    }

    return rank;
}

/*
    Push-based (BFS-style) PageRank
*/
vector<double> parallel_pagerank_bfs(
    const Graph& graph,
    int iterations,
    double damping,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    if (V == 0) return {};

    vector<double> rank(V, 1.0 / V);
    vector<double> next_rank(V, 0.0);

    threads = engine::get_thread_count(threads);

    for (int iter = 0; iter < iterations; iter++) {

        // One local buffer per thread
        vector<vector<double>> local_buffers(threads, vector<double>(V, 0.0));

        engine::parallel_for(0, threads, threads, [&](int tid) {
            int chunk = engine::chunk_size(V, threads);
            int start = tid * chunk;
            int end   = min(V, start + chunk);

            for (int u = start; u < end; u++) {
                if (adj[u].empty()) continue;

                double share = rank[u] / adj[u].size();
                for (int v : adj[u]) {
                    local_buffers[tid][v] += share;
                }
            }
        });

        // Merge local buffers (serial, safe)
        fill(next_rank.begin(), next_rank.end(), 0.0);
        for (int t = 0; t < threads; t++) {
            for (int v = 0; v < V; v++) {
                next_rank[v] += local_buffers[t][v];
            }
        }

        // Apply damping
        engine::parallel_for(0, V, threads, [&](int v) {
            next_rank[v] =
                (1.0 - damping) / V +
                damping * next_rank[v];
        });

        rank.swap(next_rank);
    }

    return rank;
}