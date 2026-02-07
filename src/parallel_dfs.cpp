#include <bits/stdc++.h>
using namespace std;

#include "../include/dfs.hpp"
#include "../include/engine.hpp"

vector<bool> parallel_dfs(
    const Graph& graph,
    int source,
    int threads
) {
    int V = graph.vertices();
    const auto& adj = graph.getAdj();

    vector<atomic<bool>> visited(V);
    for (int i = 0; i < V; i++)
        visited[i] = false;

    // Shared work stack
    stack<int> st;
    mutex st_mutex;

    visited[source] = true;
    st.push(source);

    threads = engine::get_thread_count(threads);
    vector<thread> workers;

    auto worker = [&]() {
        while (true) {
            int u = -1;

            // Get work
            {
                lock_guard<mutex> lock(st_mutex);
                if (st.empty())
                    return;
                u = st.top();
                st.pop();
            }

            // Explore neighbors
            for (int v : adj[u]) {
                if (!visited[v].exchange(true)) {
                    lock_guard<mutex> lock(st_mutex);
                    st.push(v);
                }
            }
        }
    };

    for (int t = 0; t < threads; t++)
        workers.emplace_back(worker);

    for (auto& th : workers)
        th.join();

    vector<bool> result(V);
    for (int i = 0; i < V; i++)
        result[i] = visited[i];

    return result;
}