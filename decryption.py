import pyAesCrypt
import os


def decryption(file, code):
    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        code,
        buffer_size
    )

    os.remove(file)


def main():
    password = input("Enter password for decoding the file: ")
    decryption("data.json.crp", password)


if __name__ == '__main__':
    main()
