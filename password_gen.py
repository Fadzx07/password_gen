import random
import string

def generate_password(length=12):
    # All the characters we can use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"
    
    # Combine everything
    all_chars = lowercase + uppercase + digits + symbols
    
    # Pick random characters
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

# Ask user for length
try:
    length = int(input("How many characters? (default 12): ") or 12)
    password = generate_password(length)
    print(f"\nYour password: {password}")
except:
    print("Please enter a number")