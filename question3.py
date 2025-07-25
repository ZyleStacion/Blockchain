from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Step 1: Generate our key-pair
def generate_key_pair():
    # Generate a private key on the SECP256K1 curve 
    private_key = ec.generate_private_key(ec.SECP256K1())
    # ... and a corresponding public key
    public_key = private_key.public_key()

    # Print an unencrypted version of the private key
    visible_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    # Print the public key in a human-readable format
    visible_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # Print both keys in a human-readable format
    print("\nPrivate Key:")
    print(visible_private_key.decode('utf-8'))
    print("Public Key:")
    print(visible_public_key.decode('utf-8'))

    
    return private_key, public_key

# Step 2: Get user input (converted into bytes)
message = input("Enter a string: ").encode('utf-8')

# Print the original message
print("Message: " + message.decode('utf-8'))

# Step 3: Sign the message using the private key to create a digital signature
def sign_message(private_key, message):
    digital_signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )

    return digital_signature

# Step 4: Verify the signature against the original message

# Run our functions
private_key, public_key = generate_key_pair()
signature = sign_message(private_key, message)

def verify_signature(signature, message, public_key):
    signature = bytes(signature)
    message = bytes(message)
    
    # Print the validation result
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        print("Result: Signature is valid")
    except InvalidSignature:
        print("Result: Signature is invalid")

verify_signature(signature, message, public_key)