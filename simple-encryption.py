# simple_encryption.py
from cryptography.fernet import Fernet

# Step 1: Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Step 2: Encrypt a message
plaintext = b"Hello, Advanced Cryptography!"
ciphertext = cipher.encrypt(plaintext)

# Step 3: Decrypt the message
decrypted_text = cipher.decrypt(ciphertext)

# Step 4: Print results
print("Generated Key:", key.decode())
print("Plaintext:", plaintext.decode())
print("Ciphertext:", ciphertext.decode())
print("Decrypted Text:", decrypted_text.decode())
