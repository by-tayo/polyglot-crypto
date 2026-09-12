# Polyglot-Crypto: AES & RSA Implementations

A zero-dependency, ground-up reference implementation of core cryptographic primitives (**AES-128** and **RSA**) engineered across **C (C99)**, **Python**, **Go**, **Java**, and **JavaScript**. Every algorithm operates strictly from scratch—avoiding external cryptography libraries—and guarantees cross-language parity via a shared JSON test vector harness.

---

## Features

* **AES-128 (FIPS 197):** Full Substitution-Permutation Network (SPN) implementation including `SubBytes` (S-box over $\text{GF}(2^8)$), `ShiftRows`, `MixColumns` Galois field multiplication, and the 10-round key expansion schedule.
* **RSA (PKCS #1):** Core integer factorization trapdoor operations implementing key generation, relation calculations, and square-and-multiply modular exponentiation for encryption and decryption.
* **Polyglot Parity:** Automated cross-validation across all language environments using a shared, language-agnostic `shared/test-vectors.json` test suite.

---

## Repository Structure

```text
.
├── .devcontainer/         # Universal dev environment configuration
├── shared/
│   └── test-vectors.json  # Standardized JSON test vectors for AES and RSA
├── scripts/
│   └── run_all_tests.sh   # Unified multi-language test automation harness
├── c/                     # C99 source files and strict GCC Makefile
├── python/                # Pure Python modules and test runner
├── go/                    # Go modules and zero-dependency test runner
├── java/                  # JDK 17+ classes and JSON parser
└── javascript/            # Node.js implementations and test runner
```

## Mathematical Foundations

### 1. AES-128 State Transformations
AES processes a 128-bit state matrix ($4 \times 4$ byte grid) across 10 rounds:
* **SubBytes:** Non-linear inversion over Galois Field $\text{GF}(2^8)$ followed by an affine mapping.
* **ShiftRows:** Cyclical left row offsets: row $r$ shifts left by $r$ bytes ($r \in \{0, 1, 2, 3\}$).
* **MixColumns:** Matrix multiplication transforming columns over the polynomial ring $\mathbb{Z}_2[x] / (x^4 + 1)$.
* **AddRoundKey:** Bitwise XOR against round keys generated via the key schedule.

### 2. RSA Modular Arithmetic
RSA derives its security from the computational difficulty of factoring large composite primes in $\mathbb{Z}_n^*$:
* **Key Relations:**
  $$n = p \times q, \quad \phi(n) = (p - 1)(q - 1)$$
  $$\gcd(e, \phi(n)) = 1, \quad d \cdot e \equiv 1 \pmod{\phi(n)}$$
* **Encryption / Decryption:**
  $$C \equiv M^e \pmod n \quad \Longleftrightarrow \quad M \equiv C^d \pmod n$$

---

## Quickstart

### Clone the Repository
```bash
git clone [https://github.com/by-tayo/polyglot-crypto.git](https://github.com/by-tayo/polyglot-crypto.git)
cd polyglot-crypto
```

### Run All Tests (One-Command Verification)

Execute the unified test harness from the root directory to verify all 5 languages in sequence:

```bash
chmod +x scripts/run_all_tests.sh
./scripts/run_all_tests.sh
```

### Individual Language Execution

### C (C99)

```bash
cd c
make clean && make test
```

### Python (3.8+)

```bash
cd python
python3 test_runner.py
```

### Go (1.20+)

```bash
cd go
go run src/main.go src/aes.go src/rsa.go
```

### JavaScript (Node.js)

```bash
cd javascript
node test_runner.js
```

### Java (JDK 21+)

```bash
cd java
javac -d bin src/*.java && java -cp bin Main && rm -rf bin
```
