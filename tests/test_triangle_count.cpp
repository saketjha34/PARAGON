#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/triangle_count.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

/*
    Graph:
        0
       / \
      1---2

    One triangle
*/
void test_parallel_triangle_single() {
    Graph g(3);

    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 0);

    long long result = triangle_count_parallel(g, 4);

    ASSERT_EQ(result, 1);
}

/*
    Graph:
        0 -- 1 -- 2 -- 3

    No triangles
*/
void test_parallel_triangle_none() {
    Graph g(4);

    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 3);

    long long result = triangle_count_parallel(g, 4);

    ASSERT_EQ(result, 0);
}

/*
    Graph:
        0 --- 1
         \   /|
           2--3

    Two triangles
*/
void test_parallel_triangle_multiple() {
    Graph g(4);

    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 0);

    g.addEdge(1, 3);
    g.addEdge(2, 3);

    long long result = triangle_count_parallel(g, 4);

    ASSERT_EQ(result, 2);
}

/*
    Fully connected K4 graph
    Triangles = C(4,3) = 4
*/
void test_parallel_triangle_clique() {
    Graph g(4);

    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            g.addEdge(i, j);
        }
    }

    long long result = triangle_count_parallel(g, 4);

    ASSERT_EQ(result, 4);
}

REGISTER_TEST("Parallel Triangle Single", test_parallel_triangle_single);
REGISTER_TEST("Parallel Triangle None", test_parallel_triangle_none);
REGISTER_TEST("Parallel Triangle Multiple", test_parallel_triangle_multiple);
REGISTER_TEST("Parallel Triangle Clique", test_parallel_triangle_clique);