#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include "rsa_core.h"

int main() {
    printf("--- Polyglot Crypto: RSA Engine Test ---\n\n");

    // Corrected RSA Test Vector Parameters ($61 \times 53 = 3233$)
    uint64_t n = 3233; 
    uint64_t e = 17;
    uint64_t d = 2753;
    uint64_t plaintext = 42;

    printf("Plaintext Message: %" PRIu64 "\n", plaintext);

    uint64_t ciphertext = rsa_encrypt(plaintext, e, n);
    printf("Encrypted Ciphertext: %" PRIu64 "\n", ciphertext);

    uint64_t decrypted = rsa_decrypt(ciphertext, d, n);
    printf("Decrypted Message: %" PRIu64 "\n", decrypted);

    if (decrypted == plaintext) {
        printf("\nRSA Verification Successful!\n");
    } else {
        printf("\nRSA Verification Failed!\n");
    }

    return 0;
}