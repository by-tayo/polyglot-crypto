#ifndef RSA_CORE_H
#define RSA_CORE_H

#include <stdint.h>

// Modular exponentiation: (base^exp) % mod using 64-bit intermediates to prevent overflow
uint64_t mod_pow(uint64_t base, uint64_t exp, uint64_t mod);

// Core RSA operations
uint64_t rsa_encrypt(uint64_t message, uint64_t e, uint64_t n);
uint64_t rsa_decrypt(uint64_t ciphertext, uint64_t d, uint64_t n);

#endif // RSA_CORE_H