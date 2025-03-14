from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os
import bcrypt

# File paths
KEY_FILE = "key.key"
PWD_FILE = "pwd.txt"
MASTER_PWD_FILE = "master_pwd.hash"

# Generate and save a key derived from the master password
def generate_key_from_master_password(master_password):
    salt = b"salt_"  # Use a fixed salt for simplicity (in production, use a random salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

# Save the master password hash to a file
def save_master_password(master_password):
    hashed = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt())
    with open(MASTER_PWD_FILE, "wb") as f:
        f.write(hashed)

# Verify the master password
def verify_master_password(input_password):
    if not os.path.exists(MASTER_PWD_FILE):
        return False
    with open(MASTER_PWD_FILE, "rb") as f:
        hashed = f.read()
    return bcrypt.checkpw(input_password.encode(), hashed)

# Initialize Fernet with the key derived from the master password
def initialize_fernet(master_password):
    key = generate_key_from_master_password(master_password)
    return Fernet(key)

# View stored passwords
def view(fer):
    if not os.path.exists(PWD_FILE):
        print("No passwords stored yet!")
        return

    with open(PWD_FILE, "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" not in data:
                print(f"Skipping invalid line: {data}")
                continue
            user, encrypted_pass = data.split("|")
            try:
                decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
                print("User:", user, "| Password:", decrypted_pass)
            except InvalidToken:
                print("Error: Unable to decrypt password for user:", user)
            except Exception as e:
                print(f"An unexpected error occurred for user {user}: {e}")

# Add a new password
def add(fer):
    name = input("Account name: ")
    pwd = input("Password: ")
    try:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()  # Encrypt and decode to string
        with open(PWD_FILE, "a") as f:
            f.write(name + "|" + encrypted_pwd + "\n")
        print("Password added successfully!")
    except Exception as e:
        print(f"An error occurred while adding the password: {e}")

# Main function
def main():
    # Check if the master password is set
    if not os.path.exists(MASTER_PWD_FILE):
        print("Welcome! Let's set up your master password.")
        master_password = input("Enter a master password: ")
        save_master_password(master_password)
        print("Master password set successfully!")
    else:
        # Verify the master password
        master_password = input("Enter your master password: ")
        if not verify_master_password(master_password):
            print("Incorrect master password. Access denied.")
            return

    # Initialize Fernet with the master password
    fer = initialize_fernet(master_password)

    # Main loop
    while True:
        mode = input("Would you like to add a new password or view the existing ones (view/add/q to quit): ").lower()
        if mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        elif mode == "q":
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter 'view', 'add', or 'q'.")

if __name__ == "__main__":
    main()