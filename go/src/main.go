package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"os"
)

type TestVectors struct {
	AES128 struct {
		Key        []byte `json:"key"`
		Plaintext  []byte `json:"plaintext"`
		Ciphertext []byte `json:"ciphertext"`
	} `json:"aes_128"`
	RSABasic struct {
		P               uint64 `json:"p"`
		Q               uint64 `json:"q"`
		N               uint64 `json:"n"`
		PublicExponent  uint64 `json:"public_exponent"`
		PrivateExponent uint64 `json:"private_exponent"`
		PlaintextInt    uint64 `json:"plaintext_int"`
		CiphertextInt   uint64 `json:"ciphertext_int"`
	} `json:"rsa_basic"`
}

func main() {
	fmt.Println("=== Running Polyglot Crypto Test Suite (Go) ===")

	filePath := "../shared/test-vectors.json"
	data, err := os.ReadFile(filePath)
	if err != nil {
		filePath = "shared/test-vectors.json"
		data, err = os.ReadFile(filePath)
		if err != nil {
			fmt.Printf("[FAIL] Could not load test-vectors.json: %v\n", err)
			os.Exit(1)
		}
	}

	var vectors TestVectors
	if err := json.Unmarshal(data, &vectors); err != nil {
		fmt.Printf("[FAIL] Could not parse JSON: %v\n", err)
		os.Exit(1)
	}

	// 1. Validate AES-128
	aes, err := NewAESCipher(vectors.AES128.Key)
	if err != nil {
		fmt.Printf("[FAIL] AES Init error: %v\n", err)
		os.Exit(1)
	}

	ciphertext, err := aes.Encrypt(vectors.AES128.Plaintext)
	if err != nil {
		fmt.Printf("[FAIL] AES Encrypt error: %v\n", err)
		os.Exit(1)
	}

	if bytes.Equal(ciphertext, vectors.AES128.Ciphertext) {
		fmt.Println("[PASS] AES-128 Encryption matches test vectors.")
	} else {
		fmt.Println("[FAIL] AES-128 Encryption mismatch!")
		os.Exit(1)
	}

	// 2. Validate RSA
	rsa := vectors.RSABasic
	ct := RSAEncrypt(rsa.PlaintextInt, rsa.PublicExponent, rsa.N)
	pt := RSADecrypt(ct, rsa.PrivateExponent, rsa.N)

	if ct == rsa.CiphertextInt && pt == rsa.PlaintextInt {
		fmt.Println("[PASS] RSA-Basic Encryption & Decryption match test vectors.")
	} else {
		fmt.Println("[FAIL] RSA-Basic test vector mismatch!")
		os.Exit(1)
	}

	fmt.Println("\n=== Test Suite Complete ===")
}