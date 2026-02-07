#include <bits/stdc++.h>
using namespace std;

#include "../include/engine.hpp"
#include "test_framework.hpp"
#include "test_registry.hpp"

void test_thread_count() {
    int t = engine::get_thread_count();
    ASSERT_TRUE(t >= 1);
}

void test_parallel_for_sum() {
    vector<int> arr(100, 1);
    atomic<int> sum = 0;

    engine::parallel_for(0, arr.size(), 4, [&](int i) {
        sum += arr[i];
    });

    ASSERT_EQ(sum, 100);
}

REGISTER_TEST("Engine Thread Count", test_thread_count);
REGISTER_TEST("Engine Parallel For", test_parallel_for_sum);