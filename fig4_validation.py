# fig4_validation.py

def validate_input(text):
    if not text.strip():
        raise ValueError("Input cannot be empty.")
    if not any(char.isalpha() for char in text):
        raise ValueError("Input must contain alphabetic characters.")
    return text

def validate_key(key):
    if not key.strip():
        raise ValueError("Key cannot be empty.")
    if not key.isalpha():
        raise ValueError("Key must only contain letters.")
    return key.upper()

# Example usage with Caesar Cipher
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

# --- Run Example ---
try:
    plaintext = validate_input("DATA PRIVACY IS ESSENTIAL")
    shift = 5
    ciphertext = caesar_encrypt(plaintext, shift)
    decrypted = caesar_decrypt(ciphertext, shift)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted:", decrypted)

except ValueError as e:
    print("Error:", e)
