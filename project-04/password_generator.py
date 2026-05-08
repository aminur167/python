import random
import string

# generates a random password with given length
def generate_password(length=12, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
    ]
    if use_special:
        password.append(random.choice(string.punctuation))

    for _ in range(length - len(password)):
        password.append(random.choice(chars))

    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    print("Password Generator")
    print("-" * 30)

    for i in range(5):
        pw = generate_password(16)
        print(f"  {i+1}. {pw}")

    print("\nShort password (8 chars, no special):")
    print(f"  {generate_password(8, use_special=False)}")
