#include <bits/stdc++.h>
using namespace std;

#include "../include/triangle_count.hpp"
#include "../include/engine.hpp"

/*
    Helper: count intersection size of two sorted vectors
*/
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

/*
    Parallel triangle counting
*/
long long triangle_count_parallel(
    const Graph& graph,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    threads = engine::get_thread_count(threads);

    vector<vector<int>> g = adj;
    for (auto& v : g)
        sort(v.begin(), v.end());

    vector<long long> local_counts(threads, 0);

    engine::parallel_for(0, threads, threads, [&](int tid) {
        int chunk = engine::chunk_size(V, threads);
        int start = tid * chunk;
        int end   = min(V, start + chunk);

        long long local = 0;

        for (int u = start; u < end; u++) {
            for (int v : g[u]) {
                if (v > u) {
                    local += count_intersection(g[u], g[v], v);
                }
            }
        }

        local_counts[tid] = local;
    });

    long long total = 0;
    for (long long c : local_counts)
        total += c;

    return total;
}