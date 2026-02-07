#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/pagerank.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_pagerank_basic() {
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

    auto rank = parallel_pagerank(g, 30, 0.85, 4);

    ASSERT_EQ(rank.size(), 3);

    double sum = 0.0;
    for (double r : rank)
        sum += r;

    // PageRank values should sum to ~1
    ASSERT_TRUE(abs(sum - 1.0) < 1e-6);
}

void test_pagerank_disconnected() {
    /*
        Graph:
        0 -> 1
        2 (isolated)
    */

    Graph g(3, true);
    g.addEdge(0, 1);

    auto rank = parallel_pagerank(g, 20, 0.85, 2);

    ASSERT_EQ(rank.size(), 3);

    // All ranks should be non-negative
    for (double r : rank)
        ASSERT_TRUE(r >= 0.0);
}

REGISTER_TEST("PageRank Basic Cycle", test_pagerank_basic);
REGISTER_TEST("PageRank Disconnected Graph", test_pagerank_disconnected);