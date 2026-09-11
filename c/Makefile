CC = gcc
CFLAGS = -Wall -Wextra -std=c99
SRC_DIR = src
OBJ_DIR = obj

# List of source files
SRCS = $(SRC_DIR)/main.c $(SRC_DIR)/aes_core.c $(SRC_DIR)/rsa_core.c $(SRC_DIR)/test_parser.c

# Convert .c source files to .o object files
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

# Executable name
TARGET = main

# Default rule
all: $(TARGET)

# Link the object files to create the executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

# Compile the source files into object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up build artifacts
clean:
	rm -rf $(OBJ_DIR) $(TARGET)

# Run the program
test: all
	./$(TARGET)