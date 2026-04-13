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

void test_constructor_basic() {
    Graph g(5);

    ASSERT_EQ(g.vertices(), 5);
    ASSERT_FALSE(g.isDirected());
}

void test_constructor_directed() {
    Graph g(4, true);

    ASSERT_EQ(g.vertices(), 56);   // 4
    ASSERT_TRUE(g.isDirected());
}

void test_constructor_adj_list() {
    vector<vector<int>> adj = {
        {1, 2},
        {0},
        {0}
    };

    Graph g(adj);

    ASSERT_EQ(g.vertices(), 3);
    ASSERT_TRUE(g.hasEdge(0, 1));
    ASSERT_TRUE(g.hasEdge(0, 2));
}

void test_constructor_edge_list() {
    Graph g(3, {{0,1}, {1,2}});

    ASSERT_TRUE(g.hasEdge(0,1));
    ASSERT_TRUE(g.hasEdge(1,2));
}


/*
    ============================
    EDGE OPERATIONS
    ============================
*/

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

void test_add_edges_bulk() {
    Graph g(4);

    g.addEdges({{0,1}, {1,2}, {2,3}});

    ASSERT_TRUE(g.hasEdge(0,1));
    ASSERT_TRUE(g.hasEdge(1,2));
    ASSERT_TRUE(g.hasEdge(2,3));
}


/*
    ============================
    DEGREE TESTS
    ============================
*/

void test_degree() {
    Graph g(4);

    g.addEdges({{0,1}, {0,2}, {0,3}});

    ASSERT_EQ(g.degree(0), 3);
    ASSERT_EQ(g.degree(1), 1);
}


/*
    ============================
    BUILD METHODS
    ============================
*/

void test_build_from_adj_matrix() {
    vector<vector<int>> mat = {
        {0,1,1},
        {1,0,0},
        {1,0,0}
    };

    Graph g;
    g.buildFromAdjMatrix(mat);

    ASSERT_EQ(g.vertices(), 3);
    ASSERT_TRUE(g.hasEdge(0,1));
    ASSERT_TRUE(g.hasEdge(0,2));
}

void test_build_from_adj_list() {
    vector<vector<int>> adj = {
        {1},
        {0,2},
        {1}
    };

    Graph g;
    g.buildFromAdjList(adj);

    ASSERT_TRUE(g.hasEdge(1,2));
    ASSERT_TRUE(g.hasEdge(2,1));
}


/*
    ============================
    ADD VERTEX
    ============================
*/

void test_add_vertex() {
    Graph g(2);

    g.addVertex();

    ASSERT_EQ(g.vertices(), 3);
}


/*
    ============================
    EXCEPTION TESTS
    ============================
*/

void test_invalid_edge() {
    Graph g(2);

    bool caught = false;

    try {
        g.addEdge(0, 5);
    } catch (...) {
        caught = true;
    }

    ASSERT_TRUE(caught);
}

void test_invalid_degree() {
    Graph g(2);

    bool caught = false;

    try {
        g.degree(5);
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

void test_complex_graph() {
    Graph g(6);

    g.addEdges({
        {0,1}, {0,2}, {1,3},
        {2,3}, {3,4}, {4,5}
    });

    ASSERT_TRUE(g.hasEdge(0,1));
    ASSERT_TRUE(g.hasEdge(2,3));
    ASSERT_FALSE(g.hasEdge(5,0));

    ASSERT_EQ(g.degree(3), 3);
}


/*
    ============================
    ADJ VALIDATION
    ============================
*/

void test_get_adj() {
    Graph g(3);

    g.addEdges({{0,1}, {0,2}});

    auto adj = g.getAdj();

    ASSERT_EQ(adj[0].size(), 2);
    ASSERT_EQ(adj[1].size(), 1);
}


/*
    ============================
    STRESS TEST
    ============================
*/

void test_small_stress() {
    int n = 100;

    Graph g(n);

    for (int i = 0; i < n-1; i++) {
        g.addEdge(i, i+1);
    }

    for (int i = 0; i < n-1; i++) {
        ASSERT_TRUE(g.hasEdge(i, i+1));
    }
}


/*
    ============================
    REGISTER ALL TESTS
    ============================
*/

REGISTER_TEST("Constructor Basic", test_constructor_basic);
REGISTER_TEST("Constructor Directed", test_constructor_directed);
REGISTER_TEST("Constructor Adj List", test_constructor_adj_list);
REGISTER_TEST("Constructor Edge List", test_constructor_edge_list);

REGISTER_TEST("Undirected Edges", test_edges_undirected);
REGISTER_TEST("Directed Edges", test_edges_directed);
REGISTER_TEST("Add Edges Bulk", test_add_edges_bulk);

REGISTER_TEST("Degree", test_degree);

REGISTER_TEST("Build From Adj Matrix", test_build_from_adj_matrix);
REGISTER_TEST("Build From Adj List", test_build_from_adj_list);

REGISTER_TEST("Add Vertex", test_add_vertex);

REGISTER_TEST("Invalid Edge", test_invalid_edge);
REGISTER_TEST("Invalid Degree", test_invalid_degree);

REGISTER_TEST("Complex Graph", test_complex_graph);

REGISTER_TEST("Get Adjacency", test_get_adj);

REGISTER_TEST("Small Stress", test_small_stress);