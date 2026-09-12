import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println("=== Running Polyglot Crypto Test Suite (Java) ===");

        Path path = Path.of("../shared/test-vectors.json");
        if (!Files.exists(path)) {
            path = Path.of("shared/test-vectors.json");
        }

        String json = Files.readString(path);

        // Parse AES arrays with regex to avoid external JSON dependencies
        int[] key = extractIntArray(json, "key");
        int[] plaintext = extractIntArray(json, "plaintext");
        int[] expectedCiphertext = extractIntArray(json, "ciphertext");

        AES aes = new AES(key);
        int[] ciphertext = aes.encrypt(plaintext);

        if (Arrays.equals(ciphertext, expectedCiphertext)) {
            System.out.println("[PASS] AES-128 Encryption matches test vectors.");
        } else {
            System.out.println("[FAIL] AES-128 Encryption mismatch!");
            System.exit(1);
        }

        // Parse RSA fields
        long n = extractLong(json, "n");
        long e = extractLong(json, "public_exponent");
        long d = extractLong(json, "private_exponent");
        long pt = extractLong(json, "plaintext_int");
        long expectedCt = extractLong(json, "ciphertext_int");

        long ct = RSA.encrypt(pt, e, n);
        long decrypted = RSA.decrypt(ct, d, n);

        if (ct == expectedCt && decrypted == pt) {
            System.out.println("[PASS] RSA-Basic Encryption & Decryption match test vectors.");
        } else {
            System.out.println("[FAIL] RSA-Basic test vector mismatch!");
            System.exit(1);
        }

        System.out.println("\n=== Test Suite Complete ===");
    }

    private static int[] extractIntArray(String json, String keyName) {
        Pattern pattern = Pattern.compile("\"" + keyName + "\"\\s*:\\s*\\[([^\\]]+)\\]");
        Matcher matcher = pattern.matcher(json);
        if (!matcher.find()) throw new IllegalArgumentException("Key not found: " + keyName);
        String[] parts = matcher.group(1).split(",");
        int[] arr = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i].trim());
        }
        return arr;
    }

    private static long extractLong(String json, String keyName) {
        Pattern pattern = Pattern.compile("\"" + keyName + "\"\\s*:\\s*(\\d+)");
        Matcher matcher = pattern.matcher(json);
        if (!matcher.find()) throw new IllegalArgumentException("Field not found: " + keyName);
        return Long.parseLong(matcher.group(1));
    }
}