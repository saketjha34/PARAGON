#include <bits/stdc++.h>
using namespace std;

#include "../include/bfs.hpp"
#include "../include/engine.hpp"

/*
    Level-synchronous parallel BFS
*/
vector<int> parallel_bfs(
    const Graph& graph,
    int source,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    // Distance array (atomic for thread safety)
    vector<atomic<int>> dist(V);
    for (int i = 0; i < V; i++)
        dist[i] = -1;

    // Initialize source
    dist[source] = 0;

    vector<int> frontier;
    frontier.push_back(source);

    int level = 0;

    while (!frontier.empty()) {
        vector<int> next_frontier;
        mutex frontier_mutex;

        // Parallel over current frontier
        engine::parallel_for(
            0,
            (int)frontier.size(),
            threads,
            [&](int idx) {
                int u = frontier[idx];

                for (int v : adj[u]) {
                    int expected = -1;

                    // Atomically mark visited
                    if (dist[v].compare_exchange_strong(expected, level + 1)) {
                        lock_guard<mutex> lock(frontier_mutex);
                        next_frontier.push_back(v);
                    }
                }
            }
        );

        frontier = move(next_frontier);
        level++;
    }

    // Convert atomic<int> to int
    vector<int> result(V);
    for (int i = 0; i < V; i++)
        result[i] = dist[i];

    return result;
}