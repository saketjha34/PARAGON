#pragma once
#include <bits/stdc++.h>
using namespace std;

#include "graph.hpp"

/*
    Parallel PageRank

    - Iterative BSP-style algorithm
    - Thread-safe
    - Suitable for large graphs

    Parameters:
    - iterations : number of PageRank iterations
    - damping    : damping factor (usually 0.85)
    - threads    : number of threads (-1 = auto)

    Returns:
    - vector<double> rank values
*/

vector<double> parallel_pagerank(
    const Graph& graph,
    int iterations = 20,
    double damping = 0.85,
    int threads = -1
);


/*
    Push-based (BFS-style) PageRank

    - Each node pushes rank to neighbors
    - BFS-like frontier expansion
    - BSP-style iterations
*/
vector<double> parallel_pagerank_bfs(
    const Graph& graph,
    int iterations = 20,
    double damping = 0.85,
    int threads = -1
);