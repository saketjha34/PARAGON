#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/pagerank.hpp"

int main() {
    cout << "===== PARALLEL PAGERANK EXAMPLE =====\n\n";

    /*
        Directed graph edges:
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

    int V = 4;              // nodes: 0,1,2,3
    Graph g(V, true);       // directed graph
    g.addEdges(edges);

    cout << "Graph constructed\n";
    cout << "Vertices: " << V << "\n\n";

    cout << "Adjacency list:\n";
    g.printGraph();
    cout << "\n";

    int iterations = 30;
    double damping = 0.85;
    int threads = 4;

    cout << "Running Parallel PageRank (pull-based)\n";
    cout << "Iterations: " << iterations << "\n";
    cout << "Damping factor: " << damping << "\n";
    cout << "Threads: " << threads << "\n\n";

    vector<double> rank =
        parallel_pagerank(g, iterations, damping, threads);

    // Sort nodes by rank
    vector<pair<int,double>> ranked_nodes;
    for (int i = 0; i < rank.size(); i++) {
        ranked_nodes.push_back({i, rank[i]});
    }

    sort(ranked_nodes.begin(), ranked_nodes.end(),
         [](const auto& a, const auto& b) {
             return a.second > b.second;
         });

    cout << "===== PAGE RANK RESULTS =====\n";
    cout << fixed << setprecision(6);

    for (auto &p : ranked_nodes) {
        cout << "Node " << p.first
             << " -> Rank: " << p.second << "\n";
    }

    cout << "\n===== PAGERANK EXAMPLE COMPLETED =====\n";
    return 0;
}