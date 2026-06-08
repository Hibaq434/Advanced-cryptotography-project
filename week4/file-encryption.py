# fig3_file_encryption.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def encrypt_file(input_file, output_file, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file, "rb") as f:
        plaintext = f.read()

    padded_plaintext = pad(plaintext)
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    with open(output_file, "wb") as f:
        f.write(ciphertext)

def decrypt_file(input_file, output_file, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    with open(input_file, "rb") as f:
        ciphertext = f.read()

    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted = unpad(decrypted_padded)

    with open(output_file, "wb") as f:
        f.write(decrypted)

# Example usage
key = os.urandom(32)  # 256-bit key
iv = os.urandom(16)   # 128-bit IV

# Encrypt file
encrypt_file("sample.txt", "encrypted.bin", key, iv)
print("File encrypted successfully!")

# Decrypt file
decrypt_file("encrypted.bin", "decrypted.txt", key, iv)
print("File decrypted successfully!")
