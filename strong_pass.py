import os
import base64
import requests
import string

# Generate random password with specified criteria


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    password_characters = []
    if use_uppercase:
        password_characters.extend([c for c in string.ascii_uppercase])
    if use_lowercase:
        password_characters.extend([c for c in string.ascii_lowercase])
    if use_digits:
        password_characters.extend([c for c in string.digits])
    if use_symbols:
        # ASCII printable characters
        password_characters.extend([chr(i) for i in range(33, 127)])
        # All Unicode characters
        password_characters.extend([chr(i) for i in range(161, 1114112)])
    password_bytes = os.urandom(length)
    password = ''.join(
        [password_characters[b % len(password_characters)] for b in password_bytes])
    return password

# Get random bytes from RANDOM.ORG - Byte Generator API


def get_random_bytes(length):
    MAX_BYTES_PER_REQUEST = 1024
    if length <= MAX_BYTES_PER_REQUEST:
        response = requests.get(
            f"https://www.random.org/cgi-bin/randbyte?nbytes={length}&format=h")
        if response.status_code == 200:
            return bytes.fromhex(response.text.strip())
    else:
        password_bytes = bytearray()
        chunks = (length + MAX_BYTES_PER_REQUEST - 1) // MAX_BYTES_PER_REQUEST
        for i in range(chunks):
            chunk_length = min(
                length - i*MAX_BYTES_PER_REQUEST, MAX_BYTES_PER_REQUEST)
            response = requests.get(
                f"https://www.random.org/cgi-bin/randbyte?nbytes={chunk_length}&format=h")
            if response.status_code == 200:
                password_bytes.extend(bytes.fromhex(response.text.strip()))
            else:
                raise Exception(
                    f"Failed to get random bytes. Error code: {response.status_code}")
        return password_bytes

    raise Exception(
        "Failed to get random bytes from RANDOM.ORG - Byte Generator API.")


# Get user input for password criteria
print("Password Generator")
print("------------------")
length = int(input("Enter password length: "))
use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Use digits? (y/n): ").lower() == 'y'
use_symbols = input("Use symbols? (y/n): ").lower() == 'y'

# Generate password
password_bytes = get_random_bytes(length)
password_characters = generate_password(
    length, use_uppercase, use_lowercase, use_digits, use_symbols)
password = ''.join([password_characters[b % len(password_characters)]
                   for b in password_bytes])

# Store password in file
with open('password_str.txt', 'w') as file:
    file.write(password)

print(f"Password generated: {password}")
print("Password has been stored in password_str.txt")
