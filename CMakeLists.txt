cmake_minimum_required(VERSION 3.16)

project(ParallelGraphEngine
    VERSION 1.0
    LANGUAGES CXX
)

# ================= C++ SETTINGS =================
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)   # needed for bits/stdc++.h

# ================= INCLUDE DIR =================
include_directories(include)

# ================= LIBRARY =================
file(GLOB SRC_FILES
    src/*.cpp
)

add_library(graph_engine STATIC
    ${SRC_FILES}
)

# ================= TESTS =================
file(GLOB TEST_FILES
    tests/*.cpp
)

add_executable(run_tests
    ${TEST_FILES}
)

target_link_libraries(run_tests
    graph_engine
)

# ================= EXAMPLES =================

add_executable(example_bfs examples/bfs.cpp)
target_link_libraries(example_bfs graph_engine)

add_executable(example_dfs examples/dfs.cpp)
target_link_libraries(example_dfs graph_engine)

add_executable(example_connected_components examples/connected_components.cpp)
target_link_libraries(example_connected_components graph_engine)

add_executable(example_pagerank examples/pagerank.cpp)
target_link_libraries(example_pagerank graph_engine)

add_executable(example_parallel_pagerank_bfs examples/parallel_pagerank_bfs.cpp)
target_link_libraries(example_parallel_pagerank_bfs graph_engine)

add_executable(example_sssp examples/sssp.cpp)
target_link_libraries(example_sssp graph_engine)

add_executable(example_triangle_count examples/triangle_count.cpp)
target_link_libraries(example_triangle_count graph_engine)

# ================= BENCHMARKS =================

add_executable(benchmark_sssp benchmark/benchmark_sssp.cpp)
target_link_libraries(benchmark_sssp graph_engine)

add_executable(benchmark_pagerank benchmark/benchmark_pagerank.cpp)
target_link_libraries(benchmark_pagerank graph_engine)

add_executable(benchmark_connected_components
    benchmark/benchmark_connected_components.cpp
)
target_link_libraries(benchmark_connected_components graph_engine)

add_executable(benchmark_triangle_count
    benchmark/benchmark_triangle_count.cpp
)
target_link_libraries(benchmark_triangle_count graph_engine)