#include <bits/stdc++.h>
using namespace std;

#include "../include/connected_components.hpp"
#include "../include/engine.hpp"

/*
    Parallel Connected Components
    Shiloach–Vishkin style (pointer jumping)
*/
vector<int> parallel_connected_components(
    const Graph& graph,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    threads = engine::get_thread_count(threads);

    vector<int> parent(V);
    for (int i = 0; i < V; i++)
        parent[i] = i;

    bool changed = true;

    while (changed) {
        atomic<bool> any_change(false);

        // Hooking phase
        engine::parallel_for(0, V, threads, [&](int u) {
            for (int v : adj[u]) {
                int pu = parent[u];
                int pv = parent[v];

                if (pu == pv) continue;

                int high = max(pu, pv);
                int low  = min(pu, pv);

                if (parent[high] == high) {
                    parent[high] = low;
                    any_change.store(true, memory_order_relaxed);
                }
            }
        });

        // Pointer jumping (path compression)
        engine::parallel_for(0, V, threads, [&](int u) {
            while (parent[u] != parent[parent[u]]) {
                parent[u] = parent[parent[u]];
            }
        });

        changed = any_change.load();
    }

    // Final compression
    engine::parallel_for(0, V, threads, [&](int u) {
        while (parent[u] != parent[parent[u]]) {
            parent[u] = parent[parent[u]];
        }
    });

    return parent;
}