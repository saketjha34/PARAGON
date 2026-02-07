#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/triangle_count.hpp"
#include "benchmark_utils.hpp"

static inline int count_intersection(
    const vector<int>& a,
    const vector<int>& b,
    int min_val
) {
    int i = 0, j = 0, cnt = 0;

    // skip values <= min_val to enforce ordering
    while (i < a.size() && a[i] <= min_val) i++;
    while (j < b.size() && b[j] <= min_val) j++;

    while (i < a.size() && j < b.size()) {
        if (a[i] == b[j]) {
            cnt++;
            i++; j++;
        } else if (a[i] < b[j]) {
            i++;
        } else {
            j++;
        }
    }
    return cnt;
}

long long triangle_count_sequential(const Graph& graph) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    // Make sorted adjacency lists
    vector<vector<int>> g = adj;
    for (auto& v : g)
        sort(v.begin(), v.end());

    long long total = 0;

    for (int u = 0; u < V; u++) {
        for (int v : g[u]) {
            if (v > u) {
                total += count_intersection(g[u], g[v], v);
            }
        }
    }

    return total;
}


int main() {
    int V = 20;
    int E = 200000;

    Graph g = generate_random_graph(V, E);

    cout << "=== Triangle Counting Benchmark ===\n";

    long long t1 = time_ms([&]() {
        triangle_count_sequential(g);
    });

    long long t2 = time_ms([&]() {
        triangle_count_parallel(g, 8);
    });

    cout << "Sequential: " << t1 << " ms\n";
    cout << "Parallel  : " << t2 << " ms\n";
}