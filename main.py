import manager
from art import tprint
from colorama import Fore

from config import SECRET_PASSWORD


def main():
    tprint("password    manager")
    print(Fore.WHITE + "-" * 115)
    password = input(Fore.CYAN + "Enter password: ")

    if password != SECRET_PASSWORD:
        print(Fore.RED + "INVALID PASSWORD!!!")
        quit()

    while True:
        manager.get_input()


if __name__ == '__main__':
    main()
