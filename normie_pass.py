import os
import base64

# Define function to check password strength


def check_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digits = any(char.isdigit() for char in password)
    symbols = any(not char.isalnum() for char in password)
    return (length, uppercase, lowercase, digits, symbols)

# Define function to generate random password using all Unicode characters


def generate_password(length):
    password_bytes = os.urandom(length)
    password = base64.b64encode(password_bytes, altchars=None).decode('utf-8')
    return password

# Define function to increase overall entropy via a free random API


def increase_entropy(password):
    # TODO: implement function to increase entropy using a free random API
    return password


# Get password length from user input
while True:
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Generate password
password = generate_password(length)

# Increase overall entropy
password = increase_entropy(password)

# Check password strength
password_length, password_uppercase, password_lowercase, password_digits, password_symbols = check_password_strength(
    password)

# Output results
print(f"\nPassword generated: {password}")
print("Password has been stored in password.txt")
print("\nPassword strength:")
print(f"Length: {password_length}")
print(f"Uppercase letters: {'Yes' if password_uppercase else 'No'}")
print(f"Lowercase letters: {'Yes' if password_lowercase else 'No'}")
print(f"Digits: {'Yes' if password_digits else 'No'}")
print(f"Symbols: {'Yes' if password_symbols else 'No'}")

# Store password in file
with open('password.txt', 'w') as file:
    file.write(password)
