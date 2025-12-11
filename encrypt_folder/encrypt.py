from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print("Key generated and saved to secret.key")

generate_key()




import os
from cryptography.fernet import Fernet

# Load key
def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher = Fernet(key)

def encrypt_file(file_path, output_path):
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)

    with open(output_path, "wb") as f:
        f.write(encrypted_data)

def encrypt_folder(source_folder, dest_folder):
    for root, dirs, files in os.walk(source_folder):
        # Maintain folder structure
        relative_path = os.path.relpath(root, source_folder)
        target_folder = os.path.join(dest_folder, relative_path)

        os.makedirs(target_folder, exist_ok=True)

        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_folder, file + ".enc")

            encrypt_file(source_file, target_file)
            print(f"Encrypted: {source_file}")

# Run encryption
encrypt_folder("myfolder", "encrypted")
print("Folder encrypted successfully!")
