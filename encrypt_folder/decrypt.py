import os
from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher = Fernet(key)

def decrypt_file(file_path, output_path):
    with open(file_path, "rb") as f:
        encrypted = f.read()

    decrypted = cipher.decrypt(encrypted)

    with open(output_path, "wb") as f:
        f.write(decrypted)

def decrypt_folder(source_folder, dest_folder):
    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        target_folder = os.path.join(dest_folder, relative_path)

        os.makedirs(target_folder, exist_ok=True)

        for file in files:
            if file.endswith(".enc"):
                source_file = os.path.join(root, file)
                output_file = os.path.join(target_folder, file.replace(".enc", ""))

                decrypt_file(source_file, output_file)
                print(f"Decrypted: {source_file}")

# Run decryption
decrypt_folder("encrypted", "decrypted")
print("Folder decrypted successfully!")
