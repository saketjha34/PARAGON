#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/sssp.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

static const double INF = 1e18;

void test_sssp_basic() {
    /*
        Graph:
        0 --1--> 1 --2--> 2
         \                 ^
          \----4----------/

        Shortest paths from 0:
        dist[0] = 0
        dist[1] = 1
        dist[2] = 3
    */

    WeightedGraph g(3, true);

    g.addEdge(0, 1, 1.0);
    g.addEdge(1, 2, 2.0);
    g.addEdge(0, 2, 4.0);

    auto dist = parallel_dijkstra(g, 0, 4);

    ASSERT_TRUE(abs(dist[0] - 0.0) < 1e-9);
    ASSERT_TRUE(abs(dist[1] - 1.0) < 1e-9);
    ASSERT_TRUE(abs(dist[2] - 3.0) < 1e-9);
}

void test_sssp_disconnected() {
    /*
        Graph:
        0 --1--> 1

        Node 2 is disconnected
    */

    WeightedGraph g(3, true);
    g.addEdge(0, 1, 1.0);

    auto dist = parallel_dijkstra(g, 0, 2);

    ASSERT_TRUE(abs(dist[0] - 0.0) < 1e-9);
    ASSERT_TRUE(abs(dist[1] - 1.0) < 1e-9);
    ASSERT_TRUE(dist[2] >= INF / 2);   // unreachable
}

void test_sssp_undirected_graph() {
    /*
        Undirected graph:
        0 --2-- 1 --1-- 2

        Shortest path 0 -> 2 = 3
    */

    WeightedGraph g(3, false);

    g.addEdge(0, 1, 2.0);
    g.addEdge(1, 2, 1.0);

    auto dist = parallel_dijkstra(g, 0, 2);

    ASSERT_TRUE(abs(dist[0] - 0.0) < 1e-9);
    ASSERT_TRUE(abs(dist[1] - 2.0) < 1e-9);
    ASSERT_TRUE(abs(dist[2] - 3.0) < 1e-9);
}

REGISTER_TEST("SSSP Basic", test_sssp_basic);
REGISTER_TEST("SSSP Disconnected Graph", test_sssp_disconnected);
REGISTER_TEST("SSSP Undirected Graph", test_sssp_undirected_graph);