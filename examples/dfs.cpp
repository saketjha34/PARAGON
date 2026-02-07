#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/dfs.hpp"
// #include "../src/parallel_dfs.cpp"

int main() {
    cout << "===== PARALLEL DFS EXAMPLE =====\n\n";

    /*
        Graph structure:

            0
           / \
          1   3
          |
          2       4 (isolated)
    */

    Graph g(5);   // undirected graph

    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(0, 3);
    // node 4 is isolated

    cout << "Graph adjacency list:\n";
    g.printGraph();
    cout << "\n";

    int source = 0;
    int threads = 4;   // try 1, 2, 4, etc.

    cout << "Running parallel DFS from source: " << source << "\n";
    cout << "Using threads: " << threads << "\n\n";

    vector<bool> visited = parallel_dfs(g, source, threads);

    cout << "Reachable nodes from source " << source << ":\n";
    for (int i = 0; i < visited.size(); i++) {
        cout << "Node " << i << " -> ";
        cout << (visited[i] ? "Reachable" : "Not reachable") << "\n";
    }

    cout << "\n===== DFS EXAMPLE COMPLETED =====\n";
    return 0;
}