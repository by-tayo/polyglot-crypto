import json
import os

def generate_test_vectors():
    # FIPS-197 Standard AES-128 Test Vector
    aes_vector = {
        "key": [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c],
        "plaintext": [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34],
        "ciphertext": [0x39, 0x25, 0x84, 0x1d, 0x02, 0xdc, 0x09, 0xfb, 0xdc, 0x11, 0x85, 0x97, 0x19, 0x6a, 0x0b, 0x32],
        "round_1_state": [0x19, 0x3d, 0xe3, 0xbe, 0xa0, 0xf4, 0xe2, 0x2b, 0x9a, 0xc6, 0x8d, 0x2a, 0xe9, 0xf8, 0x48, 0x08]
    }

    # RSA Mathematical Baseline (Using small primes for easy verification)
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = pow(e, -1, phi)
    message = 42
    rsa_ciphertext = pow(message, e, n)

    rsa_vector = {
        "p": p, "q": q, "n": n, "phi": phi,
        "public_exponent": e,
        "private_exponent": d,
        "plaintext_int": message,
        "ciphertext_int": rsa_ciphertext
    }

    # Output to the shared directory
    output_path = os.path.join("..", "shared", "test-vectors.json")
    
    with open(output_path, "w") as f:
        json.dump({"aes_128": aes_vector, "rsa_basic": rsa_vector}, f, indent=4)
        
    print(f"Test vectors successfully written to {output_path}")

if __name__ == "__main__":
    generate_test_vectors()