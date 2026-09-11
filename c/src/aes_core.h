#ifndef AES_CORE_H
#define AES_CORE_H

#include <stdint.h>

// AES-128 uses a 4x4 state matrix of 8-bit bytes
typedef uint8_t state_t[4][4];

// Core AES transformations
void SubBytes(state_t state);
void ShiftRows(state_t state);
void MixColumns(state_t state);
void AddRoundKey(state_t state, const uint8_t* round_key);
void KeyExpansion(const uint8_t *input_key, uint8_t *expanded_key);

#endif // AES_CORE_H