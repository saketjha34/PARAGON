#pragma once

#include <cstdint>   // for int64_t (better than long long)

#include "graph.hpp"

/*
    Triangle Counting

    Counts number of triangles (u, v, w) such that:
    u < v < w and edges exist between all pairs.

    Works on UNDIRECTED graphs.
*/

std::int64_t triangle_count_parallel(
    const Graph& graph,
    int threads = -1
);