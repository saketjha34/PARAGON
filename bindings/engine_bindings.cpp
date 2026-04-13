#include <pybind11/pybind11.h>
#include "engine.hpp"

namespace py = pybind11;

void bind_engine(py::module_ &m) {

    m.def("hardware_threads", &engine::hardware_threads);
    m.def("get_thread_count", &engine::get_thread_count);
    m.def("chunk_size", &engine::chunk_size);
}