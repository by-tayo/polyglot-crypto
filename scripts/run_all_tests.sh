#!/bin/bash
set -e

echo "=== Running Polyglot Crypto Test Suite ==="

# 1. Python
echo "Running Python tests..."
cd python && python3 test_runner.py && cd ..

# 2. C
echo "Running C tests..."
cd c && make clean && make test && cd ..

# 3. Go
echo "Running Go tests..."
cd go && go run src/main.go src/aes.go src/rsa.go && cd ..

# 4. JavaScript
echo "Running JavaScript tests..."
cd javascript && node test_runner.js && cd ..

# 5. Java
echo "Running Java tests..."
cd java && javac -d bin src/*.java && java -cp bin Main && rm -rf bin && cd ..

echo "=== All 5 Polyglot Language Suites Passed Successfully ==="