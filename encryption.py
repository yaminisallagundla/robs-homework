from cryptography.fernet import Fernet

# Generating a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

data_to_encrypt = b"Aashish Paruvada"

# Encrypting the data
encrypted_data = cipher_suite.encrypt(data_to_encrypt)

print("Original Data:", data_to_encrypt)
print("Encrypted Data:", encrypted_data)

# Decrypting the data
decrypted_data = cipher_suite.decrypt(encrypted_data)

print("Decrypted Data:", decrypted_data.decode())