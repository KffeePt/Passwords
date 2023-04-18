import math

# Define function to calculate password strength and crack time


def check_password_strength(file_path):
    # Load password from file
    with open(file_path, 'r') as file:
        password = file.read().strip()

    # Calculate password strength
    length = len(password)
    uppercase = sum(1 for c in password if c.isupper())
    lowercase = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    symbols = sum(1 for c in password if not c.isalnum())
    entropy = math.log2((uppercase + lowercase + digits + symbols) ** length)

    # Calculate time to crack with supercomputer
    crack_time = 2 ** (entropy + math.log2(1000000000)) / 1000000000  # seconds
    crack_time /= 3600 * 24 * 365.25  # years

    # Output results
    strength = (entropy / 256) * 100  # percentage
    print(f"Password strength: {strength:.2f}%")
    print(f"Time to crack (with supercomputer): {crack_time:.2f} years")

# Define console UI to prompt for file path


def console_ui():
    file_path = input("Enter the path of the file to check: ")
    check_password_strength(file_path)


# Call console UI function
console_ui()
