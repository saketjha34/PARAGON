Installation Guide
==================

This guide explains how to install **PARAGON**, including system requirements,
platform-specific setup, and a quick start example.

PARAGON is a hybrid **C++ + Python** library. While most users can install it
directly via pip, some environments (especially Windows) may require build tools.


Requirements
------------

**Python**
~~~~~~~~~~

- Python **3.9 – 3.11** (recommended: **3.11**)

.. note::

   Python 3.12+ may work but is not officially tested for all builds.

    **Core Dependencies**

    - C++ compiler (GCC / Clang / MSVC)
    - CMake (>= 3.16)
    - Ninja (recommended for faster builds)

.. warning::

   If prebuilt wheels are not available for your platform, PARAGON will be built
   from source during installation. Ensure all build tools are installed.


Installation via pip (Recommended)
---------------------------------

Install directly from PyPI:

.. code-block:: bash

   pip install paragon-engine

.. note::

   This will automatically download a prebuilt wheel if available.
   Otherwise, it will build the package from source.


Platform-Specific Setup
-----------------------

Linux (Ubuntu / Debian)
~~~~~~~~~~~~~~~~~~~~~~~

Install required system dependencies:

.. code-block:: bash

   sudo apt update
   sudo apt install -y build-essential cmake ninja-build

Then install PARAGON:

.. code-block:: bash

   pip install paragon-engine


macOS
~~~~~

Install dependencies using Homebrew:

.. code-block:: bash

   brew install cmake ninja

Ensure Xcode Command Line Tools are installed:

.. code-block:: bash

   xcode-select --install

Then install PARAGON:

.. code-block:: bash

   pip install paragon-engine


Windows
~~~~~~~

Windows requires a proper C++ build environment.

**Step 1: Install Build Tools**

Download and install:

https://visualstudio.microsoft.com/visual-cpp-build-tools/

During installation, select:

- ✔ Desktop development with C++
- ✔ MSVC compiler
- ✔ Windows SDK
- ✔ CMake tools for Windows

.. warning::

   Missing any of the above components may cause build failures during installation.


**Step 2: Install Python dependencies**

.. code-block:: bash

   pip install --upgrade pip
   pip install cmake ninja pybind11


**Step 3: Install PARAGON**

.. code-block:: bash

   pip install paragon-engine


.. note::

   On Windows, it is recommended to use the **x64 Native Tools Command Prompt**
   for best compatibility.


Verify Installation
-------------------

You can verify that PARAGON is installed correctly:

.. code-block:: python

    from paragon import Graph
    from paragon.algorithms import parallel_bfs, parallel_dfs

    NUM_THREADS = 4

    g = Graph(5)
    g.add_edges([
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4)
    ])

    distance = parallel_bfs(graph=g, source=0, threads=NUM_THREADS)
    print(distance)

    visited = parallel_dfs(graph=g, source=0, threads=NUM_THREADS)
    print(visited)

Expected output:

.. code-block:: text

    [0, 1, 2, 3, 4]
    [True, True, True, True, True]


Quick Start
-----------

Here is a simple example using PARAGON:

.. code-block:: python

    from paragon import WeightedGraph
    from paragon.algorithms import parallel_dijkstra

    g = WeightedGraph(6)

    g.add_edges([
        (0, 1, 4.0),
        (0, 2, 2.0),
        (1, 3, 5.0),
        (2, 1, 1.0),
        (2, 3, 8.0),
        (3, 4, 3.0),
        (4, 5, 1.0)
    ])

    dist = parallel_dijkstra(g, 0)

    for i, d in enumerate(dist):
        print(f"Distance from 0 → {i}: {d}")


Stable Release
--------------

The latest stable release is available on PyPI:

https://pypi.org/project/paragon-engine/

Install the latest version:

.. code-block:: bash

   pip install paragon-engine

To install a specific version:

.. code-block:: bash

   pip install paragon-engine==0.1.9


Troubleshooting
---------------

**1. Build errors during installation**

Ensure the following are installed:

- CMake (>= 3.16)
- C++ compiler
- Ninja


**2. Import errors**

.. code-block:: text

   ModuleNotFoundError: paragon

Fix by reinstalling:

.. code-block:: bash

   pip install --force-reinstall paragon-engine


**3. CMake not found**

Install via pip:

.. code-block:: bash

   pip install cmake


**4. Windows-specific issues**

- Use Visual Studio Build Tools
- Run installation in Developer Command Prompt


.. tip::

   If you encounter issues, please open an issue on GitHub with logs and system details.