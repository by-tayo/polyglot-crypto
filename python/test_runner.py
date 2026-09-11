import json
import os
from aes_core import AES
from rsa_core import RSA

def run_tests():
    # Locate the shared test vectors file relative to the script
    vector_path = os.path.join("..", "shared", "test-vectors.json")
    if not os.path.exists(vector_path):
        vector_path = "shared/test-vectors.json" # Fallback if run from root

    with open(vector_path, "r") as f:
        vectors = json.load(f)

    print("=== Running Polyglot Crypto Test Suite (Python) ===\n")

    # 1. Test AES-128
    aes_data = vectors["aes_128"]
    key = bytes(aes_data["key"])
    plaintext = bytes(aes_data["plaintext"])
    expected_ciphertext = bytes(aes_data["ciphertext"])

    aes = AES(key)
    ciphertext = aes.encrypt(plaintext)

    if ciphertext == expected_ciphertext:
        print("[PASS] AES-128 Encryption matches test vectors.")
    else:
        print("[FAIL] AES-128 Encryption mismatch!")

    # 2. Test RSA
    rsa_data = vectors["rsa_basic"]
    n = rsa_data["n"]
    e = rsa_data["public_exponent"]
    d = rsa_data["private_exponent"]
    pt = rsa_data["plaintext_int"]
    expected_ct = rsa_data["ciphertext_int"]

    ct = RSA.encrypt(pt, e, n)
    decrypted = RSA.decrypt(ct, d, n)

    if ct == expected_ct and decrypted == pt:
        print("[PASS] RSA-Basic Encryption & Decryption match test vectors.")
    else:
        print("[FAIL] RSA-Basic test vector mismatch!")

    print("\n=== Test Suite Complete ===")

if __name__ == "__main__":
    run_tests()