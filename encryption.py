import pyAesCrypt
import os


def encryption(file, code):
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        code,
        buffer_size
    )

    os.remove(file)


def main():
    password = input("Enter password for encoding the file: ")
    encryption("data.json", password)


if __name__ == '__main__':
    main()
