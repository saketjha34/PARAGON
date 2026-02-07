#pragma once
#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"

inline long long time_ms(function<void()> fn) {
    auto start = chrono::high_resolution_clock::now();
    fn();
    auto end = chrono::high_resolution_clock::now();
    return chrono::duration_cast<chrono::milliseconds>(end - start).count();
}

// Generate random unweighted graph
inline Graph generate_random_graph(
    int V, int E, bool directed = false
) {
    Graph g(V, directed);
    mt19937 rng(42);
    uniform_int_distribution<int> dist(0, V - 1);

    for (int i = 0; i < E; i++) {
        int u = dist(rng);
        int v = dist(rng);
        if (u != v)
            g.addEdge(u, v);
    }
    return g;
}

// Generate random weighted graph
inline WeightedGraph generate_random_weighted_graph(
    int V, int E, bool directed = false
) {
    WeightedGraph g(V, directed);
    mt19937 rng(42);
    uniform_int_distribution<int> dist(0, V - 1);
    uniform_real_distribution<double> wdist(1.0, 10.0);

    for (int i = 0; i < E; i++) {
        int u = dist(rng);
        int v = dist(rng);
        if (u != v)
            g.addEdge(u, v, wdist(rng));
    }
    return g;
}