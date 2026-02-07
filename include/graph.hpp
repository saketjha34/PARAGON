#pragma once
#include <bits/stdc++.h>
using namespace std;

class Graph {
private:
    int V;                                 // Number of vertices
    bool directed;                         // Directed or undirected graph
    vector<vector<int>> adj;               // Adjacency list

public:
    /* ================= CONSTRUCTORS ================= */

    // Default constructor
    Graph() : V(0), directed(false) {}

    // Create graph with V vertices
    Graph(int vertices, bool isDirected = false) {
        V = vertices;
        directed = isDirected;
        adj.resize(V);
    }

    // Create graph from adjacency list
    Graph(const vector<vector<int>>& adjacency, bool isDirected = false) {
        V = adjacency.size();
        directed = isDirected;
        adj = adjacency;
    }

    // Create graph from edge list
    Graph(int vertices, const vector<pair<int,int>>& edges, bool isDirected = false) {
        V = vertices;
        directed = isDirected;
        adj.resize(V);
        for (auto &e : edges) {
            addEdge(e.first, e.second);
        }
    }

    /* ================= BASIC UTILITIES ================= */

    // Number of vertices
    int vertices() const {
        return V;
    }

    // Check if graph is directed
    bool isDirected() const {
        return directed;
    }

    // Get adjacency list
    const vector<vector<int>>& getAdj() const {
        return adj;
    }

    /* ================= MODIFY GRAPH ================= */

    // Add a new vertex
    void addVertex() {
        adj.push_back({});
        V++;
    }

    // Add an edge u -> v
    void addEdge(int u, int v) {
        if (u >= V || v >= V)
            throw out_of_range("Vertex index out of range");

        adj[u].push_back(v);
        if (!directed) {
            adj[v].push_back(u);
        }
    }

    // Add multiple edges
    void addEdges(const vector<pair<int,int>>& edges) {
        for (auto &e : edges) {
            addEdge(e.first, e.second);
        }
    }

    /* ================= BUILD FROM DATA ================= */

    // Build graph from adjacency matrix
    void buildFromAdjMatrix(const vector<vector<int>>& matrix) {
        int n = matrix.size();
        V = n;
        adj.assign(V, {});

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j]) {
                    adj[i].push_back(j);
                    if (!directed && i != j)
                        adj[j].push_back(i);
                }
            }
        }
    }

    // Build graph from adjacency list
    void buildFromAdjList(const vector<vector<int>>& adjacency) {
        V = adjacency.size();
        adj = adjacency;
    }

    /* ================= GRAPH INFO ================= */

    // Degree of a vertex
    int degree(int u) const {
        if (u >= V)
            throw out_of_range("Vertex index out of range");
        return adj[u].size();
    }

    // Check edge existence
    bool hasEdge(int u, int v) const {
        if (u >= V || v >= V)
            throw out_of_range("Vertex index out of range");
        return find(adj[u].begin(), adj[u].end(), v) != adj[u].end();
    }

    /* ================= DEBUG ================= */

    // Print adjacency list
    void printGraph() const {
        for (int i = 0; i < V; i++) {
            cout << i << " : ";
            for (int v : adj[i]) {
                cout << v << " ";
            }
            cout << "\n";
        }
    }
};


/*
    WeightedGraph

    - Inherits from Graph
    - Stores (neighbor, weight)
    - Used for SSSP / Dijkstra
*/
class WeightedGraph : public Graph {
private:
    vector<vector<pair<int,double>>> wadj;

public:
    /* ================= CONSTRUCTORS ================= */

    WeightedGraph() : Graph() {}

    WeightedGraph(int vertices, bool isDirected = false)
        : Graph(vertices, isDirected) {
        wadj.resize(vertices);
    }

    /* ================= WEIGHTED EDGES ================= */

    void addEdge(int u, int v, double w) {
        if (u >= vertices() || v >= vertices())
            throw out_of_range("Vertex index out of range");

        wadj[u].push_back({v, w});
        if (!isDirected())
            wadj[v].push_back({u, w});
    }

    void addEdges(const vector<tuple<int,int,double>>& edges) {
        for (auto& [u, v, w] : edges)
            addEdge(u, v, w);
    }

    /* ================= ACCESS ================= */

    const vector<vector<pair<int,double>>>& getWeightedAdj() const {
        return wadj;
    }

    /* ================= DEBUG ================= */

    void printWeightedGraph() const {
        for (int i = 0; i < wadj.size(); i++) {
            cout << i << " : ";
            for (auto& [v, w] : wadj[i]) {
                cout << "(" << v << ", w=" << w << ") ";
            }
            cout << "\n";
        }
    }
};