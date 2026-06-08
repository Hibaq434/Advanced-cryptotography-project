# fig5_testing.py

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

# --- Test Cases ---
test_cases = [
    ("DATA PRIVACY IS ESSENTIAL", 5, "PRIVACY"),
    ("SECURE SYSTEM DESIGN", 3, "SYSTEM"),
    ("ENCRYPTION IS POWERFUL", 7, "POWER"),
]

for text, shift, key in test_cases:
    print("\n=== Test Case ===")
    print("Plaintext:", text)

    # Caesar
    caesar_ciphertext = caesar_encrypt(text, shift)
    caesar_decrypted = caesar_decrypt(caesar_ciphertext, shift)
    print("Caesar (Shift={}):".format(shift))
    print("Ciphertext:", caesar_ciphertext)
    print("Decrypted:", caesar_decrypted)

    # Vigenère
    vigenere_ciphertext = vigenere_encrypt(text, key)
    vigenere_decrypted = vigenere_decrypt(vigenere_ciphertext, key)
    print("Vigenère (Key={}):".format(key))
    print("Ciphertext:", vigenere_ciphertext)
    print("Decrypted:", vigenere_decrypted)
