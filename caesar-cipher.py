# caesar_cipher.py

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

# Example usage
plaintext = "HELLO CYBERSECURITY ENTHUSIAST"
shift = 3

ciphertext = caesar_encrypt(plaintext, shift)
decrypted = caesar_decrypt(ciphertext, shift)

print("Plaintext:", plaintext)
print("Shift:", shift)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
