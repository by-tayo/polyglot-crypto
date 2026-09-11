class RSA:
    @staticmethod
    def encrypt(message: int, e: int, n: int) -> int:
        return pow(message, e, n)

    @staticmethod
    def decrypt(ciphertext: int, d: int, n: int) -> int:
        return pow(ciphertext, d, n)


if __name__ == "__main__":
    print("--- Polyglot Crypto: Python RSA Engine Test ---\n")

    n = 3233
    e = 17
    d = 2753
    plaintext = 42

    print(f"Plaintext Message: {plaintext}")
    
    ciphertext = RSA.encrypt(plaintext, e, n)
    print(f"Encrypted Ciphertext: {ciphertext}")
    
    decrypted = RSA.decrypt(ciphertext, d, n)
    print(f"Decrypted Message: {decrypted}")

    if decrypted == plaintext:
        print("\nRSA Verification Successful!")
    else:
        print("\nRSA Verification Failed!")