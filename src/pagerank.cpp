#include <vector>
#include <algorithm>
#include <stdexcept>

#include "../include/pagerank.hpp"
#include "../include/engine.hpp"


std::vector<double> parallel_pagerank(
    const Graph& graph,
    int iterations,
    double damping,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    // ================= VALIDATION =================
    if (V == 0)
        return {};

    if (iterations <= 0)
        throw std::invalid_argument("iterations must be positive");

    if (damping <= 0.0 || damping >= 1.0)
        throw std::invalid_argument("damping must be in (0,1)");

    // ================= BUILD INCOMING GRAPH =================
    std::vector<std::vector<int>> incoming(V);
    for (int u = 0; u < V; u++) {
        for (int v : adj[u]) {
            incoming[v].push_back(u);
        }
    }

    // ================= INITIALIZE =================
    std::vector<double> rank(V, 1.0 / V);
    std::vector<double> new_rank(V, 0.0);

    threads = engine::get_thread_count(threads);

    // ================= ITERATIONS =================
    for (int iter = 0; iter < iterations; iter++) {

        // -------- HANDLE DANGLING NODES --------
        double dangling_sum = 0.0;
        for (int u = 0; u < V; u++) {
            if (adj[u].empty()) {
                dangling_sum += rank[u];
            }
        }

        // -------- PARALLEL UPDATE --------
        engine::parallel_for(0, V, threads, [&](int v) {
            double sum = 0.0;

            // Sum contributions from incoming edges
            for (int u : incoming[v]) {
                if (!adj[u].empty()) {
                    sum += rank[u] / adj[u].size();
                }
            }

            // PageRank formula with dangling correction
            new_rank[v] =
                (1.0 - damping) / V +
                damping * (sum + dangling_sum / V);
        });

        // -------- SWAP ARRAYS --------
        rank.swap(new_rank);

        // -------- RESET BUFFER (IMPORTANT) --------
        std::fill(new_rank.begin(), new_rank.end(), 0.0);
    }

    return rank;
}


/*
    Push-based (BFS-style) PageRank
*/
std::vector<double> parallel_pagerank_bfs(
    const Graph& graph,
    int iterations,
    double damping,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    if (V == 0) return {};

    if (iterations <= 0)
        throw std::invalid_argument("iterations must be positive");

    if (damping <= 0.0 || damping >= 1.0)
        throw std::invalid_argument("damping must be in (0,1)");

    std::vector<double> rank(V, 1.0 / V);
    std::vector<double> next_rank(V, 0.0);

    threads = engine::get_thread_count(threads);

    for (int iter = 0; iter < iterations; iter++) {

        // DANGLING NODES
        double dangling_sum = 0.0;
        for (int u = 0; u < V; u++) {
            if (adj[u].empty()) {
                dangling_sum += rank[u];
            }
        }

        // Thread-local buffers
        std::vector<std::vector<double>> local_buffers(
            threads, std::vector<double>(V, 0.0)
        );

        engine::parallel_for(0, threads, threads, [&](int tid) {
            int chunk = engine::chunk_size(V, threads);
            int start = tid * chunk;
            int end   = std::min(V, start + chunk);

            for (int u = start; u < end; u++) {
                if (adj[u].empty()) continue;

                double share = rank[u] / adj[u].size();
                for (int v : adj[u]) {
                    local_buffers[tid][v] += share;
                }
            }
        });

        // Merge buffers
        std::fill(next_rank.begin(), next_rank.end(), 0.0);
        for (int t = 0; t < threads; t++) {
            for (int v = 0; v < V; v++) {
                next_rank[v] += local_buffers[t][v];
            }
        }

        // FINAL UPDATE WITH DANGLING FIX
        engine::parallel_for(0, V, threads, [&](int v) {
            next_rank[v] =
                (1.0 - damping) / V +
                damping * (next_rank[v] + dangling_sum / V);
        });

        rank.swap(next_rank);
    }

    return rank;
}