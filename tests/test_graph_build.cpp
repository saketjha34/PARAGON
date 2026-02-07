#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_build_from_adj_list() {
    vector<vector<int>> adj = {{1}, {0}};
    Graph g(adj);
    ASSERT_EQ(g.vertices(), 2);
}

void test_build_from_edge_list() {
    vector<pair<int,int>> edges = {{0,1}};
    Graph g(2, edges);
    ASSERT_TRUE(g.hasEdge(0,1));
}

REGISTER_TEST("Build from Adjacency List", test_build_from_adj_list);
REGISTER_TEST("Build from Edge List", test_build_from_edge_list);