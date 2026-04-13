#include <vector>
#include <atomic>
#include <stack>
#include <thread>
#include <mutex>

#include "../include/parallel_dfs.hpp"
#include "../include/engine.hpp"

std::vector<bool> parallel_dfs(
    const Graph& graph,
    int source,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    std::vector<std::atomic<bool>> visited(V);
    for (int i = 0; i < V; i++)
        visited[i] = false;

    // Shared work stack
    std::stack<int> st;
    std::mutex st_mutex;

    visited[source] = true;
    st.push(source);

    threads = engine::get_thread_count(threads);
    std::vector<std::thread> workers;

    auto worker = [&]() {
        while (true) {
            int u = -1;

            // Get work
            {
                std::lock_guard<std::mutex> lock(st_mutex);
                if (st.empty())
                    return;
                u = st.top();
                st.pop();
            }

            // Explore neighbors
            for (int v : adj[u]) {
                if (!visited[v].exchange(true)) {
                    std::lock_guard<std::mutex> lock(st_mutex);
                    st.push(v);
                }
            }
        }
    };

    for (int t = 0; t < threads; t++)
        workers.emplace_back(worker);

    for (auto& th : workers)
        th.join();

    std::vector<bool> result(V);
    for (int i = 0; i < V; i++)
        result[i] = visited[i].load();

    return result;
}