#pragma once
#include <bits/stdc++.h>
using namespace std;

#define TEST_CASE(name) void name()
inline void RUN_TEST(const string& test_name, function<void()> test) {
    try {
        test();
        cout << "[PASS] " << test_name << "\n";
    } catch (const exception& e) {
        cout << "[FAIL] " << test_name << " : " << e.what() << "\n";
    }
}


#define ASSERT_TRUE(cond) if (!(cond)) throw runtime_error("Assertion failed: " #cond)

#define ASSERT_FALSE(cond) if ((cond)) throw runtime_error("Assertion failed: " #cond)

#define ASSERT_EQ(a, b) if ((a) != (b)) { throw runtime_error("Assertion failed: " #a " != " #b); }