# fig5_aes_performance.py

import time
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

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

# Create a large test file
with open("large_sample.txt", "wb") as f:
    f.write(os.urandom(5 * 1024 * 1024))  # 5 MB random data

# Measure encryption time
start = time.time()
encrypt_file("large_sample.txt", "encrypted_large.bin", key, iv)
enc_time = time.time() - start

# Measure decryption time
start = time.time()
decrypt_file("encrypted_large.bin", "decrypted_large.txt", key, iv)
dec_time = time.time() - start

print("File size: 5 MB")
print("Encryption time: {:.6f} seconds".format(enc_time))
print("Decryption time: {:.6f} seconds".format(dec_time))
