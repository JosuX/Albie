import sys

from cryptography.fernet import Fernet

import csv

from script.compression.compress import compress

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def load_key():
    key = b'zap3o2NQDZswqNtQnUB9fYuqSY3RplYNdRkc4f-uL14='
    return key

def encrypt(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
        compressed_data = compress(file_data)
        encrypted_data = f.encrypt(compressed_data)
        file.close()
        return encrypted_data

def decrypt(crypt):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(crypt)
    return decrypted

def encrypt_bytes(crypt):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(crypt)
    return encrypted


