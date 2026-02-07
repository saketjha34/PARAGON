#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/connected_components.hpp"
#include "benchmark_utils.hpp"

// Sequential CC (DFS-based)
void dfs_cc(const Graph& g, int u, vector<int>& comp, int id) {
    comp[u] = id;
    for (int v : g.getAdj()[u])
        if (comp[v] == -1)
            dfs_cc(g, v, comp, id);
}

int main() {
    int V = 20;
    int E = 20000000;

    cout << "=== Connected Components Benchmark ===\n";
    Graph g = generate_random_graph(V, E);

    long long t1 = time_ms([&]() {
        vector<int> comp(V, -1);
        int id = 0;
        for (int i = 0; i < V; i++)
            if (comp[i] == -1)
                dfs_cc(g, i, comp, id++);
    });

    long long t2 = time_ms([&]() {
        parallel_connected_components(g, 10);
    });

    cout << "Sequential CC: " << t1 << " ms\n";
    cout << "Parallel CC  : " << t2 << " ms\n";
}