
import math
import string


COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "letmein",
    "welcome123"
}


def analyze_password(password):

    if not password:
        return {
            "score": 0,
            "strength": "Very Weak",
            "issues": ["Password cannot be empty."],
            "entropy": 0
        }

    issues = []
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        issues.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    # Check character diversity
    checks = [
        (any(c.islower() for c in password), "Add lowercase letters."),
        (any(c.isupper() for c in password), "Add uppercase letters."),
        (any(c.isdigit() for c in password), "Add numbers."),
        (any(c in string.punctuation for c in password),
         "Add special characters.")
    ]

    for passed, message in checks:
        if passed:
            score += 1
        else:
            issues.append(message)

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        issues.append("This is a commonly used password.")

    # Check repeated characters
    if len(set(password)) < len(password) / 2:
        score -= 1
        issues.append("Too many repeated characters.")

    score = max(0, min(score, 6))

    # Estimate entropy using the available character pool
    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    entropy = (
        round(len(password) * math.log2(pool_size), 2)
        if pool_size else 0
    )

    if score <= 1:
        strength = "Very Weak"
    elif score <= 3:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "score": score,
        "strength": strength,
        "issues": issues,
        "entropy": entropy
    }
