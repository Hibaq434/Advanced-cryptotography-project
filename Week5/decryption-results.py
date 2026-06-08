# fig4_decryption_results.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def unpad(data):
    return data[:-data[-1]]

def decrypt_file(input_file, output_file, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    with open(input_file, "rb") as f:
        ciphertext = f.read()

    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted = unpad(decrypted_padded)

    with open(output_file, "wb") as f:
        f.write(decrypted)

    print("Decryption complete. Output file:", output_file)
    print("Decrypted content preview:")
    print(decrypted.decode(errors="replace"))  # show readable text
