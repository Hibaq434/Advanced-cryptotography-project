# fig2_key_generation.py

import os

def generate_aes_key_iv():
    # Generate a random 256-bit AES key (32 bytes)
    key = os.urandom(32)
    # Generate a random 128-bit IV (16 bytes)
    iv = os.urandom(16)

    print("Generated AES Key (256-bit):", key.hex())
    print("Generated IV (128-bit):", iv.hex())
    print("Key length:", len(key), "bytes")
    print("IV length:", len(iv), "bytes")

# Example usage
generate_aes_key_iv()
