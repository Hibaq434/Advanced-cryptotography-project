# fig5_performance.py

import time

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
plaintext = "STREAMCIPHER DEMO" * 1000  # longer text for performance test

# Measure encryption time
start = time.time()
cipher_bytes = rc4(key, plaintext)
enc_time = time.time() - start

# Measure decryption time
start = time.time()
decrypted_bytes = rc4(key, ''.join(chr(b) for b in cipher_bytes))
dec_time = time.time() - start

decrypted_text = ''.join(chr(b) for b in decrypted_bytes)

print("Plaintext length:", len(plaintext))
print("Encryption time: {:.6f} seconds".format(enc_time))
print("Decryption time: {:.6f} seconds".format(dec_time))
print("Decrypted matches plaintext:", decrypted_text == plaintext)
