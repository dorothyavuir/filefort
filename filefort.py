import os
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(filename='filefort.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FileFort:
    def __init__(self, key_file='filefort.key'):
        self.key_file = key_file
        self.key = self.load_key()

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)
        logging.info("New encryption key generated and saved.")
        return key

    def load_key(self):
        if not os.path.exists(self.key_file):
            logging.info("Key file not found, generating a new key.")
            return self.generate_key()
        with open(self.key_file, 'rb') as key_file:
            logging.info("Encryption key loaded.")
            return key_file.read()

    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
            fernet = Fernet(self.key)
            encrypted_data = fernet.encrypt(data)
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)
            logging.info(f"File {file_path} encrypted successfully.")
        except Exception as e:
            logging.error(f"Failed to encrypt {file_path}: {str(e)}")

    def decrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)
            logging.info(f"File {file_path} decrypted successfully.")
        except Exception as e:
            logging.error(f"Failed to decrypt {file_path}: {str(e)}")

if __name__ == "__main__":
    ff = FileFort()
    # Example usage
    # ff.encrypt_file('example.txt')
    # ff.decrypt_file('example.txt')