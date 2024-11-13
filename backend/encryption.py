from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

KEY = get_random_bytes(16)  # AES-128 key
IV = get_random_bytes(16)   # Initialization vector

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

def encrypt_text(plain_text):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    padded_text = pad(plain_text)
    encrypted_bytes = cipher.encrypt(padded_text.encode())
    return b64encode(encrypted_bytes).decode()

def decrypt_text(cipher_text):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decoded_bytes = b64decode(cipher_text)
    decrypted_bytes = cipher.decrypt(decoded_bytes)
    return unpad(decrypted_bytes.decode())
