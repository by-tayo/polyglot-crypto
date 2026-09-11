#include <stdio.h>
#include <string.h>
#include <stdint.h>

// A zero-dependency, naive JSON extractor tailored to our specific format
void extract_aes_array(const char* filepath, const char* target_key, uint8_t* array_out) {
    FILE *file = fopen(filepath, "r");
    if (!file) {
        printf("Error: Could not open %s\n", filepath);
        return;
    }

    // Read the file into a buffer
    char buffer[2048];
    size_t bytes_read = fread(buffer, 1, sizeof(buffer) - 1, file);
    buffer[bytes_read] = '\0'; 
    fclose(file);

    // Format our search string, e.g., "\"key\": ["
    char search_str[64];
    snprintf(search_str, sizeof(search_str), "\"%s\": [", target_key);

    // Locate the start of the array
    char *ptr = strstr(buffer, search_str);
    if (ptr) {
        ptr += strlen(search_str); // Move pointer past the bracket
        
        for (int i = 0; i < 16; i++) {
            // Parse the integer value
            unsigned int val;
            sscanf(ptr, "%u", &val);
            array_out[i] = (uint8_t)val;
            
            // Fast-forward to the next comma
            ptr = strchr(ptr, ',');
            if (ptr) ptr++; // Skip the comma for the next loop iteration
        }
    }
}