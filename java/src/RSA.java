import java.math.BigInteger;

public class RSA {
    public static long encrypt(long message, long e, long n) {
        BigInteger m = BigInteger.valueOf(message);
        BigInteger exp = BigInteger.valueOf(e);
        BigInteger mod = BigInteger.valueOf(n);
        return m.modPow(exp, mod).longValue();
    }

    public static long decrypt(long ciphertext, long d, long n) {
        BigInteger c = BigInteger.valueOf(ciphertext);
        BigInteger exp = BigInteger.valueOf(d);
        BigInteger mod = BigInteger.valueOf(n);
        return c.modPow(exp, mod).longValue();
    }
}