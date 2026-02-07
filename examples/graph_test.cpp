#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"

int main() {
    cout << "===== GRAPH FUNCTIONALITY TEST =====\n\n";

    /* ----------------- Test 1: Empty Graph ----------------- */
    cout << "[Test 1] Empty Graph\n";
    Graph g1;
    cout << "Vertices: " << g1.vertices() << "\n\n";

    /* ----------------- Test 2: Graph with Vertices ----------------- */
    cout << "[Test 2] Graph with 5 vertices (Undirected)\n";
    Graph g2(5);
    g2.printGraph();
    cout << "\n";

    /* ----------------- Test 3: Add Vertices ----------------- */
    cout << "[Test 3] Adding 2 vertices dynamically\n";
    g2.addVertex();
    g2.addVertex();
    cout << "Vertices after adding: " << g2.vertices() << "\n";
    g2.printGraph();
    cout << "\n";

    /* ----------------- Test 4: Add Edges ----------------- */
    cout << "[Test 4] Adding edges\n";
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(3, 4);
    g2.addEdge(5, 6);
    g2.printGraph();
    cout << "\n";

    /* ----------------- Test 5: Degree & Edge Check ----------------- */
    cout << "[Test 5] Degree & Edge existence\n";
    cout << "Degree of 0: " << g2.degree(0) << "\n";
    cout << "Edge 0 -> 1 exists? " << (g2.hasEdge(0, 1) ? "YES" : "NO") << "\n";
    cout << "Edge 1 -> 3 exists? " << (g2.hasEdge(1, 3) ? "YES" : "NO") << "\n\n";

    /* ----------------- Test 6: Directed Graph ----------------- */
    cout << "[Test 6] Directed Graph\n";
    Graph g3(4, true);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 0);
    g3.printGraph();
    cout << "\n";

    /* ----------------- Test 7: Build from Adjacency List ----------------- */
    cout << "[Test 7] Build from adjacency list\n";
    vector<vector<int>> adj = {
        {1, 2},
        {0, 3},
        {0},
        {1}
    };
    Graph g4(adj);
    g4.printGraph();
    cout << "\n";

    /* ----------------- Test 8: Build from Edge List ----------------- */
    cout << "[Test 8] Build from edge list\n";
    vector<pair<int,int>> edges = {
        {0,1}, {1,2}, {2,3}, {3,0}
    };
    Graph g5(4, edges);
    g5.printGraph();
    cout << "\n";

    cout << "===== ALL TESTS COMPLETED =====\n";
    return 0;
}