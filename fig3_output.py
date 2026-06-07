# fig3_output.py

# --- Caesar Cipher ---
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# --- Vigenère Cipher ---
def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# --- Example usage ---
plaintext = "DATA PRIVACY IS ESSENTIAL"
caesar_shift = 5
vigenere_key = "PRIVACY"

# Caesar
caesar_ciphertext = caesar_encrypt(plaintext, caesar_shift)
caesar_decrypted = caesar_decrypt(caesar_ciphertext, caesar_shift)

# Vigenère
vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
vigenere_decrypted = vigenere_decrypt(vigenere_ciphertext, vigenere_key)

print("=== Caesar Cipher ===")
print("Plaintext:", plaintext)
print("Shift:", caesar_shift)
print("Ciphertext:", caesar_ciphertext)
print("Decrypted:", caesar_decrypted)

print("\n=== Vigenère Cipher ===")
print("Plaintext:", plaintext)
print("Key:", vigenere_key)
print("Ciphertext:", vigenere_ciphertext)
print("Decrypted:", vigenere_decrypted)
