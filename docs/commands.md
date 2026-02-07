Perfect 👍
Below is a **clean, copy-paste ready `.md` file** that documents **all commands** for:

* running **examples**
* running **unit tests**
* compiling individual algorithms
* common fixes / tips (Windows + MinGW)

You can name this file something like:

```
COMMANDS.md
```

or merge it later into `README.md`.

---

# 📄 `COMMANDS.md`

## Parallel Graph Engine – Build & Run Commands

This document lists **all commonly used commands** to build and run the project on **Windows (MinGW / g++)**.

All commands assume you are in the **project root directory**:

```text
Parallel Graph Engine/
```

---

## 🔧 Prerequisites

* **MinGW-w64 (g++)**
* C++17 or newer

Check installation:

```bash
g++ --version
```

---

## 📁 Folder Overview (Relevant)

```text
include/     → headers (.hpp)
src/         → implementations (.cpp)
examples/    → usage examples
tests/       → unit tests + test runner
```

---

## 🧪 Running Unit Tests (ALL at once)

This builds **all tests** and **all source files**, then runs them using the custom test runner.

### 🔹 Compile tests

```bash
g++ -std=gnu++17 tests/*.cpp src/*.cpp -o run_tests
```

### 🔹 Run tests

```bash
./run_tests
```

### ✅ Expected output

```text
[PASS] Graph Constructors
[PASS] Parallel BFS Basic
[PASS] Parallel DFS Basic
[PASS] PageRank Basic Cycle
[PASS] PageRank BFS Cycle
...
```

---

## 🚀 Running Examples

### 1️⃣ Parallel BFS (file-based graph)

Uses:

```
examples/web_graph.txt
```

#### Compile

```bash
g++ examples/parallel_bfs.cpp src/*.cpp -o bfs_example
```

#### Run

```bash
bfs_example
```

---

### 2️⃣ Parallel DFS

#### Compile

```bash
g++ -std=gnu++17 -Iinclude examples/parallel_dfs.cpp src/*.cpp -o dfs_example
```

#### Run

```bash
dfs_example
```

---

### 3️⃣ PageRank (Pull-based, file-based graph)

#### Compile

```bash
g++ -std=gnu++17 -Iinclude examples/pagerank.cpp src/*.cpp -o pagerank_example
```

#### Run

```bash
pagerank_example
```

---

### 4️⃣ PageRank (BFS-style / Push-based)

If you later add a dedicated example file:

```bash
g++ -std=gnu++17 -Iinclude examples/pagerank_bfs.cpp src/*.cpp -o pagerank_bfs_example
pagerank_bfs_example
```

---

## 🧩 Running a Single Test File (Optional)

If you want to run **only one test file** (for debugging):

```bash
g++ -std=gnu++17 -Iinclude tests/test_pagerank.cpp src/*.cpp -o test_pagerank
test_pagerank
```

---

## ⚠️ Common Errors & Fixes

### ❌ Undefined reference (linker error)

**Cause:** `.cpp` file not linked
**Fix:** Always include `src/*.cpp`

```bash
g++ examples/parallel_bfs.cpp src/*.cpp -o bfs_example
```

---

### ❌ Multiple definition error

**Cause:** Function implemented in both `src/` and `examples/`
**Rule:**

* `src/` → implementations
* `examples/` → usage only

---

### ❌ `bits/stdc++.h` not found

* Works with **MinGW / GCC**
* ❌ Not supported by MSVC

---

## 🛠 Recommended Compile Flags

```bash
-std=gnu++17   # C++ standard
-Iinclude      # include directory
-O2            # optimization (optional)
```

Example:

```bash
g++ -O2 -std=gnu++17 -Iinclude examples/parallel_bfs.cpp src/*.cpp -o bfs_example
```

---

## 🧠 Notes for Contributors

* Always run tests before adding new algorithms
* Keep implementations in `src/`
* Add examples in `examples/`
* Register new tests using `REGISTER_TEST`

---

## ✅ Quick Command Summary

| Task             | Command                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| Run all tests    | `g++ -std=gnu++17 -Iinclude tests/*.cpp src/*.cpp -o run_tests && run_tests`     |
| BFS example      | `g++ -std=gnu++17 -Iinclude examples/parallel_bfs.cpp src/*.cpp -o bfs_example`  |
| DFS example      | `g++ -std=gnu++17 -Iinclude examples/parallel_dfs.cpp src/*.cpp -o dfs_example`  |
| PageRank example | `g++ -std=gnu++17 -Iinclude examples/pagerank.cpp src/*.cpp -o pagerank_example` |

---

If you want next, I can:

* Merge this into a **full README.md**
* Add **CMake commands**
* Add **Linux/macOS commands**
* Add **benchmark commands**
* Add **CI-style test commands**

Just tell me 👍