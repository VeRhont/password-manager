import manager

from config import SECRET_PASSWORD


def main():
    password = input("Enter password: ")

    if password != SECRET_PASSWORD:
        print("INVALID PASSWORD!!!")
        quit()

    while True:
        manager.get_input(password)


if __name__ == '__main__':
    main()