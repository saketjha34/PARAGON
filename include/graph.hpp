#pragma once

#include <vector>
#include <utility>
#include <tuple>
#include <stdexcept>
#include <algorithm>
#include <iostream>

/*
    ============================
    GRAPH (BASE CLASS)
    ============================
*/
class Graph {
protected:
    int V;
    bool directed;
    std::vector<std::vector<int>> adj;

public:
    /* ===== CONSTRUCTORS ===== */

    Graph() : V(0), directed(false) {}

    Graph(int vertices, bool isDirected = false)
        : V(vertices), directed(isDirected) {
        adj.resize(V);
    }

    // From adjacency list
    Graph(const std::vector<std::vector<int>>& adjacency, bool isDirected = false) {
        V = adjacency.size();
        directed = isDirected;
        adj = adjacency;
    }

    // From edge list
    Graph(int vertices,
          const std::vector<std::pair<int,int>>& edges,
          bool isDirected = false)
        : V(vertices), directed(isDirected) {

        adj.resize(V);
        for (auto &e : edges) {
            addEdge(e.first, e.second);
        }
    }

    virtual ~Graph() = default;

    /* ===== BASIC ===== */

    int vertices() const { return V; }

    bool isDirected() const { return directed; }

    const std::vector<std::vector<int>>& getAdj() const {
        return adj;
    }

    /* ===== MODIFY ===== */

    virtual void addVertex() {
        adj.push_back({});
        V++;
    }

    virtual void addEdge(int u, int v) {
        if (u >= V || v >= V)
            throw std::out_of_range("Vertex index out of range");

        adj[u].push_back(v);
        if (!directed)
            adj[v].push_back(u);
    }

    virtual void addEdges(const std::vector<std::pair<int,int>>& edges) {
        for (auto &e : edges)
            addEdge(e.first, e.second);
    }

    /* ===== BUILD ===== */

    virtual void buildFromAdjMatrix(const std::vector<std::vector<int>>& matrix) {
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

    virtual void buildFromAdjList(const std::vector<std::vector<int>>& adjacency) {
        V = adjacency.size();
        adj = adjacency;
    }

    /* ===== INFO ===== */

    int degree(int u) const {
        if (u >= V)
            throw std::out_of_range("Invalid vertex");
        return adj[u].size();
    }

    bool hasEdge(int u, int v) const {
        if (u >= V || v >= V)
            throw std::out_of_range("Invalid vertex");

        return std::find(adj[u].begin(), adj[u].end(), v) != adj[u].end();
    }

    /* ===== DEBUG ===== */

    virtual void printGraph() const {
        for (int i = 0; i < V; i++) {
            std::cout << i << " : ";
            for (int v : adj[i])
                std::cout << v << " ";
            std::cout << "\n";
        }
    }
};


/*
    ============================
    WEIGHTED GRAPH
    ============================
*/
class WeightedGraph : public Graph {
private:
    std::vector<std::vector<std::pair<int,double>>> wadj;

public:
    /* ===== CONSTRUCTORS ===== */

    WeightedGraph() : Graph() {}

    WeightedGraph(int vertices, bool isDirected = false)
        : Graph(vertices, isDirected) {
        wadj.resize(vertices);
    }

    /* ===== MODIFY ===== */

    void addVertex() override {
        Graph::addVertex();
        wadj.push_back({});
    }

    void addEdge(int u, int v, double w) {
        if (u >= V || v >= V)
            throw std::out_of_range("Vertex index out of range");

        // weighted adjacency
        wadj[u].push_back({v, w});

        // 🔥 FIX: update base graph adjacency
        adj[u].push_back(v);

        if (!directed) {
            wadj[v].push_back({u, w});
            adj[v].push_back(u);
        }
    }

    void addEdges(const std::vector<std::tuple<int,int,double>>& edges) {
        for (auto& [u, v, w] : edges)
            addEdge(u, v, w);
    }

    /* ===== BUILD ===== */

    void buildFromAdjList(
        const std::vector<std::vector<std::pair<int,double>>>& adjacency
    ) {
        V = adjacency.size();
        wadj = adjacency;

        // keep base structure consistent
        adj.assign(V, {});
        for (int u = 0; u < V; u++) {
            for (auto& [v, _] : wadj[u]) {
                adj[u].push_back(v);
            }
        }
    }

    void buildFromAdjMatrix(
        const std::vector<std::vector<double>>& matrix
    ) {
        int n = matrix.size();
        V = n;

        wadj.assign(V, {});
        adj.assign(V, {});

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j] != 0) {
                    wadj[i].push_back({j, matrix[i][j]});
                    adj[i].push_back(j);

                    if (!directed && i != j) {
                        wadj[j].push_back({i, matrix[i][j]});
                        adj[j].push_back(i);
                    }
                }
            }
        }
    }

    /* ===== ACCESS ===== */

    const std::vector<std::vector<std::pair<int,double>>>&
    getWeightedAdj() const {
        return wadj;
    }

    /* ===== DEBUG ===== */

    void printGraph() const override {
        for (int i = 0; i < V; i++) {
            std::cout << i << " : ";
            for (auto& [v, w] : wadj[i]) {
                std::cout << "(" << v << ", " << w << ") ";
            }
            std::cout << "\n";
        }
    }

    // backward compatibility
    void printWeightedGraph() const {
        printGraph();
    }    
};