#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/dfs.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_parallel_dfs_basic() {
    /*
        Graph:
        0 -- 1 -- 2
        |
        3    4 (isolated)
    */

    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(0, 3);
    // node 4 is isolated

    auto visited = parallel_dfs(g, 0, 4);

    ASSERT_TRUE(visited[0]);
    ASSERT_TRUE(visited[1]);
    ASSERT_TRUE(visited[2]);
    ASSERT_TRUE(visited[3]);
    ASSERT_FALSE(visited[4]);
}

void test_parallel_dfs_single_node() {
    Graph g(1);
    auto visited = parallel_dfs(g, 0, 2);
    ASSERT_TRUE(visited[0]);
}

REGISTER_TEST("Parallel DFS Basic", test_parallel_dfs_basic);
REGISTER_TEST("Parallel DFS Single Node", test_parallel_dfs_single_node);