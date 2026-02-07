#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/pagerank.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_pagerank_bfs_cycle() {
    /*
        Graph:
        0 -> 1
        1 -> 2
        2 -> 0
    */

    Graph g(3, true);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 0);

    auto rank = parallel_pagerank_bfs(g, 30, 0.85, 4);

    ASSERT_EQ(rank.size(), 3);

    double sum = 0.0;
    for (double r : rank)
        sum += r;

    ASSERT_TRUE(abs(sum - 1.0) < 1e-6);
}

void test_pagerank_bfs_disconnected() {
    /*
        Graph:
        0 -> 1
        2 (isolated)
    */

    Graph g(3, true);
    g.addEdge(0, 1);

    auto rank = parallel_pagerank_bfs(g, 20, 0.85, 2);

    ASSERT_EQ(rank.size(), 3);

    for (double r : rank)
        ASSERT_TRUE(r >= 0.0);
}

REGISTER_TEST("PageRank BFS Cycle", test_pagerank_bfs_cycle);
REGISTER_TEST("PageRank BFS Disconnected", test_pagerank_bfs_disconnected);