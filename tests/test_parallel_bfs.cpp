#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/bfs.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_parallel_bfs_basic() {
    Graph g(6);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,3);
    g.addEdge(2,3);
    g.addEdge(3,4);

    auto dist = parallel_bfs(g, 0, 4);

    ASSERT_EQ(dist[0], 0);
    ASSERT_EQ(dist[1], 1);
    ASSERT_EQ(dist[2], 1);
    ASSERT_EQ(dist[3], 2);
    ASSERT_EQ(dist[4], 3);
    ASSERT_EQ(dist[5], -1);
}

REGISTER_TEST("Parallel BFS Basic", test_parallel_bfs_basic);