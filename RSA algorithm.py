import random

# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Helper function to generate large prime numbers
def generate_large_prime():
    while True:
        prime_candidate = random.randint(100, 999)  # A smaller range for simplicity
        if is_prime(prime_candidate):
            return prime_candidate

# Helper function to find the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute the modular inverse using the Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, y = extended_gcd(e, phi)
    return x % phi

# Key generation: RSA
def rsa_key_generation():
    # Step 1: Generate two large prime numbers p and q
    p = generate_large_prime()
    q = generate_large_prime()
    
    # Step 2: Compute n = p * q
    n = p * q
    
    # Step 3: Compute φ(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Step 4: Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = 65537  # Commonly used public exponent
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    # Step 5: Compute d as the modular inverse of e mod φ(n)
    d = mod_inverse(e, phi_n)
    
    # Public key (e, n) and Private key (d, n)
    return ((e, n), (d, n), p, q)

# Encryption: RSA
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    # Convert plaintext to integer (for simplicity, we assume plaintext is an integer)
    ciphertext = pow(plaintext, e, n)
    return ciphertext

# Decryption: RSA
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    # Decrypt ciphertext back to plaintext integer
    plaintext = pow(ciphertext, d, n)
    return plaintext

# Example usage
if __name__ == "__main__":
    # Key generation
    public_key, private_key, p, q = rsa_key_generation()
    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)
    
    # Example message to encrypt (in integer form)
    message = 42  # Example message (in practice, messages are encoded as integers)
    print("\nOriginal Message:", message)
    
    # Encryption
    ciphertext = rsa_encrypt(message, public_key)
    print("Encrypted Message (Ciphertext):", ciphertext)
    
    # Decryption
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print("Decrypted Message:", decrypted_message)
    
    # Additional Info
    print(f"\nPrime numbers p = {p}, q = {q}")
    print(f"Modulus n = p * q = {public_key[1]}")
    print(f"Totient φ(n) = (p-1) * (q-1) = {(p-1) * (q-1)}")
