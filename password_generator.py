
import secrets
import string


def generate_password(length=16):

    if length < 8:
        raise ValueError("Password length must be at least 8.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_characters = lowercase + uppercase + digits + symbols

    # Fill the remaining password length
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Securely shuffle the characters
    secrets.SystemRandom().shuffle(password)

    return "".join(password)
