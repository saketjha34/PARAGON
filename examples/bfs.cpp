#include <bits/stdc++.h>
using namespace std;

#include "../include/graph.hpp"
#include "../include/bfs.hpp"
// #include "../src/parallel_bfs.cpp"

int main() {
    cout << "===== PARALLEL BFS EXAMPLE =====\n\n";

    /*
        Graph structure:

        0 --- 1 --- 3 --- 4
         \          /
          \-- 2 ---/
    */

    Graph g(6);   // undirected graph with 6 vertices

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    // node 5 is disconnected

    cout << "Graph adjacency list:\n";
    g.printGraph();
    cout << "\n";

    int source = 0;
    int threads = 4;   // try changing this

    cout << "Running parallel BFS from source: " << source << "\n";
    cout << "Using threads: " << threads << "\n\n";

    vector<int> dist = parallel_bfs(g, source, threads);

    cout << "Shortest distances from source " << source << ":\n";
    for (int i = 0; i < dist.size(); i++) {
        cout << "Node " << i << " -> ";
        if (dist[i] == -1)
            cout << "Unreachable\n";
        else
            cout << dist[i] << "\n";
    }

    cout << "\n===== BFS EXAMPLE COMPLETED =====\n";
    return 0;
}