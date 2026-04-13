#include <pybind11/pybind11.h>

namespace py = pybind11;

// Core
void bind_graph(py::module_ &);
void bind_engine(py::module_ &);

// Algorithms
void bind_algorithms(py::module_ &);

PYBIND11_MODULE(_paragon, m) {
    m.doc() = "PARAGON: Parallel Graph Engine";

    // Core
    bind_graph(m);
    bind_engine(m);

    // Algorithms
    bind_algorithms(m);
}