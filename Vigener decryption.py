# Function to decrypt Vigenère Cipher
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key = key.lower()
    key_length = len(key)
    alphabet_size = 26
    a_ascii = ord('a')
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():  # Only decrypt alphabetic characters
            offset = ord(key[i % key_length]) - a_ascii  # Key shift
            if char.islower():
                decrypted_char = chr((ord(char) - a_ascii - offset) % alphabet_size + a_ascii)
            else:
                decrypted_char = chr((ord(char) - ord('A') - offset) % alphabet_size + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # Non-alphabet characters stay the same
    
    return ''.join(decrypted_text)

# Example usage
ciphertext = "LXFOPVEFRNHR"
key = "LEMON"
decrypted_message = vigenere_decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)
