# fig5_rsa_testing_validation.py

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Step 1: Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Step 2: Define test messages
messages = [
    b"RSA TEST MESSAGE 1",
    b"RSA VALIDATION MESSAGE 2",
    b"SECURE COMMUNICATION DEMO"
]

# Step 3: Encrypt and decrypt each message
for msg in messages:
    ciphertext = public_key.encrypt(
        msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    decrypted = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("\nOriginal Message:", msg.decode())
    print("Ciphertext (bytes preview):", ciphertext[:32], "...")
    print("Decrypted Message:", decrypted.decode())
    print("Validation:", "PASS" if msg == decrypted else "FAIL")
