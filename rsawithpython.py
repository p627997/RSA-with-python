import rsa

# Generate public and private keys
publickey, privatekey = rsa.newkeys(2048)

# Plain or Original text
plaintext = "Test"

# Encrypt the message using the public key
def encrypt(plaintext):
    ciphertext = rsa.encrypt(plaintext.encode(), publickey)
    return ciphertext

# Decrypt the encrypted message using the private key
def decrypt(ciphertext):
    decrypted_text = rsa.decrypt(ciphertext, privatekey).decode()
    return decrypted_text

print("Original Text: ", plaintext) # It original text - "Test"
print("Encrypted Text: ", encrypt(plaintext)) # It will return byte object
print("Decrypted Text: ", decrypt(encrypt(plaintext))) # It will return original text - "Test"
