#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_graph_constructors() {
    Graph g1;
    ASSERT_EQ(g1.vertices(), 0);

    Graph g2(5);
    ASSERT_EQ(g2.vertices(), 5);
    ASSERT_FALSE(g2.isDirected());

    Graph g3(4, true);
    ASSERT_EQ(g3.vertices(), 4);
    ASSERT_TRUE(g3.isDirected());
}

REGISTER_TEST("Graph Constructors", test_graph_constructors);