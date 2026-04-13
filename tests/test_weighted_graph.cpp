#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"


/*
    ============================
    CONSTRUCTOR TESTS
    ============================
*/

void test_weighted_constructor_basic() {
    WeightedGraph g(5);

    ASSERT_EQ(g.vertices(), 5);
    ASSERT_FALSE(g.isDirected());
}

void test_weighted_constructor_directed() {
    WeightedGraph g(3, true);

    ASSERT_TRUE(g.isDirected());
}


/*
    ============================
    EDGE OPERATIONS
    ============================
*/

void test_weighted_add_edge() {
    WeightedGraph g(3);

    g.addEdge(0, 1, 2.5);

    auto adj = g.getWeightedAdj();

    ASSERT_EQ(adj[0].size(), 1);
    ASSERT_EQ(adj[0][0].first, 1);
    ASSERT_EQ(adj[0][0].second, 2.5);

    // check base graph sync
    ASSERT_TRUE(g.hasEdge(0, 1));
}

void test_weighted_add_edge_undirected() {
    WeightedGraph g(3);

    g.addEdge(0, 1, 1.0);

    auto adj = g.getWeightedAdj();

    ASSERT_TRUE(adj[1].size() > 0);
    ASSERT_TRUE(g.hasEdge(1, 0));
}

void test_weighted_add_edge_directed() {
    WeightedGraph g(3, true);

    g.addEdge(0, 1, 1.0);

    ASSERT_TRUE(g.hasEdge(0, 1));
    ASSERT_FALSE(g.hasEdge(1, 0));
}

void test_weighted_add_edges_bulk() {
    WeightedGraph g(4);

    g.addEdges({
        {0,1,1.5},
        {1,2,2.5},
        {2,3,3.5}
    });

    ASSERT_TRUE(g.hasEdge(0,1));
    ASSERT_TRUE(g.hasEdge(1,2));
    ASSERT_TRUE(g.hasEdge(2,3));
}


/*
    ============================
    BUILD METHODS
    ============================
*/

void test_weighted_build_from_adj_list() {
    vector<vector<pair<int,double>>> adj = {
        {{1,2.5}},
        {{0,2.5}, {2,3.0}},
        {{1,3.0}},
    };

    WeightedGraph g;
    g.buildFromAdjList(adj);

    ASSERT_EQ(g.vertices(), 3);
    ASSERT_TRUE(g.hasEdge(1,2));

    auto wadj = g.getWeightedAdj();
    bool found = false;

    for (const auto& [v, w] : wadj[1]) {
        if (v == 2 && w == 3.0) {
            found = true;
            break;
        }
    }

    ASSERT_TRUE(found);
}

void test_weighted_build_from_adj_matrix() {
    vector<vector<double>> mat = {
        {0, 1.5, 0},
        {1.5, 0, 2.5},
        {0, 2.5, 0}
    };

    WeightedGraph g;
    g.buildFromAdjMatrix(mat);

    ASSERT_TRUE(g.hasEdge(0,1));
    ASSERT_TRUE(g.hasEdge(1,2));

    auto adj = g.getWeightedAdj();
    bool found = false;

    for (auto& [v, w] : adj[1]) {
        if (v == 2 && w == 2.5) {
            found = true;
            break;
        }
    }

    ASSERT_TRUE(found);
}


/*
    ============================
    DEGREE & CONSISTENCY
    ============================
*/

void test_weighted_degree() {
    WeightedGraph g(3);

    g.addEdge(0,1,1.0);
    g.addEdge(0,2,2.0);

    ASSERT_EQ(g.degree(0), 2);
}

void test_weighted_has_edge_consistency() {
    WeightedGraph g(3);

    g.addEdge(0,1,5.0);

    ASSERT_TRUE(g.hasEdge(0,1));
}


/*
    ============================
    ADD VERTEX
    ============================
*/

void test_weighted_add_vertex() {
    WeightedGraph g(2);

    g.addVertex();

    ASSERT_EQ(g.vertices(), 3);

    auto adj = g.getWeightedAdj();
    ASSERT_EQ(adj.size(), 3);
}


/*
    ============================
    EXCEPTION TESTS
    ============================
*/

void test_weighted_invalid_edge() {
    WeightedGraph g(2);

    bool caught = false;

    try {
        g.addEdge(0, 5, 1.0);
    } catch (...) {
        caught = true;
    }

    ASSERT_TRUE(caught);
}


/*
    ============================
    COMPLEX GRAPH
    ============================
*/

void test_weighted_complex_graph() {
    WeightedGraph g(5);

    g.addEdges({
        {0,1,1.0},
        {0,2,2.0},
        {1,3,3.0},
        {2,3,4.0},
        {3,4,5.0}
    });

    ASSERT_TRUE(g.hasEdge(3,4));
    ASSERT_EQ(g.degree(3), 3);
}


/*
    ============================
    STRESS TEST
    ============================
*/

void test_weighted_small_stress() {
    int n = 100;

    WeightedGraph g(n);

    for (int i = 0; i < n-1; i++) {
        g.addEdge(i, i+1, i * 1.0);
    }

    for (int i = 0; i < n-1; i++) {
        ASSERT_TRUE(g.hasEdge(i, i+1));
    }
}


/*
    ============================
    REGISTER TESTS
    ============================
*/

REGISTER_TEST("Weighted Constructor Basic", test_weighted_constructor_basic);
REGISTER_TEST("Weighted Constructor Directed", test_weighted_constructor_directed);

REGISTER_TEST("Weighted Add Edge", test_weighted_add_edge);
REGISTER_TEST("Weighted Add Edge Undirected", test_weighted_add_edge_undirected);
REGISTER_TEST("Weighted Add Edge Directed", test_weighted_add_edge_directed);
REGISTER_TEST("Weighted Add Edges Bulk", test_weighted_add_edges_bulk);

REGISTER_TEST("Weighted Build From Adj List", test_weighted_build_from_adj_list);
REGISTER_TEST("Weighted Build From Adj Matrix", test_weighted_build_from_adj_matrix);

REGISTER_TEST("Weighted Degree", test_weighted_degree);
REGISTER_TEST("Weighted Has Edge Consistency", test_weighted_has_edge_consistency);

REGISTER_TEST("Weighted Add Vertex", test_weighted_add_vertex);

REGISTER_TEST("Weighted Invalid Edge", test_weighted_invalid_edge);

REGISTER_TEST("Weighted Complex Graph", test_weighted_complex_graph);

REGISTER_TEST("Weighted Small Stress", test_weighted_small_stress);