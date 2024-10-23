# Substitution Cipher (Caesar Cipher)
def caesar_cipher_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Transposition Cipher (Columnar Transposition Cipher)
def columnar_transposition_encrypt(plaintext, key):
    # Create a grid based on the length of the key
    n = len(key)
    grid = [''] * n
    for index, char in enumerate(plaintext):
        grid[index % n] += char
    
    # Sort the columns by the key and concatenate the result
    sorted_grid = [grid[i] for i in sorted(range(n), key=lambda k: key[k])]
    return ''.join(sorted_grid)

# Combine both to create the Product Cipher
def product_cipher_encrypt(plaintext, caesar_shift, transposition_key):
    # Step 1: Apply Caesar Cipher (Substitution)
    substituted_text = caesar_cipher_encrypt(plaintext, caesar_shift)
    
    # Step 2: Apply Columnar Transposition Cipher (Transposition)
    encrypted_text = columnar_transposition_encrypt(substituted_text, transposition_key)
    
    return encrypted_text

# Decryption steps

# Caesar Cipher Decryption
def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Columnar Transposition Cipher Decryption
def columnar_transposition_decrypt(ciphertext, key):
    n = len(key)
    columns = [''] * n
    sorted_key = sorted(range(n), key=lambda k: key[k])
    column_length = len(ciphertext) // n
    
    # Recreate the grid by filling sorted columns
    start = 0
    for i in sorted_key:
        columns[i] = ciphertext[start:start + column_length]
        start += column_length
    
    # Read the characters in the original column order
    decrypted_text = ''
    for i in range(column_length):
        for column in columns:
            if i < len(column):
                decrypted_text += column[i]
    
    return decrypted_text

# Combine both to decrypt the Product Cipher
def product_cipher_decrypt(ciphertext, caesar_shift, transposition_key):
    # Step 1: Reverse Columnar Transposition Cipher
    transposed_text = columnar_transposition_decrypt(ciphertext, transposition_key)
    
    # Step 2: Reverse Caesar Cipher (Substitution)
    decrypted_text = caesar_cipher_decrypt(transposed_text, caesar_shift)
    
    return decrypted_text

# Example usage
plaintext = "HELLOTHISISPRODUCTCIPHER"
caesar_shift = 3  # Shift for Caesar cipher
transposition_key = "312"  # Key for Columnar Transposition Cipher

# Encryption
encrypted_text = product_cipher_encrypt(plaintext, caesar_shift, transposition_key)
print(f"Encrypted Text: {encrypted_text}")

# Decryption
decrypted_text = product_cipher_decrypt(encrypted_text, caesar_shift, transposition_key)
print(f"Decrypted Text: {decrypted_text}")
