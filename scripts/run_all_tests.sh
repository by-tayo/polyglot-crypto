#!/bin/bash
set -e

echo "=== Running Polyglot Crypto Test Suite ==="

# 1. Run Python tests
echo "Running Python implementation tests..."
cd python && python3 test_runner.py && cd ..

# 2. Run C tests
echo "Running C implementation tests..."
cd c && make clean && make test && cd ..

# 3. Run Go tests
echo "Running Go implementation tests..."
cd go && go run src/main.go src/aes.go src/rsa.go && cd ..

echo "=== All Polyglot Tests Passed Successfully ==="