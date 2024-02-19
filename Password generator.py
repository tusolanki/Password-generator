import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    # Insert "@" at a random position in the generated password
    index = random.randint(0, length)
    password = password[:index] + '@' + password[index:]
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
