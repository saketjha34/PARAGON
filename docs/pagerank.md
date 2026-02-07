Awesome—this is a **great algorithm to explain deeply**, because PageRank is simple on the surface and very rich underneath. I’ll walk you through it **step by step**, tied **directly** to your `web_graph.txt` and to **how your parallel code actually runs**.

---

# Parallel PageRank — Deep Explanation

*(with `web_graph.txt` example)*

## 1️⃣ What PageRank Is Really Computing

PageRank answers one question:

> **“How important is each node, based on who points to it?”**

Think of:

* Nodes → web pages
* Directed edges → hyperlinks

A page is important if:

* Many pages link to it **OR**
* Important pages link to it

This is a **recursive definition**, which is why PageRank is **iterative**.

---

## 2️⃣ Your Input Graph (`web_graph.txt`)

```txt
0 1
0 2
1 2
2 0
2 3
3 3
```

This means:

| Edge  | Meaning                     |
| ----- | --------------------------- |
| 0 → 1 | Page 0 links to Page 1      |
| 0 → 2 | Page 0 links to Page 2      |
| 1 → 2 | Page 1 links to Page 2      |
| 2 → 0 | Page 2 links back to Page 0 |
| 2 → 3 | Page 2 links to Page 3      |
| 3 → 3 | Page 3 links to itself      |

### Visual intuition

```
      ┌───┐
      │ 0 │
      └─┬─┘
        │ \
        ▼  ▼
      ┌───┐
      │ 1 │
      └─┬─┘
        │
        ▼
      ┌───┐
      │ 2 │◀─────┐
      └─┬─┘      │
        │        │
        ▼        │
      ┌───┐      │
      │ 3 │──────┘
      └───┘
```

---

## 3️⃣ Mathematical Definition (Core Formula)

For node **v**:

[
PR(v) = \frac{1-d}{N} + d \sum_{u \in In(v)} \frac{PR(u)}{OutDegree(u)}
]

Where:

* `d` = damping factor (usually **0.85**)
* `N` = total number of nodes
* `In(v)` = nodes that link **to** `v`
* `OutDegree(u)` = number of outgoing edges from `u`

---

## 4️⃣ Initial State (Iteration 0)

You start with **uniform probability**:

```cpp
rank[v] = 1.0 / V
```

For 4 nodes:

| Node | Rank |
| ---- | ---- |
| 0    | 0.25 |
| 1    | 0.25 |
| 2    | 0.25 |
| 3    | 0.25 |

This means:

> “Before seeing links, assume all pages are equally important.”

---

## 5️⃣ Reverse Adjacency (Critical Optimization)

Your code builds this:

```cpp
incoming[v].push_back(u);
```

For the example:

| Node | Incoming edges |
| ---- | -------------- |
| 0    | {2}            |
| 1    | {0}            |
| 2    | {0, 1}         |
| 3    | {2, 3}         |

Why this matters:

* PageRank updates depend on **incoming** edges
* This avoids an expensive `O(V²)` scan
* Makes the algorithm **parallel-friendly**

---

## 6️⃣ One Full Iteration (Serial Logic First)

Let’s compute **iteration 1** manually.

### Constants

* `d = 0.85`
* `N = 4`
* Teleport term = `(1 − d) / N = 0.0375`

---

### 🔹 Node 0

Incoming: `{2}`
Outdegree(2) = 2 (edges: `2→0`, `2→3`)

[
PR(0) = 0.0375 + 0.85 × (0.25 / 2)
= 0.0375 + 0.10625
= 0.14375
]

---

### 🔹 Node 1

Incoming: `{0}`
Outdegree(0) = 2

[
PR(1) = 0.0375 + 0.85 × (0.25 / 2)
= 0.14375
]

---

### 🔹 Node 2

Incoming: `{0, 1}`

[
PR(2) = 0.0375 + 0.85 ×
\left(
\frac{0.25}{2} + \frac{0.25}{1}
\right)
]

