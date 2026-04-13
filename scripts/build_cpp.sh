#!/usr/bin/env bash

set -e  # Exit on error

# -------- CONFIG --------
BUILD_DIR="build"
BUILD_TYPE="Release"   # Change to Debug if needed
JOBS=$(nproc)          # Auto-detect CPU cores

# -------- STEP 1: Create build directory --------
echo "Creating build directory..."
mkdir -p $BUILD_DIR

# -------- STEP 2: Configure with CMake --------
echo "Configuring project with CMake..."
cmake -S . -B $BUILD_DIR -DCMAKE_BUILD_TYPE=$BUILD_TYPE

# -------- STEP 3: Build --------
echo "Building project using $JOBS cores..."
cmake --build $BUILD_DIR -- -j$JOBS

# -------- DONE --------
echo "Build completed successfully!"