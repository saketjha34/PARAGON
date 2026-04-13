#include <vector>
#include <algorithm>

#include "../include/triangle_count.hpp"
#include "../include/engine.hpp"

/*
    Helper: count intersection size of two sorted vectors
*/
static inline int count_intersection(
    const std::vector<int>& a,
    const std::vector<int>& b,
    int min_val
) {
    int i = 0, j = 0, cnt = 0;

    while (i < (int)a.size() && a[i] <= min_val) i++;
    while (j < (int)b.size() && b[j] <= min_val) j++;

    while (i < (int)a.size() && j < (int)b.size()) {
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
std::int64_t triangle_count_parallel(
    const Graph& graph,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    threads = engine::get_thread_count(threads);

    std::vector<std::vector<int>> g = adj;
    for (auto& v : g)
        std::sort(v.begin(), v.end());

    std::vector<std::int64_t> local_counts(threads, 0);

    engine::parallel_for(0, threads, threads, [&](int tid) {
        int chunk = engine::chunk_size(V, threads);
        int start = tid * chunk;
        int end   = std::min(V, start + chunk);

        std::int64_t local = 0;

        for (int u = start; u < end; u++) {
            for (int v : g[u]) {
                if (v > u) {
                    local += count_intersection(g[u], g[v], v);
                }
            }
        }

        local_counts[tid] = local;
    });

    std::int64_t total = 0;
    for (auto c : local_counts)
        total += c;

    return total;
}