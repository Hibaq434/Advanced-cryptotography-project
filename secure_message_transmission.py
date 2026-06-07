# fig4_secure_message_transmission.py

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Step 1: Generate RSA key pair (recipient)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Step 2: Sender encrypts message with recipient's public key
message = b"SECURE TRANSMISSION DEMONSTRATION"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Sender's Original Message:", message.decode())
print("Ciphertext (bytes preview):", ciphertext[:64], "...")

# Step 3: Recipient decrypts message with private key
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Recipient's Decrypted Message:", decrypted.decode())
