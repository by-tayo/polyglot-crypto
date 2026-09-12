class RSA {
  static modPow(base, exponent, modulus) {
    base = BigInt(base);
    exponent = BigInt(exponent);
    modulus = BigInt(modulus);

    let result = 1n;
    base = base % modulus;
    while (exponent > 0n) {
      if (exponent % 2n === 1n) {
        result = (result * base) % modulus;
      }
      exponent /= 2n;
      base = (base * base) % modulus;
    }
    return Number(result);
  }

  static encrypt(message, e, n) {
    return this.modPow(message, e, n);
  }

  static decrypt(ciphertext, d, n) {
    return this.modPow(ciphertext, d, n);
  }
}

module.exports = RSA;