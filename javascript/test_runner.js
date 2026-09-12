const fs = require('fs');
const path = require('path');
const AES = require('./aes');
const RSA = require('./rsa');

console.log("=== Running Polyglot Crypto Test Suite (JavaScript) ===");

let vectorPath = path.join(__dirname, '../shared/test-vectors.json');
if (!fs.existsSync(vectorPath)) {
  vectorPath = path.join(process.cwd(), 'shared/test-vectors.json');
}

const rawData = fs.readFileSync(vectorPath, 'utf8');
const vectors = JSON.parse(rawData);

// 1. Test AES-128
const aesData = vectors.aes_128;
const aes = new AES(aesData.key);
const ct = aes.encrypt(aesData.plaintext);

const aesMatch = ct.length === aesData.ciphertext.length && 
                 ct.every((val, idx) => val === aesData.ciphertext[idx]);

if (aesMatch) {
  console.log("[PASS] AES-128 Encryption matches test vectors.");
} else {
  console.log("[FAIL] AES-128 Encryption mismatch!");
  process.exit(1);
}

// 2. Test RSA
const rsaData = vectors.rsa_basic;
const rsaCt = RSA.encrypt(rsaData.plaintext_int, rsaData.public_exponent, rsaData.n);
const rsaPt = RSA.decrypt(rsaCt, rsaData.private_exponent, rsaData.n);

if (rsaCt === rsaData.ciphertext_int && rsaPt === rsaData.plaintext_int) {
  console.log("[PASS] RSA-Basic Encryption & Decryption match test vectors.");
} else {
  console.log("[FAIL] RSA-Basic test vector mismatch!");
  process.exit(1);
}

console.log("\n=== Test Suite Complete ===");