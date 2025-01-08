# FileFort

## Overview

FileFort is a Python-based application designed to enhance file protection on Windows systems using advanced security protocols and encryption. It utilizes the `cryptography` library to encrypt and decrypt files, providing a robust layer of security for sensitive data.

## Features

- **Encryption**: Secure your files with strong encryption algorithms.
- **Decryption**: Easily decrypt files when needed.
- **Key Management**: Automatically generates and manages encryption keys.
- **Logging**: Comprehensive logging for all operations to help track actions and errors.

## Requirements

- Python 3.6+
- `cryptography` library

To install the required library, run:
```bash
pip install cryptography
```

## Usage

### Initialization

Upon first run, FileFort will generate an encryption key and save it in `filefort.key`. This key is essential for encrypting and decrypting files, so ensure it is securely stored.

### Encrypt a File

To encrypt a file, use the `encrypt_file` method:

```python
ff = FileFort()
ff.encrypt_file('path/to/your/file.txt')
```

### Decrypt a File

To decrypt a file, use the `decrypt_file` method:

```python
ff = FileFort()
ff.decrypt_file('path/to/your/file.txt')
```

## Logging

All actions, including errors, are logged in `filefort.log`. This log file can be used to audit operations or troubleshoot issues.

## Security Considerations

- Ensure the `filefort.key` file is kept secure. Losing this key means you cannot decrypt your files.
- Regularly back up your encrypted files and encryption key to prevent data loss.

## License

FileFort is released under the [MIT License](LICENSE).

## Contribution

Contributions are welcome! Please submit a pull request or open an issue for discussion.