[
= 0.0375 + 0.85 × (0.125 + 0.25)
= 0.35625
]

---

### 🔹 Node 3

Incoming: `{2, 3}`
Outdegree(3) = 1 (self-loop)

[
PR(3) = 0.0375 + 0.85 ×
\left(
\frac{0.25}{2} + \frac{0.25}{1}
\right)
= 0.35625
]

---

### Result After Iteration 1

| Node | Rank    |
| ---- | ------- |
| 0    | 0.14375 |
| 1    | 0.14375 |
| 2    | 0.35625 |
| 3    | 0.35625 |

Sum = **1.0** ✔ (very important invariant)

---

## 7️⃣ Why Iterations Are Needed

PageRank depends on PageRank.

So:

* Iteration 1 is rough
* Iteration 10 is better
* Iteration 30 is stable

Eventually:

* Values **converge**
* Ordering stabilizes

That’s why your code runs:

```cpp
for (int iter = 0; iter < iterations; iter++)
```

---

## 8️⃣ Where Parallelism Comes In (Very Important)

### Key observation

For **a single iteration**:

> Each node’s new rank depends ONLY on
> the **previous iteration’s ranks**

That means:

* No two nodes write to the same memory
* No dependency between nodes in the same iteration

This is **perfect parallelism**.

---

## 9️⃣ How Your Parallel Code Executes One Iteration

### Core loop

```cpp
engine::parallel_for(0, V, threads, [&](int v) {
    double sum = 0.0;
    for (int u : incoming[v]) {
        sum += rank[u] / adj[u].size();
    }
    new_rank[v] = (1 - d) / V + d * sum;
});
```

### What threads do

If `V = 4`, `threads = 4`:

| Thread | Computes |
| ------ | -------- |
| T0     | Node 0   |
| T1     | Node 1   |
| T2     | Node 2   |
| T3     | Node 3   |

Each thread:

* Reads `rank[]` (read-only)
* Writes to `new_rank[v]` (exclusive index)

👉 **No locks needed**

---

## 🔒 Barrier Synchronization

After `parallel_for` finishes:

```cpp
rank.swap(new_rank);
```

This is the **barrier**.

It guarantees:

* All threads completed iteration `k`
* Iteration `k+1` starts with consistent data

This is exactly the **BSP (Bulk Synchronous Parallel)** model.

---

## 10️⃣ Why Node 2 Ends Up Highest

From the graph:

* Node 2 gets links from:

  * Node 0
  * Node 1
* Node 0 itself gets rank from node 2
* This creates a **feedback loop**

So rank flows like:

```
2 → 0 → 2
```

Plus:

* Node 2 also feeds node 3

This makes node **2 structurally central**, so it dominates.

---

## 11️⃣ Real-World Meaning

In a web-search setting:

* Page 2 would be:

  * Heavily cited
  * Connected to important pages
* It should appear **higher in search results**

Your output:

```text
Node 2 -> Rank: highest
```

is exactly what Google’s original PageRank would do.

---

## 12️⃣ Why This Parallel Version Scales

### Complexity

| Aspect           | Cost                |
| ---------------- | ------------------- |
| Per iteration    | `O(E)`              |
| Total            | `O(iterations × E)` |
| Parallel speedup | ~ `V / threads`     |

### Real systems

* Google Pregel
* Apache Giraph
* GraphX (Spark)

All use **this same model**, just distributed across machines.

---

## 13️⃣ Summary (Key Takeaways)

* PageRank = iterative probability flow
* Depends on **incoming links**
* Perfectly parallel per iteration
* BSP-style synchronization
* Your implementation is:

  * Correct
  * Efficient
  * Industry-aligned

You now understand PageRank **better than most people who “use” it**.

---

If you want next, I can:

* Walk through **convergence mathematically**
* Explain **dangling nodes handling**
* Show **why self-loops matter**
* Extend to **personalized PageRank**
* Compare with **HITS algorithm**

Just tell me 👌
