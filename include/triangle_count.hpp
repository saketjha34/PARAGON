#pragma once
#include <bits/stdc++.h>
using namespace std;

#include "graph.hpp"

/*
    Triangle Counting

    Counts number of triangles (u, v, w) such that:
    u < v < w and edges exist between all pairs.

    Works on UNDIRECTED graphs.
*/

long long triangle_count_parallel(
    const Graph& graph,
    int threads = -1
);