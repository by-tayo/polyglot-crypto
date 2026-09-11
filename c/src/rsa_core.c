#include "rsa_core.h"

// Computes (base^exp) % mod safely using square-and-multiply
uint64_t mod_pow(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base = base % mod;
    
    while (exp > 0) {
        if (exp % 2 == 1) {
            res = (__int128)(res * base) % mod; // Use 128-bit casting to prevent overflow during multiplication
        }
        base = (__int128)(base * base) % mod;
        exp /= 2;
    }
    return res;
}

uint64_t rsa_encrypt(uint64_t message, uint64_t e, uint64_t n) {
    return mod_pow(message, e, n);
}

uint64_t rsa_decrypt(uint64_t ciphertext, uint64_t d, uint64_t n) {
    return mod_pow(ciphertext, d, n);
}