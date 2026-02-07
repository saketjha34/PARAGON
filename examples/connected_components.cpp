#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/connected_components.hpp"

int main() {
    cout << "===== PARALLEL CONNECTED COMPONENTS (MANUAL GRAPH) =====\n\n";

    /*
        Graph structure (UNDIRECTED):

        Component 1: 0 -- 1 -- 2
        Component 2: 3 -- 4
        Component 3: 5 (isolated)

            0 -- 1 -- 2     3 -- 4     5
    */

    Graph g(6);   // undirected graph with 6 vertices

    // Component 1
    g.addEdge(0, 1);
    g.addEdge(1, 2);

    // Component 2
    g.addEdge(3, 4);

    // Component 3: node 5 is isolated

    cout << "Adjacency list:\n";
    g.printGraph();
    cout << "\n";

    int threads = 4;

    cout << "Running parallel connected components\n";
    cout << "Threads: " << threads << "\n\n";

    vector<int> comp = parallel_connected_components(g, threads);

    // Group nodes by component label
    unordered_map<int, vector<int>> components;
    for (int i = 0; i < comp.size(); i++) {
        components[comp[i]].push_back(i);
    }

    cout << "===== CONNECTED COMPONENTS =====\n";
    int idx = 1;
    for (auto& [label, nodes] : components) {
        cout << "Component " << idx++ << " : ";
        for (int node : nodes)
            cout << node << " ";
        cout << "\n";
    }

    cout << "\n===== CC EXAMPLE COMPLETED =====\n";
    return 0;
}