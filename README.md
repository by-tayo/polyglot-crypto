# Polyglot-Crypto: AES & RSA Implementations

## Overview
This repository provides a ground-up implementation of the Advanced Encryption Standard (AES) and Rivest-Shamir-Adleman (RSA) algorithms across five programming languages: Python, C, Go, Java, and JavaScript. The implementation supports core cryptographic operations without relying on external dependencies, providing insights into the algorithm's mechanics. 

## Features
* **AES Encryption/Decryption:** Contains helper functions for XOR operations, byte substitution, shifting rows, mixing columns, and key scheduling.
* **RSA Encryption/Decryption:** Implements the three main stages of RSA: Key Generation, Encryption, and Decryption. 
* **Polyglot Consistency:** Validates internal logic across all languages using a shared `test-vectors.json` file.

## Prerequisites
* **C:** GCC Compiler (`gcc` or `g++`)
* **Python:** Python 3.x
* **Go:** Go 1.18+
* **Java:** JDK 21+
* **JavaScript:** Node.js

## Implementation Structure

### AES Base
Defines core AES operations and serves as a base class/module for AES encryption and decryption implementations.
* `SubBytes()`: Non-linear byte substitution.
* `ShiftRows()`: Cyclical shifting of the state matrix.
* `MixColumns()`: Galois Field $GF(2^8)$ multiplication.
* `AddRoundKey()`: Bitwise XOR of the state with the current round key.

### RSA Base
Implements the RSA (Rivest–Shamir–Adleman) algorithm, a popular asymmetric encryption and decryption method.
* `generate_keys(p, q)`: Handles the Key Generation stage.
* `encrypt(message)`: Encrypts the data using the Public Key to get the ciphertext.
* `decrypt(ciphertext)`: Decrypts the ciphertext using the Private Key to get the original data.

## Algorithm Explanation

### RSA Algorithm
The RSA algorithm is based on the factorization of large numbers and modular arithmetic. It involves the following steps:
1. **Key Generation:** 
   * Choose two large prime numbers, $p$ and $q$.
   * Calculate their product, $n = p \times q$.
   * Calculate the totient function $\Phi(n) = (p - 1) \times (q - 1)$.
   * Choose an encryption exponent $e$ such that $1 < e < \Phi(n)$ and $e$ is co-prime with $\Phi(n)$.
   * Calculate the decryption exponent $d$ such that $(d \times e) \equiv 1 \pmod{\Phi(n)}$.
2. **Encryption:** The message $M$ is transformed into ciphertext $C$ using the formula $C = M^e \pmod n$ with the public key.
3. **Decryption:** The ciphertext is then converted back into the plaintext message using $M = C^d \pmod n$ with the private key.

## 📂 Repo Structure
```
.
├── .devcontainer/         # Codespaces universal environment config
├── shared/                # Standardized JSON test cases for AES and RSA (including intermediate states)
├── scripts/               # BASH automation (e.g., run_all_tests.sh)
├── python/                # Python implementations and unittests
├── c/                     # C source files and GCC Makefiles
├── go/                    # Go modules and _test.go files
├── java/                  # Java source and JUnit tests
└── javascript/            # Node.js implementation and Jest tests
```
## Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/yourusername/polyglot-crypto.git](https://github.com/yourusername/polyglot-crypto.git)
cd polyglot-crypto
```

### 2. Example: C Implementation
Compile the AES/RSA library and your program:

```bash
cd c/
gcc -c aes_core.c
gcc main.c aes_core.o -o main
./main
```

3. Example: Python Implementation

Navigate to the Python directory to execute the code.
Run the script directly using Python 3.

```bash
cd python/
python3 main.py
```

4. Example: Go Implementation

Initialize the Go module to handle the package dependencies.
Run the main Go file directly.

```bash

cd go/
go mod init polyglot-crypto
go run main.go
```

5. Example: Java Implementation

Navigate to your Java source folder to compile the files.
Compile using javac and run the resulting class file.

```bash
cd java/
javac Main.java
java Main
```

6. Example: JavaScript (Node.js) Implementation

Initialize npm to create your package configuration.
Run the script using the Node environment.

```bash
cd javascript/
npm init -y
node main.js
```
