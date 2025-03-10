import string

def check_password_strength(password):
    strength = 0
    if len(password) >= 8: strength += 1
    if any(c.isupper() for c in password): strength += 1
    if any(c.islower() for c in password): strength += 1
    if any(c.isdigit() for c in password): strength += 1
    if any(c in string.punctuation for c in password): strength += 1
    return ["Weak", "Medium", "Strong"][min(strength, 2)]

if __name__ == "__main__":
    password = input("Enter password: ")
    print("Password Strength:", check_password_strength(password))
