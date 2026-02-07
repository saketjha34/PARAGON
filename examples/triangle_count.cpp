#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/triangle_count.hpp"

int main() {
    cout << "=== Parallel Triangle Counting Example ===\n\n";

    /*
        Graph:

            0 ----- 1
             \     /|
              \   / |
                2---3

        Triangles:
            (0,1,2)
            (1,2,3)

        Expected answer = 2
    */

    Graph g(4);   // undirected graph by default

    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 0);

    g.addEdge(1, 3);
    g.addEdge(2, 3);

    cout << "Graph adjacency list:\n";
    g.printGraph();
    cout << "\n";

    int threads = 4;

    cout << "Running parallel triangle counting...\n";
    cout << "Threads used: " << threads << "\n\n";

    long long triangles = triangle_count_parallel(g, threads);

    cout << "Number of triangles: " << triangles << "\n";

    cout << "\n=== Example Finished ===\n";
    return 0;
}