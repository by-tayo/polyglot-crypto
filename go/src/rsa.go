package main

import "math/big"

// Encrypt computes (message^e) % n
func RSAEncrypt(message, e, n uint64) uint64 {
	m := new(big.Int).SetUint64(message)
	exp := new(big.Int).SetUint64(e)
	mod := new(big.Int).SetUint64(n)

	res := new(big.Int).Exp(m, exp, mod)
	return res.Uint64()
}

// Decrypt computes (ciphertext^d) % n
func RSADecrypt(ciphertext, d, n uint64) uint64 {
	c := new(big.Int).SetUint64(ciphertext)
	exp := new(big.Int).SetUint64(d)
	mod := new(big.Int).SetUint64(n)

	res := new(big.Int).Exp(c, exp, mod)
	return res.Uint64()
}