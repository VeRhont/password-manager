import json

from colorama import Fore
from config import SECRET_PASSWORD
from password import generate_password
from encryption import encryption
from decryption import decryption


def print_item(data):
    print()
    print(Fore.LIGHTMAGENTA_EX + f"website: {Fore.GREEN} {data['website']}")
    print(Fore.LIGHTMAGENTA_EX + f"login: {Fore.GREEN} {data['login']}")
    print(Fore.LIGHTMAGENTA_EX + f"password: {Fore.GREEN} {data['password']}")
    print()


def encrypt(func):
    def wrapper(*args):
        decryption("data.json.crp", SECRET_PASSWORD)
        func(*args)
        encryption("data.json", SECRET_PASSWORD)
    return wrapper


def create_password():
    password = generate_password()
    print(f"Your generated password: {Fore.LIGHTYELLOW_EX} {password}")

    return password


@encrypt
def add_account(website, login, password):

    user_data = {
        "website": website,
        "login": login,
        "password": password
    }

    with open("data.json", "r", encoding="utf-8") as file:
        file_data = json.load(file)

    with open("data.json", "w") as file:
        file_data.append(user_data)
        json.dump(file_data, file, indent=4)

    print(Fore.LIGHTGREEN_EX + 'Account added successfully')
    print()


@encrypt
def get_account_password(website):
    with open("data.json", "r", encoding="utf-8") as file:
        file_data = json.load(file)

        for item in file_data:
            if item.get("website") == website:
                print_item(item)
                return
        else:
            print(Fore.RED + "Account doesn't exist!")
            print()


@encrypt
def get_all_passwords():
    with open("data.json", "r", encoding="utf-8") as file:
        file_data = json.load(file)

        for item in file_data:
            print_item(item)


@encrypt
def delete_all():
    with open("data.json", "w", encoding="utf-8") as file:
        file.write("["
                   ""
                   "]")

    print(Fore.RED + "All data is deleted")
    print()


def get_input():
    temp = input(Fore.LIGHTYELLOW_EX + "0 - create account\n1 - add account\n2 - get password\n3 - get all passwords\n4 - delete all"
                     "\n5 - quit\n--> ")

    try:
        temp = int(temp)
    except:
        print(Fore.RED + "Invalid input")
        print()

    if temp == 0:
        website = input(Fore.CYAN + "website: ")
        login = input(Fore.CYAN + "login: ")
        password = create_password()
        add_account(website, login, password)

    elif temp == 1:
        website = input(Fore.CYAN + "website: ")
        login = input(Fore.CYAN + "login: ")
        password = input(Fore.CYAN + "password: ")
        add_account(website, login, password)

    elif temp == 2:
        website = input(Fore.CYAN + "website: ")
        get_account_password(website)

    elif temp == 3:
        get_all_passwords()

    elif temp == 4:
        if input(Fore.RED + "Enter password: ") == SECRET_PASSWORD:
            delete_all()
        else:
            print(Fore.RED + "Invalid password")
            print()

    elif temp == 5:
        quit()
