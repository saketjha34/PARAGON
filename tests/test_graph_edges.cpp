#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_edges_undirected() {
    Graph g(3);
    g.addEdge(0, 1);
    g.addEdge(1, 2);

    ASSERT_TRUE(g.hasEdge(0, 1));
    ASSERT_TRUE(g.hasEdge(1, 0));
    ASSERT_EQ(g.degree(1), 2);
}

void test_edges_directed() {
    Graph g(3, true);
    g.addEdge(0, 1);

    ASSERT_TRUE(g.hasEdge(0, 1));
    ASSERT_FALSE(g.hasEdge(1, 0));
}

REGISTER_TEST("Undirected Edges", test_edges_undirected);
REGISTER_TEST("Directed Edges", test_edges_directed);