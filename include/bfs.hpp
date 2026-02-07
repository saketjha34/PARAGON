#pragma once
#include <bits/stdc++.h>
using namespace std;

#include "graph.hpp"

/*
    Parallel Breadth First Search (BFS)

    - Level-synchronous traversal
    - Thread-safe
    - Unweighted shortest paths

    Returns:
    - vector<int> distance array
      distance[i] = shortest distance from source to i
      distance[i] = -1 if unreachable
*/

vector<int> parallel_bfs(
    const Graph& graph,
    int source,
    int threads = -1
);