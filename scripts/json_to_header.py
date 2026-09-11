import json
import os

def generate_c_header():
    json_path = os.path.join("..", "shared", "test-vectors.json")
    header_path = os.path.join("..", "c", "src", "test_vectors.h")
    
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    with open(header_path, 'w') as f:
        f.write("#ifndef TEST_VECTORS_H\n#define TEST_VECTORS_H\n\n")
        f.write("#include <stdint.h>\n\n")
        
        # Convert AES arrays to C static constants
        aes = data["aes_128"]
        for key, val in aes.items():
            hex_vals = ", ".join([f"0x{v:02x}" for v in val])
            f.write(f"static const uint8_t aes_tv_{key}[16] = {{ {hex_vals} }};\n")
            
        f.write("\n#endif // TEST_VECTORS_H\n")
        
    print(f"Successfully generated {header_path}")

if __name__ == "__main__":
    generate_c_header()