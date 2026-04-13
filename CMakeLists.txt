cmake_minimum_required(VERSION 3.16)

project(ParagonEngine
    VERSION 1.0
    LANGUAGES CXX
)

# ================= OPTIONS =================
option(BUILD_EXAMPLES "Build examples" OFF)
option(BUILD_TESTS "Build tests" OFF)
option(BUILD_BENCHMARKS "Build benchmarks" OFF)

# ================= C++ SETTINGS =================
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# ================= INCLUDE DIR =================
include_directories(${CMAKE_SOURCE_DIR}/include)

# ================= SOURCE FILES =================
file(GLOB SRC_FILES ${CMAKE_SOURCE_DIR}/src/*.cpp)

# ================= CORE LIBRARY =================
add_library(graph_engine STATIC ${SRC_FILES})

set_target_properties(graph_engine PROPERTIES POSITION_INDEPENDENT_CODE ON)

# ================= PYTHON + PYBIND11 =================
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# AUTO-DETECT pybind11 (works with pip install)
execute_process(
    COMMAND ${Python3_EXECUTABLE} -c "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE pybind11_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

list(APPEND CMAKE_PREFIX_PATH ${pybind11_dir})

find_package(pybind11 REQUIRED)

# ================= BINDINGS =================
file(GLOB_RECURSE BINDING_SOURCES ${CMAKE_SOURCE_DIR}/bindings/*.cpp)

# ================= PYTHON MODULE =================
pybind11_add_module(_paragon ${BINDING_SOURCES})

target_link_libraries(_paragon PRIVATE graph_engine)

# ================= INSTALL (FOR pip) =================
install(TARGETS _paragon
    LIBRARY DESTINATION paragon
    RUNTIME DESTINATION paragon
)

# ================= OPTIMIZATION =================
if(MSVC)
    target_compile_options(_paragon PRIVATE /O2)
else()
    target_compile_options(_paragon PRIVATE -O3)
endif()

# ================= TESTS =================
if(BUILD_TESTS)
    file(GLOB TEST_FILES ${CMAKE_SOURCE_DIR}/tests/*.cpp)

    add_executable(run_tests ${TEST_FILES})
    target_link_libraries(run_tests PRIVATE graph_engine)
endif()

# ================= EXAMPLES =================
if(BUILD_EXAMPLES)

    add_executable(example_bfs examples/bfs.cpp)
    target_link_libraries(example_bfs PRIVATE graph_engine)

    add_executable(example_dfs examples/dfs.cpp)
    target_link_libraries(example_dfs PRIVATE graph_engine)

    add_executable(example_connected_components examples/connected_components.cpp)
    target_link_libraries(example_connected_components PRIVATE graph_engine)

    add_executable(example_pagerank examples/pagerank.cpp)
    target_link_libraries(example_pagerank PRIVATE graph_engine)

    add_executable(example_parallel_pagerank_bfs examples/parallel_pagerank_bfs.cpp)
    target_link_libraries(example_parallel_pagerank_bfs PRIVATE graph_engine)

    add_executable(example_sssp examples/sssp.cpp)
    target_link_libraries(example_sssp PRIVATE graph_engine)

    add_executable(example_triangle_count examples/triangle_count.cpp)
    target_link_libraries(example_triangle_count PRIVATE graph_engine)

endif()

# ================= BENCHMARKS =================
if(BUILD_BENCHMARKS)

    add_executable(benchmark_sssp benchmark/benchmark_sssp.cpp)
    target_link_libraries(benchmark_sssp PRIVATE graph_engine)

    add_executable(benchmark_pagerank benchmark/benchmark_pagerank.cpp)
    target_link_libraries(benchmark_pagerank PRIVATE graph_engine)

    add_executable(benchmark_connected_components
        benchmark/benchmark_connected_components.cpp
    )
    target_link_libraries(benchmark_connected_components PRIVATE graph_engine)

    add_executable(benchmark_triangle_count
        benchmark/benchmark_triangle_count.cpp
    )
    target_link_libraries(benchmark_triangle_count PRIVATE graph_engine)

endif()