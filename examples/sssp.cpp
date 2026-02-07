#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/sssp.hpp"

int main() {
    cout << "===== PARALLEL SSSP (DIJKSTRA) EXAMPLE =====\n\n";

    /*
        Directed weighted graph:

            (1)        (2)
        0 ------> 1 ------> 2
         \                     ^
          \-----(4)-------------/

        Expected shortest paths from source 0:
        dist[0] = 0
        dist[1] = 1
        dist[2] = 3
    */

    WeightedGraph g(3, true);   // directed weighted graph

    g.addEdge(0, 1, 1.0);
    g.addEdge(1, 2, 2.0);
    g.addEdge(0, 2, 4.0);

    cout << "Weighted graph:\n";
    g.printWeightedGraph();
    cout << "\n";

    int source = 0;
    int threads = 4;

    cout << "Running parallel SSSP\n";
    cout << "Source node: " << source << "\n";
    cout << "Threads: " << threads << "\n\n";

    vector<double> dist = parallel_dijkstra(g, source, threads);

    cout << "===== SHORTEST PATH DISTANCES =====\n";
    for (int i = 0; i < dist.size(); i++) {
        cout << "Node " << i << " -> ";
        if (dist[i] >= 1e18 / 2)
            cout << "Unreachable\n";
        else
            cout << dist[i] << "\n";
    }

    cout << "\n===== SSSP EXAMPLE COMPLETED =====\n";
    return 0;
}