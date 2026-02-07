#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/pagerank.hpp"
#include "benchmark_utils.hpp"

// Sequential PageRank
vector<double> pagerank_seq(const Graph& g, int iters) {
    int V = g.vertices();
    vector<double> r(V, 1.0 / V), nr(V);

    for (int it = 0; it < iters; it++) {
        fill(nr.begin(), nr.end(), 0.15 / V);
        for (int u = 0; u < V; u++) {
            for (int v : g.getAdj()[u]) {
                nr[v] += 0.85 * r[u] / g.getAdj()[u].size();
            }
        }
        r.swap(nr);
    }
    return r;
}

int main() {
    int V = 20;
    int E = 20000000;

    cout << "=== PageRank Benchmark ===\n";
    Graph g = generate_random_graph(V, E, true);

    long long t1 = time_ms([&]() {
        pagerank_seq(g, 20);
    });

    long long t2 = time_ms([&]() {
        parallel_pagerank(g, 20, 0.85, 10);
    });

    cout << "Sequential PageRank: " << t1 << " ms\n";
    cout << "Parallel PageRank  : " << t2 << " ms\n";
}