#pragma once

#include <vector>

#include "graph.hpp"

/*
    Parallel Single Source Shortest Path (SSSP)

    - Works on WeightedGraph
    - Non-negative edge weights
    - Parallel edge relaxation
*/

std::vector<double> parallel_dijkstra(
    const WeightedGraph& graph,
    int source,
    int threads = -1
);