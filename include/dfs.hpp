#pragma once
#include <bits/stdc++.h>
using namespace std;

#include "graph.hpp"

/*
    Parallel Depth First Search (DFS)

    - Task-based traversal
    - Thread-safe
    - Explores reachable nodes from a source

    Returns:
    - vector<bool> visited array
      visited[i] = true if reachable from source
*/

vector<bool> parallel_dfs(
    const Graph& graph,
    int source,
    int threads = -1
);