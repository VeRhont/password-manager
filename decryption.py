import pyAesCrypt
import os


def decryption(file, password):
    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    os.remove(file)


def main():
    password = input("Enter password for decoding the file: ")
    decryption("data.json", password)


if __name__ == '__main__':
    main()
