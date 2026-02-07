#pragma once
#include <bits/stdc++.h>
using namespace std;

/*
    Engine utilities for parallel execution
    --------------------------------------
    This file provides common helpers used
    across all parallel graph algorithms.
*/

namespace engine {

    /* ================= THREAD UTILITIES ================= */

    // Get number of hardware threads (fallback to 1)
    inline int hardware_threads() {
        unsigned int hc = thread::hardware_concurrency();
        return hc == 0 ? 1 : hc;
    }

    // Decide how many threads to use
    inline int get_thread_count(int requested = -1) {
        if (requested <= 0)
            return hardware_threads();
        return min(requested, hardware_threads());
    }

    /* ================= CHUNKING ================= */

    // Calculate chunk size for dividing work
    inline int chunk_size(int total_work, int threads) {
        if (threads <= 0) return total_work;
        return (total_work + threads - 1) / threads;
    }

    /* ================= PARALLEL FOR ================= */

    // Generic parallel for-loop
    // Executes func(i) for i in [start, end)
    template <typename Func>
    void parallel_for(int start, int end, int threads, Func func) {
        threads = get_thread_count(threads);

        int total = end - start;
        if (total <= 0) return;

        int chunk = chunk_size(total, threads);
        vector<thread> workers;

        for (int t = 0; t < threads; t++) {
            int s = start + t * chunk;
            int e = min(end, s + chunk);

            if (s >= e) break;

            workers.emplace_back([=]() {
                for (int i = s; i < e; i++)
                    func(i);
            });
        }

        for (auto& th : workers)
            th.join();
    }

    /* ================= PARALLEL FOREACH ================= */

    // Parallel for-each over a container
    template <typename Container, typename Func>
    void parallel_for_each(const Container& c, int threads, Func func) {
        parallel_for(0, (int)c.size(), threads, [&](int i) {
            func(c[i]);
        });
    }

} // namespace engine