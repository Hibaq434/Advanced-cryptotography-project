# fig1_aes.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def aes_encrypt_decrypt(plaintext):
    # Generate a random 256-bit key and 128-bit IV
    key = os.urandom(32)   # 256-bit key
    iv = os.urandom(16)    # 128-bit initialization vector

    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Pad plaintext to block size (16 bytes)
    pad_len = 16 - (len(plaintext) % 16)
    padded_plaintext = plaintext + chr(pad_len) * pad_len

    # Encrypt
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext.encode()) + encryptor.finalize()

    # Decrypt
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted = decrypted_padded[:-decrypted_padded[-1]].decode()

    return key, iv, ciphertext, decrypted

# Example usage
plaintext = "BLOCK CIPHER DEMONSTRATION"
key, iv, ciphertext, decrypted = aes_encrypt_decrypt(plaintext)

print("Plaintext:", plaintext)
print("Key (hex):", key.hex())
print("IV (hex):", iv.hex())
print("Ciphertext (hex):", ciphertext.hex())
print("Decrypted:", decrypted)
