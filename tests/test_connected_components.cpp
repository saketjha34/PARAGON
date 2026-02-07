#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/connected_components.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_cc_multiple_components() {
    /*
        Components:
        {0,1,2}   {3,4}   {5}
    */

    Graph g(6);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(3, 4);
    // node 5 isolated

    auto comp = parallel_connected_components(g, 4);

    ASSERT_TRUE(comp[0] == comp[1]);
    ASSERT_TRUE(comp[1] == comp[2]);

    ASSERT_TRUE(comp[3] == comp[4]);

    ASSERT_FALSE(comp[0] == comp[3]);
    ASSERT_FALSE(comp[0] == comp[5]);
}

void test_cc_single_component() {
    Graph g(4);
    g.addEdge(0,1);
    g.addEdge(1,2);
    g.addEdge(2,3);

    auto comp = parallel_connected_components(g, 2);

    for (int i = 1; i < 4; i++)
        ASSERT_TRUE(comp[i] == comp[0]);
}

void test_cc_all_isolated() {
    Graph g(3);
    auto comp = parallel_connected_components(g, 2);

    ASSERT_EQ(comp[0], 0);
    ASSERT_EQ(comp[1], 1);
    ASSERT_EQ(comp[2], 2);
}

REGISTER_TEST("CC Multiple Components", test_cc_multiple_components);
REGISTER_TEST("CC Single Component", test_cc_single_component);
REGISTER_TEST("CC All Isolated", test_cc_all_isolated);