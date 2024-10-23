def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Shift within the bounds of the alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetical characters remain unchanged
    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)  # Decrypting is just reversing the shift


if __name__ == "__main__":
    # Example usage
    plaintext = "Hello, World!"
    shift = 3
    
    print("Original Plaintext:", plaintext)
    
    # Encrypt the plaintext
    encrypted = caesar_encrypt(plaintext, shift)
    print("Encrypted Text:", encrypted)
    
    # Decrypt the ciphertext
    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted Text:", decrypted)
