#pragma once

#include <vector>

#include "graph.hpp"

/*
    Parallel Connected Components (Label Propagation)

    - Iterative BSP-style algorithm
    - Thread-safe
    - Works for undirected graphs

    Returns:
    - vector<int> component labels
      nodes with same label belong to same component
*/

std::vector<int> parallel_connected_components(
    const Graph& graph,
    int threads = -1
);