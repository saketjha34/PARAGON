#include <bits/stdc++.h>
using namespace std;

#include "test_registry.hpp"
#include "test_framework.hpp"

int main() {
    cout << "===== RUNNING ALL UNIT TESTS =====\n\n";

    int passed = 0, failed = 0;

    for (auto& [name, testFunc] : getTestRegistry()) {
        try {
            testFunc();
            cout << "[PASS] " << name << "\n";
            passed++;
        } catch (const exception& e) {
            cout << "[FAIL] " << name << " : " << e.what() << "\n";
            failed++;
        }
    }

    cout << "\n===== TEST SUMMARY =====\n";
    cout << "Passed: " << passed << "\n";
    cout << "Failed: " << failed << "\n";

    return failed == 0 ? 0 : 1;
}