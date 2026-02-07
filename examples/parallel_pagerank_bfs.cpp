#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/pagerank.hpp"

int main() {
    cout << "===== PARALLEL PAGERANK (BFS / PUSH STYLE) =====\n\n";

    /*
        Directed graph:

            0 -> 1
            0 -> 2
            1 -> 2
            2 -> 0
            2 -> 3
            3 -> 3
    */

    vector<pair<int,int>> edges = {
        {0, 1},
        {0, 2},
        {1, 2},
        {2, 0},
        {2, 3},
        {3, 3}
    };

    int V = 4;
    Graph g(V, true);   // directed graph
    g.addEdges(edges);

    cout << "Graph constructed explicitly\n";
    cout << "Vertices: " << V << "\n\n";

    cout << "Adjacency list:\n";
    g.printGraph();
    cout << "\n";

    int iterations = 20;
    double damping = 0.85;
    int threads = 4;

    cout << "Running Parallel PageRank (push / BFS-style)\n";
    cout << "Iterations: " << iterations << "\n";
    cout << "Damping factor: " << damping << "\n";
    cout << "Threads: " << threads << "\n\n";

    vector<double> ranks =
        parallel_pagerank_bfs(g, iterations, damping, threads);

    cout << "===== PAGERANK SCORES =====\n";
    cout << fixed << setprecision(6);

    for (int i = 0; i < ranks.size(); i++) {
        cout << "Node " << i << " -> " << ranks[i] << "\n";
    }

    cout << "\n===== PAGERANK BFS EXAMPLE COMPLETED =====\n";
    return 0;
}