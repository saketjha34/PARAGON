#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "connected_components.hpp"
#include "pagerank.hpp"
#include "parallel_bfs.hpp"
#include "parallel_dfs.hpp"
#include "sssp.hpp"
#include "triangle_count.hpp"

namespace py = pybind11;

void bind_algorithms(py::module_ &m) {

    m.def("parallel_connected_components",
          &parallel_connected_components,
          py::arg("graph"),
          py::arg("threads") = -1);

    m.def("parallel_pagerank",
          &parallel_pagerank,
          py::arg("graph"),
          py::arg("iterations") = 20,
          py::arg("damping") = 0.85,
          py::arg("threads") = -1);

    m.def("parallel_pagerank_bfs",
          &parallel_pagerank_bfs,
          py::arg("graph"),
          py::arg("iterations") = 20,
          py::arg("damping") = 0.85,
          py::arg("threads") = -1);

    m.def("parallel_bfs",
          &parallel_bfs,
          py::arg("graph"),
          py::arg("source"),
          py::arg("threads") = -1);

    m.def("parallel_dfs",
          &parallel_dfs,
          py::arg("graph"),
          py::arg("source"),
          py::arg("threads") = -1);

    m.def("parallel_dijkstra",
          &parallel_dijkstra,
          py::arg("graph"),
          py::arg("source"),
          py::arg("threads") = -1);

    m.def("triangle_count_parallel",
          &triangle_count_parallel,
          py::arg("graph"),
          py::arg("threads") = -1);
}