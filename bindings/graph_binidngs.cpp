#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "graph.hpp"

namespace py = pybind11;

void bind_graph(py::module_ &m) {

    // ================= GRAPH =================
    py::class_<Graph>(m, "Graph")
        .def(py::init<>())
        .def(py::init<int, bool>(),
             py::arg("vertices"),
             py::arg("directed") = false)

        .def(py::init<const std::vector<std::vector<int>>&, bool>(),
             py::arg("adjacency"),
             py::arg("directed") = false)

        .def(py::init<int, const std::vector<std::pair<int,int>>&, bool>(),
             py::arg("vertices"),
             py::arg("edges"),
             py::arg("directed") = false)

        .def("vertices", &Graph::vertices)
        .def("is_directed", &Graph::isDirected)
        .def("get_adj", &Graph::getAdj)

        .def("add_vertex", &Graph::addVertex)
        .def("add_edge", &Graph::addEdge)
        .def("add_edges", &Graph::addEdges)

        .def("build_from_adj_matrix", &Graph::buildFromAdjMatrix)
        .def("build_from_adj_list", &Graph::buildFromAdjList)

        .def("degree", &Graph::degree)
        .def("has_edge", &Graph::hasEdge)

        .def("print_graph", &Graph::printGraph)
    ;

    // ================= WEIGHTED GRAPH =================
    py::class_<WeightedGraph, Graph>(m, "WeightedGraph")
        .def(py::init<>())
        .def(py::init<int, bool>(),
             py::arg("vertices"),
             py::arg("directed") = false)

        .def("add_edge", &WeightedGraph::addEdge)
        .def("add_edges", &WeightedGraph::addEdges)

        .def("build_from_adj_list", &WeightedGraph::buildFromAdjList)
        .def("build_from_adj_matrix", &WeightedGraph::buildFromAdjMatrix)

        .def("get_adj", &WeightedGraph::getWeightedAdj)

        .def("print_graph", &WeightedGraph::printGraph)
    ;
}