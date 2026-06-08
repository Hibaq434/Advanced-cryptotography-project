# fig4_rc4.py

def rc4(key, data):
    # Key Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    keystream = []
    for _ in range(len(data)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)

    # Encrypt/Decrypt
    return [ord(d) ^ k for d, k in zip(data, keystream)]

# Example usage
key = "SECRET"
plaintext = "STREAMCIPHER DEMO"

# Encrypt
cipher_bytes = rc4(key, plaintext)
print("Plaintext:", plaintext)
print("Ciphertext (bytes):", cipher_bytes)

# Decrypt (apply RC4 again on ciphertext)
decrypted_bytes = rc4(key, ''.join(chr(b) for b in cipher_bytes))
decrypted_text = ''.join(chr(b) for b in decrypted_bytes)

print("Decrypted:", decrypted_text.encode("utf-8", "replace").decode("utf-8"))
