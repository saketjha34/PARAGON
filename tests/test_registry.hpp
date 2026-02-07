#pragma once
#include <bits/stdc++.h>
using namespace std;

using TestFunc = function<void()>;

// Global registry
inline vector<pair<string, TestFunc>>& getTestRegistry() {
    static vector<pair<string, TestFunc>> tests;
    return tests;
}

// Auto-register macro
#define REGISTER_TEST(test_name, func) static bool _##func##_registered = []() {getTestRegistry().push_back({test_name, func}); return true; }()